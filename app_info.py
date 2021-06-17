from xml.dom.minidom import parseString
import os
import subprocess as sp
import pydot


def MAP(gpath):
    dot_graph = pydot.Dot(graph_type="graph",rankdir="LR")

    with open(gpath, 'r') as f:
        data = f.read()
    dom = parseString(data)

    def a_node(name):
        x = pydot.Node(name, shape="box")
        dot_graph.add_node(x)

    def a_edge(e1, e2):
        edge = pydot.Edge(e1, e2)
        dot_graph.add_edge(edge)

    def add_to_list(l, name):
        nodes = dom.getElementsByTagName(name)
        for c, node in enumerate(nodes):
            l.insert(c, node.getAttribute('android:name'))

    activities = []
    actn = []
    serv = []
    prov = []
    recv = []

    # nest_list = [[activites, 'activity'], [actn, 'action'], [serv, 'service'], [prov, 'provider'], [recv, 'receiver']]
    #
    # for i, j in nest_list:
    #     add_to_list(i, j)
    #
    # a_node("Apk")
    #
    # for i, j in nest_list:
    #     if len(i) > 20:
    #         i[:] = i[:20]
    #     if len(i) > 0:
    #         a_node(j)
    #         a_node('\n'.join(i))
    #         a_edge('Apk', j)
    #         a_edge(j, '\n'.join(i))

    nest_list1 = [[activities, 'activity'], [actn, 'action']]
    nest_list2 = [[serv, 'service'], [prov, 'provider'], [recv, 'receiver']]

    for i, j in nest_list1:
        add_to_list(i, j)
    for i, j in nest_list2:
        add_to_list(i, j)


    for i, j in nest_list1:
        if len(i) > 20:
            i[:] = i[:20]
        if len(i) > 0:
            a_node(j)
            a_node('\n'.join(i))
            a_edge(j, 'Apk')
            a_edge('\n'.join(i), j)

    for i, j in nest_list2:
        if len(i) > 20:
            i[:] = i[:20]
        if len(i) > 0:
            a_node(j)
            a_node('\n'.join(i))
            a_edge('Apk', j)
            a_edge(j, '\n'.join(i))

    dot_graph.set_size("15,15!")
    dot_graph.write_png("mp.png",)