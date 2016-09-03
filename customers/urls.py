from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^login-register/$', views.login_register, name="login_register"),
    url(r'^contact-us/$', views.contact_us, name="contact_us"),
    url(r'^faq/$', views.faq, name="faq"),
    url(r'^about/$', views.about, name="about"),
    url(r'^process-registration/$', views.process_registration, name="process_registration"),
    url(r'^process-login/$', views.process_login, name="process_login"),
    url(r'^password-reset/$', views.password_reset, name="password_reset"),
]