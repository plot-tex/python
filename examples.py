import numpy as np
from sklearn.datasets import make_moons
from sklearn.datasets import make_blobs

from figures.figure import Figure
from figures.picture import Picture
from figures.symbolic import SymbolicIntervals3D
from figures.plot import Plot
from figures.plot import LinePlot
from figures.plot import ScatterPlot
from figures.confidence import ConfidenceIntervals


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

    fig.print_figure(figure_name='confidence1')

    values = np.random.rand(100, 2)
    values[:, 0] += 2.0
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
            ConfidenceIntervals(
                values=values,
                interval_type='normal',
                legend='Normal',
                params={
                    'blue': '',
                    'only marks': ''
                }
            )
        ).add_plot(
            ConfidenceIntervals(
                values=values,
                interval_type='bootstrap',
                legend='Bootstrap',
                params={
                    'red': '',
                    'only marks': ''
                }
            )
        )
    )

    fig.print_figure(figure_name='confidence2')

    X_moons, y_moons = make_moons(200)
    X_blobs, y_blobs = make_blobs(200)

    fig = Figure()
    fig.add_picture(
        Picture(
            width='3in',
            height='3in',
        ).add_plot(
            ScatterPlot(
                x=X_moons[y_moons == 0, 0],
                y=X_moons[y_moons == 0, 1],
                legend='Class -',
                params={
                    'red': '',
                    'mark': '-'
                }
            )
        ).add_plot(
            ScatterPlot(
                x=X_moons[y_moons == 1, 0],
                y=X_moons[y_moons == 1, 1],
                legend='Class +',
                params={
                    'blue': '',
                    'mark': '+'
                }
            )
        )
    ).add_picture(
        Picture(
            width='3in',
            height='3in',
        ).add_plot(
            ScatterPlot(
                x=X_blobs[y_blobs == 0, 0],
                y=X_blobs[y_blobs == 0, 1],
                legend='Class -',
                params={
                    'red': '',
                    'mark': '-'
                }
            )
        ).add_plot(
            ScatterPlot(
                x=X_blobs[y_blobs == 1, 0],
                y=X_blobs[y_blobs == 1, 1],
                legend='Class +',
                params={
                    'blue': '',
                    'mark': '+'
                }
            )
        )
    )

    fig.print_figure(figure_name='scatter')
