import numpy as np

from figures.figure import Figure
from figures.picture import Picture
from figures.symbolic import SymbolicIntervals3D
from figures.plot import Plot
from figures.plot import LinePlot
from figures.plot import ScatterPlot


if __name__ == '__main__':

    mins = np.random.rand(10, 3)
    maxs = mins + np.random.rand(10, 3)

    fig = Figure()
    fig.add_picture(
        Picture(
            x_lims=[0, 5],
            y_lims=[0, 5],
            z_lims=[0, 5],
            width='2in',
            height='2in'
        ).add_plot(
            SymbolicIntervals3D(
                mins=mins,
                maxs=maxs,
                legend='A',
                params={'color': 'black'})
        ).add_plot(
            SymbolicIntervals3D(
                mins=mins+1,
                maxs=maxs+1,
                legend='B',
                params={'color': 'gray'})
        ).add_plot(
            SymbolicIntervals3D(
                mins=mins+0.5,
                maxs=maxs+0.5,
                legend='C',
                params={'color': 'blue'})
        )
    ).add_picture(
        Picture(
            x_lims=[0, 5],
            y_lims=[0, 5],
            z_lims=[0, 5],
            width='2in',
            height='2in'
        ).add_plot(
            SymbolicIntervals3D(
                mins=mins,
                maxs=maxs,
                legend='A',
                params={'color': 'black'})
        ).add_plot(
            SymbolicIntervals3D(
                mins=mins+1,
                maxs=maxs+1,
                legend='B',
                params={'color': 'gray'})
        )
    )

    fig.print_figure(figure_name='test')

    fig = Figure()
    fig.add_picture(
        Picture(
            width='3in',
            height='3in',
            params={
                'xticklabels': ['LVQ', 'PSO'],
                'xtick': [1, 2]
            }
        ).add_plot(
            LinePlot(
                x=[1, 2],
                y=[16.1669354839, 16.1818548387],
                errors_x=[[0.5, 1], [0.8, 2]],
                errors_y=[[10.9634664698, 10.9634664698], [8.6805174518,
                                                           8.6805174518]],
                params={
                    'error bars': '',
                    'y dir': 'both',
                    'y explicit': '',
                    'x dir': 'both',
                    'x explicit': '',
                    'blue': ''
                })
        )
    )

    fig.print_figure(figure_name='confidence')