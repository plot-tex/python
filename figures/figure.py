from __future__ import division

import os


class Figure:
    def __init__(self, caption='', label='', placement='H', centering=True,
                 pic_files=True):
        self._caption = caption
        self._label = label
        self._placement = placement
        self._centering = centering
        self._pic_files = pic_files
        self._pictures = []
        self._pic_captions = []
        self._pic_labels = []

    def add_picture(self, picture, caption='', label=''):
        self._pictures.append(picture)
        self._pic_captions.append(caption)
        self._pic_labels.append(label)
        return self

    def print_figure(self, figure_name='figure', path=''):
        if not os.path.exists(path) and path != '':
            os.makedirs(path)
        filename = os.path.join(path, figure_name + '.tex')
        with open(filename, 'w') as f:
            f.write('\\begin{figure}[' + self._placement + ']\n')
            f.write('\t\\caption{' + self._caption + '}\n')
            f.write('\t\\label{' + self._label + '}\n')
            if self._centering:
                f.write('\t\\centering\n')
            if len(self._pictures) == 1:
                f.write(self._pictures[0].print_picture() + '\n')
            elif len(self._pictures) > 1:
                for i, picture in enumerate(self._pictures):
                    if self._pic_files:
                        sub_name = figure_name + '-subfig-{}'.format(i + 1)
                        sub_filename = os.path.join(path, sub_name + '.tex')
                        with open(sub_filename, 'w') as sub_f:
                            sub_f.write(picture.print_picture())
                    f.write('\t\\subfloat[' + self._pic_captions[i])
                    f.write(' \\label{' + self._pic_labels[i] + '}]{\n')
                    if self._pic_files:
                        f.write('\t\t\\input{' + sub_name + '}\n')
                    else:
                        f.write(picture.print_picture() + '\n')
                    f.write('\t}\n')
                    if i < (len(self._pictures) - 1):
                        f.write('\t\\hfill\n')
            f.write('\\end{figure}\n')
        return self


if __name__ == '__main__':
    from picture import Picture

    fig = Figure()
    fig.add_picture(Picture()).add_picture(Picture()).add_picture(Picture())
    fig.print_figure(figure_name='test', path='../tables')
