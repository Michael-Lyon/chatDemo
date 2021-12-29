from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from chat.models import Messages, Room

# Create your views here.

def home(request):
    return render(request, 'chat/home.html')

def room(request, **kwargs):
    room = str(kwargs['room'])
    print(room)
    username = kwargs['username']
    room_detail = Room.objects.get(name=room)
    return render(request, 'chat/room.html', {'room':room, 'username':username, 'room_details':room_detail})

def checkview(request):
    # if request.method == 'POST':
    room = request.POST['room_name']
    username = request.POST['username']
    print(room)
    print(Room.objects.filter(name=room).exists())
    if Room.objects.filter(name=room).exists():
        return redirect(reverse('chat:room', kwargs= {'room':room, 'username':username}))
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        print("craeted")   
        return redirect(reverse('chat:room', kwargs={'room': room, 'username': username}))
    

def send(request):
    message = request.POST['message']
    print(message)
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Messages.objects.create(
        value=message,
        user=username,
        room=room_id
    )

    new_message.save
    print("Good here")
    return HttpResponse("Message sent successfully")


def getMessages(request,  **kwargs):
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
    room = str(kwargs['room'])
    room_details = Room.objects.get(name=room)
    messages = Messages.objects.filter(room=room_details.id)
    return JsonResponse({'messages': list(messages.values())})
