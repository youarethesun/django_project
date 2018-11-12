from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from .forms import LoginForm,CommentForm, SimpleForm


def index(request):
    return render(request,'polls/index.html')


def show_forms(request):
    context = dict()
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('polls:login_succeed'))
    context['form'] = form
    print(form)
    print(1111111)
    print(context)
    return render(request, 'polls/show_forms.html', context)


def form_login_succeed(request):
    context = {'login': 'login succeed'}
    return render(request, 'polls/login_succeed.html', context)


def comment_form(request):
    context = dict()
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('polls:login_succeed'))
    context['form'] = form
    return render(request, 'polls/comment_form.html', context)


def simple_form(request):
    context = dict()
    form = SimpleForm()
    if request.method == 'POST':
        form = SimpleForm(request.POST)
        if form.is_valid():
            return HttpResponse('ok')
    context['form'] = form
    return render(request, 'polls/simple_form.html', context)




