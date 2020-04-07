from django.shortcuts import render , get_object_or_404, redirect
from .models import Main
from django.core.files.storage import FileSystemStorage
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
from django.contrib.auth import authenticate, login, logout
from trending.models import Trending
import random
from random import randint
from django.contrib.auth.models import User, Group, Permission
from manager.models import Manager
import string
from random import randint
# Create your views here.

def home(request):

    # site = Main.objects.filter(pk=2)
    site = Main.objects.get(pk = 1)
    news = News.objects.all().order_by('-pk')
    lastnews = News.objects.all().order_by('-pk')[:3]
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()

    popnews = News.objects.all().order_by('-show')
    popnews2 = News.objects.all().order_by('-show')[:3]
    trending = Trending.objects.all().order_by('-pk')[:5]

    #random_object = Trending.objects.all()[random(0,len(trending)-1)]

    return render(request, 'front/home.html', {'site' : site, 'news': news, 'cat':cat, 'subcat': subcat, 'lastnews': lastnews, 'popnews':popnews,'popnews2':popnews2, 'trending':trending})

def about(request):
    site = Main.objects.get(pk=2)
    news = News.objects.filter(act=1).order_by('-pk')
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
    lastnews = News.objects.filter(act=1).order_by('-pk')[:3]
    popnews = News.objects.filter(act=1).order_by('-show')
    popnews2 = News.objects.filter(act=1).order_by('-show')[:3]
    trending = Trending.objects.all().order_by('-pk')[:5]
    return render(request, 'front/about.html', {'site' : site, 'news': news, 'cat':cat, 'subcat': subcat, 'lastnews': lastnews, 'popnews':popnews,'popnews2':popnews2, 'trending':trending})

def panel(request):

    # login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # login check end

    perm = 0
    perms = Permission.objects.filter(user=request.user)
    for i in perms :
        if i.codename == "master_user" : perm = 1

    rand = ""
    for i in range(10):
        rand = rand + random.choice(string.ascii_letters)

    return render(request, 'back/home.html',{'rand':rand})

def mylogin(request):

    if request.method == 'POST':
        utxt = request.POST.get('username')
        ptxt = request.POST.get('password')

        if utxt != "" and ptxt != "":
            user = authenticate(username = utxt, password = ptxt)

            if user != None:

                login(request , user)
                return redirect('panel')

    return render(request, 'front/login.html')

def myregister(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if name == "" :
            msg = "Input Your Name"
            return render(request, 'front/msgbox.html', {'msg':msg})


        if password1 != password2 :
            msg = "Your Pass Didn't Match"
            return render(request, 'front/msgbox.html', {'msg':msg})

        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0

        for i in password1 :

            if i >= "0" and i <= "9" :
                count1 = 1
            if i >= "A" and i <= "Z" :
                count2 = 1
            if i >= 'a' and i <= 'z' :
                count3 = 1
            if i >= "!" and i <= "(" :
                count4 = 1

        if count1 == 0 or count2 == 0 or count3 == 0 or count4 == 0 :
            msg = "Your Pass Is Not Strong"
            return render(request, 'front/msgbox.html', {'msg':msg})

        if len(password1) < 8 :
            msg = "Your Pass Most Be 8 Character"
            return render(request, 'front/msgbox.html', {'msg':msg})

        if len(User.objects.filter(username=uname)) == 0 and len(User.objects.filter(email=email)) == 0 :

            user = User.objects.create_user(username=uname,email=email,password=password1)
            b = Manager(name = name, utxt = uname, email = email)
            b.save()

    return render(request, 'front/login.html')

def mylogout(request):

    logout(request)

    return redirect('mylogin')

def site_setting(request):

    # login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # login check end



    if request.method == 'POST':
        name = request.POST.get('name')
        tell = request.POST.get('tell')
        fb = request.POST.get('fb')
        tw = request.POST.get('tw')
        yt = request.POST.get('yt')
        txt = request.POST.get('txt')
        link = request.POST.get('link')

        if fb == "" : fb = "#"
        if tw == "" : tw = "#"
        if yt == "" : yt = "#"
        if link == "" : link = "#"

        if name == "" or tell == "" or txt == "":
            error = "All Fiels Required Filled"
            return render(request, 'back/error.html',{'error':error})

        try:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)

            picurl = url
            picname = filename

        except:
            picurl = "-"
            picname = "-"


        try:
            myfile2 = request.FILES['myfile2']
            fs2 = FileSystemStorage()
            filename2 = fs2.save(myfile2.name, myfile2)
            url2 = fs2.url(filename2)

            picurl2 = url2
            picname2 = filename2
        except:
            picurl2 = "-"
            picname2 = "-"


        b = Main.objects.get(pk = 1)
        b.name = name
        b.tell = tell
        b.tw = tw
        b.fb = fb
        b.link = link
        b.yt = yt
        b.about = txt
        if picurl != "-" : b.picurl = picurl
        if picname != "-" : b.picname = picname
        if picurl2 != "-" : b.picurl2 = picurl2
        if picname2 != "-" : b.picname2 = picname2
        b.save()

    site = Main.objects.get(pk=1)

    return render(request, 'back/settings.html',{'site':site})


def about_setting(request):

    # login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # login check end

    if request.method == 'POST':

        txt = request.POST.get('txt')

        if txt == "":
            error = "All Fiels Required Filled"
            return render(request, 'back/error.html',{'error':error})

        b = Main.objects.get(pk=1)
        b.abouttxt = txt
        b.save()

    about = Main.objects.get(pk=1).abouttxt

    return render(request, 'back/about_setting.html', {'about': about})



def contact(request):

    site = Main.objects.get(pk = 1)
    news = News.objects.all().order_by('-pk')
    lastnews = News.objects.all().order_by('-pk')[:3]
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()

    popnews = News.objects.all().order_by('-show')
    popnews2 = News.objects.all().order_by('-show')[:3]
    trending = Trending.objects.all().order_by('-pk')[:5]

    return render(request, 'front/contact.html',{'site' : site, 'news': news, 'cat':cat, 'subcat': subcat, 'lastnews': lastnews, 'popnews':popnews,'popnews2':popnews2, 'trending':trending})



def change_pass(request):

    # login check start
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end

    if request.method == 'POST' :

        oldpass = request.POST.get('oldpass')
        newpass = request.POST.get('newpass')

        if oldpass == "" or newpass == "" :
            error = "All Fields Requirded"
            return render(request, 'back/error.html' , {'error':error})

        user = authenticate(username=request.user, password=oldpass)

        if user != None :

            if len(newpass) < 8 :
                error = "Your Password Most Be At Less 8 Character"
                return render(request, 'back/error.html' , {'error':error})

            count1 = 0
            count2 = 0
            count3 = 0
            count4 = 0

            for i in newpass :

                if i > "0" and i < "9" :
                    count1 = 1
                if i > "A" and i < "Z" :
                    count2 = 1
                if i > 'a' and i < 'z' :
                    count3 = 1
                if i > "!" and i < "(" :
                    count4 = 1

            if count1 == 1 and count2 == 1 and count3 == 1 and count4 == 1 :

                user = User.objects.get(username=request.user)
                user.set_password(newpass)
                user.save()
                return redirect('mylogout')
            else:
                error = "Your Password Is Not Correct in formate"
                return render(request, 'back/error.html' , {'error':error})

        else:

            error = "Your Password Is Not Correct"
            return render(request, 'back/error.html' , {'error':error})


    return render(request, 'back/changepass.html')
