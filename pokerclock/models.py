from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Tournament(models.Model):

	blinds = models.CharField(default="", max_length=200) #sghdfjdfj
	players = models.IntegerField(default=3)
	level_time = models.IntegerField(default=10)
	buy_in = models.IntegerField(default=0)
	rebuys_bool = models.BooleanField(default=False)
	addon_bool = models.BooleanField(default=False)
	rebuy_level_stop = models.IntegerField(default=6)
	rebuy_price = models.IntegerField(default=0)
	addon_price = models.IntegerField(default=0)
	break_time = models.IntegerField(default=0)
	knockout_type = models.CharField(default="C", max_length=1) #A - fixed, B - progressive, C - no KO
	knockout_price = models.IntegerField(default=0)
	player_names = models.CharField(default="", max_length=200)

	def __str__(self):
		return self.name