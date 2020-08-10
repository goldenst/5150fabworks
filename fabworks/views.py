from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model


from .forms import ContactForm, LoginForm, RegisterForm

# ---------------------- LANDING ---------------------------
def landing(request):
    return render(request, 'landing.html', {})

# ----------------------- ABOUT ---------------------------
def about(request):
    return render(request, "about.html", {})

# ---------------------- CONTACT ----------------------------
def contact(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "form" : contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    # if request.method == "POST":
    #     # print(request.POST)
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('comment'))
    return render(request, "contact/view.html", context)

# ---------------------------- LOGIN ------------------------------------
def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form" : form
    } 
    
    print('user is loged in')
    print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            # context['form'] = LoginForm()
            return redirect("/")
        else:
            # Return an 'invalid login' error message.
            print('ERROR')

    return render(request, "auth/login.html", context)

# --------------------------------- REGISTER ---------------------------------
User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form" : form
    } 

    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)

    return render(request, "auth/register.html", context)
