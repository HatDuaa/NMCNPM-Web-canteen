from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author', None)
        self.dish = kwargs.pop('dish', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        comment = super().save(commit=False)
        comment.author = self.author
        comment.dish = self.dish
        comment.save()

    class Meta:
        model = Comment
        fields = ["body"]
