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
	msg.edit("<i>🤬 Starting fem oppressing...</i>")
	percent = 0
	while(percent<100):
		try:
			msg.edit("<i><b>🤬 Opressed: </b>"+str(percent)+"%</i>")
			percent += random.randint(1,5)
			sleep(0.05)
		except FloodWait as e:
			sleep(e.x)
	msg.edit("<b><i>✔️ All feminists in the chat successfully oppressed</i></b>")
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
	orig_text=msg.text.replace("%nmlast ", "")
	text = int(orig_text)
	chid=msg.chat.id
	msg.delete()
	for message in _.search_global(filter="empty" , limit=text):
		_.send_message(chid, message.text)
		sleep(0.1)
@Client.on_message(filters.command("nmsearch", prefixes = "%")&filters.me)
def seek(_, msg):
	count = int(msg.text.split(" ")[1]) 
	orig_text=msg.text.split(" ", maxsplit = 2)[2]
	text = orig_text
	chid=msg.chat.id
	msg.delete()
	for message in _.search_global(text , limit=count):
		_.send_message(chid, message.text)
		sleep(0.1)
@Client.on_message(filters.command("nmctype", prefixes = "%")&filters.me)
def ctype(_, msg):
	symbol=msg.text.split(" ")[1]
	orig_text=msg.text.split(" ", maxsplit = 2)[2]
	text = orig_text
	tbp = ""
	typing_symbol = symbol
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
@Client.on_message(filters.command("nmcountmsg", prefixes = "%")&filters.me)
def count(_, msg):
	chid=msg.chat.id
	msg.edit("<i><b>Messages in chat:</b> "+str(_.get_history_count(chid))+"</i>") 
@Client.on_message(filters.command("nmhelp", prefixes = "%")&filters.me)
def help(_, msg):
	chid=msg.chat.id
	msg.edit("<b>Nekit Painted Module commands:</b>\n\n<b><i>Message flood: </i></b><code>%nmspam</code> <i>text</i>, <code>%nmspamphoto</code> <i>photo URL</i>, <code>%nmspamvideo</code> <i>video URL</i>, <code>%nmspamsticker</code> <i>sticker URL</i>, <code>%nmspamdoc</code> <i>document URL</i>, <code>%nmspamgif</code> <i>GIF URL</i>, <code>%nmspamvoice</code> <i>audio URL</i>\n<b><i>Animations: </i></b><code>%nmantifem</code>, <code>%nmtype</code> <i>text</i>, <code>%nmctype</code> <i>[symbol] [text]</i>, <code>%nmticker</code> <i>text</i>\n<b><i>Chat action simulation: </i></b><code>%nmstatus</code> <i>typing|upload_photo|upload_video|upload_audio|upload_document|find_location|upload_video_note|choose_contact|playing|speaking|cancel</i>\n<b><i>Message search: </i></b><code>%nmlast</code> <i>message limit</i>, <code>%nmsearch</code> <i>[message limit] [query]</i>\n<b><i>Chat information: </i></b><code>%nmcountmsg</code>\n<b><i>Technical commands: </i></b> <code>%nnmtest</code>, <code>%nmversion</code>") 
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
def tester(_, msg):
	msg.edit("<i><b>Module works good</b></i>")
@Client.on_message(filters.command("nmversion", prefixes = "%")&filters.me)
def version(_, msg):
	msg.edit("<i><b>Nekit Painted Module</b> for <b>Painted-Userbot</b> v1.0.1\nDo not distribute</i>")
