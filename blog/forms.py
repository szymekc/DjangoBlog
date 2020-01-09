from django import forms
from .models import Post, Comment
from re import match


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'title', 'text', 'date']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'post', 'text', 'date']
# class PostForm(forms.Form):
#     title = forms.CharField(required=1, max_length=200)
#     text = forms.CharField(required=1, widget=forms.Textarea)
#     date = forms.DateTimeField(required=0, input_formats=('%d/%m/%y'))


#     def clean_title(self):
#         title = self.cleaned_data.get('title')
#         if not match(r'[A-Za-z_][A-Za-z0-9_ ]*$', title):
#             print('Invalid title!')
#             raise forms.ValidationError('Invalid title')
#         return title
