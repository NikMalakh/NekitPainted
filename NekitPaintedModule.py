from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from time import sleep
import random  
chid=0
@Client.on_message(filters.command("type", prefixes = "%")&filters.me)
def type(_, msg):t
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
@Client.on_message(filters.command("antifem", prefixes = "%")&filters.me)
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
@Client.on_message(filters.command("status", prefixes = "%")&filters.me)
def status(_, msg):
	orig_text=msg.text.split("/status ", maxsplit = 1)[1]
	text = orig_text
	chid=msg.chat.id
	app.send_chat_action(chid, text)
	msg.delete()
@Client.on_message(filters.command("last", prefixes = "%")&filters.me)
def search(_, msg):
	orig_text=msg.text.split("/last ", maxsplit = 1)[1]
	text = int(orig_text)
	chid=msg.chat.id
	msg.delete()
	for message in app.search_global(filter="empty" , limit=text):
		app.send_message(chid, message.text)
		sleep(0.1)
@Client.on_message(filters.command("search", prefixes = "%")&filters.me)
def seek(_, msg):
	orig_text=msg.text.split("/search ", maxsplit = 1)[1]
	text = orig_text
	chid=msg.chat.id
	msg.delete()
	for message in app.search_global(text , limit=25):
		app.send_message(chid, message.text)
		sleep(0.1)
@Client.on_message(filters.command("countmsg", prefixes = "%")&filters.me)
def count(_, msg):
	chid=msg.chat.id
	msg.edit("<b>Количество сообщений в чате:</b> "+str(app.get_history_count(chid))) 
@Client.on_message(filters.command("help", prefixes = "%")&filters.me)
def count(_, msg):
	chid=msg.chat.id
	msg.edit("<b>Список команд юзербота</b>\n\n<b><i>Анимации: </i></b><code>/antifem</code>, <code>/type</code> <i>текст</i>, <code>/ticker</code> <i>текст</i>\n<b><i>Фейковый статус: </i></b><code>/status</code> <i>typing|upload_photo|upload_video|upload_audio|upload_document|find_location|upload_video_note|choose_contact|playing|speaking|cancel</i>\n<b><i>Поиск сообщений: </i></b><code>/last</code> <i>кол-во сообщений</i>, <code>/search</code> <i>запрос</i>\n<b><i>Информация о чате: </i></b><code>/countmsg</code>") 
@app.on_message(filters.command("ticker", prefixes = "%")&filters.me)
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
