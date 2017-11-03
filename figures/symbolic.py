from __future__ import division

# Author: Telmo de Menezes e Silva Filho <tmfilho@gmail.com>
#
# License: MIT

from plot import Plot


class SymbolicIntervals(Plot):
    def __init__(self, mins=None, maxs=None, legend=None, params=None):
        super(SymbolicIntervals, self).__init__(legend=legend, params=params)
        self._mins = mins
        self._maxs = maxs

    def print_plot(self):
        plot = '\t\\addplot[no markers,{}]\n'.format(self._apply_params())
        for [a, b], [c, d] in zip(self._mins, self._maxs):
            rect = '\t\t({},{}) rectangle '.format(a, b)
            rect += '(axis cs:{},{})\n'.format(c, d)
            plot += rect
        if self._legend is not None:
            plot += '\t;\\addlegendentry{%s}\n' % self._legend
        else:
            plot += '\t;\n'
        return plot


class SymbolicIntervals3D(Plot):
    def __init__(self, mins=None, maxs=None, legend=None, params=None):
        super(SymbolicIntervals3D, self).__init__(legend=legend, params=params)
        self._mins = mins
        self._maxs = maxs

    def print_plot(self):
        plot = ''
        op = self._apply_params()
        for [a, b, c], [d, e, f] in zip(self._mins, self._maxs):
            cube = "\t\t\\hypercube[%s]{%f}{%f}{%f}{%f}{%f}{%f}\n" % (
                op, a, b, c, d, e, f)
            plot += cube
        s = "\t\t\\addplot[{}] coordinates ".format(op)
        if self._legend is not None:
            s += "{(%f,%f)}; \\addlegendentry{%s}\n" % (
                self._maxs[0, 0], self._maxs[0, 1], self._legend)
        plot += s
        return plot
