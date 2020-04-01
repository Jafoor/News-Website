from django.shortcuts import render , get_object_or_404, redirect
from .models import Cat

# Create your views here.

def cat_list(request):

    cat = Cat.objects.all()
    return render(request , 'back/cat_list.html', {'cat' : cat})

def cat_add(request):

    if request.method == 'POST':
        name = request.POST.get('name')

        if name == "":
            error = "Please Write a name of category"
            return render(request, 'back/error.html' ,{'error':error})

        b = Cat(name = name)
        b.save()

        if len(Cat.objects.filter(name=name)) != 0:
            error = "This Category is added before"
            return render(request, 'back/error.html' ,{'error':error})

        return redirect('cat_list')

    return render(request , 'back/cat_add.html')
