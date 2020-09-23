from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta: #이 form 을 만들기위해 어떤 model이 쓰이는지 알려주기 위함
        model = Post
        fields = ('name','age', 'image', 'slice_location', 'text') # "__all__" if you want every attribute of the model to appear