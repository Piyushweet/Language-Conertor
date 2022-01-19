#first of install the reqired module from the command 
/// if you are using vscode the
pip install tkinter
pip install googletrans
pip install textblob

if using colab or anaconda use
!pip install tkinter
!pip install googletrans
!pip install textblob
///
#importing modules needed
from cProfile import label
from fnmatch import translate
from math import comb
from tkinter import *
from tkinter import ttk,messagebox
from turtle import width
import googletrans
import textblob


#creating main windoe button 
root=Tk()
root.title("Language Translator")
root.geometry("1080x500")

label2=Label(root,text ="Created By: Piyush", font = 'arial 35 bold', bg ='#022c5c' , width = '16')
label2.place(x=300,y=440)

label3=Label(root,text ="LANGUAGE TRANSLATOR", font = 'arial 40 bold', bg ='#022c5c' , width = '22')
label3.place(x=180,y=0)

#getting Language to be translate
def label_change():
    c=combo1.get()
    c1=combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000,label_change)

    
#function to translate the language
def translate_now():
    global language
    try:
        text_=text1.get(1.0,END)
        c2=combo1.get()
        c3=combo2.get()
        if(text_):
            words=textblob.TextBlob(text_)
            lan=words.detect_language()
            for i,j in language.items():
                if(j==c3):
                    lan_=i
            words=words.translate(from_lang=lan,to=str(lan_))
            text2.delete(1.0,END)
            text2.insert(END,words)
    except Exception as e:
        messagebox.showerror("googletrans","please try again")



language=googletrans.LANGUAGES
languageV=list(language.values())
lang1=language.keys()

#for chossing language
combo1=ttk.Combobox(root,values=languageV,font="Roboto 14",state="r")
combo1.place(x=110,y=85)
combo1.set("ENGLISH")

#conforming that language is selected
label1=Label(root,text="ENGLISH",font="segoe 30 bold",bg="white",width=18,bd=5,relief=GROOVE)
label1.place(x=10,y=115)

#Building the block where to insert text
f=Frame(root,bg="Black",bd=5)
f.place(x=10,y=183,width=440,height=210)

text1=Text(f,font="Robeto 20",bg="white",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=430,height=200)

#for making the scroll bar active
scrollbar1=Scrollbar(f)
scrollbar1.pack(side="right",fill="y")

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

#for chossing language
combo2=ttk.Combobox(root,values=languageV,font="Roboto 14",state="r")
combo2.place(x=730,y=85)
combo2.set("SELECT LANGUAGE")

#conforming that language is selected
label2=Label(root,text="ENGLISH",font="segoe 30 bold",bg="white",width=18,bd=5,relief=GROOVE)
label2.place(x=620,y=115)


#Building the block where to output text to be showed
f1=Frame(root,bg="Black",bd=5)
f1.place(x=620,y=183,width=440,height=210)

text2=Text(f1,font="Robeto 20",bg="white",relief=GROOVE,wrap=WORD)
text2.place(x=0,y=0,width=430,height=200)



#for making the scroll bar active
scrollbar2=Scrollbar(f1)
scrollbar2.pack(side="right",fill="y")

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)


#creating translate button
translate=Button(root,text="Translate",font="Roboto 15 bold italic",activebackground="#f9e4ad",cursor="hand2",bd=5,bg="#ea9f5a",fg="white",command=translate_now)
translate.place(x=480,y=250)


label_change()

root.configure(bg="#5ec4db")
root.mainloop()
