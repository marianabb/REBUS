from rebus_site.profilemgr.models import UserProfile


def user_created(sender, user, request, **kwargs):
    UserProfile.objects.create(user=user)

    user.first_name = request.POST.get('first_name', None)
    user.last_name = request.POST.get('last_name', None)
    profile = user.get_profile()
    profile.url = request.POST.get('url', None)
    profile.phone = request.POST.get('phone', None)
    profile.work_address = request.POST.get('work_address', None)
    profile.city = request.POST.get('city', None)
    profile.country = request.POST.get('country', None)
    profile.image = request.FILES.get('image', None)
    user.save()
    profile.save()


from registration.signals import user_registered
user_registered.connect(user_created)
