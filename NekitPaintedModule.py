from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from time import sleep
import random  
chid=0
'''
{"settings": {"debug": "True"}, "creationlist": ["idk", "NoName"], "notes": {"test": "lo"}}
'''
@Client.on_message(filters.command("nmtype", prefixes = "%")&filters.me)
def type(_, msg):
	orig_text=msg.text.split("%nmtype ", maxsplit = 1)[1]
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
@Client.on_message(filters.command("nmantifem", prefixes = "%")&filters.me)
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
@Client.on_message(filters.command("nmspam", prefixes = "%")&filters.me)
def raid(_, msg):
	orig_text=msg.text.split("%nmspam ", maxsplit = 1)[1]
	text = orig_text
	chid=msg.chat.id
	msg.delete()
	for i in range(1,50):
		_.send_message(chid,text)
		sleep(0.03)
@Client.on_message(filters.command("nmspamphoto", prefixes = "%")&filters.me)
def photo(_, msg):
	orig_text=msg.text.split("%nmspamphoto ", maxsplit = 1)[1]
	text = orig_text
	chid=msg.chat.id
	msg.delete()
	for i in range(1,25):
		_.send_photo(chid,text)
		sleep(0.05)
@Client.on_message(filters.command("nmspamvideo", prefixes = "%")&filters.me)
def vid(_, msg):
	orig_text=msg.text.split("%nmspamvideo ", maxsplit = 1)[1]
	text = orig_text
	chid=msg.chat.id
	msg.delete()
	for i in range(1,25):
		_.send_video(chid,text)
		sleep(0.075)
@Client.on_message(filters.command("nmspamgif", prefixes = "%")&filters.me)
def gif(_, msg):
	orig_text=msg.text.split("%nmspamgif ", maxsplit = 1)[1]
	text = orig_text
	chid=msg.chat.id
	msg.delete()
	for i in range(1,25):
		_.send_animation(chid,text)
		sleep(0.05)
@Client.on_message(filters.command("nmspamvoice", prefixes = "%")&filters.me)
def aud(_, msg):
	orig_text=msg.text.split("%nmspamvoice ", maxsplit = 1)[1]
	text = orig_text
	chid=msg.chat.id
	msg.delete()
	for i in range(1,25):
		_.send_audio(chid,text)
		sleep(0.05) 
@Client.on_message(filters.command("nmspamdoc", prefixes = "%")&filters.me)
def doc(_, msg):
	orig_text=msg.text.split("%nmspamdoc ", maxsplit = 1)[1]
	text = orig_text
	chid=msg.chat.id
	msg.delete()
	for i in range(1,25):
		_.send_document(chid,text)
		sleep(0.05) 
@Client.on_message(filters.command("nmspamsticker", prefixes = "%")&filters.me)
def stick(_, msg):
	orig_text=msg.text.split("%nmspamsticker ", maxsplit = 1)[1]
	text = orig_text
	chid=msg.chat.id
	msg.delete()
	for i in range(1,25):
		_.send_sticker(chid,text)
		sleep(0.05) 
@Client.on_message(filters.command("nmstatus", prefixes = "%")&filters.me)
def status(_, msg):
	orig_text=msg.text.split("%nmstatus ", maxsplit = 1)[1]
	text = orig_text
	chid=msg.chat.id
	_.send_chat_action(chid, text)
	msg.delete()
@Client.on_message(filters.command("nmlast", prefixes = "%")&filters.me)
def search(_, msg):
	orig_text=msg.text.split("%last ", maxsplit = 1)[1]
	text = int(orig_text)
	chid=msg.chat.id
	msg.delete()
	for message in _.search_global(filter="empty" , limit=text):
		_.send_message(chid, message.text)
		sleep(0.1)
@Client.on_message(filters.command("nmsearch", prefixes = "%")&filters.me)
def seek(_, msg):
	orig_text=msg.text.split("%nmsearch ", maxsplit = 1)[1]
	text = orig_text
	chid=msg.chat.id
	msg.delete()
	for message in _.search_global(text , limit=25):
		_.send_message(chid, message.text)
		sleep(0.1)
@Client.on_message(filters.command("nmcountmsg", prefixes = "%")&filters.me)
def count(_, msg):
	chid=msg.chat.id
	msg.edit("<b>Количество сообщений в чате:</b> "+str(_.get_history_count(chid))) 
@Client.on_message(filters.command("nmhelp", prefixes = "%")&filters.me)
def count(_, msg):
	chid=msg.chat.id
	msg.edit("<b>Список команд юзербота</b>\n\n<b><i>Спам: </i></b><code>%nmspam</code> <i>текст</i>, <code>%nmspamphoto</code> <i>фото</i>, <code>%nmspamvideo</code> <i>видео</i>, <code>%nmspamsticker</code> <i>стикер</i>, <code>%nmspamdoc</code> <i>файл</i>, <code>%nmspamgif</code> <i>анимация</i>, <code>%nmspamvoice</code> <i>голосовое сообщение</i>\n<b><i>Анимации: </i></b><code>%nmantifem</code>, <code>%nmtype</code> <i>текст</i>, <code>%nmticker</code> <i>текст</i>\n<b><i>Фейковый статус: </i></b><code>%nmstatus</code> <i>typing|upload_photo|upload_video|upload_audio|upload_document|find_location|upload_video_note|choose_contact|playing|speaking|cancel</i>\n<b><i>Поиск сообщений: </i></b><code>%nmlast</code> <i>кол-во сообщений</i>, <code>%nmsearch</code> <i>запрос</i>\n<b><i>Информация о чате: </i></b><code>%nmcountmsg</code>\n<b><i>Технические команды: </b></i><code>%nmtest</code>") 
@Client.on_message(filters.command("nmticker", prefixes = "%")&filters.me)
def tcker(_, msg):
	orig_text=msg.text.split("%nmticker ", maxsplit = 1)[1]
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
@Client.on_message(filters.command("nmtest", prefixes = "%")&filters.me)
def test(_, msg):
	msg.edit("<i>Модуль работает отлично</i>")
