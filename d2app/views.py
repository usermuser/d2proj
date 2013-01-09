#! -*- coding:utf-8 -*-
# Create your views here.
from django.shortcuts import render_to_response, HttpResponse
from d2app.models import Hero, Item

def get_herofunc(request, heroname):
    try:
        tryvar=Hero.objects.get(name=heroname)
        #tryitem=Hero.objects.get(itemname=tryvar.item)
#        tryitem=Item.objects.get(item=tryvar.item)
#        tryitem=Item.objects.get(name=tryvar.item)
    except Hero.DoesNotExist:
        return HttpResponse('Героя с таким именем нет!')

#    return render_to_response('base.html',{'tryvar': tryvar},{'tryitem':tryitem})
    return render_to_response('base.html',{'tryvar': tryvar})
#    return render_to_response('base.html',{'tryvar': tryvar},{'tryitem1':tryitem1},{'tryitem2':tryitem2})

#def hello(request):
#    return HttpResponse('Здравствуй Мир!')

#def eartfunc(request):
#    var=Hero.objects.get(name='earthshaker')
#    return render_to_response('earthshaker.html',{'var': var})

#def get_hero(request, hero1):
#    try:
#        hero_o=Hero.objects.get(name=hero1)
#    except Hero.DoesNotExists:
#        return http.HttpResponse('Героя с таким именем не существкует!')
#
#    return render_to_response('earthshaker.html',{'var': var})
    
