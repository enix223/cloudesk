from django.db import models
from django.contrib.auth.models import User

DB_TYPES = ((1, 'MS SQL Server'), (2, 'MySQL'), )
EXPORT_FILE_TYPE = ((1, 'Excel 2007/2010 format (.xlsx)'), (2, 'Excel 2003 format (.xls)'), (3, 'Comma separated file (.csv)'), )


class Connection(models.Model):
    dbtype = models.IntegerField('DB Type', choices=DB_TYPES)
    name = models.CharField('DB Connection name', max_length=50)
    server = models.CharField('DB Server Address', max_length=100)
    user = models.CharField('DB User name', max_length=50)
    password = models.CharField('DB User Password', max_length=100)
    port = models.IntegerField('DB Server Port')
    database = models.CharField('DB Catalog/Database Name', max_length=100)
    owner = models.ForeignKey(User)




