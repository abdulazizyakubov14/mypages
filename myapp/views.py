from django.shortcuts import render
from.models import*
from django.contrib import messages
import telebot
my_id = 1705528794
bot = telebot.TeleBot('1748274627:AAHHZGfA8bYPDzKKJmUHIqHNinW2rTC03Wg')


# Create your views here.

def index(request):
	porto = Portfolio.objects.all()
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		phone = request.POST['phone']
		message = request.POST['message']
		Contact.objects.create(name=name,phone=phone,email=email,message=message)
		# messages.add_message(request, messages.SUCCESS, 'Tabriklaymiz aloqa muofaqiyat amalga oshirildi tez orada sizbilan bog\'lanamiz')
		bot.send_message(my_id,f"Sayitdan xabar bor\nIsmi:  {name}\nTelfon raqami:  {phone}\nEmail:  {email}\n Xabari:  {message}")
	return render(request,'index.html',{'porto':porto})
