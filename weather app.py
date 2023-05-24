from tkinter import*
from tkinter import ttk
import requests
def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=15f24c4fb1640a9faa90e5a69b12ed34").json()
    w_label1.config(text=data["weather"][0]["main"])
    wa_label1.config(text=data['weather'][0]["Discription"])
    temp_label1.config(text=str(data["main"]["temp"]-273.15))
    per_label1.config(text=data["main"]["pressure"])
win = Tk()
win.title("Devesh Weather App")
win.config(bg="orange")
win.geometry("600x600")
name_label = Label(win,text="Devesh Weather App",
                   font=("Time New Roman",32,"bold"))
name_label.place(x=30,y=60,height=50,width=450)
city_name=StringVar()
list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat",
           "Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh",
           "Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim",
           "Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal",
           "Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu",
           "Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com =ttk.Combobox(win,text="Devesh Weather App",values=list_name,
                  font=("Time New Roman",28,"bold"))
com.place(x=30,y=120,height=50,width=450)
w_label = Label(win,text="Weather Climate",
                font=("Times New Roman",20,"bold"))
w_label.place(x=25,y=250,height=50,width=200)
w_label1 = Label(win,text=" ",
                font=("Times New Roman",20,"bold"))
w_label1.place(x=250,y=250,height=50,width=200)
wa_label = Label(win,text="Weather Discription",
                font=("Times New Roman",17,"bold"))
wa_label.place(x=25,y=330,height=50,width=210)
wa_label1 = Label(win,text=" ",
                font=("Times New Roman",17,"bold"))
wa_label1.place(x=250,y=330,height=50,width=210)

temp_label = Label(win,text="Temprature",
                font=("Times New Roman",19,"bold"))
temp_label.place(x=25,y=400,height=50,width=210)
temp_label1 = Label(win,text=" ",
                font=("Times New Roman",19,"bold"))
temp_label1.place(x=250,y=400,height=50,width=210)

per_label = Label(win,text="Pressure",
                font=("Times New Roman",17,"bold"))
per_label.place(x=25,y=450,height=50,width=210)
per_label1 = Label(win,text=" ",
                font=("Times New Roman",17,"bold"))
per_label1.place(x=250,y=450,height=50,width=210)
done_button = Button(win,text="Done",
                     font=("Time New Roman",20,"bold"),command=data_get)
done_button.place(y=190,height=50,width=100,x=200)

win.mainloop()