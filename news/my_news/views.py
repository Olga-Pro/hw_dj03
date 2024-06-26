from django.shortcuts import render, redirect
from .models import News_post
from .forms import New_postForm

# Create your views here.
def home(request):
    news = News_post.objects.all()
    return render(request, 'my_news/news.html', {'news': news})

def create_news(request):
    error =''
    if request.method == 'POST':
        form = New_postForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = "Данные заполнены некорректно"
    form = New_postForm()
    return render(request, 'my_news/add_new_post.html', {'form':form, 'error':error})