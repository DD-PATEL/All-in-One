from django.shortcuts import render, HttpResponse, redirect
from .models import Member, Product
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from .forms import ProductForm
from django.contrib.auth.decorators import login_required 
from django.forms import inlineformset_factory
from django.core.mail import send_mail


# Create your views here.
def index(request):
    return render(request, "index.html")


def signupPage(request):
        if request.method == "POST":
            username = request.POST["username"]
            email = request.POST["email"]
            password1 = request.POST["password1"]
        
            myuser = User.objects.create_user(username, email, password1)
            myuser.save()
            
            messages.success(request, "Successfully created an account for " + username)

            return redirect('login')

        return render(request, 'signup.html')


def loginPage(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Welcome " + username)
                return redirect('home')
            else:
                messages.warning(request, 'Username or Password is incorrect.')
        
        return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')



def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


def createProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        print('Printing POST:', request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')

    context = {'form': form}
    return render(request, 'create_product.html', context)


def membershipForm(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        phone = request.POST['phone']
        byear = request.POST['byear']

        print("FIRST STEP")

        membership = Member(name=name, email=email, password=password, phone=phone, byear=byear, date=datetime.today())
        membership.save()  
        print("SECOND STEP")
        messages.success(request, "Congratulation!!! You are now PRIME member")

    return render(request, 'membership.html')


def contactUs(request):
    print("Query Initiated")
    if request.method == "POST":
        a = request.POST.get('name')
        b = request.POST.get('email')
        c = request.POST.get('phone')
        d = request.POST.get('desc')
        
        body = {
            'name':a,
            'email':b,
            'mobile':c,
            'message':d,
        }
        message = "\n".join(body.values())
        subject="Contact Us Queries"
        send_mail(subject, message, 'tronphoenix3@gmail.com', ['anonymousbahubali@gmail.com'], fail_silently=False)
        print("Mail Sent Successfully")
        messages.success(request,"Mail Sent SuccessFully")
        return redirect('/')

    else:
        return render(request,'contact.html')     
