from django.shortcuts import render, HttpResponse, redirect
from . import models

def index(request):
    context={
        "all_shows": models.Show.objects.all()
    }
    return render(request, 'restful_tv/index.html', context)

def new_show(request):
    return render(request, 'restful_tv/addnewshow.html')

def create(request):
    show_info = models.Show.objects.create(title=request.POST['title'], network=request.POST['network'], released_date=request.POST['release_date'], description=request.POST['description'])
    print(show_info, "show info")
    return redirect("/shows/"+str(show_info.id)) #redirecting to url with show.id in it, can't pass context over

def show(request, show_id):
    #need to pass info from show_id(passed thru url)  to this page
    show_info=models.Show.objects.get(id=show_id)
    context={
        "show_info": show_info
    }
    return render(request, 'restful_tv/showtv.html', context)

def edit(request, show_id):
    show_info=models.Show.objects.get(id=show_id)
    context={
        "show_info": show_info
    }
    return render(request, 'restful_tv/editshow.html', context)

def update(request, show_id):
    update_show=models.Show.objects.get(id=show_id)
    update_show.title=request.POST['u_title']
    update_show.save()
    update_show.network=request.POST['u_network']
    update_show.save()
    update_show.released_date=request.POST['u_release_date']
    update_show.save()
    update_show.description=request.POST['u_description']
    update_show.save()
    return redirect ('/shows/'+str(show_id))

def delete(request, show_id):
    delete_show = models.Show.objects.get(id=show_id)
    delete_show.delete()
    return redirect ("/")