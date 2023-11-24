from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# from django.conf import global_settings
# from askcompany import settings
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('blog/', include('blog.urls')),
    path('instagram/', include('instagram.urls')),
]

# DEBUG가 참일때만 실행
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    import debug_toolbar
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
    