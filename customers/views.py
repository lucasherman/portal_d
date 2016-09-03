from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from customers.forms import CustomerRegistrationForm, CustomerLoginForm

def index(request):
    template = loader.get_template('customers/index.html')
    context = {}

    return HttpResponse(template.render(context, request))


def login_register(request):
    context = RequestContext(request)

    registered = False

    if request.method == 'POST':
        customer_registration_form = CustomerRegistrationForm(data=request.POST)

        if customer_registration_form.is_valid():
            customer = customer_registration_form.save()
            customer.set_password(customer.password)
            customer.save()
        else:
            print(customer_registration_form.errors)
    else:
        customer_registration_form = CustomerRegistrationForm()
        customer_login_form = CustomerLoginForm()

    return render_to_response(
        'customers/login_register.html',
        {
            'customer_registration_form' : customer_registration_form,
            'customer_login_form' : customer_login_form,
            'registered' : registered
        },
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

def process_registration(request):
    pass

def process_login(request):
    pass

def password_reset(request):
    return render_to_response(
        'customers/password_reset.html'
    )







