from django import forms

#name, attributes, and fields of form
class CreateNewList(forms.Form):
    #same fields as data object
    name = forms.CharField(label="Name", max_length=200)
    #prevents form from being vaild if not checked, not even shown
    # check = forms.BooleanField()