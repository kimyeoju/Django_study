from django.urls import path, re_path, register_converter
from . import views


from .converters import YearConverter, MonthConverter, DayConverter

register_converter(YearConverter, 'converter_year')
register_converter(MonthConverter, 'converter_month')
register_converter(DayConverter, 'converter_day')

app_name = 'instagram' # URL Reverse에서 namespace 역할을 하게 된다.

urlpatterns = [
    path('new/', views.post_new, name='post_new'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    # path('archives/<int:year>/', views.archives_year),
    # re_path(r'archives/(?P<year>20\d{2})/', views.archives_year),
    # path('archives/<converter_year:year>/', views.archives_year),
    path('archive/', views.post_archive, name='post_archive'),
    # 년도(year)
    path('archive/<converter_year:year>/', views.post_year_archive, name='post_year_archive'),
    # 달 (month)
    # path('archive/<converter_year:year>/<converter_month:month>/', views.post_m,onth_archive, name='post_month_archive'),
    # 일 (day)
    # path('archive/<converter_year:year>/<converter_month:month>/<converter_day:day>/', views.post_day_archive, name='post_day_archive'),
    
]