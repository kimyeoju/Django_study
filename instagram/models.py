from django.db import models

# Create your models here.
class Post(models.Model):
    message = models.TextField() # self.first = first
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y/%m/%d')
    # instagram/post/2023/11/12/AnyConv.com__보안_해킹_아이콘_026.png로 저장
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        # return f"Custom Post object ({self.id})" -> Custom Post object (1)
        return self.message
    
    def message_length(self):
        return f'{len(self.message)} 글자'
    message_length.short_description = "메세지 글자수"