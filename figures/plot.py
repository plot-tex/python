from __future__ import division

# Author: Telmo de Menezes e Silva Filho <tmfilho@gmail.com>
#
# License: MIT

import numpy as np

from util.functions import parse_param


class Plottable(object):
    def __init__(self, legend='', params=None):
        self._legend = legend
        self.params = params

    def print_plot(self):
        pass

    def _apply_params(self):
        params_str = ''
        error_str = ''
        discard = []
        if 'error bars' in self.params:
            error_str += 'error bars,'
            discard.append('error bars')
            if 'x explicit' in self.params:
                error_str += 'x explicit,'
                discard.append('x explicit')
            if 'x dir' in self.params:
                error_str += 'x dir={},'.format(self.params['x dir'])
                discard.append('x dir')
            if 'y explicit' in self.params:
                error_str += 'y explicit,'
                discard.append('y explicit')
            if 'y dir' in self.params:
                error_str += 'y dir={},'.format(self.params['y dir'])
                discard.append('y dir')
        if self.params is not None:
            for param in self.params:
                if param not in discard:
                    value = self.params[param]
                    if value is None or value == '':
                            params_str += '{},'.format(param)
                    else:
                        params_str += '{}={},'.format(param, parse_param(value))
        return params_str + error_str


class Plot(Plottable):
    def __init__(self, x=None, y=None, errors_x=None, errors_y=None,
                 legend=None, params=None):
        super(Plot, self).__init__(legend=legend, params=params)
        self._x = x
        self._y = y
        self._errors_x = errors_x
        self._errors_y = errors_y
        if self._errors_x is None and self._errors_y is not None:
            self._errors_x = np.zeros_like(self._errors_y)
        if self._errors_y is None and self._errors_x is not None:
            self._errors_y = np.zeros_like(self._errors_x)

    def print_plot(self):
        if self._errors_y is not None and ('error bars' not in self.params or
                                           'y dir' not in self.params or
                                           'y explicit' not in self.params):
            raise ValueError('Errors for y variable supplied, but error bar '
                             'params are missing. Please supply the following '
                             'param values: "error bars", "y dir" and '
                             '"y explicit"')
        if self._errors_x is not None and ('error bars' not in self.params or
                                           'x dir' not in self.params or
                                           'x explicit' not in self.params):
            raise ValueError('Errors for x variable supplied, but error bar '
                             'params are missing. Please supply the following '
                             'param values: "error bars", "x dir" and '
                             '"x explicit"')

        plot = '\t\\addplot[{}] coordinates '.format(self._apply_params())
        plot += '{\n'
        if self._errors_x is None and self._errors_y is None:
            for a, b in zip(self._x, self._y):
                plot += '\t\t({},{})\n'.format(a, b)
        else:
            for a, b, [c, d], [e, f] in zip(self._x, self._y, self._errors_x,
                                            self._errors_y):
                plot += '\t\t({},{})+=({},{})-=({},{})\n'.format(a, b, d, f,
                                                                 c, e)
        if self._legend is not None:
            plot += '\t};\\addlegendentry{%s}\n' % self._legend
        else:
            plot += '\t};\n'
        return plot


class LinePlot(Plot):
    def __init__(self, x=None, y=None, errors_x=None, errors_y=None,
                 legend=None, params=None):
        super(LinePlot, self).__init__(x=x, y=y, errors_x=errors_x,
                                       errors_y=errors_y, legend=legend,
                                       params=params)
        self._x = x
        self._y = y
        self.params['no markers'] = ''


class ScatterPlot(Plot):
    def __init__(self, x=None, y=None, errors_x=None, errors_y=None,
                 legend=None, params=None):
        super(ScatterPlot, self).__init__(x=x, y=y, errors_x=errors_x,
                                          errors_y=errors_y, legend=legend,
                                          params=params)
        self._x = x
        self._y = y
        self.params['only marks'] = ''
