from __future__ import division


class Picture:
    def __init__(self, width='3in', height='3in', x_lims=None, y_lims=None,
                 z_lims=None, x_label='', y_label='', z_label='', options=None):
        self._width = width
        self._height = height
        self._x_lims = x_lims
        self._y_lims = y_lims
        self._z_lims = z_lims
        self._x_label = x_label
        self._y_label = y_label
        self._z_label = z_label
        self._options = options
        self._plots = []

    def add_plot(self, plot):
        self._plots.append(plot)
        return self

    def print_picture(self):
        picture = '\\begin{tikzpicture}\n'
        picture += '\t\\begin{axis}[\n'
        if self._x_lims is not None:
            picture += '\t\txmin = {},\n'.format(self._x_lims[0])
            picture += '\t\txmax = {},\n'.format(self._x_lims[1])
        if self._y_lims is not None:
            picture += '\t\tymin = {},\n'.format(self._y_lims[0])
            picture += '\t\tymax = {},\n'.format(self._y_lims[1])
        if self._z_lims is not None:
            picture += '\t\tzmin = {},\n'.format(self._z_lims[0])
            picture += '\t\tzmax = {},\n'.format(self._z_lims[1])
        if self._x_label != '':
            picture += '\t\txlabel = {},\n'.format(self._x_label)
        if self._y_label != '':
            picture += '\t\tylabel = {},\n'.format(self._y_label)
        if self._z_label != '':
            picture += '\t\tzlabel = {},\n'.format(self._z_label)
        picture += '\t\twidth = {},\n'.format(self._width)
        picture += '\t\theight = {},\n'.format(self._height)
        picture += self._apply_options()
        picture += '\t]\n'
        for plot in self._plots:
            picture += plot.print_plot()
        picture += '\t\\end{axis}\n'
        picture += '\\end{tikzpicture}'
        return picture

    def _apply_options(self):
        options = ''
        if self._options is not None:
            if 'legend' in self._options.keys():
                pos = self._options['legend']['position']
                anchor = self._options['legend']['anchor']
                legend = '\t\tlegend style={at={'
                legend += '(axis cs:{},{})'.format(pos[0], pos[1])
                legend += '},anchor=' + anchor + '},\n'
                options += legend
            for option in self._options:
                if option != 'legend':
                    value = options[option]
                    if value is None or value == '':
                        options += '\t\t{},\n'.format(option)
                    else:
                        options += '\t\t{}={},\n'.format(option, value)
        return options
