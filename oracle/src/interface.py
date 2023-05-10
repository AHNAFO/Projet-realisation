
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from function_interface import *


ASSETS_PATH = Path(r"./assets/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1074x527")
window.configure(bg = "#000000")


variableGlobale()

canvas = Canvas(
    window,
    bg = "#000000",
    height = 527,
    width = 1074,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_image_1_select = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: change_color_button(button_1,button_image_1,button_image_1_select),
    relief="flat",
    text=False
)
button_1.place(
    x=280.00067138671875,
    y=393.0,
    width=188.00006103515625,
    height=33.0
)


button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_image_2_select = PhotoImage(
    file=relative_to_assets("button_10.png"))

button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: change_color_button(button_2,button_image_2,button_image_2_select),
    relief="flat",
    text=False
)
button_2.place(
    x=280.00067138671875,
    y=334.0,
    width=188.00006103515625,
    height=33.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_image_3_select = PhotoImage(
    file=relative_to_assets("button_11.png"))

button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: change_color_button(button_3,button_image_3,button_image_3_select),
    relief="flat",
    text=False
)
button_3.place(
    x=280.00067138671875,
    y=275.0,
    width=188.00006103515625,
    height=33.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_image_4_select = PhotoImage(
    file=relative_to_assets("button_12.png"))

button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: change_color_button(button_4,button_image_4,button_image_4_select),
    relief="flat",
    text=False
)
button_4.place(
    x=280.00067138671875,
    y=190.0,
    width=188.00006103515625,
    height=33.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_image_5_select = PhotoImage(
    file=relative_to_assets("button_13.png"))

button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: change_color_button(button_5,button_image_5,button_image_5_select),
    relief="flat",
    text=False
)
button_5.place(
    x=69.00067138671875,
    y=393.0,
    width=188.0,
    height=33.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_image_6_select = PhotoImage(
    file=relative_to_assets("button_14.png"))

button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: change_color_button(button_6,button_image_6,button_image_6_select),
    relief="flat",
    text=False
)
button_6.place(
    x=69.00067138671875,
    y=334.0,
    width=188.0,
    height=33.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_image_7_select = PhotoImage(
    file=relative_to_assets("button_15.png"))

button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: change_color_button(button_7,button_image_7,button_image_7_select),
    relief="flat",
    text=False
)
button_7.place(
    x=69.00067138671875,
    y=275.0,
    width=188.0,
    height=33.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_image_8_select = PhotoImage(
    file=relative_to_assets("button_16.png"))

button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: change_color_button(button_8,button_image_8,button_image_8_select),
    relief="flat",
    text=False
)
button_8.place(
    x=69.00067138671875,
    y=225.0,
    width=188.0,
    height=33.0
)

button_image_19 = PhotoImage(
    file=relative_to_assets("button_19.png"))
button_image_19_select = PhotoImage(
    file=relative_to_assets("button_18.png"))

button_19 = Button(
    image=button_image_19,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: change_color_button(button_19,button_image_19,button_image_19_select),
    relief="flat",
    text=False
)
button_19.place(
    x=280.00067138671875,
    y=450.0,
    width=188.0,
    height=33.0
)

button_image_20 = PhotoImage(
    file=relative_to_assets("button_20.png"))
button_image_20_select = PhotoImage(
    file=relative_to_assets("button_21.png"))

button_20 = Button(
    image=button_image_20,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: change_color_button(button_20,button_image_20,button_image_20_select),
    relief="flat",
    text=False
)
button_20.place(
    x=69.00067138671875,
    y=190.0,
    width=188.0,
    height=33.0
)

button_image_22 = PhotoImage(
    file=relative_to_assets("button_22.png"))
button_image_22_select = PhotoImage(
    file=relative_to_assets("button_23.png"))

button_22 = Button(
    image=button_image_22,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: change_color_button(button_22,button_image_22,button_image_22_select),
    relief="flat",
    text=False
)
button_22.place(
    x=280.00067138671875,
    y=226.0,
    width=188.0,
    height=33.0
)

button_image_17 = PhotoImage(
    file=relative_to_assets("button_17.png"))
button_17 = Button(
    image=button_image_17,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: calculate_begin(tab_buttons),
    relief="flat"
)
button_17.place(
    x=753.000732421875,
    y=297.0,
    width=129.0,
    height=48.4000244140625
)

tab_buttons = [button_1,button_2,button_3,button_4,button_5,button_6,button_7,button_8, button_19, button_20, button_22]


canvas.create_text(
    280.00067138671875,
    158.0,
    anchor="nw",
    text="Choisir 1 à 4 prédicteur",
    fill="#38B6FF",
    font=("Junge Regular", 18 * -1)
)
canvas.create_text(
    80.0,
    158.0,
    anchor="nw",
    text="Choisir 1 à 4 sources",
    fill="#38B6FF",
    font=("Junge Regular", 18 * -1)
)

canvas.create_text(
    659.000732421875,
    180.0,
    anchor="nw",
    text="Entrer une source de 0 et 1 (optionnel)",
    fill="#38B6FF",
    font=("Junge Regular", 18 * -1)
)
##############################
canvas.create_text(
    480.0,
    158.0,
    anchor="nw",
    text="Suivant",
    fill="#38B6FF",
    font=("Junge Regular", 18 * -1)
)
canvas.create_text(
    500.0,
    189.0,
    anchor="nw",
    text="?",
    fill="#38B6FF",
    font=("Junge Regular", 26 * -1)
)
canvas.create_text(
    500.0,
    392.0,
    anchor="nw",
    text="?",
    fill="#38B6FF",
    font=("Junge Regular", 26 * -1)
)
canvas.create_text(
    500.0,
    334.0,
    anchor="nw",
    text="?",
    fill="#38B6FF",
    font=("Junge Regular", 26 * -1)
)
canvas.create_text(
    500.0,
    300.0,
    anchor="nw",
    text="?",
    fill="#38B6FF",
    font=("Junge Regular", 26 * -1)
)
canvas.create_text(
    500.0,
    290.0,
    anchor="nw",
    text="?",
    fill="#38B6FF",
    font=("Junge Regular", 26 * -1)
)
canvas.create_text(
    500.0,
    275.0,
    anchor="nw",
    text="?",
    fill="#38B6FF",
    font=("Junge Regular", 26 * -1)
)
canvas.create_text(
    500.0,
    265.0,
    anchor="nw",
    text="?",
    fill="#38B6FF",
    font=("Junge Regular", 26 * -1)
)

#######################
#ATTENDU
canvas.create_text(
    659.000732421875,
    400.0,
    anchor="nw",
    text="Attendu",
    fill="#38B6FF",
    font=("Junge Regular", 26 * -1)
)
canvas.create_text(
    659.000732421875,
    450.0,
    anchor="nw",
    text="?",
    fill="#38B6FF",
    font=("Junge Regular", 26 * -1)
)


canvas.create_text(
    106.00067138671875,
    37.0,
    anchor="nw",
    text="WHO IS THE BEST PREDICTOR ?",
    fill="#38B6FF",
    font=("JuliusSansOne Regular", 36 * -1)
)
canvas.create_rectangle(
    63.0,
    105.5,
    834.0,
    112.5,
    fill="#3B37FF",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    831.500732421875,
    233.5,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#4A4545",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=659.000732421875,
    y=212.0,
    width=345.0,
    height=41.0
)
window.resizable(False, False)
window.mainloop()