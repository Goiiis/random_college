import tkinter as tk
import random
import sqlite3 as sql
import webbrowser

connection = sql.connect("college.db")
    
cursor = connection.cursor()

rows = cursor.execute("SELECT rank FROM colleges WHERE rank BETWEEN 10 AND 20 ORDER BY rank").fetchall()
print(rows)

window = tk.Tk()
window.title("college")
window.geometry("500x500")

def show():
    ans = my_text.get(1.0, 99.0)
    ans2 = my_text2.get(1.0, 99.0)
    try:
        int(ans2)
        int(ans)
    except:
        my_label2.config(text="please use numbers")
    rows = cursor.execute("SELECT name FROM colleges WHERE rank BETWEEN ? AND ? ORDER BY rank", (int(ans), int(ans2))).fetchall()
    urls = ""
    for word in random.choice(rows)[0].split(" "):
        urls += word
        urls += "+"
    webbrowser.open(f'https://www.google.com/search?q={urls}')
    my_label2.config(text=rows)
    S

labl = tk.Label(window, text="insert rank ceiling:")
labl.pack(pady=0)

my_text = tk.Text(window, width=60, height=1)
my_text.pack(pady=20)

my_label = tk.Label(window, text="insert rank floor:")
my_label.pack(pady=0)

my_text2 = tk.Text(window, width=60, height=1)
my_text2.pack(pady=20)

button_frame = tk.Frame(window)
button_frame.pack()

finalize = tk.Button(button_frame, text="Open Random College", command=show)
finalize.grid(row=0, column=0)

my_label2 = tk.Label(window, text="", wraplength=500)
my_label2.pack(pady=0)

window.mainloop()
