from django.shortcuts import render, redirect
from vamsiele.forms import usersdetailsform
from vamsiele.models import users

# Create your views here.
def base(request):
    return render(request, 'vamsiele/base.html')
def home(request):
    return render(request, 'vamsiele/home.html')
def about(request):
    return render(request, 'vamsiele/aboutus.html')
def products(request):
    return render(request, 'vamsiele/products.html')
def gallery(request):
    return render(request, 'vamsiele/Gallery.html')
def contact(request):
    data = usersdetailsform()
    if request.method == "POST":
        form = usersdetailsform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/users')
    return render(request, 'vamsiele/contactus.html', {'key': data })
def userss(request):
    user = users.objects.all()
    return render(request, 'vamsiele/users.html',{'keys': user})
