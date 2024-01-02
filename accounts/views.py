from django.contrib.auth import get_user_model, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView, CreateView
from accounts.forms import ProfileForm
from accounts.models import Profile
from django.shortcuts import redirect
from django.conf import settings


User = get_user_model()


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


# 선택 1
class SignupView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = settings.LOGIN_URL
    template_name = 'accounts/signup_form.html'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        # 현재 뷰에서 처리 중인 객체를 나타냄 UserCreationForm을 통해 새로 등록한 사용자를 나타냄
        user = self.object
        # 사용자를 로그인 상태로 만들어주는 함수 auth_login(self.request(현재 요청 객체 -> 현재 요청에 관한 정보에 접근), user(로그인 할 사용자 객체))
        # 즉, 새로 생성된 사용자를 현재 요청에 로그인 시키는 것 이는 사용자가 회원가입을 완료한 후에 로그인 상태로 애플리케이션을 계속 사용할 수 있도록 해줌
        auth_login(self.request, user)
        return response


signup = SignupView.as_view()


# 선택 2
# signup = CreateView.as_view(
#     model=User,
#     form_class=UserCreationForm,
#     success_url=settings.LOGIN_URL,
#     template_name='accounts/signup_form.html'
# )


def logout(request):
    pass