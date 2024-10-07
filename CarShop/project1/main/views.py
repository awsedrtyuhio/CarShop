from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

from .forms import Image
from .models import LoadMultipleImages
from .data import *

# Create your views here.

def index(request):
    
    return render(request, 'main\index.html', {'cars': cars, 'categoryes': categoryes, 'category': category, 'isAdmin': isAdmin, 'isLogin': isLogin, 'user': user})

def SingIn(request):
    if request.method == 'POST':
        luser = request.POST

        for _user in users:
            if _user['login'] == luser['login'] and _user['password'] == luser['password']:
                global isLogin, isAdmin, user
                isLogin = True
                isAdmin = bool(_user['isAdmin'])
                user = _user
                

                print(isAdmin)
                return render(request, 'main\index.html', {'cars': cars, 'categoryes': categoryes, 'category': category, 'isAdmin': isAdmin, 'isLogin': isLogin, 'user': user})
        return render(request, 'main\SingIn.html', {'isFailed': True, 'categoryes': categoryes})
    else: return render(request, 'main\SingIn.html', {'categoryes': categoryes})

def SingUp(request):
    if request.method == 'POST':
        ruser = request.POST
        form = Image(ruser, request.FILES)

        if form.is_valid():
            form.save()
            img_obj = form.instance

            global users, user, isLogin, isAdmin

            for _user in users:
                if _user['login'] == ruser['login']:
                    return render(request, 'main\SingUp.html', {'form': Image, 'categoryes': categoryes})

            users.append({
                'login': ruser['login'],
                'password': ruser['password'],
                'isAdmin': False,
                'img': img_obj.image.url
            })

            isLogin = True
            isAdmin = False
            user = users[len(users) - 1]
            

            return render(request, 'main\index.html', {'cars': cars,  'categoryes': categoryes, 'category': category,  'isAdmin': isAdmin, 'isLogin': isLogin, 'user': user})
    else: return render(request, 'main\SingUp.html', {'form': Image, 'categoryes': categoryes})

def Exit(request):
    global isAdmin, isLogin, user
    isAdmin = False
    isLogin = False
    user = None

    
    return render(request, 'main\index.html', {'cars': cars, 'categoryes': categoryes, 'category': category, 'isAdmin': isAdmin, 'isLogin': isLogin, 'user': user})

def Sort(request):
    global category
    category = None if request.POST['Category'] == "Все" else request.POST['Category']
    
    return render(request, 'main\index.html', {'cars': cars, 'categoryes': categoryes, 'category': category, 'isAdmin': isAdmin, 'isLogin': isLogin, 'user': user})
    
def Search(request):
    resul = []
    
    for item in cars:
        if str(item['name']).lower() == request.POST['Search'].lower() or str(item['name']).lower().__contains__(request.POST['Search'].lower()):
            if category != None and item['category'] == category:
                resul.append(item)
            else:
                resul.append(item)

    if len(resul) > 0:
        return render(request, 'main\index.html', {'cars': resul, 'categoryes': categoryes, 'category': category, 'isAdmin': isAdmin, 'isLogin': isLogin, 'user': user})
    else:
        if category == None:
            return render(request, "main\Error.html", {'error': "По запросу '" + request.POST['Search'] + "' ничего не найдено!"})
        else:
            return render(request, "main\Error.html", {'error': "В категории '" + category + "' по запросу '" + request.POST['Search'] + "' ничего не найдено!"})

def Remove(request):
    name = request.POST['name']

    _list = []

    for item in cars:
        if item['name'] != name:
            _list.append(item)

    cars.clear()
    for item in _list:
        cars.append(item)

    return render(request, 'main\index.html', {'cars': cars, 'categoryes': categoryes, 'category': category, 'isAdmin': isAdmin, 'isLogin': isLogin, 'user': user})

def About(request):
    if request.method == 'POST':
        pass
    else:
        car = GetCarByName(request.GET['name'])

        sum = 0
        haveUserComment = False

        try:
            for comment in car['comments']:
                sum += int(comment['raiting'])
                if user != None and comment['user']['login'] == user['login']:
                    haveUserComment = True
            
            return render(request, 'main/about.html', {'user': user, 'isLogin': isLogin, 'categoryes': categoryes, 'car': car, 'aRaiting': sum/len(car['comments']), 'haveUserComment': haveUserComment})
        except:
            return render(request, 'main/about.html', {'user': user, 'isLogin': isLogin, 'categoryes': categoryes, 'car': car, 'aRaiting': 0, 'haveUserComment': haveUserComment})

def Comment(request):

    for car in cars:
        if car['name'] == request.POST['name']:
            car['comments'].append({
                'user': user,
                'raiting': int(request.POST['raiting']),
                'comment': request.POST['comment'],
            })
            break

    return render(request, 'main\index.html', {'cars': cars, 'categoryes': categoryes, 'category': category, 'isAdmin': isAdmin, 'isLogin': isLogin, 'user': user})

def AddCar(request):
    if request.method == 'POST':
        newCar = request.POST
        
        form = Image(newCar, request.FILES)

        if form.is_valid():
            form.save()
            img_obj = form.instance

            cars.append({
                'name': newCar['name'],
                'category': newCar['category'],
                'img': img_obj.image.url,
                'price': float(newCar['price']),
                'comments': [],
                'about': newCar['about']
            })
        return render(request, 'main\index.html', {'cars': cars, 'categoryes': categoryes, 'category': category, 'isAdmin': isAdmin, 'isLogin': isLogin, 'user': user})
    else:
        return render(request, 'main\AddCar.html', {'categoryes': categoryes, 'form': Image, 'isLogin': isLogin, 'user': user})

def Change(request):
    if request.method == 'POST':
        newCar = request.POST

        for item in cars:
            if item['name'] == newCar['oldName']:

                item['name'] = newCar['name']
                item['category'] = newCar['category']
                item['img'] = newCar['img']
                item['price'] = float(newCar['price'])
                item['about'] = newCar['about']

                break

        return render(request, 'main\index.html', {'cars': cars, 'categoryes': categoryes, 'category': category, 'isAdmin': isAdmin, 'isLogin': isLogin, 'user': user})
    else:

        for item in cars:
            if item['name'] == request.GET['name']:
                return render(request, 'main\Change.html', {'categoryes': categoryes, 'car': item})