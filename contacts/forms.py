from django import forms
from .models import Contact

# class ContactForm(forms.ModelForm):
#
#     name = forms.CharField(
#         widget=forms.TextInput(attrs={
#             'class':'input-bordered w-full',
#             'placeholder':'Contact Name'
#         })
#     )
#
#    email = forms.CharField(
#         widget=forms.TextInput(attrs={
#             'class':'input-bordered w-full',
#             'placeholder':'Contact Name'
#         })
#
#     )
#     class Meta:
#         model = Contact
#         fields = (
#             'name', 'email'
#         )