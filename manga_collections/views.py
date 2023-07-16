from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from manga_collections.forms import MangaCollectionCreationForm, MangaCollectionUpdateForm
from manga_collections.models import MangaCollection

import simplejson as json


# Collection register view
@login_required(login_url='login')
def collection_register(request):
    # GET method, return form with current info
    if request.method == 'GET':
        form = MangaCollectionCreationForm()
        return render(request, 'manga_collection_register.html', {'form': form})

    # POST method, save changes
    elif request.method == 'POST':
        form = MangaCollectionCreationForm(request.POST, request.FILES)
        if form.is_valid():
            collection = form.save(commit=False)
            collection.owner = request.user
            collection.save()
            messages.success(request, 'Manga collection added successfully!')
            return redirect('my_collections')


# My collections view
@login_required(login_url='login')
def my_collections(request):
    # Check if there is any collection for this user
    collections = True if MangaCollection.objects.filter(owner=request.user) else False

    # Define collections
    active_collections = None
    finished_collections = None
    wish_collections = None
    
    # If there are collections, get them
    if collections:
        active_collections = MangaCollection.objects.filter(owner=request.user, status=0)
        finished_collections = MangaCollection.objects.filter(owner=request.user, status=1)
        wish_collections = MangaCollection.objects.filter(owner=request.user, status=2)
    
    # Define view context
    context = {
        'collections': collections,
        'active_collections': active_collections,
        'finished_collections': finished_collections,
        'wish_collections': wish_collections,
    }

    return render(request, 'my_collections.html', context)


# Collection update view
@login_required(login_url='login')
def collection_update(request, id):
    try:
        manga_collection = MangaCollection.objects.get(pk=id)

        # GET method
        if request.method == 'GET':
            form = MangaCollectionUpdateForm(instance=manga_collection)

            context = {
                'form': form,
                'img': manga_collection.image or None,
                'bought': manga_collection.get_bought_str(),
                'id': manga_collection.id
            }

            return render(request, 'manga_collection_update.html', context)
        
        # POST method
        elif request.method == 'POST':
            want = str(request.POST['want'])

            if manga_collection.bought:
                json_dec = json.decoder.JSONDecoder()
                saved_volumes = json_dec.decode(manga_collection.bought)
                
            else:
                saved_volumes = list()

            # If there are any volume to add, add them
            if want:
                bought_list = get_list(want)
                
                

                # If user wants to remove the volumes, remove them
                if 'delete' in request.POST:
                    for item in bought_list:
                        if item in saved_volumes:
                            saved_volumes.remove(item)

                # If user wants to add the volumes, add them
                else:
                    not_buy = ''
                    for item in bought_list:
                        if item not in saved_volumes:
                            saved_volumes.append(item)
                        else:
                            not_buy += f'{item}, '
                    
                    not_buy = not_buy.removesuffix(', ')
                    if not_buy:
                        messages.warning(request, f'Do not buy the following volumes: {not_buy}')

            # Convert the bought list to json and save it
            bought = json.dumps(saved_volumes)
            
            data = {
                'title': request.POST['title'],
                'bought': bought,
                'status': request.POST['status']
            }

            form = MangaCollectionUpdateForm(data=data, instance=manga_collection)
            form.save()

            return redirect('collection_update', id)
            
    except:
        messages.error(request, 'Something went wrong when updating your collection. Try again later!')
        return redirect('my_collections')


# Collection delete view
@login_required(login_url='login')
def collection_delete(request, id):
    try:
        collection = MangaCollection.objects.get(pk=id)
        collection.image.delete(save=False)
        collection.delete()
        messages.success(request, 'Collection deleted successfully!')

    except:
        messages.error(request, 'No collection found!')

    finally:
        return redirect('my_collections')


# Get bought list, based on a string
def get_list(bought: str):
    '''
    This function gets a string and return a list.
    Examples:
        - Input: "1, 2, 3"          -> [1, 2, 3]
        - Input: "1-5"              -> [1, 2, 3, 4, 5]
        - Input: "1-5, 7, 10-14"    -> [1, 2, 3, 4, 5, 7, 10, 11, 12, 13, 14]
    '''
    
    bought = bought.replace(' ', '')
    bought_list = bought.split(',')

    final_list = list()
    for item in bought_list:
        if '-' in item:
            split = item.split('-')
            first = int(split[0])
            last = int(split[1])
            for number in range(first, last+1):
                final_list.append(number)
        
        else:
            final_list.append(int(item))

    return final_list
            