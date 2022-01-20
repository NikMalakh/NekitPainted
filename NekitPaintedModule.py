from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from time import sleep
import random  
import requests
import math
import cmath
chid=0
'''
{"settings": {"debug": "True"}, "creationlist": ["idk", "NoName"], "notes": {"test": "lo"}}
'''
def datadef():
    return {"name":"NekitPaintedModule","help":"Type %nmhelp for help","description":"Official module for Painted Userbot. One day it can become popular"}
def sqrt(x):
	try:
		if x>=0:
			return math.sqrt(x)
		else:
			return cmath.sqrt(x)
	except:
		return cmath.sqrt(x)
def flt(x):
	try:
		if float(x)%1==0:
			return int(x) 
		else:
			return float(x) 
	except:
		return x
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
@Client.on_message(filters.command("nmprocess", prefixes = "%")&filters.me)
def ugnet(_, msg):
	orig_text=msg.text.split("%nmprocess ", maxsplit = 1)[1]
	text = orig_text
	msg.edit("<i>Starting {0}...</i>".format(text))
	percent = 0
	while(percent<100):
		try:
			msg.edit("<i><b>{0}: </b>".format(text)+str(percent)+"%</i>")
			percent += random.randint(1,5)
			sleep(0.05)
		except FloodWait as e:
			sleep(e.x)
	msg.edit("<b><i>✔️ {0} finished successfully</i></b>".format(text))
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
	msg.edit("<b>Nekit Painted Module commands:</b>\n\n<b><i>Message flood: </i></b><code>%nmspam</code> <i>[amount] [text]</i>, <code>%nmspamphoto</code> <i>[amount] [URL]</i>, <code>%nmspamvideo</code> <i>[amount] [URL]</i>, <code>%nmspamsticker</code> <i>[amount] [URL]</i>, <code>%nmspamdoc</code> <i>[amount] [URL]</i>, <code>%nmspamgif</code> <i>[amount] [URL]</i>, <code>%nmspamvoice</code> <i>[amount] [URL]</i>\n<b><i>Arts: </i></b><code>%nmart</code> <i>[art]|help</i>, <code>%nmcart</code> <i>([art] text)|help</i>\n<b><i>Animations: </i></b><code>%nmprocess</code> <i>text</i>, <code>%nmtype</code> <i>text</i>, <code>%nmctype</code> <i>[symbol] [text]</i>, <code>%nmticker</code> <i>text</i>\n<b><i>Chat action simulation: </i></b><code>%nmstatus</code> <i>typing|upload_photo|upload_video|upload_audio|upload_document|find_location|upload_video_note|choose_contact|playing|speaking|cancel</i>\n<b><i>Message search: </i></b><code>%nmlast</code> <i>message limit</i>, <code>%nmsearch</code> <i>[message limit] [query]</i>\n<b><i>Chat information: </i></b><code>%nmcountmsg</code>\n<b><i>Self-destructive messages: </i></b><code>%nmdes</code> <i>[amount of seconds] [message text]</i>\n<b><i>Calculations: </i></b> <code>%nmrand</code> <i>[lower limit] [higher limit]</i>, <code>%nmcalc</code> <i>expression <b><u>(unsafe!)</u></b>, <code>%nmeq</code> <i>([type] [numbers])|help</i>, <code>%nmmath</code> [operation] [operands]</i>\n<b><i>Technical commands: </i></b> <code>%nnmtest</code>, <code>%nmversion</code>") 
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
	msg.edit("<i><b>Nekit Painted Module</b> for <b>Painted-Userbot</b> v1.2.0\nDo not distribute</i>")
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
		text = "<i>Art not found. Type <code>%nmcart help</code> for all arts</i>" 
	msg.edit(text) 
@Client.on_message(filters.command("nmcopy", prefixes = "%")&filters.me)
def copy(_, msg):
	if not hasattr(msg.reply_to_message, 'text'):
		msg.edit("<i><b>A reply is required</b></i>")
		return
	message = msg.reply_to_message 
	user = message.from_user
	id = user.id
	fstname = user.first_name
	lstname = "" if user.last_name is None else user.last_name
	bio = "" if _.get_chat(id).bio is None else _.get_chat(id).bio[:69]
	msg.delete()
	_.update_profile(first_name=fstname, last_name=lstname, bio=bio)
	_.set_profile_photo(_.download_media(_.get_profile_photos(id, limit=1)[0].file_id))
@Client.on_message(filters.command("nmph", prefixes = "%")&filters.me)
def ph(_, msg):
	if message.photo is None:
		return
	chid = msg.chat.id
	photo = _.download_media(msg)
	with open(photo, 'rb') as f:
   		_.send_message(chid, requests.post('http://telegra.ph/upload', files={'file': ('file', f, 'image/jpeg')}  ).json())

@Client.on_message(filters.command("nmeq", prefixes = "%")&filters.me)
def eq(_, msg):
	args=msg.text.split(" ")
	try:
		typ=args[1]
		oth=msg.text.split(" ", maxsplit=2)[2]
	except:
		pass
	if typ=="l":
		try:
			numbers=oth.split(" ") 
			k=flt(numbers[0])
			b=flt(numbers[1])
		except:
			msg.edit("<i>Please provide 2 numbers: <code>k b</code>, where <code>kx=b</code></i>")
			return
		if k==0:
			msg.edit("<i>Equation has no roots as <code>k=0</code></i>")
			return
		result=flt(b/k) 
		msg.edit("<i><b>{0}x={1}</b>\nx=b/k={1}/{0}=<b>{2}</b></i>".format(k, b, result))
	elif typ=="q":
		try:
			numbers=oth.split(" ") 
			a=flt(numbers[0])
			b=flt(numbers[1])
			c=flt(numbers[2])
		except:
			msg.edit("<i>Please provide 3 numbers: <code>a b c</code>, where <code>ax²+bx+c=0</code></i>")
			return
		d=flt(b**2-4*a*c) 
		x1=flt((-b+sqrt(d))/(2*a)) 
		x2=flt((-b-sqrt(d))/(2*a)) 
		msg.edit("<i><b>{0}x²+{1}x+{2}=0</b>\n<b>Step 1. </b>Calculate discriminant\nΔ=b²-4ac=({1})²-4*{0}*{2}={3}\n<b>Step 2. </b>Find roots using quadratics root formula\nx=(-b±√Δ)/(2a)=({4}±√({3}))/(2*{0})\nx=[{5}; {6}]</i>".format(a, b, c, d, -b, x1, x2))
	elif typ=="b":
		try:
			numbers=oth.split(" ") 
			a=flt(numbers[0])
			b=flt(numbers[1])
			c=flt(numbers[2])
		except:
			msg.edit("<i>Please provide 3 numbers: <code>a b c</code>, where <code>ax⁴+bx²+c=0</code></i>")
			return
		d=flt(b**2-4*a*c) 
		t1=flt((-b+sqrt(d))/(2*a)) 
		t2=flt((-b-sqrt(d))/(2*a)) 
		x1=flt(sqrt(t1)) 
		x2=flt(-sqrt(t1)) 
		x3=flt(sqrt(t2)) 
		x4=flt(-sqrt(t2)) 
		msg.edit("<i><b>{0}x⁴+{1}x²+{2}=0</b>\nAssume <code>t=x²</code>, so <b>{0}t²+{1}t+{2}=0</b>\n<b>Step 1. </b>Calculate discriminant\nΔ=b²-4ac=({1})²-4*{0}*{2}={3}\n<b>Step 2. </b>Find roots using quadratics root formula\nt=(-b±√Δ)/(2a)=({4}±√({3}))/(2*{0})\nt=[{5}; {6}]\n<b>Step 3. </b>Solve equation x²=t for each <code>t</code>\nx=[{7}; {8}; {9}; {10}]</i>".format(a, b, c, d, -b, t1, t2, x1, x2, x3, x4))
	elif typ=="help":
		msg.edit("<i><b>Available types of equations</b>\n<code>•l</code>\nNumbers: <code>a b</code>, where ax=b\n<code>•q</code>\nNumbers: <code>a b c</code>, where ax²+bx+c=0\n<code>•b</code>\nNumbers: <code>a b c</code>, where ax⁴+bx²+c=0</i>")
	else:
		msg.edit("<i>I can't solve this type of equation. Type <code>%nmeq help</code> for all available types</i>")
@Client.on_message(filters.command("nmmath", prefixes = "%")&filters.me)
def math(_, msg):
	args=msg.text.split(" ")
	try:
		typ=args[1]
		oth=msg.text.split(" ", maxsplit=2)[2]
		numbers=oth.split() 
	except:
		pass
	if typ=="sqrt":
		a = flt(numbers[0])
		if a>=0:
			val = flt(sqrt(a)) 
		else:
			val = cmath.sqrt(a)
		expr = "√({0})".format(a) 
	elif typ=="cbrt":
		a=flt(numbers[0])
		if a>=0:
			val = flt(a**(1./3))
		else:3125
			val = -flt(abs(a)**(1./3))
		expr="³√{0}".format(a)
	elif typ=="root":
		a=flt(numbers[0])
		pw=flt(numbers[1])
		if a>=0:
			val = flt(a**(1./pow)) 
		elif a<0 and pw%2!=0:
			val = -flt(abs(a)**(1./pw)) 
		elif a<0 and pw==2:
			val = cmath.sqrt(a)
		else:
			val = cmath.pow(a, 1./pw)
		expr = "{0}^(1/{1})".format(a, pw) 
	elif typ=="pow":
		a=flt(numbers[0])
		pw=flt(numbers[1])
		val = flt(a**pw) 
		expr = "{0}^({1})".format(a, pw)  
	elif typ=="abs":
		a=flt(numbers[0]) 
		val=flt(abs(a)) 
		expr="|{0}|".format(a) 
	else:
		msg.edit("<i><b>Available functions</b>\n•<code>sqrt<code> a — returns square root of a\n•<code>cbrt</code> a — returns cubic root of a\n•<code>root</code> a pow — returns root of a, pow defines power of root\n•<code>pow</code> a pow — returns a to power of pow\n•<code>abs</code> a — returns absolute value of a</i>")
		return 
	msg.edit("<i><b>Expression: </b>{0}\n<b>Value: {1}</b></i>".format(expr, val))
 
