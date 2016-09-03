from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from customers.forms import UserForm

def index(request):
    template = loader.get_template('customers/index.html')
    context = {}

    return HttpResponse(template.render(context, request))


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

def contact_us(request):
    return render_to_response(
        'customers/contact_us.html'
    )

def faq(request):
    return render_to_response(
        'customers/faq.html'
    )


def about(request):
    return render_to_response(
        'customers/about.html'
    )






