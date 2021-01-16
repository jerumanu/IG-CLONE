from django.shortcuts import render
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# from .forms import NewsLetterForm
# #......
@login_required(login_url='/accounts/login/')
