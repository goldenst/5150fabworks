from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model


from .forms import ContactForm

# ---------------------- LANDING ---------------------------
def landing(request):
    # print(request.session.get('first_name', 'Unkown'))
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


