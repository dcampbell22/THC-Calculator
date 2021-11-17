
import tkinter as tk

root=tk.Tk()

# setting the windows size and name
root.geometry("300x200")
root.title('THC Calculator')

# declaring string variable
# for storing THC, THCa, and batch inputs
THCa_var=tk.StringVar()
THC_var=tk.StringVar()
Batch_var=tk.StringVar()


# defining a function that will
# caluculate THCa and THC and
# print them on the screen
def submit():

	Batch=Batch_var.get()
	THCa=THCa_var.get()
	THC=THC_var.get()
	Total_THCa = float(THCa) *.877
	Total_THC = float (THC) + float (Total_THCa)

	print ("Production Batch: " + Batch)
	print("The THCa is: " + THCa)
	print ("The total THCa is: " + str(Total_THCa))
	print("The THC is: " + THC)
	print("The total THC is: " + str(Total_THC))
	print ("-------------------------------")

	Batch_var.set("")
	THCa_var.set("")
	THC_var.set("")


# creating a label for
# name using widget Label

Batch_label = tk.Label(root, text= 'Production Batch', font=('calibre',10, 'bold'))
Batch_entry = tk.Entry(root,textvariable = Batch_var, font=('calibre',10, 'normal'))

THCa_label = tk.Label(root, text = 'THCa Percent', font=('calibre',10, 'bold'))

# creating a entry for input
# name using widget Entry
THCa_entry = tk.Entry(root,textvariable = THCa_var, font=('calibre',10,'normal'))

THC_label = tk.Label(root, text = 'THC Percent', font=('calibre', 10, 'bold'))
THC_entry = tk.Entry(root,textvariable = THC_var, font=('calibre',10,'normal'))


# creating a button using the widget
# Button that will call the submit function
sub_btn=tk.Button(root,text = 'Submit', command = submit)

# placing the label and entry in
# the required position using grid
# method
Batch_label.grid(row=0, column=0)
Batch_entry.grid(row=0, column=1)
THC_label.grid(row=1,column=0)
THC_entry.grid(row=1, column=1)
THCa_label.grid(row=2,column=0)
THCa_entry.grid(row=2,column=1)
sub_btn.grid(row=4,column=1)

# performing an infinite loop
# for the window to display
root.mainloop()
