from xml.dom.minidom import parseString
import os
import subprocess as sp
import pydot


def basic_map(gpath):
    dot_graph = pydot.Dot(graph_type="graph")

    with open(gpath, 'r') as f:
        data = f.read()
    dom = parseString(data)

    def a_node(name):
        x = pydot.Node(name, shape="box")
        dot_graph.add_node(x)

    def a_edge(e1, e2):
        edge = pydot.Edge(e1, e2)
        dot_graph.add_edge(edge)

    fe = []

    def features():
        nodes = dom.getElementsByTagName('uses-feature')
        co = 0
        for c, node in enumerate(nodes):
            co += 1
            fe.insert(c, node.getAttribute('android:name').split('.')[-1].upper())

    features()

    apk_info = []
    apk_name = ''

    nodes = dom.getElementsByTagName('manifest')
    for node in nodes:
        apk_name = node.getAttribute("package")
        apk_info.insert(0, f'PackageName:{node.getAttribute("package")}')
        apk_info.insert(1, f'compileSdkVersion:{node.getAttribute("android:compileSdkVersion")}')
        apk_info.insert(2, f'compileSdkVersionCodename:{node.getAttribute("android:compileSdkVersionCodename")}')
        apk_info.insert(3, f'platformBuildVersionCode:{node.getAttribute("platformBuildVersionCode")}')
        apk_info.insert(4, f'platformBuildVersionName:{node.getAttribute("platformBuildVersionName")}')
        apk_info.insert(5, f'Version:{node.getAttribute("android:versionName")}')

    def fnd():
        temp = gpath.split('/')[:-2]
        tmp_path = '/'.join(temp)
        # cmd = 'tree /home/niranjan/Downloads/wtsap >> /home/niranjan/Downloads/wtsap/a1.txt'
        cmd1 = 'tree ' + tmp_path + " >> " + tmp_path + '/dir_str.txt'
        os.system(cmd1)
        temp_path = tmp_path + '/resources'
        cmd = 'tree ' + temp_path + ' | tail -1'
        r_out = sp.getoutput(cmd)
        temp_path = tmp_path + '/sources'
        cmd = 'tree ' + temp_path + ' | tail -1'
        s_out = sp.getoutput(cmd)
        out = 'Resources: ' + r_out + '\n' + 'Sources: ' + s_out
        return out

    out = fnd()

    apk_name = apk_name.split('.')[-1].upper()

    a_edge(apk_name, "Basic Info")
    a_edge(apk_name, 'Features')
    a_edge(apk_name, 'Directory Info')

    a_edge("Basic Info", '\n'.join(apk_info))
    a_edge('Features', '\n'.join(fe))
    a_edge('Directory Info', out)


    dot_graph.write_png("basic_map.png")

