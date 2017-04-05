#Imports:
import telebot 
from telebot import types
import editdistance

#Token for Telegram Bot:
bot= telebot.TeleBot("371335528:AAFDplGN8aKIfri4_ll09CyLRaAIZ4rqyB8")


def levPole(s1):
	pol="Pole"
	pol2="oro"
	
	if ((s1[1]=="P" or s1[1]=="o")):
		if (editdistance.eval(s1,pol)<3 or editdistance.eval(s1,pol2)<3):
			if (editdistance.eval(s1,pol)!=0 and editdistance.eval(s1,pol2)!=0):
				return True

def levSubPole(s1):
	spol="Subpole"
	spol2="plata"
	
	if ((s1[1]=="S" or s1[1]=="p")):
		if (editdistance.eval(s1,spol)<3 or editdistance.eval(s1,spol2)<3):
			if (editdistance.eval(s1,spol)!=0 or editdistance.eval(s1,spol2)!=0):
				return True

def levFail(s1):
	fl="Fail"
	fl2="bronce"
	
	if (s1[1]=="F" or s1[1]=="b"):
		if(editdistance.eval(s1,fl)<3 or editdistance.eval(s1,fl2)<3):
			if (editdistance.eval(s1,fl)!=0 or editdistance.eval(s1,fl2)!=0):
				return True



#Bot message usage:
@bot.message_handler(func= lambda m: True)
def respuesta(m):
	if (levPole(m.text)):
		bot.send_message(m.chat.id,"Has ganado moralmente")
	elif (levSubPole(m.text)):
		bot.send_message(m.chat.id,"Casi lo consigues, campeón")
	elif (levFail(m.text)):
		bot.send_message(m.chat.id,"Gracias por intentarlo")

@bot.message_handler(func= lambda m: m.text=="Sonríe, eres especial")
def muerte(m):
	bot.reply_to(m,":(")

print("Running...")
bot.polling()
