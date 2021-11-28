from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from time import sleep
import random  
import requests
chid=0
'''
{"settings": {"debug": "True"}, "creationlist": ["idk", "NoName"], "notes": {"test": "lo"}}
'''
def datadef():
    return {"name":"NekitPaintedModule","help":"Type %nmhelp for help","description":"Official module for Painted Userbot. One day it can become popular"}
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
	orig_text=msg.text.split(" ", maxsplit=2)[2]
	count=int(msg.text.split(" ")[1])
	text = orig_text
	chid=msg.chat.id
	msg.delete()
	for i in range(0,count):
		_.send_message(chid,text)
		sleep(0.03)
@Client.on_message(filters.command("nmspamphoto", prefixes = "%")&filters.me)
def photo(_, msg):
	orig_text=msg.text.split(" ", maxsplit=2)[2]
	count=int(msg.text.split(" ")[1])
	text = orig_text
	chid=msg.chat.id
	msg.delete()
	for i in range(0,count):
		_.send_photo(chid,text)
		sleep(0.05)
@Client.on_message(filters.command("nmspamvideo", prefixes = "%")&filters.me)
def vid(_, msg):
	orig_text=msg.text.split(" ", maxsplit=2)[2]
	count=int(msg.text.split(" ")[1])
	text = orig_text
	chid=msg.chat.id
	msg.delete()
	for i in range(0,count):
		_.send_video(chid,text)
		sleep(0.075)
@Client.on_message(filters.command("nmspamgif", prefixes = "%")&filters.me)
def gif(_, msg):
	orig_text=msg.text.split(" ", maxsplit=2)[2]
	count=int(msg.text.split(" ")[1])
	text = orig_text
	chid=msg.chat.id
	msg.delete()
	for i in range(0,count):
		_.send_animation(chid,text)
		sleep(0.05)
@Client.on_message(filters.command("nmspamvoice", prefixes = "%")&filters.me)
def aud(_, msg):
	orig_text=msg.text.split(" ", maxsplit=2)[2]
	count=int(msg.text.split(" ")[1])
	text = orig_text
	chid=msg.chat.id
	msg.delete()
	for i in range(0,count):
		_.send_audio(chid,text)
		sleep(0.05) 
@Client.on_message(filters.command("nmspamdoc", prefixes = "%")&filters.me)
def doc(_, msg):
	orig_text=msg.text.split(" ", maxsplit=2)[2]
	count=int(msg.text.split(" ")[1])
	text = orig_text
	chid=msg.chat.id
	msg.delete()
	for i in range(0,count):
		_.send_document(chid,text)
		sleep(0.05) 
@Client.on_message(filters.command("nmspamsticker", prefixes = "%")&filters.me)
def stick(_, msg):
	orig_text=msg.text.split(" ", maxsplit=2)[2]
	count=int(msg.text.split(" ")[1])
	text = orig_text
	chid=msg.chat.id
	msg.delete()
	for i in range(0,count):
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
def last(_, msg):
	orig_text=msg.text.replace("%nmlast ", "")
	text = int(orig_text)
	chid=msg.chat.id
	msg.delete()
	for message in _.search_global(filter="empty" , limit=text):
		try:
			_.send_message(chid, "<i>"+message.from_user.first_name+"</i><b> in </b><i>"+message.chat.title+": </i>"+message.text)
			sleep(0.1)
		except:
			_.send_message(chid, "<i>An error occured while sending the message</i>")
@Client.on_message(filters.command("nmsearch", prefixes = "%")&filters.me)
def search(_, msg):
	count = int(msg.text.split(" ")[1]) 
	orig_text=msg.text.split(" ", maxsplit = 2)[2]
	text = orig_text
	chid=msg.chat.id
	msg.delete()
	for message in _.search_global(text , limit=count):
		try:
			_.send_message(chid, "<i>"+message.from_user.first_name+"</i><b> in </b><i>"+message.chat.title+": </i>"+message.text)
			sleep(0.1)
		except:
			_.send_message(chid, "<i>An error occured while sending the message</i>")
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
	msg.edit("<b>Nekit Painted Module commands:</b>\n\n<b><i>Message flood: </i></b><code>%nmspam</code> <i>[amount] [text]</i>, <code>%nmspamphoto</code> <i>[amount] [URL]</i>, <code>%nmspamvideo</code> <i>[amount] [URL]</i>, <code>%nmspamsticker</code> <i>[amount] [URL]</i>, <code>%nmspamdoc</code> <i>[amount] [URL]</i>, <code>%nmspamgif</code> <i>[amount] [URL]</i>, <code>%nmspamvoice</code> <i>[amount] [URL]</i>\n<b><i>Arts: </i></b><code>%nmart</code> <i>[art]|help</i>, <code>%nmcart</code> <i>([art] text)|help</i>\n<b><i>Animations: </i></b><code>%nmantifem</code>, <code>%nmtype</code> <i>text</i>, <code>%nmctype</code> <i>[symbol] [text]</i>, <code>%nmticker</code> <i>text</i>\n<b><i>Chat action simulation: </i></b><code>%nmstatus</code> <i>typing|upload_photo|upload_video|upload_audio|upload_document|find_location|upload_video_note|choose_contact|playing|speaking|cancel</i>\n<b><i>Message search: </i></b><code>%nmlast</code> <i>message limit</i>, <code>%nmsearch</code> <i>[message limit] [query]</i>\n<b><i>Chat information: </i></b><code>%nmcountmsg</code>\n<b><i>Self-destructive messages: </i></b><code>%nmdes</code> <i>[amount of seconds] [message text]</i>\n<b><i>Calculations: </i></b> <code>%nmrand</code> <i>[lower limit] [higher limit]</i>, <code>%nmcalc</code> <i>expression <b><u>(unsafe!)</u></b></i>\n<b><i>Technical commands: </i></b> <code>%nnmtest</code>, <code>%nmversion</code>") 
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
	msg.edit("<i><b>Nekit Painted Module</b> for <b>Painted-Userbot</b> v1.1.0\nDo not distribute</i>")
@Client.on_message(filters.command("nmrand", prefixes = "%")&filters.me)
def rand(_, msg):
	rand1 = int(msg.text.split(" ")[1])
	rand2 = int(msg.text.split(" ")[2])
	rand = random.randint(rand1, rand2)
	msg.edit("<i>I choose <b>{0}</b></i>".format(rand))
@Client.on_message(filters.command("nmcalc", prefixes = "%")&filters.me)
def calc(_, msg):
	expr=msg.text.split("%nmcalc ", maxsplit = 1)[1]
	val = eval(expr)
	msg.edit("<i><b>Expression: </b>{0}\n<b>Answer: </b>{1}</i>".format(expr, val))
@Client.on_message(filters.command("nmart", prefixes = "%")&filters.me)
def art(_, msg):
	a=msg.text.split("%nmart ", maxsplit = 1)[1]
	if a=="f":
		text = random.choice([r"""
███████╗
██╔════╝
█████╗░░
██╔══╝░░
██║░░░░░
╚═╝░░░░░""", r"""
╭━━━╮
┃╭━━╯
┃╰━━╮
┃╭━━╯
┃┃
╰╯"""]) 
	elif a=="ahah":
		text = random.choice([r"""
░█▀▀█ █░░█ █▀▀█ █░░█ 
▒█▄▄█ █▀▀█ █▄▄█ █▀▀█ 
▒█░▒█ ▀░░▀ ▀░░▀ ▀░░▀""", r"""
╭━━━┳╮╱╱╱╱╭╮
┃╭━╮┃┃╱╱╱╱┃┃
┃┃╱┃┃╰━┳━━┫╰━╮
┃╰━╯┃╭╮┃╭╮┃╭╮┃
┃╭━╮┃┃┃┃╭╮┃┃┃┃
╰╯╱╰┻╯╰┻╯╰┻╯╰╯"""]) 
	elif a=="lol":
		text = random.choice([r"""
┏┓╋╋╋╋╋┏┓
┃┃╋╋╋╋╋┃┃
┃┃╋╋┏━━┫┃
┃┃╋┏┫┏┓┃┃
┃┗━┛┃┗┛┃┗┓
┗━━━┻━━┻━┛""", r"""
██╗░░░░░░█████╗░██╗░░░░░
██║░░░░░██╔══██╗██║░░░░░
██║░░░░░██║░░██║██║░░░░░
██║░░░░░██║░░██║██║░░░░░
███████╗╚█████╔╝███████╗
╚══════╝░╚════╝░╚══════╝"""])
	elif a=="salam":
		text = random.choice([r"""
█▀ ▄▀█ █░░ ▄▀█ █▀▄▀█
▄█ █▀█ █▄▄ █▀█ █░▀░█""", r"""
▒█▀▀▀█ █▀▀█ █░░ █▀▀█ █▀▄▀█ 
░▀▀▀▄▄ █▄▄█ █░░ █▄▄█ █░▀░█ 
▒█▄▄▄█ ▀░░▀ ▀▀▀ ▀░░▀ ▀░░░▀"""]) 
	elif a=="yes":
		text = random.choice([r"""
╭━━━╮
┃╭━╮┃
┃╰━━┳╮╭┳━┳━━╮
╰━━╮┃┃┃┃╭┫┃━┫
┃╰━╯┃╰╯┃┃┃┃━┫
╰━━━┻━━┻╯╰━━╯""", r"""
█▄█ █▀▀ ▄▀█ █░█
░█░ ██▄ █▀█ █▀█"""])
	elif a=="no":
		text = random.choice([r"""
███╗░░██╗░█████╗░
████╗░██║██╔══██╗
██╔██╗██║██║░░██║
██║╚████║██║░░██║
██║░╚███║╚█████╔╝
╚═╝░░╚══╝░╚════╝░""", r"""
╭━╮╱╭╮
┃┃╰╮┃┃
┃╭╮╰╯┣━━┳━━┳━━╮
┃┃╰╮┃┃╭╮┃╭╮┃┃━┫
┃┃╱┃┃┃╰╯┃╰╯┃┃━┫
╰╯╱╰━┻━━┫╭━┻━━╯
╱╱╱╱╱╱╱╱┃┃
╱╱╱╱╱╱╱╱╰╯"""])   
	elif a=="help":
		text = "<b><i>Available arts:</i></b>\n<code>f</code>\n<code>lol</code>\n<code>ahah</code>\n<code>salam</code>\n<code>yes</code>\n<code>no</code>" 
	else:
		text = "<i>Art not found. Type <code>%nmart help</code> for all arts</i>" 
	msg.edit(text) 
@Client.on_message(filters.command("nmdes", prefixes = "%")&filters.me)
def des(_, msg):
	tim=float(msg.text.split(" ")[1]) 
	text=msg.text.split(" ", maxsplit = 2)[2]
	msg.edit(text)
	sleep(tim)
	msg.delete() 
@Client.on_message(filters.command("nmcart", prefixes = "%")&filters.me)
def textar(_, msg):
	a=msg.text.split(" ")[1]
	if a!="help":
		try:
			txt=msg.text.split(" ", maxsplit = 2)[2] 
		except:
			msg.edit("<b><i>You need to provide some text</i></b>") 
			return
	if a=="tv":
		text = r"""<b>░▀▄░░▄▀
▄▄▄██▄▄▄▄▄░▀█▀▐░▌
█▒░▒░▒░█▀█░░█░▐░▌
█░▒░▒░▒█▀█░░█░░█
█▄▄▄▄▄▄███══════

{0}</b>""".format(txt) 
	elif a=="whoosh":
		text = r""".∧＿∧
( ･ω･｡)つ━☆・*。
⊂  ノ    ・゜ .
しーＪ   °。  *´¨)
             .· ´¸.·*´¨) ¸.·*¨)
                     (¸.·´ (¸.·'* ☆

Whoosh and <code>{0}</code>""".format(txt)
	elif a=="fairy":
		text = r""".∧＿∧
( ･ω･｡)つ━☆・*。
⊂  ノ    ・゜ .
しーＪ   °。  *´¨)
             .· ´¸.·*´¨) ¸.·*¨)
                     (¸.·´ (¸.·'* ☆

<code>{0}</code>""".format(txt)
	elif a=="help":
		text = "<b><i>Available arts with text:</i></b>\n<code>tv</code>\n<code>whoosh</code>\n<code>fairy</code>" 
	else:
		text = "<i>Art not found. Type <code>%nmart help</code> for all arts</i>" 
	msg.edit(text) 
@Client.on_message(filters.command("nmph", prefixes = "%")&filters.me)
def ph(_, msg):
	if msg.reply_to_message!=None:
		reply_message = msg.reply_to_message
		data = check_media(reply_message)
		if isinstance(data, bool):
			msg.edit("<b>Reply to photo or video/gif</b>")
			return
	else:
		msg.edit("<b>Reply to photo or video/gif</b>")
		return	
	file = _.download_media(data)
	path = requests.post('https://te.legra.ph/upload', files={'file': ('file', file, None)}).json()
	try:
		link = 'https://te.legra.ph'+path[0]['src']
	except KeyError:
		link = path["error"]
	msg.edit("<b>"+link+"</b>")
def check_media(reply_message):
	if reply_message and reply_message.media:
		if reply_message.photo:
			data = reply_message.photo
		elif reply_message.video:
			data = reply_message.video 
		else:
			return False
	if not data or data is None:
		return False
	else:
		return data 
