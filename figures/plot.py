from __future__ import division

# Author: Telmo de Menezes e Silva Filho <tmfilho@gmail.com>
#
# License: MIT


class Plot(object):
    def __init__(self, legend='', params=None):
        self._legend = legend
        self.params = params

    def print_plot(self):
        pass

    def _apply_params(self):
        options = ''
        if self.params is not None:
            for option in self.params:
                value = self.params[option]
                if value is None or value == '':
                    options += '{},'.format(option)
                else:
                    options += '{}={},'.format(option, value)
        return options
