from django.views.generic import ListView, DetailView
from django.http import HttpResponse, HttpRequest, Http404
from django.shortcuts import get_object_or_404, render
from .models import Post

post_list = ListView.as_view(model=Post)

# def post_list(request):
#     qs = Post.objects.all()
#     q = request.GET.get('q', '')
#     if q:
#         qs = qs.filter(message__icontains=q)
#     return render(request, 'instagram/post_list.html', {
#         'post_list': qs,
#         'q':q,
#     })


    # pk=pk에서 앞에 pk는 필드의 종류를 지정 뒤의 pk는 값
# def post_detail(request, pk):
# 선택 1 
#     post = get_object_or_404(Post, pk=pk)
# 선택 2
#     # try:
#     #     post = Post.objects.get(pk=pk) # DoesNotExist 예외
#     # except Post.DoesNotExist:
#     #     raise Http404
    
#     return render(request, 'instagram/post_detail.html', {
#         'post': post,
#     })

# 선택 3
post_detail = DetailView.as_view(model=Post) 


def archives_year(request, year):
    return HttpResponse(f'{year}년 archives')