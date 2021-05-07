import tkinter
from newsapi import NewsApiClient
from tkinter import *
import webbrowser
from PIL import ImageTk, Image
import pyttsx3


def callback(link):
    webbrowser.open_new(link)


def speak_out():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    for i in range (len(articles)):
        to_say = articles[i]
        engine.say(to_say['title'])
    engine.runAndWait()


def news_display(event):
    val = source_list_name.index(selection.get())
    headlines = newsapi.get_top_headlines(sources=source_list_id[val])
    global articles
    articles = headlines['articles']

    title=[]
    url = []

    for i in range(len(articles)):
        my_article = articles[i]
        title.append(my_article['title'])
        url.append(my_article['url'])

    deli = 100
    svar = StringVar()
    labl = Label(window, textvariable=svar, justify = CENTER, bg = "red", width = 50, font = "bold")

    def shif():
        shif.msg = shif.msg[1:] + shif.msg[0]
        svar.set(shif.msg)
        window.after(deli, shif)

    break_label = Label(window,text = "Breaking News:", justify = LEFT, font = "bold")
    break_label.place(x=30, y=60)

    headline_label = Label(window, text = "Headlines:", justify = LEFT, font = "bold")
    headline_label.place(x=30, y=90)
    shif.msg = '| ' + title[0]
    shif()
    labl.place(x=180, y=62)

    news_item1 = Label(window, text=title[0],  justify=LEFT)
    news_item1.place(x=30, y=120)
    news_item1.bind("<Button-1>", lambda e: callback(url[0]))

    news_item2 = Label(window, text=title[1], justify=LEFT)
    news_item2.place(x=30, y=140)
    news_item2.bind("<Button-1>", lambda e: callback(url[1]))

    news_item3 = Label(window, text=title[2], justify=LEFT)
    news_item3.place(x=30, y=160)
    news_item3.bind("<Button-1>", lambda e: callback(url[2]))

    news_item4 = Label(window, text=title[3], justify=LEFT)
    news_item4.place(x=30, y=180)
    news_item4.bind("<Button-1>", lambda e: callback(url[3]))

    news_item5 = Label(window, text=title[4], justify=LEFT)
    news_item5.place(x=30, y=200)
    news_item5.bind("<Button-1>", lambda e: callback(url[4]))

    news_item6 = Label(window, text=title[5], justify=LEFT)
    news_item6.place(x=30, y=220)
    news_item6.bind("<Button-1>", lambda e: callback(url[5]))

    news_item7 = Label(window, text=title[6], justify=LEFT)
    news_item7.place(x=30, y=240)
    news_item7.bind("<Button-1>", lambda e: callback(url[6]))

    news_item8 = Label(window, text=title[7], justify=LEFT)
    news_item8.place(x=30, y=260)
    news_item8.bind("<Button-1>", lambda e: callback(url[7]))

    news_item9 = Label(window, text=title[8], justify=LEFT)
    news_item9.place(x=30, y=280)
    news_item9.bind("<Button-1>", lambda e: callback(url[8]))

    news_item10 = Label(window, text=title[9], justify=LEFT)
    news_item10.place(x=30, y=300)
    news_item10.bind("<Button-1>", lambda e: callback(url[9]))


window = Tk()

window.title("NewsApp")
window.geometry("800x350")

Source_name = Label(window, text="Choose the source", font ="bold")
Source_name.place(x=180, y=20)

newsapi = NewsApiClient(api_key='3ada1d3722ba4aff81ab30b96e20b3b4')

sources = newsapi.get_sources()

x = len(sources['sources'])

source_list_id = []
source_list_name = []

for i in range(x):
    source_list_name.append(sources['sources'][i]['name'])
    source_list_id.append(sources['sources'][i]['id'])

selection = tkinter.StringVar(0)

source_choose = OptionMenu(window, selection, *source_list_name, command=news_display)
source_choose.config(width=30)
source_choose.place(x=370, y=20)

speaker = Image.open('speaker2.png')
resized = speaker.resize((30,30),Image.ANTIALIAS)
speaker_img = ImageTk.PhotoImage(resized)

text_to_speech = Button(window, image=speaker_img, command= speak_out, width=30, height=30 )
text_to_speech.place(x=0, y=0)


window.mainloop()
