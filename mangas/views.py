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
    
    if mangas:
        finished_mangas = Manga.objects.filter(owner=request.user, is_finished=True)
        active_mangas = Manga.objects.filter(owner=request.user, is_finished=False)

    context = {
        'mangas': mangas,
        'finished_mangas': finished_mangas or None,
        'active_mangas': active_mangas or None,
    }

    return render(request, 'my_mangas.html', context)


@login_required(login_url='login')
def manga_update(request, id):
    try:
        manga = Manga.objects.get(pk=id)
        url = f'{manga.url}{manga.chapter}#/!page0'
        if request.method == 'GET':
            data = {
                'title': manga.title,
                'chapter': manga.chapter,
                'url': manga.url,
                'is_finished': manga.is_finished
            }
            
            form = MangaUpdateForm(data=data, instance=manga)
            img = manga.image

            return render(request, 'update_manga.html', {'form': form, 'img': img, 'id': id, 'url': url})
        
        elif request.method == 'POST':
            form = MangaUpdateForm(request.POST, instance=manga)
            form.save()
            return redirect('my_mangas')
        
    except:
        messages.error(request, 'Something went wrong when updating manga!')
        return redirect('my_mangas')


@login_required(login_url='login')
def manga_delete(request, id):
    try:
        manga = Manga.objects.get(pk=id)
        manga.image.delete(save=False)
        manga.delete()
        messages.success(request, 'Manga added successfully!')
        
    except:
        messages.error(request, 'No manga found!')

    finally:
        return redirect('my_mangas')