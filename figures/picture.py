from __future__ import division

# Author: Telmo de Menezes e Silva Filho <tmfilho@gmail.com>
#
# License: MIT

import numpy as np

from symbolic import SymbolicIntervals3D
from util.functions import parse_param


class Picture:
    def __init__(self, width='3in', height='3in', x_lims=None, y_lims=None,
                 z_lims=None, x_label='', y_label='', z_label='', params=None):
        self.width_ = width
        self.height_ = height
        self.x_lims_ = x_lims
        self.y_lims_ = y_lims
        self.z_lims_ = z_lims
        self.x_label_ = x_label
        self.y_label_ = y_label
        self.z_label_ = z_label
        self.params = params
        self.plots_ = []

    def add_plot(self, plot):
        self.plots_.append(plot)
        return self

    def print_picture(self):
        picture = '\\begin{tikzpicture}\n'
        if np.any([type(plot) == SymbolicIntervals3D for plot in self.plots_]):
            picture += _hypercube()
        picture += '\t\\begin{axis}[\n'
        if self.x_lims_ is not None:
            picture += '\t\txmin = {},\n'.format(self.x_lims_[0])
            picture += '\t\txmax = {},\n'.format(self.x_lims_[1])
        if self.y_lims_ is not None:
            picture += '\t\tymin = {},\n'.format(self.y_lims_[0])
            picture += '\t\tymax = {},\n'.format(self.y_lims_[1])
        if self.z_lims_ is not None:
            picture += '\t\tzmin = {},\n'.format(self.z_lims_[0])
            picture += '\t\tzmax = {},\n'.format(self.z_lims_[1])
        if self.x_label_ != '':
            picture += '\t\txlabel = {},\n'.format(self.x_label_)
        if self.y_label_ != '':
            picture += '\t\tylabel = {},\n'.format(self.y_label_)
        if self.z_label_ != '':
            picture += '\t\tzlabel = {},\n'.format(self.z_label_)
        picture += '\t\twidth = {},\n'.format(self.width_)
        picture += '\t\theight = {},\n'.format(self.height_)
        picture += self._apply_params()
        picture += '\t]\n'
        for plot in self.plots_:
            picture += plot.print_plot()
        picture += '\t\\end{axis}\n'
        picture += '\\end{tikzpicture}'
        return picture

    def _apply_params(self):
        params_str = ''
        if self.params is not None:
            if 'legend' in self.params.keys():
                pos = self.params['legend']['position']
                anchor = self.params['legend']['anchor']
                legend = '\t\tlegend style={at={'
                legend += '(axis cs:{},{})'.format(pos[0], pos[1])
                legend += '},anchor=' + anchor + '},\n'
                params_str += legend
            for param in self.params:
                if param != 'legend':
                    value = self.params[param]
                    if value is None or value == '':
                        params_str += '\t\t{},\n'.format(param)
                    else:
                        params_str += '\t\t{}={},\n'.format(param,
                                                            parse_param(value))
        return params_str


def _hypercube():
    command = "\t\\newcommand{\hypercube}[7][black]{\n"
    s_top = "\t\t\\draw[#1] (axis cs: #2,#3,#4) -- (axis cs: #2,#6,#4)"
    s_top += " -- (axis cs: #5,#6,#4) -- (axis cs: #5,#3,#4) -- cycle;\n"
    command += s_top
    s_bottom = "\t\t\\draw[#1] (axis cs: #2,#3,#7) -- (axis cs: #2,#6,#7)"
    s_bottom += " -- (axis cs: #5,#6,#7) -- (axis cs: #5,#3,#7) -- cycle;\n"
    command += s_bottom
    command += "\t\t\\draw[#1] (axis cs: #2,#3,#4) -- (axis cs: #2,#3," \
               "#7);\n"
    command += "\t\t\\draw[#1] (axis cs: #2,#6,#4) -- (axis cs: #2,#6," \
               "#7);\n"
    command += "\t\t\\draw[#1] (axis cs: #5,#3,#4) -- (axis cs: #5,#3," \
               "#7);\n"
    command += "\t\t\\draw[#1] (axis cs: #5,#6,#4) -- (axis cs: #5,#6," \
               "#7);\n"
    command += "\t}\n"
    return command
