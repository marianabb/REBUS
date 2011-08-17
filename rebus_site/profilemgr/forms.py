from registration.forms import RegistrationForm
from django import forms


class UserProfileForm(RegistrationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    url = forms.URLField(required=False)
    phone = forms.CharField(max_length=20, required=False)
    work_address = forms.CharField(widget=forms.Textarea, required=False)
    city = forms.CharField(max_length=15)
    country = forms.CharField(max_length=15)
    image = forms.FileField(required=False)


    def clean(self):
        cleaned_data = self.cleaned_data
        
        # Only make changes if the profile is being updated
        import ipdb; ipdb.set_trace()
        if request.path == '/accounts/update':
           pass 

        return cleaned_data
