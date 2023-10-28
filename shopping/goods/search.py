from django import forms


class SearchForm(forms.Form):
    keyword = forms.CharField(label="search", max_length=100)