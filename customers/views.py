from django.shortcuts import render

from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from customers.forms import UserForm

def index(request):
    return HttpResponse("Hello, world. You're at the customers index.")


def login_register(request):
    context = RequestContext(request)

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render_to_response(
        'customers/login_register.html',
        {'user_form' : user_form, 'registered' : registered },
        context
    )

