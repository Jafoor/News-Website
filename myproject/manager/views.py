from django.shortcuts import render , get_object_or_404, redirect
from .models import Manager
from django.core.files.storage import FileSystemStorage
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
from django.contrib.auth import authenticate, login, logout
from trending.models import Trending
import random
from random import randint
from django.contrib.auth.models import User

# Create your views here.

def manager_list(request):

    manager = Manager.objects.all()

    return render(request , 'back/manager_list.html',{'manager':manager})

def manager_del(request, pk):

    manager = Manager.objects.get(pk=pk)
    b = User.objects.filter(username = manager.utxt)
    b.delete()

    manager.delete()
    return redirect('manager_list')
