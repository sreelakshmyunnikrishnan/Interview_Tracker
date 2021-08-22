
# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
# from . models import FileUpload
from django.contrib import messages
from .models import Notifications
from intrack.models import UserProfile
from .form import EntryForm
from .form import NoteForm
from intrack.models import AddInt
from intrack.models import Notes
from datetime import datetime

from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate,login,logout


# # @login_required
# # def enter(request):
# #     if request.user.usertype == 'client':
# #         if request.method == 'POST':
# #             res = request.FILES['resume']
# #             img = request.FILES['image']
# #             # file = FileUpload()
# #             file.resume = res
# #             file.image = img
# #             file.save()
# #             return HttpResponse("<script>alert('File is uploaded!');window.location.href='http://127.0.0.1:8000/';</script>")
# #         else:
# #             return render(request,'upload.html')
# #     else:
# #         return HttpResponse('Try again with valid user credentials')

def register(request):
    if request.method=='POST':
        user = request.POST.get('username')
        email = request.POST.get('email')
        passw = request.POST.get('password')
        type = request.POST.get('type')
        UserProfile.objects.create_user(username=user,email= email, password=passw,usertype=type)
        return render(request,'login.html')
    else:
        return render(request,'register.html')


def logins(request):
    if request.method=='POST':
        usern = request.POST.get('username')
        passw = request.POST.get('password')

        user = authenticate(request,username=usern,password=passw)

        if user is not None and user.usertype == 'admin':
            login(request,user)
            # return render(request,'adminpage.html')
            return redirect(showadmin)



        elif user is not None and user.usertype == 'user':
            login(request,user)
            return redirect(entry)
            # return render(request,'userpage.html')
        else:
            return HttpResponse('Sorry Invalid details')
    else:
        return render(request, 'login.html')



def showadmin(request):
    log=UserProfile.objects.all()
    return render(request,'adminpage.html',{'log':log})


@login_required
def entry(request):
    ent=AddInt.objects.filter(user=request.user)
    form=EntryForm(request.POST or None) 
    if request.method=="POST" :
        if form.is_valid():
            try:
                form.save()               
                return redirect(showuser)
            except:
                print("Form not Valid")              
    else:
        return render(request,'userpage.html',{'form':form})
       
def showuser(request):
    ent=AddInt.objects.filter(user=request.user)
    return render(request,'histview.html',{'ent':ent})      

def note(request):
    form=NoteForm(request.POST or None)
    if request.method=="POST":
        if form.is_valid():
            try:
                    form.save()
                    return redirect(shownote)
            except:
                    print("Not Valid")
    else:
        return render(request,'note.html',{'form': form})

def shownote(request):
    note=Notes.objects.filter(user=request.user).order_by('note_date')
    return render(request,'noteview.html',{'note':note})

def delnote(request,id):
    note=Notes.objects.get(id=id)
    note.delete()
    return redirect(shownote)

def notedit(request,id):
    note=Notes.objects.get(id=id)
    return render(request,'notedit.html' ,{'note':note})

def noteupdate(request,id):
    note=Notes.objects.get(id=id)
    form=NoteForm(request.POST ,instance=note)
    if form.is_valid():
        form.save()
        return redirect(showuser) 
    return render(request,'notedit.html',{'note':note})


def alert(request):
    ent=AddInt.objects.filter(user=request.user).order_by('-scd_date')
    return render(request,'alert.html',{'ent':ent})
   
def delint(request,id):
    ent=AddInt.objects.get(id=id)
    ent.delete()
    return redirect(showuser)

# @login_required
def edit(request,id):  
    ent=AddInt.objects.get(id=id)
    return render(request,'useredit.html',{'ent,':ent})

     
def update(request,id):
    ent=AddInt.objects.get(id=id)
    form=EntryForm(request.POST or None,instance=ent)
    if form.is_valid():
        form.save()
        return redirect(showuser)        
    return render(request,'useredit.html',{'ent':ent})



def logouts(request):
    logout(request)
    return redirect(logins)