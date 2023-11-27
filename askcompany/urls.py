from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# from django.conf import global_settings
# from askcompany import settings
from django.conf import settings
from django.views.generic import TemplateView, RedirectView

# class RootView(TemplateView):
#     template_name = 'root.html'

urlpatterns = [
    # path('', TemplateView.as_view(template_name='root.html'), name='root'),
    path('', RedirectView.as_view(
        # url='/instagram/'
        pattern_name = 'instagram:post_list',
        ), name='root'),
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
    