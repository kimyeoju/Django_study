from django.contrib import admin
from django.utils.safestring import mark_safe # HTML을 안전하게 마크업
from .models import Post

# admin.site.register(Post)
@admin.register(Post) # Wrapping
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo_tag', 'message', 'message_length', 'is_public', 'created_at','updated_at']
    list_display_links = ['message']
    list_filter = ['created_at', 'is_public']
    search_fields = ['message']
    
    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}" style="width: 72px;" />')
        return None
    
    # def message_length(self, post): # admin은 post를 끌고옴
    #     return f'{len(post.message)} 글자'