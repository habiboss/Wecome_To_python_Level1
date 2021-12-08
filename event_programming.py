import tkinter

#handle for timer event

def alarm():
    print('calling the pizza company')

#handler for ringing doorbel
def doorbell():
    print('ding ding')
    print('opening the door')

#handler for when the phone rings
def phonecall():
    print("answering the phone")

#create buttons and assign callbacks
root = tkinter.Tk()
tkinter.Button(root, text='Ring Doorbel', command=doorbell).pack()
tkinter.Button(root, text="Call Phone", command=phonecall).pack()

#set a timer for 1 second
root.after(4000, alarm)

#start the event
root.mainloop()