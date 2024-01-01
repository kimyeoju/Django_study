from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView
from accounts.forms import ProfileForm
from accounts.models import Profile
from django.shortcuts import redirect



# 선택 1
# @login_required
# def profile(request):
#     return render(request, 'accounts/profile.html')


# 선택 2
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'

profile = ProfileView.as_view()


# class ProfileUpdateView(LoginRequiredMixin, UpdateView):
#     model = Profile
#     form_class = ProfileForm
    
# profile_edit = ProfileUpdateView.as_view()


@login_required
def profile_edit(request):
    try:
        # 프로필이 있는지 확인
        profile = request.user.profile
    # Profile.objects.get(user=request.user) 위의 코드랑 같은 코드
    except Profile.DoesNotExist:
        profile = None
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'accounts/profile_form.html', {
        'form' : form,
    })
    

def signup(request):
    pass

def logout(request):
    pass