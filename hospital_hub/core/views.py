from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from core.forms import *

from .models import *



# Create your views here.

def home(request):
    hospitals=Hospital.objects.all()
    
    context={"hospitals":hospitals}
    return render(request,"core/index.html",context=context)

def loginpage(request):

    if request.method=="POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user=User.objects.get(username=username)

            if(user is not None):
                print(user)
            else:
                messages.error(request, 'User does not exist')
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Replace 'home' with the name of your desired home URL pattern
            else:
                form = AuthenticationForm()

    else:
        form=LoginForm()
    context={"form":form}
    return render(request,"core/login.html",context=context)

def signuppage(request):

    if request.method == 'POST':
        form = SignupForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Replace 'home' with the desired URL after successful signup
    else:
        form = SignupForm()

    context={"form":form}
    return render(request,"core/signup.html",context=context)


def dashbord(request):

    hospital=Hospital.objects.get(created_by=request.user)
    services=Service.objects.filter(hospital=hospital)
    comments=Comment.objects.filter(hospital=hospital)
    appointments=Appointment.objects.filter(hospital=hospital)

    if request.method=="POST":
        name=request.POST.get("name")
        detail=request.POST.get("detail")
        print(name,detail)
        newService=Service(name=name,detail=detail,hospital=hospital)
        newService.save()
        messages.success(request,'New Service Added')
        return redirect("dashbord")
    

    context={"hospital":hospital,"services":services,"comments":comments,"appointments":appointments}

    return render(request,"core/dashbord.html",context=context)


def detail(request,id):
    hospital=Hospital.objects.get(id=id)
    hospitalImage=HospitalImage.objects.filter(hospital=hospital)
    hospitalVideo=HospitalVideo.objects.get(hospital=hospital)
    service=Service.objects.filter(hospital=hospital)
    comments=Comment.objects.filter(hospital=hospital)

    if request.method=="POST":
        if request.POST.get("comment") is not None:
            email=request.user.email
            comment=request.POST.get("comment")
            newcomment=Comment(email=email,comment=comment,hospital=hospital)
            newcomment.save()
            return redirect("detail" ,id)

        else:
            first_name=request.POST.get("first_name")
            last_name=request.POST.get("last_name")
            age=request.POST.get("age")
            gender=request.POST.get("gender")
            service_name=request.POST.get("service")
            service_selacted=Service.objects.get(name=service_name)
            newAppointment=Appointment(hospital=hospital,first_name=first_name,last_name=last_name,age=age,gender=gender,created_by=request.user,service_id=service_selacted)
            newAppointment.save()
            return redirect("detail",id)



    context={"hospital":hospital,"images":hospitalImage,"video":hospitalVideo,"services":service,"comments":comments}

    return render(request,"core/detail.html",context=context)

def add_Hospital(request):
    if request.method=="POST":
        name=request.POST.get("name")
        description=request.POST.get("description")
        address=request.POST.get("address")
        images=request.FILES.getlist('image')
        video=request.FILES['video']
        logo=request.FILES['logo']
        created_by=request.user


        newHospital=Hospital(name=name,description=description,address=address,created_by=created_by,logo=logo)
        newHospital.save()
        user=User.objects.get(id=newHospital.created_by.id)
        user.created_hospital=True
        user.save()

        for image in images:
            print(images)
            newHospitalImage=HospitalImage(hospital=newHospital,imagefile=image)
            newHospitalImage.save()
            
        newHospitalVideo=HospitalVideo(hospital=newHospital,videofile=video)
        newHospitalVideo.save()

        return redirect("home")
        
    return render(request,"core/add-hospital1.html")

def logoutUser(request):
    logout(request)
    return redirect('home')


