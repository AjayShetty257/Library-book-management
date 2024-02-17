
import sqlite3

from tkinter import *
import tkinter.ttk as tkk


root = Tk()

def Database():
    global conn, cursor
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('create table if not exists library(title text, author text, year integer, isbn integer)')

def Create():
    if title.get() == " " or author.get() == " " or year.get() == " " or isbn.get() == " " :
        txt_result.config(text = "Please enter all the fields", fd = "red")

    else :
        Database()
        cursor.execute("insert into library(title,author,year,isbn) values(?,?,?,?),str(title.get()),str(author.get()),int(year.get()),int(isbn.get())")

        conn.commit()
        title.set(" ")
        author.set(" ")
        year.set(" ")
        isbn.set("")

        cursor.close()
        conn.close()
        txt_result.config(text = "record inserted!", fg = "green")

def Read():
    tree.delete(*tree.get_children)
    Database()
    cursor.execute("select * from library order by title asc")
    fetch = cursor.fetchall()
    for data in fetch :
        tree.insert(' ','end',values = (data[1],data[2],data[3],data[4]))

    cursor.close()
    txt_result.config(text = "Successfully fetch data!",fg = "black")

def exit():
    result = tkMessageBox.askquestion('Do you want to exit?(y/n)',icon = 'warning')

    if result == 'yes':
        root.destroy()
        exit()


# Variable declaration
title = StringVar()
author = StringVar()
year = IntVar()
isbn = IntVar()

