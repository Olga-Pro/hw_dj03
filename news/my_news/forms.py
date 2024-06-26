from .models import News_post
from django.forms import ModelForm


class New_postForm(ModelForm):
    class Meta:
        model = News_post
        fields = ['title', 'short_description', 'text', 'pub_date']