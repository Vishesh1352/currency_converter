import tkinter as tk
from tkinter import *
from tkinter import ttk

from fetchapi import *


def Err_msg(Error_msg):
    err_text = ""
    for i in Error_msg:
        err_text = err_text+i+"\n"
    error_label.config(text=err_text)


def lable_clear():

    result_label.config(text="")
    error_label.config(text="")


def text_clear():

    from_currency_combo.set('')
    to_currency_combo.set('')
    amount_entry.delete(0, END)
    lable_clear()


def convert_currency():
    counter = 0
    Error_msg = []
    lable_clear()

    source = from_currency_combo.get()
    if source not in currencies.keys():
        Error_msg.append("Please enter valid value in FROM field.")
        counter += 1

    destination = to_currency_combo.get()
    if destination not in currencies.keys():
        Error_msg.append("Please enter valid value in TO field.")
        counter += 1

    try:
        amount = amount_entry.get()
        amount_int = int(amount)
    except ValueError:
        counter += 1
        Error_msg.append("Please enter integer value in AMOUNT field.")
        return Err_msg(Error_msg)

    if amount_int <= 0 or amount_int == NONE:
        counter += 1
        Error_msg.append("Please enter integer value in AMOUNT field.")

    if counter == 0:
        result_arg = web_int+API_KEY+"/pair/"+source+"/"+destination+"/"+amount
        result = requests.get(f'{result_arg}').json()
        converted_result = result['conversion_result']
        formatted_result = f'{amount} {source} = {converted_result} {destination}'
        result_label.config(text=formatted_result)

    elif counter > 0:
        Err_msg(Error_msg)


white = '#FFFFFF'
primary = '#7C0A02'
secondary = '#32CBFF'

root = tk.Tk()
root.title("Currency_Converter")
root.geometry(str(350)+"x"+str(400)+"+"+str(350)+"+"+str(400))
root.resizable(height=FALSE, width=FALSE)

top_frame = Frame(root, bg=primary, width=350, height=400)
top_frame.grid(row=0, column=0)

name_label = Label(top_frame, text='Currency Converter', bg=primary,
                   fg=white, pady=35, padx=50, justify=CENTER, font=('Poppins 20 bold'))
name_label.grid(row=0, column=0)

bottom_frame = Frame(root, width=350, height=400)
bottom_frame.grid(row=1, column=0)

from_currency_label = Label(
    bottom_frame, text='FROM:', font=('Poppins 10 bold'), justify=LEFT)
from_currency_label.place(x=100, y=10)
from_currency_combo = ttk.Combobox(bottom_frame, values=list(
    currencies.keys()), width=14, font=('Poppins 10 bold'))
from_currency_combo.place(x=100, y=30)

to_currency_label = Label(bottom_frame, text='TO:',
                          font=('Poppins 10 bold'), justify=LEFT)
to_currency_label.place(x=100, y=60)
to_currency_combo = ttk.Combobox(bottom_frame, values=list(
    currencies.keys()), width=14, font=('Poppins 10 bold'))
to_currency_combo.place(x=100, y=80)

amount_label = Label(bottom_frame, text='AMOUNT:', font=('Poppins 10 bold'))
amount_label.place(x=115, y=115)
amount_entry = Entry(bottom_frame, width=25, font=('Poppins 15 bold'))
amount_entry.place(x=25, y=135)

result_label = Label(bottom_frame, text='', font=('Poppins 10 bold'))
result_label.place(x=105, y=165)

error_label = Label(bottom_frame, text='', font=('Poppins 10 bold'))
error_label.place(x=8, y=165)

convert_button = Button(bottom_frame, text="CONVERT", bg=secondary, fg=white, font=(
    'Poppins 10 bold'), command=convert_currency)
convert_button.place(x=25, y=245)

Clear_button = Button(bottom_frame, text="CLEAR", bg=secondary,
                      fg=white, font=('Poppins 10 bold'), command=text_clear)
Clear_button.place(x=225, y=245)

root.mainloop()