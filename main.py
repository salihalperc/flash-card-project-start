import csv
from tkinter import *
from pandas import pandas, DataFrame
import random
BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
words = pandas.read_csv("./data/words_for_progress.csv")
words = words.to_dict(orient="records")


current_card = random.choice(words)
new_word = current_card["English"]
SCORE = 0



def word():
    global current_card

    current_card = random.choice(words)
    new_word = current_card["English"]
    window.after(3000, flip_card)
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(canvas_text, text="English", fill="black")
    canvas.itemconfig(canvas_word, text=new_word, fill="black")





def flip_card():
    global current_card
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(canvas_text, text="Turkish", fill="white")
    tur_word = current_card["Turkish"]
    canvas.itemconfig(canvas_word, text=tur_word, fill="white")

def is_known():
    words.remove(current_card)
    word()
    data = pandas.DataFrame(words)
    data.to_csv("data/words_to_learn.csv", index=False)






my_tik = PhotoImage(file="./images/right.png")
my_x = PhotoImage(file="./images/wrong.png")
tik_button = Button(image=my_tik, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=is_known)
tik_button.grid(row=1, column=1)
x_button = Button(image=my_x, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=word)
x_button.grid(row=1, column=0)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")

window.after(3000, flip_card)
canvas = Canvas(width=800, height=526)
canvas_image = canvas.create_image(400, 263, image=card_front)
canvas_text = canvas.create_text(400, 150, text="English", font=("Ariel", 40, "italic"), fill="black")

canvas_word = canvas.create_text(400, 263, text=new_word, font=("Ariel", 60, "bold"), fill="black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
# turkish = Label(text="Turkish", font=("Ariel", 40, "italic"), fg="black", bg="white")
# turkish.place(x=350, y=100)
# turk_word = Label(text="word", font=("Ariel", 60, "bold"), fg="black", bg="white")
# turk_word.place(x=350, y=213)



# window.after(3000)
# canvas.create_image(400, 263, image=card_back)
# canvas.create_text(400, 150, text="Turkish", font=("Ariel", 40, "italic"), fill="white")
# canvas.create_text(400, 263, text=new_dict["Turkish"], font=("Ariel", 60, "bold"), fill="white")





window.mainloop()