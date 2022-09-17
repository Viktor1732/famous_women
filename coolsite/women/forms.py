from django import forms

from .models import *


class AddPostForm(forms.ModelForm):  # Прописывае только те данные которые необходимы конечному пользователю.
    def __init__(self, *args, **kwargs): # Для того, чтобы сделать надписть в выборе категории
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Катеория не выбрана'

    class Meta:
        model = Women
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 100, 'rows': 10}),
        }
