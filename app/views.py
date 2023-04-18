from django.shortcuts import render
from app.models import *
from django.http import HttpResponse


# Create your views here.
def insert_topic(request):
    
     if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        return HttpResponse('topic_name is submitted successfully !!')
     
        return render(request,'insert_topic.html')
     
def insert_web(request):
    LOT=Topic.objects.all()
    d={'topics':LOT }
    if request.method=='POST':
        tn=request.POST['topic']
        TO=Topic.objects.get(topic_name=tn)
        name=request.POST['name']
        url=request.POST['url']
        email=request.POST['email']
        WO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url,email=email)[0]
        WO.save()
        return HttpResponse('WEBPAGE DATA IS INSERTED SUCCESSFULLY !!!!!')
    return render(request,'insert_web.html',context=d)


def insert_acces(request):
    LOA=Webpage.objects.all()
    d={'acess':LOA}
    if request.method=='POST':
        name=request.POST['wb']
        Wb=Webpage.objects.get(name=name)
        author=request.POST['author']
        date=request.POST['date']
        AC=AccessRecord.objects.get_or_create(name=Wb,author=author,date=date)[0]
        AC.save()
        return HttpResponse('AcessRecord is  submitted successfully !!!')
    return render(request,'insert_acces.html',d)


    
    
