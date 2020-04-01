from django.shortcuts import render , get_object_or_404, redirect
from .models import News
from main.models import Main
from django.core.files.storage import FileSystemStorage
import datetime
from subcat.models import SubCat
from cat.models import Cat
# Create your views here.

def news_detail(request, word):

    site = Main.objects.get(pk=1)
    news = News.objects.filter(name = word)

    return render(request, 'front/news_detail.html', {'news': news, 'site':site})

def news_list(request):

    news = News.objects.all()
    return render(request, 'back/news_list.html', {'news': news})


def news_add(request):

    now = datetime.datetime.now()

    year = now.year
    month = now.month
    day = now.day

    if len(str(day)) == 1:
        day = '0' + str(day)
    if len(str(month)) == 1:
        month = '0' + str(month)

    today = (str(year)+"/"+str(month)+"/"+str(day))
    time = str(now.hour) + ":" + str(now.minute)

    cat = SubCat.objects.all()
    #now = datetime.datetime.now() + datetime.timedelta(days = 10)

    if request.method == 'POST':
        newstitle = request.POST.get('newstitle')
        newscat = request.POST.get('newscat')
        newstxtshort = request.POST.get('newstxtshort')
        newstxt = request.POST.get('newstxt')
        newsid = request.POST.get('newscat')

        if newstitle == "" or newstxt == "" or newstxtshort == "" or newscat == "":
            error = "All Fiels Required"
            return render(request, 'back/error.html' ,{'error':error})
        try:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)


            if str(myfile.content_type).startswith("image"):

                if myfile.size < 5000000:

                    newsname = SubCat.objects.get(pk = newsid).name

                    b = News(name = newstitle , short_txt = newstxtshort , body_txt = newstxt, date = today ,time = time, picurl = url, picname = filename, writer = '-', catname = newsname, catid = newsid, show = 0)
                    b.save()
                    return redirect('news_list')
                else:
                    fs = FileSystemStorage()
                    fs.delete(filename)

                    error = "Your file is bigger than 5 MB"
                    return render(request, 'back/error.html' ,{'error':error})

            else:
                fs = FileSystemStorage()
                fs.delete(filename)

                error = "Your file is not supported please inser an image"
                return render(request, 'back/error.html' ,{'error':error})

        except:
            # delete the file
            fs = FileSystemStorage()
            fs.delete(filename)
            error = "Please insert an image"
            return render(request, 'back/error.html' ,{'error':error})

    return render(request, 'back/news_add.html',{'cat':cat})


def news_delete(request, pk):

    try:
        b = News.objects.get(pk=pk)
        fs = FileSystemStorage()
        fs.delete(b.picname)
        b.delete()
    except:
        error = "something went wrong"
        return render(request, 'back/error.html' ,{'error':error})

    return redirect('news_list')

def news_edit(request, pk):

    if len(News.objects.filter(pk=pk)) == 0:
        error = "News not found"
        return render(request, 'back/error.html' ,{'error':error})

    news = News.objects.get(pk=pk)
    cat = SubCat.objects.all()

    if request.method == 'POST':
        newstitle = request.POST.get('newstitle')
        newscat = request.POST.get('newscat')
        newstxtshort = request.POST.get('newstxtshort')
        newstxt = request.POST.get('newstxt')
        newsid = request.POST.get('newscat')

        if newstitle == "" or newstxt == "" or newstxtshort == "" or newscat == "":
            error = "All Fiels Required"
            return render(request, 'back/error.html' ,{'error':error})
        try:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)


            if str(myfile.content_type).startswith("image"):

                if myfile.size < 5000000:

                    newsname = SubCat.objects.get(pk = newsid).name

                    b = News.objects.get(pk=pk)

                    fss = FileSystemStorage()
                    fss.delete(b.picname)

                    b.name = newstitle
                    b.short_txt = newstxtshort
                    b.body_txt = newstxt
                    b.picname = filename
                    b.picurl = url
                    b.catname = newsname
                    b.catid = newsid
                    b.save()
                    return redirect('news_list')
                else:
                    fs = FileSystemStorage()
                    fs.delete(filename)

                    error = "Your file is bigger than 5 MB"
                    return render(request, 'back/error.html' ,{'error':error})

            else:
                fs = FileSystemStorage()
                fs.delete(filename)

                error = "Your file is not supported please inser an image"
                return render(request, 'back/error.html' ,{'error':error})

        except:
            print("okkkkkkkkk")
            newsname = SubCat.objects.get(pk = newsid).name

            b = News.objects.get(pk=pk)
            b.name = newstitle
            b.short_txt = newstxtshort
            b.body_txt = newstxt
            b.catname = newsname
            b.catid = newsid
            b.save()
            return redirect('news_list')

    return render(request, 'back/news_edit.html', {'pk':pk, 'news':news, 'cat':cat})
