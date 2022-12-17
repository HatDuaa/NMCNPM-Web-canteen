from django import forms
from .models import Dish

class buy_dish_form(forms.Form):
    class Meta:
        def __init__(self, *args, **kwargs):
            self.user = kwargs.pop('user', None)
            self.dish = kwargs.pop('post', None)
            super().__init__(*args, **kwargs)

        def save(self, commit=True):
            comment = super().save(commit=False)
            comment.author = self.author
            comment.dish = self.post
            comment.save()


        # model = Comment
        # fields = ["body"]
