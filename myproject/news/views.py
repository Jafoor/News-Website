from django.shortcuts import render , get_object_or_404, redirect
from .models import News
from main.models import Main
from django.core.files.storage import FileSystemStorage
# Create your views here.

def news_detail(request, word):

    site = Main.objects.get(pk=1)
    news = News.objects.filter(name = word)

    return render(request, 'front/news_detail.html', {'news': news, 'site':site})

def news_list(request):

    news = News.objects.all()
    return render(request, 'back/news_list.html', {'news': news})


def news_add(request):

    if request.method == 'POST':
        newstitle = request.POST.get('newstitle')
        newscat = request.POST.get('newscat')
        newstxtshort = request.POST.get('newstxtshort')
        newstxt = request.POST.get('newstxt')

        if newstitle == "" or newstxt == "" or newstxtshort == "" or newscat == "":
            error = "All Fiels Required"
            return render(request, 'back/error.html' ,{'error':error})

        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        url = fs.url(filename)

        b = News(name = newstitle , short_txt = newstxtshort , body_txt = newstxt, date = '2020' ,pic = url, writer = '-', catname = newscat, catid = 0, show = 0)
        b.save()
        return redirect('news_list')

    return render(request, 'back/news_add.html')
