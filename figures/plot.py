from __future__ import division

# Author: Telmo de Menezes e Silva Filho <tmfilho@gmail.com>
#
# License: MIT

import numpy as np

from util.functions import parse_param


class Plottable(object):
    """Plottable interface.

    This interface exposes the basic methods and attributes for a plot.tex
    plot. Plot classes must implement this interface.

    Parameters
    ----------
    legend : str, default: ''
        Specifies the legend of the plot
    params : dict, default: None
        Provides customization parameters for the plot. Example: params={
        'color': 'blue', 'only marks': ''}

    Attributes
    ----------
    legend_ : str
        The legend of the plot.
    params : dict
        Customization parameters.
    """
    def __init__(self, legend='', params=None):
        self.legend_ = legend
        self.params = params

    def print_plot(self):
        """Build the PGFPlots code of the plot. Must be implemented by
        implementations of Plottable.

        Parameters
        ----------

        Returns
        -------
        plot : str
            Returns the PGFPlots code of the plot.
        """
        return ''

    def _apply_params(self):
        """Parse the plot's customization parameters into a string.

        Parameters
        ----------

        Returns
        -------
        params_str : str
            Returns a string with the parsed customization parameters.
        """
        params_str = ''
        error_str = ''
        discard = []

        # Error bars must be parsed separately, because any options coming
        # after the error bars parameter are treated as error bar options,
        # so these options must come in the end of the string
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
        params_str = params_str + error_str
        return params_str


class Plot(Plottable):
    """Plot class.

    This class implements the Plottable interface and is able to draw line
    and scatter plots with optional error bars.

    Parameters
    ----------
    x : {array-like}, shape (n_samples,)
            Values for the x axis.
    y : {array-like}, shape (n_samples,)
            Values for the y axis.
    errors_x : {array-like}, shape (n_samples,2) optional
            Error values for error bars on the x axis, where column errors_x[
            :, 0] represents left error bars and column errors_x[:,
            1] represents right error bars.
    errors_y : {array-like}, shape (n_samples,2) optional
            Error values for error bars on the y axis, where column errors_y[
            :, 0] represents lower error bars and column errors_x[:,
            1] represents upper error bars.
    legend : str, default: ''
        Specifies the legend of the plot
    params : dict, default: None
        Provides customization parameters for the plot. Example: params={
        'color': 'blue', 'only marks': ''}

    Attributes
    ----------
    x_ : {array-like}, shape (n_samples,)
        The x axis values.
    y_ : {array-like}, shape (n_samples,)
        The y axis values.
    errors_x_ : {array-like}, shape (n_samples,2)
        The x axis error values.
    errors_y_ : {array-like}, shape (n_samples,2)
        The y axis error values.
    """
    def __init__(self, x, y, errors_x=None, errors_y=None,
                 legend=None, params=None):
        super(Plot, self).__init__(legend=legend, params=params)
        self.x_ = x
        self.y_ = y
        self.errors_x_ = errors_x
        self.errors_y_ = errors_y

    def print_plot(self):
        """Build the PGFPlots code of the plot.

        Parameters
        ----------

        Returns
        -------
        plot : str
            Returns the PGFPlots code of the plot.
        """
        if self.errors_y_ is not None and ('error bars' not in self.params or
                                           'y dir' not in self.params or
                                           'y explicit' not in self.params):
            raise ValueError('Errors for y variable supplied, but error bar '
                             'params are missing. Please supply the following '
                             'param values: "error bars", "y dir" and '
                             '"y explicit"')
        if self.errors_x_ is not None and ('error bars' not in self.params or
                                           'x dir' not in self.params or
                                           'x explicit' not in self.params):
            raise ValueError('Errors for x variable supplied, but error bar '
                             'params are missing. Please supply the following '
                             'param values: "error bars", "x dir" and '
                             '"x explicit"')
        if self.errors_x_ is None and self.errors_y_ is not None:
            self.errors_x_ = np.zeros_like(self.errors_y_)
        if self.errors_y_ is None and self.errors_x_ is not None:
            self.errors_y_ = np.zeros_like(self.errors_x_)

        plot = '\t\\addplot[{}] coordinates '.format(self._apply_params())
        plot += '{\n'
        if self.errors_x_ is None and self.errors_y_ is None:
            for a, b in zip(self.x_, self.y_):
                plot += '\t\t({},{})\n'.format(a, b)
        else:
            for a, b, [c, d], [e, f] in zip(self.x_, self.y_, self.errors_x_,
                                            self.errors_y_):
                plot += '\t\t({},{})+=({},{})-=({},{})\n'.format(a, b, d, f,
                                                                 c, e)
        if self.legend_ is not None and self.legend_ != '':
            plot += '\t};\\addlegendentry{%s}\n' % self.legend_
        else:
            plot += '\t};\n'
        return plot


class LinePlot(Plot):
    """Plot class.

    This class inherits from Plot and draws line plots with optional error bars.

    Parameters
    ----------
    x : {array-like}, shape (n_samples,)
            Values for the x axis.
    y : {array-like}, shape (n_samples,)
            Values for the y axis.
    errors_x : {array-like}, shape (n_samples,2) optional
            Error values for error bars on the x axis, where column errors_x[
            :, 0] represents left error bars and column errors_x[:,
            1] represents right error bars.
    errors_y : {array-like}, shape (n_samples,2) optional
            Error values for error bars on the y axis, where column errors_y[
            :, 0] represents lower error bars and column errors_x[:,
            1] represents upper error bars.
    legend : str, default: ''
        Specifies the legend of the plot
    params : dict, default: None
        Provides customization parameters for the plot. Example: params={
        'color': 'blue', 'only marks': ''}

    """
    def __init__(self, x, y, errors_x=None, errors_y=None,
                 legend=None, params=None):
        super(LinePlot, self).__init__(x=x, y=y, errors_x=errors_x,
                                       errors_y=errors_y, legend=legend,
                                       params=params)
        self.params['no markers'] = ''


class ScatterPlot(Plot):
    """Plot class.

    This class inherits from Plot and draws scatter plots with optional error
    bars.

    Parameters
    ----------
    x : {array-like}, shape (n_samples,)
            Values for the x axis.
    y : {array-like}, shape (n_samples,)
            Values for the y axis.
    errors_x : {array-like}, shape (n_samples,2) optional
            Error values for error bars on the x axis, where column errors_x[
            :, 0] represents left error bars and column errors_x[:,
            1] represents right error bars.
    errors_y : {array-like}, shape (n_samples,2) optional
            Error values for error bars on the y axis, where column errors_y[
            :, 0] represents lower error bars and column errors_x[:,
            1] represents upper error bars.
    legend : str, default: ''
        Specifies the legend of the plot
    params : dict, default: None
        Provides customization parameters for the plot. Example: params={
        'color': 'blue', 'only marks': ''}

    """
    def __init__(self, x, y, errors_x=None, errors_y=None,
                 legend=None, params=None):
        super(ScatterPlot, self).__init__(x=x, y=y, errors_x=errors_x,
                                          errors_y=errors_y, legend=legend,
                                          params=params)
        self.params['only marks'] = ''
