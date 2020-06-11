import tkinter as tk
from tkinter import *
import tkinter.messagebox

root = tk.Tk()

root.title("Currency Conversion")

Tops = Frame(root, bg='#000000', pady=2, width=2000, height=100, relief="ridge")
Tops.grid(row=0, column=0)

head = tk.Label(Tops, font=('Comic Sans MS', 19, 'bold'), text='                                Currency Converter  ',
                     bg='#000000', fg='white')
head.grid(row=1, column=0, sticky=W)

variable = tk.StringVar(root)
variable1 = tk.StringVar(root)

variable.set("currency")
variable1.set("currency")


def RealTimeCurrencyConversion():
    from forex_python.converter import CurrencyRates
    c = CurrencyRates()

    from_currency = variable.get()
    to_currency = variable1.get()

    if Amount1_field.get() == "":
        tkinter.messagebox.showinfo("Error !!", "Amount Not Entered.\n Enter valid amount.")

    elif from_currency == "currency" or to_currency == "currency":
        tkinter.messagebox.showinfo("Error !!",
                                    "Currency Not Selected.\n Please select Currency form menu.")

    else:
        new_amt = c.convert(from_currency, to_currency, float(Amount1_field.get()))
        new_amount = float("{:.4f}".format(new_amt))
        Amount2_field.insert(0, str(new_amount))


def clear_all():
    Amount1_field.delete(0, tk.END)
    Amount2_field.delete(0, tk.END)


currency_list = ["INR", "USD", "DKK", "EUR", "CAD", "CNY"]

root.configure(background='#e6e5e5')
root.geometry("700x400")

Label_1 = Label(root, font=('Comic Sans MS', 27, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=1, column=0, sticky=W)

label1 = tk.Label(root, font=('Comic Sans MS', 15, 'bold'), text="\t    Amount  :  ", bg="#e6e5e5", fg="black")
label1.grid(row=2, column=0, sticky=W)

label1 = tk.Label(root, font=('Comic Sans MS', 15, 'bold'), text="\t    From Currency  :  ", bg="#e6e5e5", fg="black")
label1.grid(row=3, column=0, sticky=W)

label1 = tk.Label(root, font=('Comic Sans MS', 15, 'bold'), text="\t    To Currency  :  ", bg="#e6e5e5", fg="black")
label1.grid(row=4, column=0, sticky=W)

label1 = tk.Label(root, font=('Comic Sans MS', 15, 'bold'), text="\t   Converted Amount  :  ", bg="#e6e5e5", fg="black")
label1.grid(row=8, column=0, sticky=W)

Label_1 = Label(root, font=('Comic Sans MS', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=5, column=0, sticky=W)

Label_1 = Label(root, font=('Comic Sans MS', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=7, column=0, sticky=W)

FromCurrency_option = tk.OptionMenu(root, variable, *currency_list)
ToCurrency_option = tk.OptionMenu(root, variable1, *currency_list)

FromCurrency_option.grid(row=3, column=0, ipadx=45, sticky=E)
ToCurrency_option.grid(row=4, column=0, ipadx=45, sticky=E)

Amount1_field = tk.Entry(root)
Amount1_field.grid(row=2, column=0, ipadx=28, sticky=E)

Amount2_field = tk.Entry(root)
Amount2_field.grid(row=8, column=0, ipadx=31, sticky=E)

Label_9 = Button(root, font=('arial', 15, 'bold'), text="   Convert  ", padx=2, pady=2, bg="Red", fg="white",
                 command=RealTimeCurrencyConversion)
Label_9.grid(row=6, column=0)

Label_1 = Label(root, font=('Comic Sans MS', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=9, column=0, sticky=W)

Label_9 = Button(root, font=('arial', 15, 'bold'), text="   Clear All  ", padx=2, pady=2, bg="white", fg="red",
                 command=clear_all)
Label_9.grid(row=10, column=0)

root.mainloop()
