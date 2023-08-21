from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import movie
from movieapp.models import movie
from.forms import movieform



def index(request):
    movies = movie.objects.all()
    context = {
        'movie_list': movies
    }
    return render(request, 'index.html', context)
def detail(request,movie_id):
    movies1=movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'movie':movies1})
def add_movie(request):
    if request.method=="POST":
     name=request.POST.get('name')
     desc=request.POST.get('desc')
     year=request.POST.get('year')
     img=request.FILES.get('img')
     movies=movie(name=name,desc=desc,year=year,img=img)
     movies.save()
     return redirect('movieapp:index')
    else:
     return render(request,'add.html')
        
def update(request,id) :
       movies=movie.objects.get(id=id)
       form=movieform(request.POST or None, request.FILES,instance=movies)
       if form.is_valid():
           form.save()
           return redirect('/')
       return render(request,'edit.html',{'form':form,'movie':movies})
def delete(request,id) :
     if request.method=='POST':
         movies=movie.objects.get(id=id)
         movies.delete()   
         return redirect('/')
     return render(request,'delete.html') 

# def delete(request, id):
#     movies = get_object_or_404(movie, id=id)
#     if request.method == 'POST':
#         movie_instance.delete()
#         return redirect('/')
#     return render(request, 'delete.html')
 
    # return HttpResponse('this is movie no %s' % movie_id)
    #  movie = None  # initialize to None
    #  if request.method == 'POST':
    #     # assign a new value to movie
    #     movie = request.POST.get('movie')
    #  return render(request, 'index.html', {'movie': movie})