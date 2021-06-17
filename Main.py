from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from xml.dom.minidom import parseString
import subprocess
import os
import pydot
from PIL import ImageTk, Image
from nvdmap import *
from PermissionsMap import *
from rr_permissions_map import *
from basicmap import *
from app_info import *

root = Tk()
root.title('Text-Editor')
root.resizable(width=True, height=True)
root.geometry("1400x660")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

my_frame = Frame(root)
my_frame.grid(row=0, column=0, sticky="nswe")
my_frame.columnconfigure(0, weight=1)
my_frame.columnconfigure(1, weight=6)
my_frame.rowconfigure(0, weight=1)

left_frame = Frame(my_frame)
left_frame.grid(row=0, column=0, sticky="nswe")
left_frame.columnconfigure(0, weight=1)
left_frame.rowconfigure(0, weight=1)
right_frame = Frame(my_frame)
right_frame.grid(row=0, column=1, sticky="nswe")
right_frame.columnconfigure(0, weight=1)
right_frame.rowconfigure(0, weight=1)

tabcontrol = ttk.Notebook(right_frame)
tabcontrol.grid(row = 0 , column = 0 , sticky = "nswe")

my_menu = Menu(root)
root.config(menu=my_menu)

scrollbar_object = Scrollbar(left_frame)
scrollbar_object2 = Scrollbar(right_frame)
scrollbar_object.grid(row=0, column=1, sticky='ns')
scrollbar_object2.grid(row=0, column=1, sticky='ns')

def new_file():
    My_Text = Text(right_frame)
    My_Text.grid(row = 0 , column = 0 , sticky = "nswe")
    tabcontrol.add(My_Text)
    root.title('New File - TextEditor')

def open_file():
    text_1 = Text(right_frame)
    text_1.grid(row=0, column=0, sticky="nswe")
    text_file = filedialog.askopenfilename(initialdir="/", title="Open file",
                                           filetypes=(("APK Files", ".apk"), ("all files", ".*")))
    name = text_file
    name = name.replace("/", "")
    root.title(f'{name}-TextEditor')
    text_file = open(text_file, 'r')
    stuff = text_file.read()
    text_1.insert(END, stuff)
    print(text_file)
    text_file.close()

def opn_file(file_path):
    text_file = file_path
    name = text_file.split("/")[-1]
    text_1 = Text(right_frame)
    text_1.grid(row=0, column=0, sticky="nswe")
    tabcontrol.add(text_1, text=name)
    root.title(f'{name}-TextEditor')
    text_file = open(text_file, 'r')
    stuff = text_file.read()
    text_1.insert(END, stuff)
    print(text_file)
    text_file.close()


def save_as_file():
    my_text = Text(right_frame, yscrollcommand = scrollbar_object2.set)
    my_text.grid(row = 0 , column = 0 , sticky = "nswe")
    text_file = filedialog.asksaveasfilename(defaultextension=".*",initialdir="/",title="Save file",filetypes=(("Text files",".txt"),("All files",".*.*")))
    if text_file:
        name = text_file
        name = name.replace("/","")
        root.title(f'{name} Saved1-TextEditor')

        text_file = open(text_file,'w')
        text_file.write(my_text.get(1.0, END))

        text_file.close()


def get_path(p):
    p = p.split(".")
    p.pop()
    return ''.join(p)

def get_path2(p):
    p = p.split("/")
    p.pop()
    return '/'.join(p)

def apkname(a):
    a = a.split("/")
    a = a[-1].split(".")
    return a[0]


apk_path = filedialog.askopenfilename(initialdir="/", title="Disassembling",
                                      filetypes=(("APK files", ".apk"), ("All files", ".apk")))

apkdir_path = get_path2(apk_path) + "/" +apkname(apk_path)



gpath = apkdir_path + "/resources/AndroidManifest.xml"

command = "jadx/./build/jadx/bin/jadx"
cmd = "cd && " + command + " " + "-d" + " " + apkdir_path + " " + apk_path
os.system(cmd)

def perm_file():
    with open(gpath, 'r') as f:
        data = f.read()
    dom = parseString(data)
    nodes = dom.getElementsByTagName('uses-permission')
    top = Toplevel()
    l = Listbox(top, height=600,
                width=650,
                bg="grey",
                activestyle="dotbox",
                font="Arial",
                fg="black")
    top.geometry("700x250")
    co = 0
    for c, node in enumerate(nodes):
        co += 1
        l.insert(c, node.getAttribute('android:name'))
    l.insert(0, f'Number of Permissions : {co}')
    l.pack()



def act_file():
    with open(gpath, 'r') as f:
        data = f.read()
    dom = parseString(data)
    nodes = dom.getElementsByTagName('activity')
    top = Toplevel()
    l = Listbox(top, height=600,
                width=650,
                bg="grey",
                activestyle="dotbox",
                font="Arial",
                fg="black")
    top.geometry("700x250")
    co = 0
    for c, node in enumerate(nodes):
        co += 1
        l.insert(c, node.getAttribute('android:name'))
    l.insert(0, f'Number of Activities : {co}')
    l.pack()


def inte_file():
    with open(gpath, 'r') as f:
        data = f.read()
    dom = parseString(data)
    nodes = dom.getElementsByTagName('action')
    top = Toplevel()
    l = Listbox(top, height=600,
                width=650,
                bg="grey",
                activestyle="dotbox",
                font="Arial",
                fg="black")
    top.geometry("700x250")
    co = 0
    for c, node in enumerate(nodes):
        co += 1
        l.insert(c, node.getAttribute('android:name'))
    l.insert(0, f'Number of Intent Actions : {co}')
    l.pack()


def intent_cat():
    with open(gpath, 'r') as f:
        data = f.read()
    dom = parseString(data)
    nodes = dom.getElementsByTagName('category')
    top = Toplevel()
    l = Listbox(top, height=600,
                width=650,
                bg="grey",
                activestyle="dotbox",
                font="Arial",
                fg="black")
    top.geometry("700x250")
    co = 0
    for c, node in enumerate(nodes):
        co += 1
        l.insert(c, node.getAttribute('android:name'))
    l.insert(0, f'Number of Intents Categories : {co}')
    l.pack()


def serv_file():
    with open(gpath, 'r') as f:
        data = f.read()
    dom = parseString(data)
    nodes = dom.getElementsByTagName('service')
    top = Toplevel()
    l = Listbox(top, height=600,
                width=650,
                bg="grey",
                activestyle="dotbox",
                font="Arial",
                fg="black")
    top.geometry("700x250")
    co = 0
    for c, node in enumerate(nodes):
        co += 1
        l.insert(c, node.getAttribute('android:name'))
    l.insert(0, f'Number of Services : {co}')
    l.pack()


def prov_file():
    with open(gpath, 'r') as f:
        data = f.read()
    dom = parseString(data)
    nodes = dom.getElementsByTagName('provider')
    top = Toplevel()
    l = Listbox(top, height=600,
                width=650,
                bg="grey",
                activestyle="dotbox",
                font="Arial",
                fg="black")
    top.geometry("700x250")
    co = 0
    for c, node in enumerate(nodes):
        co += 1
        l.insert(c, node.getAttribute('android:name'))
    l.insert(0, f'Number of providers : {co}')
    l.pack()


def recv_file():
    with open(gpath, 'r') as f:
        data = f.read()
    dom = parseString(data)
    nodes = dom.getElementsByTagName('receiver')
    top = Toplevel()
    l = Listbox(top, height=600,
                width=650,
                bg="grey",
                activestyle="dotbox",
                font="Arial",
                fg="black")
    top.geometry("700x250")
    co = 0
    for c, node in enumerate(nodes):
        co += 1
        l.insert(c, node.getAttribute('android:name'))
    l.insert(0, f'Number of Receivers : {co}')
    l.pack()


def app_file():
    with open(gpath, 'r') as f:
        data = f.read()
    dom = parseString(data)
    nodes = dom.getElementsByTagName('manifest')
    top = Toplevel()
    l = Listbox(top, height=600,
                width=650,
                bg="grey",
                activestyle="dotbox",
                font="Arial",
                fg="black")
    top.geometry("700x250")
    co = 0
    for node in nodes:
        co += 1
        l.insert(1, f'Package Name:{node.getAttribute("package")}')
        l.insert(2, f'compileSdkVersion:{node.getAttribute("android:compileSdkVersion")}')
        l.insert(3, f'compileSdkVersionCodename:{node.getAttribute("android:compileSdkVersionCodename")}')
        l.insert(4, f'XMLNS:{node.getAttribute("xmlns:android")}')
        l.insert(5, f'platformBuildVersionCode:{node.getAttribute("platformBuildVersionCode")}')
        l.insert(6, f'platformBuildVersionName:{node.getAttribute("platformBuildVersionName")}')

    l.pack()



def populate_tree(tree, node):
    if tree.set(node, "type") != 'directory':
        return

    path = tree.set(node, "fullpath")
    tree.delete(*tree.get_children(node))

    parent = tree.parent(node)

    for p in os.listdir(path):
        # for p in special_dirs + os.listdir(path):
        ptype = None
        p = os.path.join(path, p).replace('\\', '/')
        if os.path.isdir(p):
            ptype = "directory"
        elif os.path.isfile(p):
            ptype = "file"

        fname = os.path.split(p)[1]
        id = tree.insert(node, "end", text=fname, values=[p, ptype])

        if ptype == 'directory':
            if fname not in ('.', '..'):
                tree.insert(id, 0, text="dummy")
                tree.item(id, text=fname)
        elif ptype == 'file':
            size = os.stat(p).st_size
            tree.set(id, "size", "%d bytes" % size)


def populate_roots(tree):

    dir = os.path.abspath(apkdir_path).replace('\\', '/')
    node = tree.insert('', 'end', text=dir, values=[dir, "directory"])
    populate_tree(tree, node)


def update_tree(event):
    tree = event.widget
    populate_tree(tree, tree.focus())


def change_dir(event):
    tree = event.widget
    node = tree.focus()
    if tree.parent(node):
        path = os.path.abspath(tree.set(node, "fullpath"))
        if os.path.isdir(path):
            os.chdir(path)
            tree.delete(tree.get_children(''))
            populate_roots(tree)


def autoscroll(sbar, first):
    pass


def OnDoubleClick(event):
    item = tree.identify("item", event.x, event.y)
    opn_file(tree.item(item)['values'][0])


hsb = ttk.Scrollbar(orient="horizontal")

tree = ttk.Treeview(left_frame, columns=("fullpath", "type", "size"),
                    displaycolumns="size", yscrollcommand=lambda f, l: autoscroll(f, l),
                    xscrollcommand=lambda f, l: autoscroll(hsb, f))

hsb['command'] = tree.xview

tree.heading("#0", text="Directory Structure", anchor='w')
tree.heading("size", text="File Size", anchor='w')
tree.column("size", stretch=0, width=100)

populate_roots(tree)
tree.bind('<<TreeviewOpen>>', update_tree)
tree.bind('<Double-Button-1>', change_dir)
tree.bind("<Double-1>", OnDoubleClick)

tree.grid(column=0, row=0, sticky='nswe')
tree.grid(column=0, row=0, sticky='nswe')

def permap_img():
    global img_1
    per_map(gpath)
    xscrollbar_1 = Scrollbar(right_frame, orient=HORIZONTAL)
    xscrollbar_1.grid(row=1, column=0, sticky=E + W)
    yscrollbar_1 = Scrollbar(right_frame)
    yscrollbar_1.grid(row=0, column=1, sticky=N + S)
    canvas_1 = Canvas(right_frame, bd=0, xscrollcommand=xscrollbar_1.set, yscrollcommand=yscrollbar_1.set)
    canvas_1.grid(row=0, column=0, sticky=N + S + E + W)
    file = "map.png"
    img_1 = ImageTk.PhotoImage(Image.open(file))
    canvas_1.create_image(0 , 0 ,image=img_1, anchor=CENTER)
    canvas_1.config(scrollregion=canvas_1.bbox(ALL))
    xscrollbar_1.config(command=canvas_1.xview)
    yscrollbar_1.config(command=canvas_1.yview)
    tabcontrol.add(canvas_1)

def nvd_img():
    global img_2
    nvdmap(gpath)
    xscrollbar_2 = Scrollbar(right_frame, orient=HORIZONTAL)
    xscrollbar_2.grid(row=1, column=0, sticky=E + W)
    yscrollbar_2 = Scrollbar(right_frame)
    yscrollbar_2.grid(row=0, column=1, sticky=N + S)
    canvas_2 = Canvas(right_frame, xscrollcommand=xscrollbar_2.set, yscrollcommand=yscrollbar_2.set)
    canvas_2.grid(row=0, column=0, sticky=N + S + E + W)
    file = "nvd_map.png"
    img_2 = ImageTk.PhotoImage(Image.open(file))
    canvas_2.create_image(0, 0, image=img_2, anchor="center")
    canvas_2.config(scrollregion=canvas_2.bbox(ALL))
    xscrollbar_2.config(command=canvas_2.xview)
    yscrollbar_2.config(command=canvas_2.yview)
    tabcontrol.add(canvas_2)

def rr_img():
    global img_3
    rrperm(gpath)
    xscrollbar_3 = Scrollbar(right_frame, orient=HORIZONTAL)
    xscrollbar_3.grid(row=1, column=0, sticky=E + W)
    yscrollbar_3 = Scrollbar(right_frame)
    yscrollbar_3.grid(row=0, column=1, sticky=N + S)
    canvas_5 = Canvas(right_frame, bd=0, xscrollcommand=xscrollbar_3.set, yscrollcommand=yscrollbar_3.set)
    canvas_5.grid(row=0, column=0, sticky=N + S + E + W)
    file = "rr_map.png"
    img_3 = ImageTk.PhotoImage(Image.open(file))
    canvas_5.create_image(0, 0, image=img_3, anchor="center")
    canvas_5.config(scrollregion=canvas_5.bbox(ALL))
    xscrollbar_3.config(command=canvas_5.xview)
    yscrollbar_3.config(command=canvas_5.yview)
    tabcontrol.add(canvas_5)

def app_img():
    global img_4
    MAP(gpath)
    xscrollbar_4 = Scrollbar(right_frame, orient=HORIZONTAL)
    xscrollbar_4.grid(row=1, column=0, sticky=E + W)
    yscrollbar_4 = Scrollbar(right_frame)
    yscrollbar_4.grid(row=0, column=1, sticky=N + S)
    canvas_3 = Canvas(right_frame, bd=0, xscrollcommand=xscrollbar_4.set, yscrollcommand=yscrollbar_4.set)
    canvas_3.grid(row=0, column=0, sticky=N + S + E + W)
    file = "mp.png"
    img_4 = ImageTk.PhotoImage(Image.open(file))
    canvas_3.create_image(0, 0, image=img_4, anchor="center")
    canvas_3.config(scrollregion=canvas_3.bbox(ALL))
    xscrollbar_4.config(command=canvas_3.xview)
    yscrollbar_4.config(command=canvas_3.yview)
    tabcontrol.add(canvas_3)

def basic_img():
    global img_5
    basic_map(gpath)
    xscrollbar_5 = Scrollbar(right_frame, orient=HORIZONTAL)
    xscrollbar_5.grid(row=1, column=0, sticky=E + W)
    yscrollbar_5 = Scrollbar(right_frame)
    yscrollbar_5.grid(row=0, column=1, sticky=N + S)
    canvas_4 = Canvas(right_frame, bd=0, xscrollcommand=xscrollbar_5.set, yscrollcommand=yscrollbar_5.set)
    canvas_4.grid(row=0, column=0, sticky=N + S + E + W)
    file = "basic_map.png"
    img_5 = ImageTk.PhotoImage(Image.open(file))
    canvas_4.create_image(0, 0, image=img_5, anchor="center")
    canvas_4.config(scrollregion=canvas_4.bbox(ALL))
    xscrollbar_5.config(command=canvas_4.xview)
    yscrollbar_5.config(command=canvas_4.yview)
    tabcontrol.add(canvas_4)



file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

dis_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="APK", menu=dis_menu)
dis_menu.add_command(label="Show Permissions", command=perm_file)
dis_menu.add_command(label="Show Activity Names", command=act_file)
dis_menu.add_command(label="Show Intents", command=inte_file)
dis_menu.add_command(label="Show Intent Category", command=intent_cat)
dis_menu.add_command(label="Show Services", command=serv_file)
dis_menu.add_command(label="Show Providers", command=prov_file)
dis_menu.add_command(label="Show Recievers", command=recv_file)
dis_menu.add_command(label="Show App Info", command=app_file)

visual_menu = Menu(my_menu , tearoff = False)
my_menu.add_cascade(label = "Visualize", menu = visual_menu)
permissions_menu = Menu(visual_menu , tearoff = False)
permissions_menu.add_command(label = "Normal Vs Dangerous", command = nvd_img)
permissions_menu.add_command(label = "Permission Categories" , command = permap_img)
permissions_menu.add_command(label = "Read Write Permissions" , command = rr_img)
visual_menu.add_cascade(label = "Permissions", menu = permissions_menu)
visual_menu.add_command(label = "App Components" , command = app_img)
visual_menu.add_command(label = "App Features" , command = basic_img)

root.mainloop()

