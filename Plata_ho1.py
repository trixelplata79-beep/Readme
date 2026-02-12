import tkinter as tk

window = tk.Tk()

window.title("MY PROFILE")
window.geometry("600x600")
window.resizable(True,True)
window.configure(bg="lightgreen",cursor="cross")

label = tk.Label(window,text="MY PROFILE",font=("poppins",25),fg="black",bg="lightgreen",anchor="center")
label.pack(padx=5,pady=20)

label = tk.Label(window,text="Name : Trixel L. Plata",font=("poppins",8),fg="black",bg="lightgreen", anchor="center")
label.pack(anchor="w",pady=20)

label = tk.Label(window,text="Age : 18 years old",font=("poppins",8),fg="black",bg="lightgreen",anchor="center")
label.pack(anchor="w",pady=20)

label = tk.Label(window,text="Course : BSIT",font=("poppins",8),fg="black",bg="lightgreen",anchor="center")
label.pack(anchor="w",pady=20)

label = tk.Label(window,text="Birthday : March 30,2007",font=("poppins",8),fg="black",bg="lightgreen",anchor="center")
label.pack(anchor="w",pady=20)

label = tk.Label(window,text="Motto :",font=("poppins",8),fg="black",bg="lightgreen",anchor="center")
label.pack(anchor="w",pady=20)

label = tk.Label(window,text="Trust The Process",font=("poppins",8),fg="black",bg="lightgreen",anchor="center")
label.pack(padx=5,pady=20)

window.mainloop()