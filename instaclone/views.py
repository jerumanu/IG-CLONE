from django.shortcuts import render

from .forms import NewsLetterForm
#......
def news_today(request):
#........
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
        form = NewsLetterForm()
    return render(request, 'index.html', {"date": date,"news":news,"letterForm":form})
