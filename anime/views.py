from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from anime.forms import AnimeCreationForm, AnimeUpdateForm
from anime.models import Anime


# Anime register view
@login_required(login_url='login')
def anime_register(request):
    if request.method == 'GET':
        form = AnimeCreationForm()
        return render(request, 'anime_register.html', {'form': form})
    
    elif request.method == 'POST':
        form = AnimeCreationForm(request.POST, request.FILES)
        if form.is_valid():
            anime = form.save(commit=False)
            anime.owner = request.user
            anime.save()
            messages.success(request, 'Anime added successfully!')
            return redirect('my_animes')


# Anime update view
@login_required(login_url='login')
def anime_update(request, id):
    try:
        anime = Anime.objects.get(pk=id)

        # GET method, return the form with current info
        if request.method == 'GET':
            form = AnimeUpdateForm(instance=anime)

            context = {
                'form': form,
                'img': anime.image,
                'id': anime.id
            }

            return render(request, 'anime_update.html', context)
        
        # POST method, save changes
        elif request.method == 'POST':
            form = AnimeUpdateForm(request.POST, instance=anime)
            form.save()
            return redirect('anime_update', id)
        
    # If any errors occur during update process, redirect to my animes page
    except:
        messages.error(request, 'Something went wrong when updating your anime. Try again later!')
        return redirect('my_animes')
    

# Anime delete view
@login_required(login_url='login')
def anime_delete(request, id):
    try:
        anime = Anime.objects.get(pk=id)
        anime.image.delete(save=False)
        anime.delete()
        messages.success(request, 'Anime deleted successfully!')

    except:
        messages.error(request, 'No anime found!')

    finally:
        return redirect('my_animes')
    

@login_required(login_url='login')
def my_animes(request):
    has_anime = True if Anime.objects.filter(owner=request.user) else False

    active_animes = None
    finished_animes = None
    wish_animes = None
    stopped_animes = None

    if has_anime:
        active_animes = Anime.objects.filter(owner=request.user, status=0)
        finished_animes = Anime.objects.filter(owner=request.user, status=1)
        wish_animes = Anime.objects.filter(owner=request.user, status=2)
        stopped_animes = Anime.objects.filter(owner=request.user, status=3)

    context = {
        'has_anime': has_anime,
        'active_animes': active_animes,
        'finished_animes': finished_animes,
        'wish_animes': wish_animes,
        'stopped_animes': stopped_animes,
    }

    return render(request, 'my_animes.html', context)
