from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from time import sleep
import random  
chid=0
def datadef():
	return {"name": "ok"} 
@Client.on_message(filters.command("smth", prefixes = "%")&filters.me)
def type(_, msg):
	msg.edit("Что-то")
