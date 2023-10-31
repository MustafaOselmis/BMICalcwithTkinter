import tkinter

#screen
window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=400,height=400)
window.config(padx=20,pady=20,bg="grey")

#label 1
label1 = tkinter.Label(text="Enter Your Weight (Kg)")
label1 = tkinter.Label(window, text="Enter Your Weight (Kg)", bg="black", fg="white", padx=10, pady=10)
label1.pack()

# for adding space
spacer = tkinter.Label(window, text="", padx=10, pady=10)
spacer.config(bg="grey")
spacer.pack()

#entry 1

entry1 = tkinter.Entry(width=20)
entry1.pack()

# for adding space
spacer2 = tkinter.Label(window, text="", padx=10, pady=10)
spacer2.config(bg="grey")
spacer2.pack()

#label 2
label2 = tkinter.Label(text="Enter Your Height (m)")
label2.config(bg="black")
label2.config(fg="white")
label2.config(padx=10,pady=10)
label2.pack()

# for adding space
spacer3 = tkinter.Label(window, text="", padx=10, pady=10)
spacer3.config(bg="grey")
spacer3.pack()

# entry 2

entry2 = tkinter.Entry(width=20)
entry2.pack()


# for adding space
spacer4 = tkinter.Label(window, text="", padx=10, pady=10)
spacer4.config(bg="grey")
spacer4.pack()

#function for button click



def button_clicked():
    #print("buttonclicked : ")

    try:
        weight = float(entry1.get())
        height = float(entry2.get())
    except ValueError:
        label5.config(text="Enter a valid Number")
        return



    height2 = float((height ** 2))

    abc = (weight / height2)
    if abc <= 18.4:
        label5.config(text=f'Your BMI: {abc:.2f} and you are Underweight')
    if abc > 18.5 and abc <=24.9:
        label5.config(text=f'Your BMI: {abc:.2f} and you are Normal')
    if abc > 25.0 and abc <=39.9:
        label5.config(text=f'Your BMI: {abc:.2f} and you are Overweight')
    if abc > 40:
        label5.config(text=f'Your BMI: {abc:.2f} and you are Obese')


# button

button = tkinter.Button(text="button")
button.config(padx=10,pady=10,bg="black",fg="white",command=button_clicked)
button.pack()

# for adding space
spacer5 = tkinter.Label(window, text="", padx=10, pady=10)
spacer5.config(bg="grey")
spacer5.pack()

#label 5
label5 = tkinter.Label()
label5.config(text='',bg="black",fg="white",padx=100,pady=10)
label5.pack()



window.mainloop()