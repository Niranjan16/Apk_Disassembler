import pydot
import os
from xml.dom.minidom import parseString

def rrperm(gpath):
    dot_graph = pydot.Dot(graph_type="graph")
    perm = {}
    with open(gpath, 'r') as f:
        data = f.read()
    dom = parseString(data)
    nodes = dom.getElementsByTagName('uses-permission')
    data = []
    for c, node in enumerate(nodes):
        data.insert(c, node.getAttribute('android:name').split('.')[-1])

    def a_node(name, clr='white'):
        x = pydot.Node(name, color=clr, shape="box")
        dot_graph.add_node(x)

    def a_edge(e1, e2):
        edge = pydot.Edge(e1, e2)
        dot_graph.add_edge(edge)


    perm["Read Permissions"] = [i for i in data if i.split('_')[0] == "READ" or i.split('_')[0] == "GET"]
    perm["Write Permissions"] = [i for i in data if i.split('_')[0] == "WRITE"]
    perm["Send and Receive Permissions"] = [i for i in data if
                                            i.split('_')[0] == "SEND" or i.split('_')[0] == "RECEIVE" or i.split('_')[
                                                0] == "BROADCAST"]
    perm["Modify Permissions"] = [i for i in data if
                                  i.split('_')[0] == "MODIFY" or i.split('_')[0] == "CHANGE" or i.split('_')[
                                      0] == "UPDATE" or i.split('_')[0] == "MANAGE" or i.split('_')[0] == "UNINSTALL" or
                                  i.split('_')[0] == "INSTALL"]

    a_node("Permissions", "darkgreen")

    c = 0
    for i, j in perm.items():
        clrs = ["gold", "slateblue", "lightblue1", "red", "purple"]
        if len(i) > 0:
            a_node(i, clrs[c])
            a_node('\n'.join(j), clrs[c])
            a_edge("Permissions", i)
            a_edge(i, '\n'.join(j))
            c += 1

    dot_graph.write_png("rr_map.png")