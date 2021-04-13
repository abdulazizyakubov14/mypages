from django.db import models

# Create your models here.
class Portfolio(models.Model):
	name = models.CharField('Ismi',max_length=200)
	proyekt_name = models.CharField('Proyekt nomi',max_length=500)
	image = models.ImageField('Proyekt rasmi',upload_to='Porfolio/')

	class Meta:
		verbose_name = 'Portfolio'
		verbose_name_plural = 'Portfoliolar'

	def __str__(self):
		return f"{self.name}"

class Contact(models.Model):
	name = models.CharField('Ismi',max_length=300)
	email = models.EmailField('Email',max_length=300)
	phone = models.CharField('Telfon raqami',max_length=300)
	message = models.TextField('Xabar')

	class Meta:
		verbose_name = 'Aloqa'
		verbose_name_plural = 'Aloqalar'

	def __str__(self):
		return f"{self.name}"