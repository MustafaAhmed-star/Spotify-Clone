from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate 
import requests


def top_artists():
    url = "https://spotify-scraper.p.rapidapi.com/v1/chart/artists/top"

    headers = {
        "X-RapidAPI-Key": "02912db996msh068b089c778126bp13a9d9jsn380afeb7d573",
        "X-RapidAPI-Host": "spotify-scraper.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    response_data = response.json()

    artists_info = [{'name':'mustafa'},]

    if 'artists' in response_data:

        for artist in response_data['artists']:
            name = artist.get('name', 'No Name')
            avatar_url = artist.get('visuals', {}).get('avatar', [{}])[0].get('url', 'No URL')
            artist_id = artist.get('id', 'No ID')
            artists_info.append((name, avatar_url, artist_id))

    return artists_info

@login_required
def index(request):
    artists_info = top_artists()
    print(artists_info)
    context = {
        'artists_info':artists_info,
    
    }
    return render(request,'index.html',context)
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Credintails Invalid')
            
    return render(request, 'login.html')
        
def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password ==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                
                userLogin = authenticate(username=username,password=password)
                auth.login(request,userLogin)
        
                return redirect('/')
        else:
            messages.info(request,'password not matching')
            return redirect('signup')
    else:
        return render(request,'signup.html')
@login_required
def logout(request):
    auth.logout(request)
    return redirect('login')