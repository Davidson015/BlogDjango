from django import forms
from app.models import Comment

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    exclude = ['created_at', 'post']