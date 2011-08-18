from registration.forms import RegistrationForm
from django import forms
from uni_form.helpers import FormHelper, Submit, Reset
from uni_form.helpers import Layout, Fieldset, Row, HTML


class UserProfileForm(RegistrationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    url = forms.URLField(required=False)
    phone = forms.CharField(max_length=20, required=False)
    work_address = forms.CharField(widget=forms.Textarea, required=False)
    city = forms.CharField(max_length=15)
    country = forms.CharField(max_length=15)
    image = forms.ImageField(required=False)


# More simple form only for update
class UpdateProfileForm(forms.Form):
    email = forms.EmailField(max_length=75)

    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    url = forms.URLField(required=False)
    phone = forms.CharField(max_length=20, required=False)
    work_address = forms.CharField(widget=forms.Textarea, required=False)
    city = forms.CharField(max_length=15)
    country = forms.CharField(max_length=15)
    image = forms.ImageField(required=False)

    
    @property
    def helper(self):
        helper = FormHelper()
    
        style = """
        <style>
            .uniForm label, .uniForm .label {
                display: inline;
            }
        </style>

        """

        layout = Layout(
            Fieldset('',
                     'email', 
                     'first_name',
                     'last_name',
                     'url',
                     'phone',
                     'work_address',
                     'city',
                     'country',
                     HTML(style),
                     'image',
                     )
            )
        
        helper.add_layout(layout)

        submit = Submit('submit','Update')
        helper.add_input(submit)
        helper.form_method = 'POST'

        return helper
