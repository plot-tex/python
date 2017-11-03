import numpy as np
from figures.figure import Figure
from figures.picture import Picture
from figures.symbolic import SymbolicIntervals3D

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
