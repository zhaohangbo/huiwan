from django import forms
from haystack.forms import SearchForm

from .models import User

class UsersSearchForm(SearchForm):
    def no_query_found(self):
        return self.searchqueryset.all()

class RegistrationForm(forms.ModelForm):
        class Meta:
            model = User
            fields = ['email', ]
