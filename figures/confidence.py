from __future__ import division

# Author: Telmo de Menezes e Silva Filho <tmfilho@gmail.com>
#
# License: MIT

import numpy as np
from scipy.stats import bayes_mvs

from plot import Plot


class ConfidenceIntervals(Plot):
    def __init__(self, values=None, alpha=0.95, b=1000,
                 interval_type='normal', legend=None, params=None):
        if interval_type not in ['normal', 'bootstrap']:
            raise ValueError('Unknown interval type: {}. Please use choose '
                             'normal or bootstrap intervals')
        elif interval_type == 'bootstrap':
            n = values.shape[1]
            x = np.arange(n) + 1
            y = np.zeros(n)
            errors_y = np.zeros((n, 2))
            for i in np.arange(n):
                avg, r = _get_interval(values[:, i], b, 1.0 - alpha)
                y[i] = avg
                errors_y[i] = r
        else:
            n = values.shape[1]
            x = np.arange(n) + 1
            y = np.zeros(n)
            errors_y = np.zeros((n, 2))
            for i in np.arange(n):
                res_mean, _, _ = bayes_mvs(values[:, i], alpha=alpha)
                y[i] = res_mean.statistic
                errors_y[i] = res_mean.minmax[1] - y[i]
        super(ConfidenceIntervals, self).__init__(x=x, y=y, errors_x=None,
                                                  errors_y=errors_y,
                                                  legend=legend, params=params)
        self.params['error bars'] = ''
        self.params['y dir'] = 'both'
        self.params['y explicit'] = ''


def _get_interval(data, b, alpha=0.05):
    means = [np.mean(np.random.choice(data, len(data))) for i in np.arange(b)]
    means.sort()
    minimum = means[int(np.round(b * alpha / 2))]
    maximum = means[int(np.round(b * (1.0 - alpha / 2)))]
    return (minimum + maximum) / 2, (maximum - minimum) / 2
