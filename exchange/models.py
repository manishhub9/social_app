from __future__ import unicode_literals

from django.db import models

class Country(models.Model):
		cid = models.AutoField(primary_key = True)
		c_name = models.CharField(max_length = 100)
		c_code = models.CharField(max_length = 50)

		def __str__(self):
			return u'%s %s' % (self.c_name,self.c_code)
		
