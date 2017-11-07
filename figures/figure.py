from __future__ import division

# Author: Telmo de Menezes e Silva Filho <tmfilho@gmail.com>
#
# License: MIT

import os


class Figure:
    def __init__(self, caption='', label='', placement='h', centering=True,
                 pic_files=True):
        self.caption_ = caption
        self.label_ = label
        self.placement_ = placement
        self.centering_ = centering
        self.pic_files_ = pic_files
        self.pictures_ = []
        self.pic_captions_ = []
        self.pic_labels_ = []

    def add_picture(self, picture, caption='', label=''):
        self.pictures_.append(picture)
        self.pic_captions_.append(caption)
        self.pic_labels_.append(label)
        return self

    def print_figure(self, figure_name='figure', path=''):
        if not os.path.exists(path) and path != '':
            os.makedirs(path)
        filename = os.path.join(path, figure_name + '.tex')
        with open(filename, 'w') as f:
            f.write('\\begin{figure}[' + self.placement_ + ']\n')
            f.write('\t\\caption{' + self.caption_ + '}\n')
            f.write('\t\\label{' + self.label_ + '}\n')
            if self.centering_:
                f.write('\t\\centering\n')
            if len(self.pictures_) == 1:
                f.write(self.pictures_[0].print_picture() + '\n')
            elif len(self.pictures_) > 1:
                for i, picture in enumerate(self.pictures_):
                    sub_name = ''
                    if self.pic_files_:
                        sub_name = figure_name + '-subfig-{}'.format(i + 1)
                        sub_filename = os.path.join(path, sub_name + '.tex')
                        with open(sub_filename, 'w') as sub_f:
                            sub_f.write(picture.print_picture())
                    f.write('\t\\subfloat[' + self.pic_captions_[i])
                    f.write(' \\label{' + self.pic_labels_[i] + '}]{\n')
                    if self.pic_files_:
                        f.write('\t\t\\input{' + sub_name + '}\n')
                    else:
                        f.write(picture.print_picture() + '\n')
                    f.write('\t}\n')
                    if i < (len(self.pictures_) - 1):
                        f.write('\t\\hfill\n')
            f.write('\\end{figure}\n')
        return self
