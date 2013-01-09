from django.db import models

class Item(models.Model):
    itemname=models.CharField(max_length=30)

    def __unicode__(self):
        return self.itemname

class Hero(models.Model):
    name = models.CharField(max_length=30)
    #headshot = models.CharField(max_length=50)
    skill1txt = models.TextField()
    skill2txt = models.TextField()
    skill3txt = models.TextField()
    skill4txt = models.TextField()
    skill5txt = models.TextField(blank=True)
    skill6txt = models.TextField(blank=True)
    skill7txt = models.TextField(blank=True)
    skill8txt = models.TextField(blank=True)
    skill9txt = models.TextField(blank=True)
    skill10txt = models.TextField(blank=True)
    skill11txt = models.TextField(blank=True)
    skill12txt = models.TextField(blank=True)
    skill13txt = models.TextField(blank=True)
    skill14txt = models.TextField(blank=True)
    strenght = models.TextField()
    agility = models.TextField()
    intellect = models.TextField()

    item=models.ManyToManyField(Item)
    def __unicode__(self):
        return self.name

class Meta:
    ordering = ["name"]

#make expand for skills from 7 to 14

