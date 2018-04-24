from tkinter import *
import os

class App:
    def __init__(self, master):
        master.geometry("500x300")
        fm = Frame(master)
        Button(fm, text='Offline Face Detection').pack(side=TOP, anchor=W, fill=X, expand=YES)
        #os.startfile(r'offline_face_detection.py')
        Button(fm, text='Online Face Detection').pack(side=TOP, anchor=W, fill=X, expand=YES)
        #os.startfile(r'online_face_detection.py')
        Button(fm, text='Face Recognition').pack(side=TOP, anchor=W, fill=X, expand=YES)
        #os.startfile(r'face_recognition.py')
        Button(fm, text='Meet the Developers').pack(side=TOP, anchor=W, fill=X, expand=YES)
        #os.startfile(r'developers.py')


        fm.pack(fill=BOTH, expand=YES)
        
        
root = Tk()
root.option_add('*font', ('gabriola', 14, 'bold'))
root.title("Face Recognition System(Version X.0)")
display = App(root)
root.mainloop()
