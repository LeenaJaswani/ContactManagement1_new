from django.db import models

from django.core.validators import RegexValidator

# Create your models here.
class UserInfo(models.Model):
	
	Name=models.CharField(max_length=50)
	EmailAddress=models.CharField(max_length=50)
	phoneregex=RegexValidator(regex=r'^\+?1?\d{9,15}$',message="Enter in +9666666699.Upto 15 digits")	
	ContactNumber=models.CharField(validators=[phoneregex],max_length=15)
	
	HomeAddress=models.TextField(default='',blank=True)
	Birthday=models.DateField(default='',blank=True,null=True)
	Nickname=models.CharField(max_length=50,blank=True,null=True)
	def __str__(self):
		return self.Name