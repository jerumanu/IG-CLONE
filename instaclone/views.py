from django.shortcuts import render
from django.http import HttpResponse, Http404,HttpResponseRedirect

from .forms import NewsLetterForm
#......
def news_today(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()
            HttpResponseRedirect('news_today')
    else:
        form = NewsLetterForm()
    return render(request, 'index-news.html', {"date": date,"news":news,"letterForm":form})