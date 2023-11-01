from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root=Tk()
root.geometry("600x600")
root.config(background="black")

label_image=Label(root,bg="white", highlightthickness=5)
label_image.place(relx=0.5,rely=0.5,anchor=CENTER)
 
img_path=""
def openFile():
    global img_path
    img_path = filedialog.askopenfilename(title="Open Text File",filetypes=[("Image Files","*.jpg *.gif *.png *.jpg")])
    print(img_path)
    im=Image.open(img_path)    
    img=ImageTk.PhotoImage(im)
    label_image["image"]=img
    img.close()
    
def rotateImage():
    global img_path
    im =Image.open(img_path)
    img=ImageTk.PhotoImage(im.rotate(180))
    label_image["image"]=img
    print(img_path)
    img.close()

btn=Button(root,text="Open Image",font=("Times New Roman", 12), bg="grey",fg="white",command=openFile,relief=SOLID,padx=15,pady=15)
btn.place(relx=0.5,rely=0.1,anchor=CENTER)


btn=Button(root,text="Rotate Image",font=("Times New Roman", 12), bg="grey",fg="white",command=rotateImage,relief=SOLID,padx=15,pady=15)
btn.place(relx=0.5,rely=0.85,anchor=CENTER)

label_footer=Label(root,text="Creater by Yuvan",bg="black",fg="white")
label_footer.place(relx=0.5,rely=0.95,anchor=CENTER)

root.mainloop()
