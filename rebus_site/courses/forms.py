from django import forms
from uni_form.helpers import FormHelper, Submit, Reset
from uni_form.helpers import Layout, Fieldset, Row, HTML
from courses.models import School, Course
from profilemgr.models import UserProfile


class LayoutCourseForm(forms.Form):
    name = forms.CharField(label="Name", required=True, widget=forms.TextInput(), max_length=100)
    url = forms.URLField(label="Url", required=False)
    description = forms.CharField(label="Description", required=False, widget=forms.Textarea())
    language = forms.CharField(label="Language", required=True, widget=forms.TextInput(), max_length=30)
    LEVEL_CHOICES = (
        (u'', u'Select'),
        (u'bg', u'Beginner'),
        (u'im', u'Intermediate'),
        (u'ad', u'Advanced'),
        (u'ph', u'Phd')
        )
    level = forms.ChoiceField(label="Level", required=True, choices=LEVEL_CHOICES)
    TYPE_CHOICES = (
        (u'', u'Select'),
        (u'ca', u'Campus'),
        (u'on', u'Online'),
        (u'bl', u'Blended')
        )
    type = forms.ChoiceField(label="Type", required=True, choices=TYPE_CHOICES)
    
    school = forms.ModelChoiceField(label="School", required=False, empty_label="Select", queryset=School.objects.all())   
    lecturer = forms.ModelChoiceField(label="Lecturer", required=True, empty_label="Select", queryset=UserProfile.objects.all())

    # Field for a possible new school
    school_name = forms.CharField(label="School name*", required=False, widget=forms.TextInput(), max_length=100)
    school_url = forms.URLField(label="School url*", required=False)
    school_email = forms.EmailField(label="School email", required=False)
    school_phone = forms.CharField(label="School phone", required=False, widget=forms.TextInput(), max_length=20)
    school_address = forms.CharField(label="School Address", required=False, widget=forms.Textarea())
    school_city = forms.CharField(label="School city*", required=False, widget=forms.TextInput(), max_length=15)
    school_country = forms.CharField(label="School country*", required=False, widget=forms.TextInput(), max_length=15)


    def clean(self):
        cleaned_data = self.cleaned_data
        
        if cleaned_data['school']:
            pass
        else:
            s_name = cleaned_data.get('school_name')
            s_url = cleaned_data.get('school_url')
            s_city = cleaned_data.get('school_city')
            s_country = cleaned_data.get('school_country')
            if s_name and s_url and s_city and s_country:
                # Everything is fine
                pass
            else:
                # Something is missing
                msg = u"This field is required."
                if not s_name:
                    self._errors['school_name'] = self.error_class([msg])
                    del cleaned_data['school_name']
                if not s_url:
                    self._errors['school_url'] = self.error_class([msg])
                    del cleaned_data['school_url']
                if not s_city:
                    self._errors['school_city'] = self.error_class([msg])
                    del cleaned_data['school_city']
                if not s_country:
                    self._errors['school_country'] = self.error_class([msg])
                    del cleaned_data['school_country']
                    
        return cleaned_data
    


    def save(self):
        if self.cleaned_data['school']:
            school = self.cleaned_data['school']
        else:
            # Obtain and save the new school
            s_name = self.cleaned_data['school_name']
            s_url = self.cleaned_data['school_url']
            s_email = self.cleaned_data['school_email']
            s_phone = self.cleaned_data['school_phone']
            s_address = self.cleaned_data['school_address']
            s_city = self.cleaned_data['school_city']
            s_country = self.cleaned_data['school_country']
            
            new_s = School(name=s_name, url=s_url, email=s_email,
                           phone=s_phone, address=s_address, 
                           city=s_city, country=s_country)
            new_s.save()
            school = new_s

        # Get all the information
        name = self.cleaned_data['name']
        url = self.cleaned_data['url']
        description = self.cleaned_data['description']
        language = self.cleaned_data['language']
        level = self.cleaned_data['level']
        type = self.cleaned_data['type']
        lecturer = self.cleaned_data['lecturer']
        
        # Save the new course
        new_c = Course(name=name, url=url, description=description, language=language,
                       level=level, type=type, school=school, lecturer=lecturer)
        new_c.save()


    @property
    def helper(self):
        helper = FormHelper()

        layout = Layout(

            Fieldset('Choose a School or create a new one',
                     HTML('<div id="choose">'),
                     Row('school', HTML('<a id="new" href="#">Add a new School</a>')),
                     HTML('</div>'),
                     
                     HTML('<div id="create">'),
                     'school_name',
                     'school_url',
                     'school_email',
                     'school_phone',
                     'school_address',
                     'school_city',
                     'school_country',
                     HTML('<a id="old" href="#">Choose an already existent school</a>'),
                     HTML('</div>'),
                     ),

            Fieldset('',
                     HTML('<p>&nbsp;</p>'),
                     ),
            
            Fieldset('Fill in the course information',
                     'name', 
                     'lecturer',
                     'language',
                     'level',
                     'type',
                     'url',
                     'description', 
                     )
            )
        
        helper.add_layout(layout)

        submit = Submit('submit','Save')
        helper.add_input(submit)
        helper.form_method = 'POST'

        return helper
