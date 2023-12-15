from pyrogram import Client
from time import sleep

def telegram(a):
    app = Client("my_account")

    def pr(f):
        app.send_message(601766913, f)

    with app:
        pr(a)