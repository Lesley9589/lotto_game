from tkinter import *
from tkinter import messagebox
import datetime

root = Tk()
root.title("National Lottery")
root.geometry("500x200")

# To display time and date in the gui
date_time = datetime.datetime.now()
lbl_date = Label(root, text=date_time)
lbl_date.grid(row=7, column=2)

#entry box to enter details when logging in
entry10 = Entry(root)
entry11 = Entry(root)
lbl1 = Label(root, text="Login To Play:")
lbl2 = Label(root, text="Name And Surname:")
lbl3 = Label(root, text="Age:")

#function to capture age upon logging in
def ages():
    try:
        age = int(entry10.get())
        if age >= 18:
            messagebox.showinfo("Processing", "Good luck")
            root.withdraw()
            second_window()

        else:
            messagebox.showinfo("Processing", "Due To Your Age You Are Unable To Play")

    except ValueError:
        messagebox.showerror("ERROR", "Please Enter Your Age!")

#second gui window to play lotto
def second_window():

    window = Tk()
    window.title("Ithuba")
    window.geometry("407x560")

    label1 = Label(window, text="Input Your Lotto Numbers:")

    text1 = Text(window, height=5, width=50)
    text2 = Text(window, height=5, width=50)
    text3 = Text(window, height=5, width=50)

#six entry boxes to input your choice of numbers
    entry2 = Entry(window, width=2)
    entry2.grid(row=2, column=1)

    entry3 = Entry(window, width=2)
    entry3.grid(row=2, column=2)

    entry4 = Entry(window, width=2)
    entry4.grid(row=2, column=3)

    entry5 = Entry(window, width=2)
    entry5.grid(row=2, column=4)

    entry6 = Entry(window, width=2)
    entry6.grid(row=2, column=5)

    entry7 = Entry(window, width=2)
    entry7.grid(row=2, column=6)

#function to make random numbers for the draw
    numbers = []

    def win():
        for x in range(6):
            import random
            mynumbers = random.randint(1, 49)
            numbers.append(mynumbers)
        text1.delete(0.0, END)
        text1.insert(0.0, numbers)
        return numbers

#six functions to retrieve user inputs and place it in a textbox
    def winning1():
        num1 = entry2
        a = num1.get()
        entry1.delete(1.0, END)
        entry1.insert(END, a + '  ')

    def winning2():
        num2 = entry3
        b = num2.get()
        entry1.delete(2.0, END)
        entry1.insert(END, b + '  ')

    def winning3():
        num3 = entry4
        c = num3.get()
        entry1.delete(3.0, END)
        entry1.insert(END, c + '  ')

    def winning4():
        num4 = entry5
        d = num4.get()
        entry1.delete(4.0, END)
        entry1.insert(END, d + '  ')

    def winning5():
        num5 = entry6
        e = num5.get()
        entry1.delete(5.0, END)
        entry1.insert(END, e + '  ')

    def winning6():
        num6 = entry7
        f = num6.get()
        entry1.delete(6.0, END)
        entry1.insert(END, f)

#function to compare the winning numbers to the user's numbers + file_write
    def lotto_plus():
        try:
            g = [int(entry2.get()), int(entry3.get()), int(entry4.get()), int(entry5.get()), int(entry6.get()),
                 int(entry7.get())]
            matched = [x for x in numbers if x in g]
            text2.insert(1.0, matched)
            mymoney = {6: "R10 000 000.00", 5: "R8 584.00", 4: "R2 384.00", 3: "R100.50", 2: "R20.00", 1: "R0.00",
                       0: "R0.00"}
            x = mymoney.get(len(matched))
            text3.insert(END, x)
            file_write = open("textfile.txt", "a+")
            file_write.write("Name and Surname: " + str(entry11.get()) + "\n")
            file_write.write("Age: " + entry10.get() + "\n")
            file_write.write("Chosen Numbers: " + str(g) + "\n")
            file_write.write("Lotto Results: " + str(numbers) + "\n")
            file_write.write("Total Earnings: " + str(x) + "\n")
            file_write.write("Time and Date: " + str(date_time) + "\n" + "\n")
            file_write.close()

        except ValueError:
            messagebox.showerror("ERROR", "Please Enter Values")

# buttons and labels to make the gui user friendly
    all_commands = lambda: [winning1(), winning2(), winning3(), winning4(), winning5(), winning6()]

    button8 = Button(window, text="Proceed", command=all_commands)
    button8.grid(row=3, columnspan=7)

    button1 = Button(window, text="Check The Winning Numbers", command=win)
    entry1 = Text(window, height=5, width=50)

    button2 = Button(window, text="Compare Numbers", command=lotto_plus)

    label2 = Label(window, text="Here is your total winnings:")

    def done():
        window.destroy()

    button3 = Button(window, text="Done", command=done)

#grid to place widgets
    label1.grid(row=1, columnspan=7)
    entry1.grid(row=4, columnspan=7)
    button1.grid(row=5, columnspan=7)
    button2.grid(row=8, columnspan=7)
    text1.grid(row=7, columnspan=7)
    text2.grid(row=11, columnspan=7)
    label2.grid(row=13, columnspan=7)
    text3.grid(row=14, columnspan=7)
    button3.grid(row=15, columnspan=7)
    window.mainloop()

btn = Button(root, text="Proceed", command=ages)

#grid to place widgets
entry10.grid(row=5, column=4, columnspan=8)
entry11.grid(row=3, column=4, columnspan=8)
lbl1.grid(row=1, column=4, columnspan=8)
lbl2.grid(row=2, column=4, columnspan=8)
lbl3.grid(row=4, column=4, columnspan=8)
btn.grid(row=6, column=4, columnspan=8)
root.mainloop()