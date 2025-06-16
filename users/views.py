from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
# 3 possibilities - valid (new) user, invalid (existing) user, get form
def register_view(request):
    if request.method == "POST": # if form is submitted
        form = UserCreationForm(request.POST)
        if form.is_valid(): # form is valid means user is new (not yet register)
            login(request, form.save())
            return redirect("posts:list") # redirect this page
    else: # not submitted form - means GET request when we first visit form 
        form = UserCreationForm()
    return render(request, "users/register.html", { "form" : form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid(): # if valid ~ existing user then login 
            login(request, form.get_user())
            # If other tab or 'new-post' redirect to login tab -> login_url + ?next=original_page
            # After successful login, user is redirected back to that original page
            if 'next' in request.POST:  
                return redirect(request.POST.get('next'))
            else:
                return redirect("posts:list")
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", { "form" : form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")
