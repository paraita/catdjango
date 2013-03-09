'''
Created on 9 mars 2013

@author: paraita
'''

from django.db import models

class Enigme(models.Model):
    id_enigme = models.IntegerField(default=0)
    titre = models.CharField(max_length=200)
    question = models.CharField(max_length=2000)
    reponse = models.CharField(max_length=200)  # la bonne reponse a donner
    indice = models.CharField(max_length=200)   # indication vers le prochain indice
    
    def __unicode__(self):
        return "[" + str(self.id_enigme) + ": " + self.titre + "]"
    
