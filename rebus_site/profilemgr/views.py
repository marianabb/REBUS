from django.shortcuts import render
from django.http import HttpResponseRedirect
from profilemgr.forms import UpdateProfileForm
from profilemgr.models import UserProfile
from django.contrib.auth.decorators import login_required


def save_updated_profile(user, request):
    # If the profile doesn't exist, create it
    if UserProfile.objects.filter(user__username=user.username).count() == 0:
        UserProfile.objects.create(user=user)
        
    user.email = request.POST.get('email', None)
    user.first_name = request.POST.get('first_name', None)
    user.last_name = request.POST.get('last_name', None)
    profile = user.get_profile()
    profile.url = request.POST.get('url', None)
    profile.phone = request.POST.get('phone', None)
    profile.work_address = request.POST.get('work_address', None)
    profile.city = request.POST.get('city', None)
    profile.country = request.POST.get('country', None)

    # Handle the image file
    if request.FILES.get('image') == None:
        if request.POST.get('image-clear') == u'on':
            # Clear the old image
            profile.image = None
    else:
        profile.image = request.FILES.get('image')
    
    user.save()
    profile.save()


@login_required()
def update_profile(request):
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            # Use custom update
            save_updated_profile(request.user, request)
            return HttpResponseRedirect('/community/')
    else:
        us = request.user
        # If the user has a profile show all fields
        if UserProfile.objects.filter(user__username=us.username).count() > 0:
            prof = us.get_profile()
            # Fill in the form with the existent values
            form = UpdateProfileForm(initial = {'email': us.email,
                                                'first_name': us.first_name,
                                                'last_name': us.last_name,
                                                'url': prof.url,
                                                'phone': prof.phone,
                                                'work_address': prof.work_address,
                                                'city': prof.city, 
                                                'country': prof.country,
                                                'image': prof.image,
                                                })
        else:
            # No profile. Fill in the form with only user values.
            form = UpdateProfileForm(initial = {'email': us.email,
                                                'first_name': us.first_name,
                                                'last_name': us.last_name,
                                                })
            
    return render(request, 'registration/update_profile.html', {'form': form, 'url_name': '/accounts/update/'})
