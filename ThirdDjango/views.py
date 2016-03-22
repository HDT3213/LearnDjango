# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.http import JsonResponse
import os

# Create your views here.

def welcome(request):
    return render(request, 'welcome.html')

def search(request):
    return render(request, 'form-post.html', None)


def search_post(request):
    context = dict()
    context.update(csrf(request))
    if request.POST:
        context['result'] = request.POST['search_content']
    return render(request, 'form-post.html', context)


def search_get(request):
    context = dict()
    if 'search_content' in request.GET:
        context['result'] = request.GET['search_content']
    return render(request, 'form-post.html', context)


def login(request):
    return render(request, 'login-session.html')


def login_validate(request):
    context = dict()
    if request.POST['password'] == 'exciting':
        request.session['current_user'] = 'NaiveUser'
        context['current_user'] = request.session['current_user']
    return render(request, 'login-success.html', context)


def keep_online(request):
    context = dict()
    context['username'] = request.session['current_user']
    return render(request, 'keep-online.html', context)


def test_cookies(request):
    context = dict()
    if 'num' in request.COOKIES:
        num = int(request.COOKIES['num']) + 1
    else:
        num = 1
    beat = ''
    for i in range(num+1):
        beat += '啊'
    context['num'] = str(num)
    context['beat'] = beat
    response = render_to_response('test-cookies.html', context)
    response.set_cookie('num', str(num))
    return response


def test_cookies2(request):
    request.session.set_test_cookie()
    print(request.session.test_cookie_worked())
    response = render_to_response('test-cookies.html', context)
    return response


def test_json(request):
    response = JsonResponse({'foo': 'bar'})
    return response


def handle_upload(request):
    print('handling upload')
    file = request.FILES['file']
    filename = str(request.FILES['file'])
    print(filename)
    if not os.path.exists('upload/'):
        os.mkdir('upload/')
    out = open('upload/' + filename, 'wb+')
    for chunk in file.chunks():
        out.write(chunk)
    print('write finished')
    # render response
    context = dict()
    context['filename'] = filename
    return render(request, 'file-upload-success.html', context)


def upload(request):
    return render(request, 'file-upload.html')

