import pydot
import os
from xml.dom.minidom import parseString

def nvdmap(gpath):
    def a_node(name):
        x = pydot.Node(name, shape="box")
        dot_graph.add_node(x)

    def a_edge(e1, e2):
        edge = pydot.Edge(e1, e2)
        dot_graph.add_edge(edge)

    dang_per = ['READ_CALENDAR', 'WRITE_CALENDAR', 'CAMERA', 'READ_CONTACTS', 'WRITE_CONTACTS', 'GET_ACCOUNTS',
                'ACCESS_FINE_LOCATION', 'ACCESS_COARSE_LOCATION', 'RECORD_AUDIO', 'READ_PHONE_STATE',
                'READ_PHONE_NUMBERS ', 'CALL_PHONE', 'ANSWER_PHONE_CALLS ', 'READ_CALL_LOG', 'WRITE_CALL_LOG',
                'ADD_VOICEMAIL', 'USE_SIP', 'PROCESS_OUTGOING_CALLS', 'BODY_SENSORS', 'SEND_SMS', 'RECEIVE_SMS',
                'READ_SMS', 'RECEIVE_WAP_PUSH', 'RECEIVE_MMS', 'READ_EXTERNAL_STORAGE', 'WRITE_EXTERNAL_STORAGE',
                'ACCESS_MEDIA_LOCATION', 'ACCEPT_HANDOVER', 'ACCESS_BACKGROUND_LOCATION', 'ACTIVITY_RECOGNITION']

    dot_graph = pydot.Dot(graph_type="graph",rankdir='LR')

    with open(gpath, 'r') as f:
        data = f.read()
    dom = parseString(data)
    nodes = dom.getElementsByTagName('uses-permission')

    l = []

    for c, node in enumerate(nodes):
        l.insert(c, node.getAttribute('android:name').split('.')[-1])

    dangerous_permissions = []
    normal_permissions = []

    for i in l:
        if i in dang_per:
            dangerous_permissions.append(i)
        else:
            normal_permissions.append(i)

    print(normal_permissions)
    print(dangerous_permissions)

    x = pydot.Node("Apk", color="pink")
    dot_graph.add_node(x)

    x = pydot.Node("Normal Permissions", color="green")
    dot_graph.add_node(x)

    x = pydot.Node("Dangerous Permissions", color="red")
    dot_graph.add_node(x)

    a_edge("Apk", "Normal Permissions")
    a_edge("Apk", "Dangerous Permissions")

    x1 = "\n".join(dangerous_permissions)
    x2 = "\n".join(normal_permissions)
    a_node(x1)
    a_node(x2)

    print(x1)
    print(x2)
    a_edge("Normal Permissions", x2)
    a_edge("Dangerous Permissions", x1)

    dot_graph.set_size("14,6.6!")
    dot_graph.write_png("nvd_map.png")
 