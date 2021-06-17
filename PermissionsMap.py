import pydot
import os
from xml.dom.minidom import parseString


def per_map(gpath):

	dot_graph = pydot.Dot(graph_type="graph")
	with open(gpath, 'r') as f:
		data = f.read()
	dom = parseString(data)
	nodes = dom.getElementsByTagName('uses-permission')
	l = []
	for c, node in enumerate(nodes):
		l.insert(c, node.getAttribute('android:name').split('.')[-1])

	calendar = [i for i in l if (i=="READ_CALENDAR" or i=="WRITE_CALENDAR")]
	contacts = [i for i in l if (i=="READ_CONTACTS" or i=="WRITE_CONTACTS" or i=="GET_ACCOUNTS")]
	locations = [i for i in l if (i=="ACCESS_COARSE_LOCATION" or i=="ACCESS_FINE_LOCATION" or i=="GET_ACCOUNTS")]
	general = [i for i in l if (i=="BLUETOOTH" or i=="CAMERA" or i=="INTERNET" or i == "NFC" or i=="VIBRATE" or i=="REBOOT")]
	phone = [i for i in l if (i=="READ_PHONE_STATE" or i=="CALL_PHONE" or i=="READ_CALL_LOG" or i == "WRITE_CALL_LOG" or i=="ADD_VOICEMAIL" or i=="USE_SIP" or i=="PROCESS_OUTGOING_CALLS" )]
	sms = [i for i in l if (i=="SEND_SMS" or i=="RECEIVE_SMS" or i=="READ_SMS" or i == "RECEIVE_WAP_PUSH" or i=="RECEIVE_MMS")]
	storage = [i for i in l if (i=="READ_EXTERNAL_STORAGE" or i=="WRITE_EXTERNAL_STORAGE")] 

	def a_node(name):
		x = pydot.Node(name , style = "filled" , shape = "box")
		dot_graph.add_node(x)

	def a_edge(e1,e2):
		edge = pydot.Edge(e1 , e2)
		dot_graph.add_edge(edge)

	def insert_into_dic(name ,arr):
		if len(arr) > 1:
			dic[name] = "\n".join(arr)

	dic = {}

	a_node("Permissions")
    


	insert_into_dic("Calendar",calendar)
	insert_into_dic("Contacts",contacts)
	insert_into_dic("Locations",locations)
	insert_into_dic("General",general)
	insert_into_dic("Phone",phone)
	insert_into_dic("Storage",storage)
	insert_into_dic("Sms",sms)

	for i,j in dic.items():
		a_node(i)
		a_node(j)
		a_edge("Permissions",i)
		a_edge(i,j)

	dot_graph.write_png("map.png")













    




    




   


    

    
        






   
    
   
    


