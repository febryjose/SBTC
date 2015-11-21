from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from forms import ContactForm
from django.views.generic.list import ListView
from sbtcapp.models import *

class Home(TemplateView):

    template_name = "home.html"

class WeAre(TemplateView):
    template_name = "weare.html" 

class OurTeam(TemplateView):
    template_name = "ourteam.html"  

class MeetOur(TemplateView):
	template_name = "meetour.html"

class Clients(TemplateView):
	template_name = "clients.html"

class ProjectDone(ListView):
	
    model = Gallery
    template_name = "projectone.html"

class ContactUs(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/contact/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        print 'hiii'



