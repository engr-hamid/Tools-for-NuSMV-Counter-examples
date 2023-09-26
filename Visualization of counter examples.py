 #first Run these commands in CMD 1.pip install tkinter 2.pip install matplotlib.pyplot
#then save this code on destop and run it.   (.txt and .csv formats are accepted u can add more then)

#from re import T
from tkinter import filedialog
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



root= tk.Tk()

canvas1 = tk.Canvas(root, width = 500, height = 300)
canvas1.pack()
label1 = tk.Label(root, text='Graph Ploter for NuSMV')
label1.config(font=('Arial', 16))
canvas1.create_window(250, 50, window=label1)

def read():
    global names,arr,traces,exec1,trace_data
    try:
        
        file_path1= filedialog.askopenfilename(title = "Select A File", filetypes = (("CSV files", "*.CSV"),
        ("Text Files", "*.txt")))
        with open(file_path1, "r") as file:
            first_line = file.readline()
        names = first_line.split()
        del names[0]
        del names[0]
        index = 0
        traces=[]
        trace_data=[]
        with open(file_path1, "r") as openfile:
            for line in openfile:
                index += 1 
                for part in line.split():
                    if "Steps\Vars" in part or "Steps" in part:
                        traces.append(index)
                        #print(index)
        #print(list(traces))
        
        size=len(traces)
        size_itr=size
        if size>1:
            head=0
            for i in range(1,size):
                row=traces[i]-traces[i-1]#12
                mydata=np.genfromtxt(file_path1, skip_header=head,max_rows=row)
                arr = mydata[1:,2:]
                trace_data.append(arr)
                #print('Data for trace ',i,'=\n', arr )
                head=head+row#13
                size_itr=size_itr-1#3-1
                #show_graph(arr)
        if size_itr==1:
                head=traces[size-1]-1
                mydata=np.genfromtxt(file_path1, skip_header=head,)
                arr = mydata[1:,2:]
                trace_data.append(arr)
        exec1=1
                

    except:
        messagebox.showerror("Error", "File could not be open please try again")
        exec1=0
    #print(list(names))
    #print(list(trace_data))
    traces_info()

global label2,button

def traces_info():

    if exec1==1:
        global label2,button
        label2.destroy()
        button.destroy()
        trc=len(traces)
        #trc=
        #text1='There are '+str(trc),' avalible in the current file.Select the trace to display.'
        #text1=str(text1)
        label=tk.Label(root, text='Please select the trace to be displayed')
        canvas1.create_window(250,90 , window=label)
        canvas1.pack()
        global value_inside1
        options_list = range(1,trc+1)
        value_inside1 = tk.StringVar(root)
        value_inside1.set("Select Trace")
        select_node1 = tk.OptionMenu(root, value_inside1, *options_list)
        canvas1.create_window(200, 120, window=select_node1) 
       
        button_s = tk.Button (root, text='Show Graph', command=show_graph, bg='palegreen2', font=('Arial', 9, 'bold'))
        canvas1.create_window(310, 120, window=button_s)


global show
show=0
def show_graph():
    global show
    if show==1:
        #plt.cla()
        plt.close()
        show=0

    display_trace_no=int(value_inside1.get())
    ind=display_trace_no-1
    arr=trace_data[ind]
    lenght=len(names)
    steps=len(arr)+1
    Values=range(1,steps)
    Values=list(Values)
    x = range(1, steps)
    
    
    #print('value of x',x,'  values ', Values)
    y=[0,1]

    global fig,leg,my_lines
    my_lines=[]
    fig, ax = plt.subplots()
    ax.set_title('Click on legend line to view a particular entity',fontsize=15)
    for a in range(lenght):
        line1, = ax.plot(x, arr[:, a], lw=2, marker='o', label=names[a])
        my_lines.append(line1)
    leg = ax.legend(fancybox=True, shadow=True,fontsize=10)
    lines_div()

    fig.canvas.mpl_connect('pick_event', on_pick)

    fontsize=15
    plt.xlabel('Steps',fontsize=fontsize)
    plt.ylabel('Qualitative States',fontsize=fontsize)
    y=range(0,2)
    Values1=[0,1]
    plt.xticks(x,Values)
    plt.yticks(y,Values1)
   
    #plt.yticks(x,yvalues)
    #plt.legend()
    show=1
    plt.show()    
          
          

def lines_div():
    #lines = [line1, line2]
    lines=list(my_lines)
    global lined
    lined = {}  # Will map legend lines to original lines.
    for legline, origline in zip(leg.get_lines(), lines):
        legline.set_picker(7)  # Enable picking on the legend line.
        legline.set_linewidth(3.0)
        lined[legline] = origline




def on_pick(event):
    # On the pick event, find the original line corresponding to the legend
    # proxy line, and toggle its visibility.
    legline = event.artist
    origline = lined[legline]
    visible = not origline.get_visible()
    origline.set_visible(visible)
    # Change the alpha on the line in the legend so we can see what lines
    # have been toggled.
    legline.set_alpha(1.0 if visible else 0.2)
    fig.canvas.draw()




label2=tk.Label(root, text='Please Select a File to Visualize')
canvas1.create_window(250,90 , window=label2)
canvas1.pack()
button = tk.Button (root, text=' Browse the file', command=read, bg='palegreen2', font=('Arial', 10, 'bold')) 
canvas1.create_window(250, 120, window=button)

button3 = tk.Button (root, text='Exit', command=root.destroy, bg='lightsteelblue2', font=('Arial', 9, 'bold'))
canvas1.create_window(250, 160, window=button3)

root.title('Graph Ploter for NuSMV')
root.mainloop()