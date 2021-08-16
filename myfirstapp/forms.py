from django import forms

class FeedbackForm(forms.Form):
    title = forms.CharField(label='title', max_length = 50, widget=forms.TextInput )
    subject = forms.CharField(label='Subject description' , max_length = 200, widget = forms.Textarea)