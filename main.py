import tkinter as tk
from tkinter import font
from bs4.element import SoupStrainer
import requests
from bs4 import BeautifulSoup

window = tk.Tk() # Setup Window 

tk.Label(text="Streamer Points Collector", font=20).pack(padx=2, pady=2)

tk.Label(text="     ").pack(padx=3, pady=1)

tk.Label(text="Enter Streamer Below", font=15).pack(padx=3, pady=1)


userEntry = tk.Entry(font=15)
userEntry.pack(padx=2, pady=2)

streamerSelected = ''
pointsCollectedThisSession = 0
classToSearch = 'CoreText-sc-cpl358-0 flEeqM'
startedCollection = False

# Handle Button Input and Key Input
def handle_click(event):
    global streamerSelected
    global classToSearch

    streamerSelected = userEntry.get()
    print(f"Entry -> {userEntry.get()}")

    URL = f'https://twitch.tv/{streamerSelected}'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    job_elements = soup.find("span", class_=classToSearch)

    print(job_elements)


button = tk.Button(master=window, text="Confirm", font=8)
button.pack()

window.bind("<Return>", handle_click)






window.mainloop()