from tkinter import *
import customtkinter as ctk
from CTkListbox import *
import customtkinter
from weather import get_weather

def draw_weather():
    city = list_cities.get()
    result = get_weather(city)
    result_weather.set(result)


window = ctk.CTk()
window.title("Погода")
window.geometry("800x600")
window.resizable(False, False)
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
label_title = ctk.CTkLabel(window, text="Погода", font=("Roboto", 50))
label_title.pack(pady=10)
list_cities = CTkListbox(window)
cities = ("Москва", "Осло", "Рига", "Ростов", "Таллин", "Вильнюс", "Стокгольм", "Киркенес", "Заполярный")
for i in range(len(cities)):
    list_cities.insert(i, cities[i])
list_cities.pack()
button = ctk.CTkButton(window, text="Узнать", command=draw_weather)
button.pack(pady=10)
result_weather = StringVar()
label_result = ctk.CTkLabel(window, textvariable=result_weather, font=("Roboto", 30))
label_result.pack()
window.mainloop()


