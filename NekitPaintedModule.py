from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from time import sleep
import random  
chid=0
```
{"settings": {"debug": "True"}, "creationlist": ["idk", "NoName"], "notes": {"test": "lo"}}
```
@Client.on_message(filters.command("type", prefixes = "/")&filters.me)
def type(_, msg):
	orig_text=msg.text.split("/type ", maxsplit = 1)[1]
	text = orig_text
	tbp = ""
	typing_symbol = "_"
	while(tbp != orig_text):
		try:
			msg.edit(tbp+typing_symbol)
			sleep(0.05)
			tbp = tbp+text[0]
			text=text[1:]
			msg.edit(tbp)
			sleep(0.05)
		except FloodWait as e:
			sleep(e.x) 
@Client.on_message(filters.command("antifem", prefixes = "/")&filters.me)
def ugnet(_, msg):
	msg.edit("🤬 Начинаем угнетать фемок")
	percent = 0
	while(percent<100):
		try:
			msg.edit("🤬 Процент угнетения: "+str(percent)+"%")
			percent += random.randint(1,5)
			sleep(0.05)
		except FloodWait as e:
			sleep(e.x)
	msg.edit("✔️ Все фемки в чате успешно угнетены")
@Client.on_message(filters.command("spam", prefixes = "/")&filters.me)
def raid(_, msg):
	orig_text=msg.text.split("/spam ", maxsplit = 1)[1]
	text = orig_text
	chid=msg.chat.id
	msg.delete()
	for i in range(1,50):
		Client.send_message(chid,text)
		sleep(0.03)
@Client.on_message(filters.command("spamphoto", prefixes = "/")&filters.me)
def photo(_, msg):
	orig_text=msg.text.split("/spamphoto ", maxsplit = 1)[1]
	text = orig_text
	chid=msg.chat.id
	msg.delete()
	for i in range(1,25):
		Client.send_photo(chid,text)
		sleep(0.05)
@Client.on_message(filters.command("spamvideo", prefixes = "/")&filters.me)
def vid(_, msg):
	orig_text=msg.text.split("/spamvideo ", maxsplit = 1)[1]
	text = orig_text
	chid=msg.chat.id
	msg.delete()
	for i in range(1,25):
		Client.send_video(chid,text)
		sleep(0.075)
@Client.on_message(filters.command("spamgif", prefixes = "/")&filters.me)
def gif(_, msg):
	orig_text=msg.text.split("/spamgif ", maxsplit = 1)[1]
	text = orig_text
	chid=msg.chat.id
	msg.delete()
	for i in range(1,25):
		Client.send_animation(chid,text)
		sleep(0.05)
@Client.on_message(filters.command("spamvoice", prefixes = "/")&filters.me)
def aud(_, msg):
	orig_text=msg.text.split("/spamvoice ", maxsplit = 1)[1]
	text = orig_text
	chid=msg.chat.id
	msg.delete()
	for i in range(1,25):
		Client.send_audio(chid,text)
		sleep(0.05) 
@Client.on_message(filters.command("spamdoc", prefixes = "/")&filters.me)
def doc(_, msg):
	orig_text=msg.text.split("/spamdoc ", maxsplit = 1)[1]
	text = orig_text
	chid=msg.chat.id
	msg.delete()
	for i in range(1,25):
		Client.send_document(chid,text)
		sleep(0.05) 
@Client.on_message(filters.command("spamsticker", prefixes = "/")&filters.me)
def stick(_, msg):
	orig_text=msg.text.split("/spamsticker ", maxsplit = 1)[1]
	text = orig_text
	chid=msg.chat.id
	msg.delete()
	for i in range(1,25):
		Client.send_sticker(chid,text)
		sleep(0.05) 
@Client.on_message(filters.command("status", prefixes = "/")&filters.me)
def status(_, msg):
	orig_text=msg.text.split("/status ", maxsplit = 1)[1]
	text = orig_text
	chid=msg.chat.id
	Client.send_chat_action(chid, text)
	msg.delete()
@Client.on_message(filters.command("last", prefixes = "/")&filters.me)
def search(_, msg):
	orig_text=msg.text.split("/last ", maxsplit = 1)[1]
	text = int(orig_text)
	chid=msg.chat.id
	msg.delete()
	for message in Client.search_global(filter="empty" , limit=text):
		Client.send_message(chid, message.text)
		sleep(0.1)
@Client.on_message(filters.command("search", prefixes = "/")&filters.me)
def seek(_, msg):
	orig_text=msg.text.split("/search ", maxsplit = 1)[1]
	text = orig_text
	chid=msg.chat.id
	msg.delete()
	for message in Client.search_global(text , limit=25):
		Client.send_message(chid, message.text)
		sleep(0.1)
@Client.on_message(filters.command("countmsg", prefixes = "/")&filters.me)
def count(_, msg):
	chid=msg.chat.id
	msg.edit("<b>Количество сообщений в чате:</b> "+str(Client.get_history_count(chid))) 
@Client.on_message(filters.command("help", prefixes = "/")&filters.me)
def count(_, msg):
	chid=msg.chat.id
	msg.edit("<b>Список команд юзербота</b>\n\n<b><i>Спам: </i></b><code>/spam</code> <i>текст</i>, <code>/spamphoto</code> <i>фото</i>, <code>/spamvideo</code> <i>видео</i>, <code>/spamsticker</code> <i>стикер</i>, <code>/spamdoc</code> <i>файл</i>, <code>/spamgif</code> <i>анимация</i>, <code>/spamvoice</code> <i>голосовое сообщение</i>\n<b><i>Анимации: </i></b><code>/antifem</code>, <code>/type</code> <i>текст</i>, <code>/ticker</code> <i>текст</i>\n<b><i>Фейковый статус: </i></b><code>/status</code> <i>typing|upload_photo|upload_video|upload_audio|upload_document|find_location|upload_video_note|choose_contact|playing|speaking|cancel</i>\n<b><i>Поиск сообщений: </i></b><code>/last</code> <i>кол-во сообщений</i>, <code>/search</code> <i>запрос</i>\n<b><i>Информация о чате: </i></b><code>/countmsg</code>") 
@Client.on_message(filters.command("ticker", prefixes = "/")&filters.me)
def tck(_, msg):
	orig_text=msg.text.split("/ticker ", maxsplit = 1)[1]
	text = orig_text
	a = text
	space=""
	fsm = 0
	lsm = 24
	while(a!=""):
		a = text[fsm:lsm]
		msg.edit("—————————————————\n"+a+"\n—————————————————")
		lsm+=1
		fsm+=1
		sleep(0.2)
