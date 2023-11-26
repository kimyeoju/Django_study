from django.urls import path, re_path, register_converter
from . import views

class YearConverter:
    regex = r"20\d{2}"
    
    # url 매칭이 되었을 때 views.archives_year 함수 호출하기 전에 인자를 한번 정리
    # 정규표현식으로 인자를 뽑아내면 그 형태는 문자열인데, int 정수로 변환해서 넘겨준다.
    def to_python(self, value):
        return int(value)
    
    # 어떤 값을 url 문자열로 리버싱할 때 호출되는 함수
    # int -> str로 변환 
    def to_url(self, value):
        return str(value)
        # return "%04d" % value


register_converter(YearConverter, 'converter_year')

urlpatterns = [
    path('', views.post_list),
    path('<int:pk>/', views.post_detail),
    # path('archives/<int:year>/', views.archives_yesr),
    # re_path(r'archives/(?P<year>20\d{2})/', views.archives_year),
    path('archives/<converter_year:year>/', views.archives_year),
    
]