from tkinter import *

root = Tk()

#THCa_var=StringVar()
#THC_var=StringVar()
#Batch_var=StringVar()

## Function Declarations
##########################################################
def thcResult():
	batchEntry = (batch.get())
	thcaEntry  = float(thca.get())
	thcEntry   = float(thc.get())

	Total_THCa = thcaEntry *.877
	Total_THC =  thcEntry + float (Total_THCa)

	dispRes.insert(0,f'Batch {batchEntry} yields a Total THCa of {Total_THCa} and a Total THC of {Total_THC}')

########################################################

# setting the windows size and name
root.geometry("400x300")
root.title('THC Calculator')
root.config(bg='#0f4b6e')

# Setting up entry variables
thca=Entry(root)
thc=Entry(root)
batch=Entry(root)

# creating a label for
# name using widget Label

batchLabel = Label(
	root,
	text='Batch',
	bg='#0f4b6e',
	fg='white'
)
thcaLabel = Label(
	root,
	text='THCa',
	bg='#0f4b6e',
	fg='white'
)
thcLabel = Label(
	root,
	text='THC',
	bg='#0f4b6e',
	fg='white'
)

# Pack Labels and Entries
batchLabel.pack()
batch.pack()
thcaLabel.pack()
thca.pack()
thcLabel.pack()
thc.pack()

# creating a button using the widget
# Button that will call the submit function
subBtn = Button(
	root,
	text='Calculate Total THC',
	relief = SOLID,
	command = thcResult
)
subBtn.pack(pady=10)

dispRes = Entry(
	root,
	width=38,
	font=('Arial',11)
)
dispRes.pack(pady=5)

# Main Loop
root.mainloop()
