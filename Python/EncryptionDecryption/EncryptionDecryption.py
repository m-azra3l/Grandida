from tkinter import *
import base64
from tkinter import messagebox
import tkinter.font as font
from tkinter import scrolledtext

#Encoding Function
def encode(key, msg):
    enc = []
    for i in range(len(msg)):
        list_key = key[i % len(key)]
        list_enc = chr((ord(msg[i]) +
                     ord(list_key)) % 256)
        enc.append(list_enc)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


#Decoding Function
def decode(key, code):
    dec = []
    enc = base64.urlsafe_b64decode(code).decode()
    for i in range(len(enc)):
        list_key = key[i % len(key)]
        list_dec = chr((256 + ord(enc[i]) - ord(list_key)) % 256)

        dec.append(list_dec)
    return "".join(dec)

#Function that executes on clicking Enc/Dec button
def Result():
    myinput = msg.get("1.0", "end-1c")
    k= key.get()
    i = mode.get()
    if (i==1):
        res.insert(END,(encode(k, myinput)))
    elif(i==2):
        res.insert(END,(decode(k, myinput)))
    else:
        messagebox.showinfo('Encryption Decryption', 'Please Choose one of Encryption or Decrption. Try again.')

#Function that executes on clicking Clear button
def Reset():
    msg.delete(1.0,END)
    key.set("")
    mode.set(0)
    res.delete(1.0,END)
    

wn = Tk()
wn.geometry("515x560")
wn.configure(bg='blue')
wn.title("Encrypt and Decrypt Messages")

key = StringVar()
mode = IntVar()

label1 = Label(wn, text='Enter message:', font=('Courier',10))
label1.place(x=50,y=40)

msg = scrolledtext.ScrolledText(wn, wrap=WORD,width=36, height=7,font=("calibre", 10,'normal'))
msg.grid(column=0, row=2, pady=40, padx=200)

label2 = Label(wn, text='Enter key:', font=('Courier',10))
label2.place(x=50,y=195)

InpKey = Entry(wn, textvariable=key, font=('calibre',10,'normal'))
InpKey.place(x=200,y=195,width=270)

label3 = Label(wn, text='Select action:', font=('Courier',10))
label3.place(x=200,y=255)

Radiobutton(wn, text='Encrypt', variable=mode, value=1).place(x=200,y=285) 
Radiobutton(wn, text='Decrypt', variable=mode, value=2).place(x=300,y=285) 

label3 = Label(wn, text='Result:', font=('Courier',10))
label3.place(x=50,y=350)

res = Text(wn, font=('calibre',10,'normal'))
res.place(x=200,y=350, width=270, height=100)


ResetBtn = Button(wn, text='Clear', bg='white', fg='black', width=10,height=1,command=Reset)
ResetBtn['font'] = font.Font( size=12)
ResetBtn.place(x=50,y=490)

ShowBtn = Button(wn,text="Enc/Dec",bg='white', fg='black',width=10,height=1,command=Result)
ShowBtn['font'] = font.Font( size=12)
ShowBtn.place(x=212,y=490)

QuitBtn = Button(wn, text='Exit', bg='white', fg='black',width=10,height=1, command=wn.destroy)
QuitBtn['font'] = font.Font( size=12)
QuitBtn.place(x=370,y=490)


wn.mainloop()
