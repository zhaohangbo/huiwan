# coding: utf-8

from django.core.urlresolvers import reverse
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import password_reset, password_reset_confirm

#from huiwan.authentication.forms import SignUpForm
#from huiwan.reviews.models import Review
#from .forms import NotesSearchForm

from django.views import generic
from .forms import SignUpForm 
# from .models import Choice, Question

class SignUpView(generic.FormView):
    form_class = SignUpForm()
    template_name = 'auth/signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name , { 'form': form })

    def post(self, request, *args, **kwargs):
        #form = SignUpForm(request.POST)
        form = self.form_class(request.POST)
        if not form.is_valid():
            messages.add_message(request, messages.ERROR, 'There are some problems while creating your account. Please review some fields.')
            return render(request, self.template_name, { 'form': form })
        else:
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            User.objects.create_user(username=username, password=password, email=email)
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.add_message(request, messages.SUCCESS, 'Your account were successfully created.')
            return HttpResponseRedirect('/' + username + '/')

class SignInView(generic.FormView):
    #form_class = SignInForm()
    template_name = 'auth/signin.html'

    def is_user_authenticated(request):
        return request.user.is_authenticated()
    
    def get(self, request, *args, **kwargs):
        if is_user_authenticated(request):
            return HttpResponseRedirect('/')
        else:
            return render(request, self.template_name) 

    def post(self, request, *args, **kwargs):
        if is_user_authenticated(request):
            return HttpResponseRedirect('/')
        else: 
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if 'next' in request.GET:
                        return HttpResponseRedirect(request.GET['next'])
                    else:
                        return HttpResponseRedirect('/')
                else:
                    messages.add_message(request, messages.ERROR, 'Your account is desactivated.')
                    return render(request,self.template_name) 
            else:
                messages.add_message(request, messages.ERROR, 'Username or password invalid.')
                return render(request, self.template_name)

class SignOutView(generic.RedirectView):
    permanent=False # HTTP status code returned. If True 301, if Flase 302
    url = '/'

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class ResetView(generic.View):
    template_name         ='auth/reset.html'
    email_template_name   ='auth/reset_email.html'
    subject_template_name ='auth/reset_subject.html'
    def get(self, request, *args, **kwargs):
        return password_reset(request, template_name=self.template_name,
                email_template_name=self.email_template_name,
                subject_template_name=self.subject_template_name,
                post_reset_redirect=reverse('success'))

class ResetConfirmView(generic.View):
    template_name='auth/reset_confirm.html'
    def get(request, uidb64=None, token=None):
        return password_reset_confirm(request, template_name=self.template_name,uidb64=uidb64, token=token,post_reset_redirect=reverse('signin'))

class SuccessView(generic.View):
    template_name = 'auth/success.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

"""
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if not form.is_valid():
            messages.add_message(request, messages.ERROR,
                    'There was some problems while creating your account. Please review some fields before submiting again.')
            return render(request, 'auth/signup.html', { 'form': form })
        else:
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            User.objects.create_user(username=username, password=password, email=email)
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.add_message(request, messages.SUCCESS, 'Your account were successfully created.')
            return HttpResponseRedirect('/' + username + '/')
    else:
        return render(request, 'auth/signup.html', { 'form': SignUpForm() })

def signin(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if 'next' in request.GET:
                        return HttpResponseRedirect(request.GET['next'])
                    else:
                        return HttpResponseRedirect('/')
                else:
                    messages.add_message(request, messages.ERROR, 'Your account is desactivated.')
                    return render(request, 'auth/signin.html')
            else:
                messages.add_message(request, messages.ERROR, 'Username or password invalid.')
                return render(request, 'auth/signin.html')
        else:
            return render(request, 'auth/signin.html')

def signout(request):
    logout(request)
    return HttpResponseRedirect('/')

def reset(request):
    return password_reset(request, template_name='auth/reset.html',
        email_template_name='auth/reset_email.html',
        subject_template_name='auth/reset_subject.txt',
        post_reset_redirect=reverse('success'))

def reset_confirm(request, uidb64=None, token=None):
    return password_reset_confirm(request, template_name='auth/reset_confirm.html',uidb64=uidb64, token=token, post_reset_redirect=reverse('signin'))

def success(request):
  return render(request, 'auth/success.html')

"""
