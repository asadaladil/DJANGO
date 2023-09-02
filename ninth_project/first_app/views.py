from django.shortcuts import render
from datetime import datetime,timedelta
from django.http import HttpResponse
# Create your views here.

#...............Cookie................

def home(request):
    response=render(request,'home.html')
    response.set_cookie('name','Adil')
    #response.set_cookie('name','Adil 2',max_age=10)# kotokkon rakte chai...
    response.set_cookie('name','Adil 2',expires=datetime.utcnow()+timedelta(days=7))# 7 din dhore set kora thakbe.....
    return response

def get_cookie(request):
    name=request.COOKIES.get('name')
    print(request.COOKIES)
    return render(request,'get_cookie.html',{'name':name})


def delete_cookie(request):
    response=render(request,'del.html')
    response.delete_cookie('name')
    return response



# Session vs cookie
""" 
session--> authentication related-ATM card related.
cookie--> dark mode, language change, remember me....

"""

def set_session(request):
    data={
        'name':'Adil',
        'age':19,
        'language': 'Bangla'
    }
    request.session.update(data)
    return render(request,'home.html')


def get_session(request):
    if 'name' in request.session:
        name=request.session.get('name')
        request.session.modified=True
        return render(request,'get_session.html',{'name':name})
    else:
        return HttpResponse("Your session has expired.Login Again")

def delete_session(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request,'del.html')