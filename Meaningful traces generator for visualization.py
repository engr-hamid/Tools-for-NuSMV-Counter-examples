#first Run these commands in CMD 1.pip install tkinter 2.pip install matplotlib.pyplot
#then save this code on destop and run it.   (.txt and .csv formats are accepted u can add more then)

from tkinter import filedialog
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
import re


root= tk.Tk()
names=[]
canvas1 = tk.Canvas(root, width = 500, height = 300)
canvas1.pack()
label1 = tk.Label(root, text='File generator for Visualization')
label1.config(font=('Arial', 16))
canvas1.create_window(250, 50, window=label1)

def read():
        global names,arr,traces,exec1,trace_data
    #try:
        
        file_path1= filedialog.askopenfilename(title = "Select A File", filetypes = (("Text Files", "*.txt"),("CSV files", "*.CSV"),
         ))

        with open(file_path1, "r") as f:
            lines = f.readlines() 
        with open(file_path1, "w") as new_f:
            for line in lines:
                if not line.startswith("***") and not line.startswith("    u") and not line.isspace() and not line.startswith("Trace")and not line.startswith("-- as") and not line.startswith("  -> I")and not line.startswith("-- as") and not line.startswith("  -- Loop"):
                    new_f.write(line)
                    
        #with open(file_path1, "r") as file:
            #first_line = file.readline()
        #names = first_line.split()
        #del names[0]
        #del names[0]
        
        index = 0
        traces=[]
        trace_location=[]
        trace_data=[]
        with open(file_path1, "r") as openfile:
            #data_lines = openfile.readlines()
            for line in openfile:
                index += 1 
                for part in line.split():
                    if "--" in part:
                        traces.append(index)
                        #print(index)
        #CTL_SPEC=[]
        control=0
        line_index=0
        file_data=[]
        
        output_control=traces.copy()
        del output_control[0]
        #print(traces)
        #print(output_control)
        data={ "Steps": "-", "input": "-", }
        with open(file_path1, "r") as open_file:
            
            
            for line in open_file:
                line_index= line_index+ 1 
                line = str(line)

                if not (line_index in traces):
                    line = re.split(r'(\s+)', line)
                    line=' '.join(line).split()
                    #print(line)
                    if line[0]!='->':
                        data.update({line[0] : line[2]}) 
                    elif line[2]=='1.1':
                        control=1
                        continue                     
                        #if line[2]=='1.1' and len(data) == 2:
                    elif line[1]=='State:' and line[2]!='1.1':
                        if control==1:
                            l_keys=list(data.keys())
                            print(*l_keys, sep='\t')
                            n='\t'.join(l_keys)
                            file_data.append(n)
                        l_values=list(data.values())
                        print(*l_values, sep='\t')
                        m='\t'.join(l_values)
                        file_data.append(m)
                        control=2
                        continue
                else:
                    if line_index in output_control:
                        if control==1:
                            l_keys=list(data.keys())
                            print(*l_keys, sep='\t')
                            n='\t'.join(l_keys)
                            file_data.append(n)
                            control=2

                        l_values=list(data.values())
                        print(*l_values, sep='\t')
                        m='\t'.join(l_values)
                        file_data.append(m)
                    #CTL_SPEC.append(line)
                    control=0
                    print(line)
                    #file_data.append(line)

        if control==1:
            l_keys=list(data.keys())
            print(*l_keys, sep='\t')
            n='\t'.join(l_keys)
            file_data.append(n)
            control=2            

        l_values=list(data.values())
        print(*l_values, sep='\t')
        m='\t'.join(l_values)
        file_data.append(m)
        

        textfile = open(file_path1, "w")
        for element in file_data:
                textfile.write(element + "\n")
        textfile.close()

        with open(file_path1, "r") as f:
            lines = f.readlines() 
        with open(file_path1, "w") as new_f:
            for line in lines:
                if not line.isspace():
                    new_f.write(line)

label2=tk.Label(root, text='Please select a File to make it ready for visualization')
canvas1.create_window(250,90 , window=label2)
canvas1.pack()
button = tk.Button (root, text=' Browse the file', command=read, bg='palegreen2', font=('Arial', 9, 'bold')) 
canvas1.create_window(250, 120, window=button)

button3 = tk.Button (root, text='Exit', command=root.destroy, bg='lightsteelblue2', font=('Arial', 9, 'bold'))
canvas1.create_window(250, 160, window=button3)

root.title('File generator for Visualization')
root.mainloop()