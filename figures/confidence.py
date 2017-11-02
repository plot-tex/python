from __future__ import division

import numpy as np


def _get_interval(data, b, alpha=0.05):
    means = [np.mean(np.random.choice(data, len(data))) for i in np.arange(b)]
    means.sort()
    minimum = means[int(np.round(b * alpha / 2))]
    maximum = means[int(np.round(b * (1.0 - alpha / 2)))]
    return (minimum + maximum) / 2, (maximum - minimum) / 2


def plot_confidence_intervals(data, labels, b, width, height, alpha=0.05):
    print "\\begin{tikzpicture}"
    print "     \\begin{axis}["
    print "          width={}in,".format(width)
    print "          height={}in,".format(height)
    print "          scale only axis,"
    print "          ylabel =$\\text{erro}$,"
    print "          xtick distance=1,"

    labels_str = "xticklabels={"
    indices = ""
    for i, label in enumerate(labels):
        labels_str += label
        indices += "{}".format(i + 1)
        if i < (len(labels) - 1):
            labels_str += ","
            indices += ","
    labels_str += "},xtick={" + indices + "}"

    print "         " + labels_str
    print "     ]"
    print "     \\addplot["
    print "          smooth,"
    print "          mark=x,"
    print "          only marks,"
    print "          blue,"
    print "          error bars/.cd, y dir=both, y explicit,"
    print "     ] plot coordinates {"
    for i, d in enumerate(data):
        avg, r = _get_interval(d, b, alpha=alpha)
        print "          ({},{})+=(0,{})-=(0,{})".format(i + 1, avg, r, r)
    print "     };"
    print "     \\end{axis}"
    print "\\end{tikzpicture}"
