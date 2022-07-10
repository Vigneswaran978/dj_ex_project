from django import forms
from .models import Review
from django.forms import ModelForm


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = "__all__"     # or supply the fields requires in a list ['first_name', 'last_name', 'starts']

        labels = {
            'first_name': 'YOUR FIRST NAME',
            'last_name': 'YOUR LAST NAME',
            'starts': 'RATING'

        }
        error_messages = {
            'starts':{
                'min_value': 'Yo! Min value is 1',
                'max_value': 'Yo! Max value is 5'
            }
        }


# class ReviewForm(forms.Form):
#     first_name = forms.CharField(label='First Name', max_length=100)
#     last_name = forms.CharField(label='Last Name', max_length=100)
#     email = forms.EmailField(label='Email')
#     review = forms.CharField(label='Please write your review here', max_length= 1000,
#                              widget=forms.Textarea(attrs={'class': 'myform',
#                                                           'rows': '2',
#                                                           'cols': '40'}))
