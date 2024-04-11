import tkinter as tk

def Enter_ms():
   user= user_text.get(1.0, 'end-1c')
   
   message= menssage_text.get(1.0,'end-1c')
   main_text.config(state="normal")
   main_text.insert("end", user+':'+message+'\n')
   main_text.config(state="disabled")
   menssage_text.delete(1.0, "end")
   
def clear_ms():
    text.set("the button 1 ha sido presionado")

window =tk.Tk()
window.title("ejemplo 1-GUI")
window.config(bg="red")
frame= tk.Frame(window)
frame.pack(padx=20,pady=20)


text= tk.StringVar()
tag=tk.Label(frame, textvariable=text,width=30)
tag.pack(pady=20)

text.set("Usuario:")
user_text = tk.Text(frame,width=25,height=1,bg="blue")
user_text.pack()


button1=tk.Button(frame, text="Enter",bg="pink", width=30, command=Enter_ms)
button1.pack()
button2=tk.Button(frame, text="delet",bg="green", width=30, command=clear_ms)
button2.pack()
main_text= tk.Text(frame, width=50, state="disabled",bg="yellow")
#main_text.config(states="disabled")
main_text.pack()
menssage_text =tk.Text(frame, width=50, height=5)
menssage_text.pack()
window.mainloop()