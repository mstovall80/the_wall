from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt



def register(request):
    errors = User.objects.basic_validator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    print(pw_hash)
    this_user = User.objects.create(
        first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=pw_hash)
    request.session['user_id'] = this_user.id

    return redirect('/')


def login(request):
    user = User.objects.filter(email=request.POST['email'])
    if User:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            return redirect('/main')
    messages.error(request, "Invalid login")
    return redirect('/')


def index(request):
    return render(request, "index.html")


def user_post_page(request):
    user_id = request.session['user_id']
    context = {
    "this_user": User.objects.get(id=user_id),
    "messages": Message.objects.all()
    }
    return render(request, "user_post_page.html", context)

def posted_message(request):
    user_id = request.session['user_id']
    user = User.objects.get(id = user_id)
    msg = Message.objects.create(message = request.POST["messages"])
    msg.post_message.add(user)
    return redirect( "/user_post_page")

def the_wall(request):
    return render(request, "the_wall.html")