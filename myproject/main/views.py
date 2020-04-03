from django.shortcuts import render , get_object_or_404, redirect
from .models import Main
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def home(request):

    # site = Main.objects.filter(pk=2)
    site = Main.objects.get(pk = 1)
    news = News.objects.all().order_by('-pk')
    lastnews = News.objects.all().order_by('-pk')[:3]
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()

    return render(request, 'front/home.html', {'site' : site, 'news': news, 'cat':cat, 'subcat': subcat, 'lastnews': lastnews})

def about(request):
    site = Main.objects.get(pk = 1)
    return render(request, 'front/about.html', {'site' : site})

def panel(request):

    # login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # login check end

    return render(request, 'back/home.html')

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


def mylogout(request):

    logout(request)

    return redirect('mylogin')
