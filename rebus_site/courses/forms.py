from django import forms
from uni_form.helpers import FormHelper, Submit, Reset
from uni_form.helpers import Layout, Fieldset, Row, HTML
from courses.models import School, Course
from profilemgr.models import UserProfile


class LayoutCourseForm(forms.Form):
    name = forms.CharField(label="Name", required=True,
                           widget=forms.TextInput(), max_length=100)
    url = forms.URLField(label="Url", required=False)
    description = forms.CharField(label="Description", required=False, 
                                  widget=forms.Textarea())
    language = forms.CharField(label="Language", required=True, 
                               widget=forms.TextInput(), max_length=30)
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

    # Only include actual lecturers with name and last name. Exclude admin users.
    lecturer = forms.ModelChoiceField(label="Lecturer", required=True, 
                                      empty_label="Select", 
                                      queryset=UserProfile.objects.exclude(user__first_name="", user__last_name=""))

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
        msg = u"This field is required"

        # Check the already existent school field
        school = cleaned_data.get('school')

        # Check the new school fields
        s_name = cleaned_data.get('school_name')
        s_url = cleaned_data.get('school_url')
        s_email = cleaned_data.get('school_email')
        s_phone = cleaned_data.get('school_phone')
        s_address = cleaned_data.get('school_address')
        s_city = cleaned_data.get('school_city')
        s_country = cleaned_data.get('school_country')

        # If an old school was selected, just continue
        if school:
            pass
        # If not, check the new school fields
        elif s_name or s_url or s_email or s_phone or s_address or s_city or s_country:
            # If one of them is full, check the mandatory ones
             if s_name and s_url and s_city and s_country:
                # Everything is fine
                pass
             else:
                 # Something is missing
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

        # Otherwise, an old school must be chosen
        else:
            self.errors['school'] = self.error_class([msg])
                    
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
                     Row('school', HTML('<input type="button" id="new" onclick="click_new()" value="Add a new school"/>')),
                     HTML('</div>'),
                     
                     HTML('<div id="create">'),
                     'school_name',
                     'school_url',
                     'school_email',
                     'school_phone',
                     'school_address',
                     'school_city',
                     'school_country',
                     HTML('<input type="button" id="old" onclick="click_old()" value="Choose an already existent school"/>'),
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
        helper.form_id = 'my_form'
        #helper.form_action = "/add_course/?status='old'"

        return helper
