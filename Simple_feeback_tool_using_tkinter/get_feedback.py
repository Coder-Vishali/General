from tkinter import *
import tkinter.messagebox
import pandas as pd
import tkinter.ttk as ttk

Question = ["Type Question 1 .........?",
            "Type Question 2 .........?",
            "Type Question 3 .........?",
            "Type Question 4 .........?",
            "Type Question 5 .........?"]
root = Tk()
root.geometry("1000x800")
root.title('Feedback Form')
# ------------------------------------Colour Fix----------------------------------------
myColor = '#F9DFAF'
root.configure(bg=myColor)
s = ttk.Style()
s.configure('Wild.TRadiobutton', background=myColor, foreground='black')


def radio_button(y_len, var):
    ttk.Radiobutton(root, text="Very Sad", variable=var, value="Very Sad",
                    style='Wild.TRadiobutton').place(x=235, y=y_len)
    ttk.Radiobutton(root, text="Sad", variable=var, value="Sad",
                    style='Wild.TRadiobutton').place(x=350, y=y_len)
    ttk.Radiobutton(root, text="Neutral", variable=var, value="Neutral",
                    style='Wild.TRadiobutton').place(x=490, y=y_len)
    ttk.Radiobutton(root, text="Happy", variable=var, value="Happy",
                    style='Wild.TRadiobutton').place(x=650, y=y_len)
    ttk.Radiobutton(root, text="Very Happy", variable=var, value="Very Happy",
                    style='Wild.TRadiobutton').place(x=780, y=y_len)

# -------------------------------------------------------------------------------------
title_1 = Label(root, text="Simple Feedback Survey", width=20, font=("bold", 20), background=myColor)
title_1.place(x=360, y=70)
# -----------------------------------Get Name------------------------------------------
label_1 = Label(root, text="FullName", width=20, font=("bold", 10), background=myColor)
label_1.place(x=80, y=130)
entry_1 = Entry(root)
entry_1.place(width=200, height=20, x=240, y=130)
# -------------------------------Question and Answer------------------------------------
label_2 = Label(root, text="Question 1", width=20, font=("bold", 10), background=myColor)
label_2.place(x=80, y=180)
label_3 = Label(root, text=Question[0], width=33, font=("bold", 10), background=myColor)
label_3.place(x=240, y=180)
label_4 = Label(root, text="Answer", width=20, font=("bold", 10), background=myColor)
label_4.place(x=70, y=220)
var = StringVar()
radio_button(y_len=220, var=var)
# ----------------------------------------------------------------------------------------
# -------------------------------Question and Answer------------------------------------
label_5 = Label(root, text="Question 2", width=20, font=("bold", 10), background=myColor)
label_5.place(x=80, y=265)
label_6 = Label(root, text=Question[1], width=35, font=("bold", 10), background=myColor)
label_6.place(x=240, y=265)
label_7 = Label(root, text="Answer", width=20, font=("bold", 10), background=myColor)
label_7.place(x=70, y=305)
var1 = StringVar()
radio_button(y_len=305, var=var1)
# ----------------------------------------------------------------------------------------
# -------------------------------Question and Answer------------------------------------
label_8 = Label(root, text="Question 3", width=20, font=("bold", 10), background=myColor)
label_8.place(x=80, y=350)
label_9 = Label(root, text=Question[2], width=35, font=("bold", 10), background=myColor)
label_9.place(x=240, y=350)
label_10 = Label(root, text="Answer", width=20, font=("bold", 10), background=myColor)
label_10.place(x=70, y=390)
var2 = StringVar()
radio_button(y_len=390, var=var2)
# ----------------------------------------------------------------------------------------
# -------------------------------Question and Answer------------------------------------
label_11 = Label(root, text="Question 4", width=20, font=("bold", 10), background=myColor)
label_11.place(x=80, y=435)
label_12 = Label(root, text=Question[3], width=29, font=("bold", 10), background=myColor)
label_12.place(x=240, y=435)
label_13 = Label(root, text="Answer", width=20, font=("bold", 10), background=myColor)
label_13.place(x=70, y=475)
var3 = StringVar()
radio_button(y_len=475, var=var3)
# ----------------------------------------------------------------------------------------
# -------------------------------Question and Answer------------------------------------
label_14 = Label(root, text="Question 5", width=20, font=("bold", 10), background=myColor)
label_14.place(x=80, y=520)
label_15 = Label(root, text=Question[4], width=40, font=("bold", 10), background=myColor)
label_15.place(x=240, y=520)
label_16 = Label(root, text="Answer", width=20, font=("bold", 10), background=myColor)
label_16.place(x=70, y=560)
var4 = StringVar()
radio_button(y_len=560, var=var4)
# ----------------------------------------------------------------------------------------
label_17 = Label(root, text="Comments", width=20, font=("bold", 10), background=myColor)
label_17.place(x=80, y=650)
entry_2 = Entry(root)
entry_2.place(width=600, height=60, x=240, y=620)


def save_data():
    in_list = [["Name", entry_1.get()], [Question[0], var.get()], [Question[1], var1.get()], [Question[2], var2.get()],
               [Question[3], var3.get()], [Question[4], var4.get()], ["Comments", entry_2.get()]]
    out_list = pd.DataFrame(in_list)
    pd.set_option('display.max_columns', 500)
    out_list.to_csv('survey.csv', index=False, header=False)


def onClick():
    tkinter.messagebox.showinfo("XYZ Team", "Thanks For Your Response")


Button(root, text='Submit', font=("bold", 10), width=20, bg="black", fg='white',
       command=lambda: [save_data(), onClick(), root.destroy()]).place(x=450, y=730)

root.mainloop()
