from django import forms

class FeedbackForm(forms.Form):
    title = forms.CharField(label='title', max_length = 50, )
    subject = forms.CharField(label='Subject description' , max_length = 200, )