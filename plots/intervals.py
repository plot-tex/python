from __future__ import division


def plot_intervals(mins_list, maxs_list, width, height, x_lims, y_lims, colors,
                   class_labels, x_label="X1", y_label="X2", options={}):
    print "\\begin{tikzpicture}"
    print "     \\begin{axis}["
    print "          xmin={},".format(x_lims[0])
    print "          xmax={},".format(x_lims[1])
    print "          ymin={},".format(y_lims[0])
    print "          ymax={},".format(y_lims[1])
    print "          xlabel={},".format(x_label)
    print "          ylabel={},".format(y_label)
    print "          width={}in,".format(width)
    print "          height={}in,".format(height)
    if "legend" in options.keys():
        pos = options["legend"]["position"]
        anchor = options["legend"]["anchor"]
        legend = "\t\tlegend style={at={"
        legend += "(axis cs:{},{})".format(pos[0], pos[1])
        legend += "},anchor=" + anchor + "}"
        print legend
    print "     ]"
    for i, (mins, maxs) in enumerate(zip(mins_list, maxs_list)):
        print "\t\\addplot[{}, no markers]".format(colors[i])
        for [a, b], [c, d] in zip(mins, maxs):
            rect = "({},{}) rectangle ".format(a, b)
            rect += "(axis cs:{},{})".format(c, d)
            print rect
        print "\t;\\addlegendentry{%s}" % class_labels[i]
    print "     \\end{axis}"
    print "\\end{tikzpicture}"


def plot_intervals_3d(mins_list, maxs_list, width, height, x_lims, y_lims,
                      z_lims, colors, class_labels, x_label="X1", y_label="X2",
                      z_label="X3", options={}):
    print "\\begin{tikzpicture}"
    print "\t\\newcommand{\hypercube}[7][black]{"
    s_top = "\t\t\\draw[#1] (axis cs: #2,#3,#4) -- (axis cs: #2,#6,#4)"
    s_top += " -- (axis cs: #5,#6,#4) -- (axis cs: #5,#3,#4) -- cycle;"
    print s_top
    s_bottom = "\t\t\\draw[#1] (axis cs: #2,#3,#7) -- (axis cs: #2,#6,#7)"
    s_bottom += " -- (axis cs: #5,#6,#7) -- (axis cs: #5,#3,#7) -- cycle;"
    print s_bottom
    print "\t\t\\draw[#1] (axis cs: #2,#3,#4) -- (axis cs: #2,#3,#7);"
    print "\t\t\\draw[#1] (axis cs: #2,#6,#4) -- (axis cs: #2,#6,#7);"
    print "\t\t\\draw[#1] (axis cs: #5,#3,#4) -- (axis cs: #5,#3,#7);"
    print "\t\t\\draw[#1] (axis cs: #5,#6,#4) -- (axis cs: #5,#6,#7);"
    print "\t}"

    print "     \\begin{axis}["
    print "          xmin={},".format(x_lims[0])
    print "          xmax={},".format(x_lims[1])
    print "          ymin={},".format(y_lims[0])
    print "          ymax={},".format(y_lims[1])
    print "          zmin={},".format(z_lims[0])
    print "          zmax={},".format(z_lims[1])
    print "          xlabel={},".format(x_label)
    print "          ylabel={},".format(y_label)
    print "          zlabel={},".format(z_label)
    print "          width={}in,".format(width)
    print "          height={}in,".format(height)
    if "legend" in options.keys():
        pos = options["legend"]["position"]
        anchor = options["legend"]["anchor"]
        legend = "\t\tlegend style={at={"
        legend += "(axis cs:{},{})".format(pos[0], pos[1])
        legend += "},anchor=" + anchor + "}"
        print legend
    print "     ]"
    for i, (mins, maxs) in enumerate(zip(mins_list, maxs_list)):
        for [a, b, c], [d, e, f] in zip(mins, maxs):
            cube = "\t\t\\hypercube[%s]{%f}{%f}{%f}{%f}{%f}{%f}" % (
                colors[i], a, b, c, d, e, f)
            print cube
        s = "\t\t\\addplot[{}] coordinates ".format(colors[i])
        s += "{(%f,%f)}; \\addlegendentry{%s};" % (
            x_lims[1] + 1, y_lims[1] + 1, class_labels[i])
        print s
    print "     \\end{axis}"
    print "\\end{tikzpicture}"
