from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    message = models.TextField() # self.first = first
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y/%m/%d')
    # instagram/post/2023/11/12/AnyConv.com__보안_해킹_아이콘_026.png로 저장
    tag_set = models.ManyToManyField('Tag', blank=True)
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        # return f"Custom Post object ({self.id})" -> Custom Post object (1)
        return self.message
    
    def get_absolute_url(self):
        return reverse('instagram:post_detail', args=[self.pk])
    
    # default 정렬
    # python manage.py shell_plus --pring-sql
    # Post.objects.all().order_by('created_at') order_by 지정 할 경우 default 정렬 적용되지 않음
    class Meta:
        ordering = ['-id']
    
    def message_length(self):
        return f'{len(self.message)} 글자'
    message_length.short_description = "메세지 글자수"
    

    # ForeignKey(to, on_delete=models.CASCADE) 1:N 관계 N측에서 작성 
class Comment(models.Model):
    # Post - post(pk) Comment - comment에 있는 post_pk
    # limit_choices_to : admin 페이지에서 공개여부가 true인 게시글만 보여줌
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                            limit_choices_to={'is_public':True}) # post_id 필드가 생성이 된다.
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.message


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # post_set = models.ManyToManyField(Post)
    
    def __str__(self):
        return self.name