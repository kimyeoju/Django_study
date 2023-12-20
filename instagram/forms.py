import re
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'message', 'photo', 'tag_set', 'is_public'
        ]
        # exclude = []
        
    def clean_message(self):
        message = self.cleaned_data.get('message')
        if message:
            # 만약 form에 'Hello 월드'라고 저장하면 '월드'라고 뜬다. 
            message = re.sub(r'[a-zA-Z]+','', message)
        return message


# 샘플 
# myapp/models.py
# Form Validation 예제

# class GameUser(models.Model):
#     server = models.CharField(max_length=10)
#     username = models.CharField(max_length=20)

# class GameUserSignupForm(forms.ModelForm):
#     class Meta:
#         model = GameUser
#         fields = ['server', 'username']
    
#     def clean_username(self):
#         'username 필드값의 좌/우 공백을 제거하고, 최소 3글자 이상 입력되었는지 체크'
#         username = self.cleaned_data.get('username', '').strip()
#         if len(username) < 3:
#             raise forms.ValidationError('3글자 이상 입력해주세요.')
#         이 리턴값으로 self.cleaned_data['username'] 값이 변경된다.
#         좌/우 공백이 제거된 (strip) username으로 변경된다.
#         return username
    
#     def clean(self):
#         cleaned_data = super().clean()
#         if self.check_exist(cleaned_data['server'], cleaned_data['username']):
#             clean 내 ValidationError는 non_field_errors 로서 노출
#             raise forms.ValidationError('서버에 이미 등록된 username입니다.')
#         return cleaned_data
    
# 위에서 check_exist 호출함
#     def check_exist(self, server, username):
#         return GameUser.objects.filter(server=server, username=username).exists()