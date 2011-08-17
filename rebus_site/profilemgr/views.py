from django.shortcuts import render
from django.http import HttpResponseRedirect
from profilemgr.forms import UserProfileForm
from profilemgr.models import UserProfile
from profilemgr.regbackend import save_profile
from django.contrib.auth.decorators import login_required


@login_required()
def update_profile(request):
#    import ipdb; ipdb.set_trace()
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            save_profile(request.user, request)
            return HttpResponseRedirect('/community/')
    else:
        u = request.user
        if u.userprofile:
            prof = u.userprofile
            # Fill in the form with the existent values
            form = UserProfileForm(initial = {'username': u.username,
                                              'email': u.email,
                                              'password1': u.password,
                                              'password2': u.password,
                                              'first_name': u.first_name,
                                              'last_name': u.last_name,
                                              'url': prof.url,
                                              'phone': prof.phone,
                                              'work_address': prof.work_address,
                                              'city': prof.city, 
                                              'country': prof.city,
                                              'image': prof.image,
                                              })
        else:
            # No profile. Fill in the form with only user values.
            form = UserProfileForm(initial = {'username': u.username,
                                              'email': u.email,
                                              'password1': u.password,
                                              'password2': u.password,
                                              'first_name': u.first_name,
                                              'last_name': u.last_name,
                                              })
    
    return render(request, 'registration/update_profile.html', {'form': form, 'url_name': '/accounts/update/'})
