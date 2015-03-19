from django.db import models
from django.contrib.auth.models import User

class ConnectionModel(models.Model):
	server   = models.CharField('DB Server Address', max_length=100)
	user     = models.CharField('DB User name', max_length=50)
	password = models.CharField('DB User Password', max_length=100)
	port     = models.IntegerField('DB Server Port')
	database = models.CharField('DB Catalog/Database Name', max_length=100)
	owner    = models.ForeignKey(User)

	

