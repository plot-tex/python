from __future__ import division

# Author: Telmo de Menezes e Silva Filho <tmfilho@gmail.com>
#
# License: MIT

from plot import Plottable


class SymbolicIntervals(Plottable):
    def __init__(self, mins=None, maxs=None, legend=None, params=None):
        super(SymbolicIntervals, self).__init__(legend=legend, params=params)
        self.mins_ = mins
        self.maxs_ = maxs

    def print_plot(self):
        plot = '\t\\addplot[no markers,{}]\n'.format(self._apply_params())
        for [a, b], [c, d] in zip(self.mins_, self.maxs_):
            rect = '\t\t({},{}) rectangle '.format(a, b)
            rect += '(axis cs:{},{})\n'.format(c, d)
            plot += rect
        if self.legend_ is not None:
            plot += '\t;\\addlegendentry{%s}\n' % self.legend_
        else:
            plot += '\t;\n'
        return plot


class SymbolicIntervals3D(Plottable):
    def __init__(self, mins=None, maxs=None, legend=None, params=None):
        super(SymbolicIntervals3D, self).__init__(legend=legend, params=params)
        self.mins_ = mins
        self.maxs_ = maxs

    def print_plot(self):
        plot = ''
        op = self._apply_params()
        for [a, b, c], [d, e, f] in zip(self.mins_, self.maxs_):
            cube = "\t\t\\hypercube[%s]{%f}{%f}{%f}{%f}{%f}{%f}\n" % (
                op, a, b, c, d, e, f)
            plot += cube
        s = "\t\t\\addplot[{}] coordinates ".format(op)
        if self.legend_ is not None:
            s += "{(%f,%f)}; \\addlegendentry{%s}\n" % (
                self.maxs_[0, 0], self.maxs_[0, 1], self.legend_)
        plot += s
        return plot
