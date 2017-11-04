from __future__ import division

# Author: Telmo de Menezes e Silva Filho <tmfilho@gmail.com>
#
# License: MIT


def parse_param(value):
    if type(value) == str:
        return value
    else:
        try:
            v = '{'
            for i, element in enumerate(list(value)):
                v += '{}'.format(element)
                if i < len(value) - 1:
                    v += ','
            v += '}'
            return v
        except TypeError:
            return value
