from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from mangas.forms import MangaForm, MangaUpdateForm
from mangas.models import Manga


@login_required(login_url='login')
def manga_register(request):
    if request.method == 'GET':
        form = MangaForm()
        return render(request, 'manga_register.html', {'form': form})
    
    elif request.method == 'POST':
        form = MangaForm(request.POST, request.FILES)
        if form.is_valid():
            manga = form.save(commit=False)
            manga.owner = request.user
            manga.save()

            messages.success(request, 'Manga added successfully!')
            return redirect('my_mangas')


@login_required(login_url='login')
def my_mangas(request):
    mangas = True if Manga.objects.filter(owner=request.user) else False 
    
    active_mangas = None
    finished_mangas = None
    wish_mangas = None
    dropped_mangas = None

    if mangas:
        active_mangas = Manga.objects.filter(owner=request.user, status=0)
        finished_mangas = Manga.objects.filter(owner=request.user, status=1)
        wish_mangas = Manga.objects.filter(owner=request.user, status=2)
        dropped_mangas = Manga.objects.filter(owner=request.user, status=3)

    context = {
        'mangas': mangas,
        'active_mangas': active_mangas or None,
        'finished_mangas': finished_mangas or None,
        'wish_mangas': wish_mangas or None,
        'dropped_mangas': dropped_mangas or None,
    }

    return render(request, 'my_mangas.html', context)


@login_required(login_url='login')
def manga_update(request, id):
    try:
        manga = Manga.objects.get(pk=id)
        if request.method == 'GET':
            data = {
                'title': manga.title,
                'chapter': manga.chapter,
                'url': manga.url,
                'status': manga.status, 
                'notes': manga.notes
            }
            
            form = MangaUpdateForm(data=data, instance=manga)
            img = manga.image

            return render(request, 'manga_update.html', {'form': form, 'img': img, 'id': id, 'url': manga.url})
        
        elif request.method == 'POST':
            form = MangaUpdateForm(request.POST, instance=manga)
            form.save()
            return redirect('manga_update', id)
        
    except:
        messages.error(request, 'Something went wrong when updating manga!')
        return redirect('my_mangas')


@login_required(login_url='login')
def manga_delete(request, id):
    try:
        manga = Manga.objects.get(pk=id)
        manga.image.delete(save=False)
        manga.delete()
        messages.success(request, 'Manga deleted successfully!')
        
    except:
        messages.error(request, 'No manga found!')

    finally:
        return redirect('my_mangas')
    



