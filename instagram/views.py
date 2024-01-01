from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.dates import ArchiveIndexView, YearArchiveView
from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponse, HttpRequest, Http404
from django.shortcuts import get_object_or_404, render, redirect
from .models import Post
from .forms import PostForm

# @login_required
# def post_new(request):
    # if request.method == 'POST':
        # form = PostForm(request.POST, request.FILES)
        # if form.is_valid():
            # commit=False면 아직 저장이 안된 상태
            # post = form.save(commit=False)
            # post.author = request.user 
            # 현재 로그인 User Instance
            # post.save()
            # messages.success(request, '포스팅을 저장했습니다.')
            
            # post = form.save(commit=False)
            # post.save()
            # models에 get_absolute_url이 구현되어 있으니 detail 페이지로 자동으로 넘어감
            # return redirect(post)
    # Get 방식
    # else:
        # Get 방식이니까 빈 form을 보여줌
    #     form = PostForm()
        
    # return render(request, 'instagram/post_form.html', {
    #     'form' : form,
    #     'post' : None,
    # })


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        messages.success(self.request, '포스팅을 저장했습니다.')
        return super().form_valid(form)
        
post_new = PostCreateView.as_view()


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    # 작성자 Check Tip
    if post.author != request.user:
        messages.error(request,'작성자만 수정할 수 있습니다.')
        return redirect(post)
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            messages.success(request, '포스팅을 수정했습니다.')
            return redirect(post)
    # Get 방식
    else:
        form = PostForm(instance=post)
        
    return render(request, 'instagram/post_form.html', {
        'form' : form,
        # edit시에는 해당 post를 넘김
        'post' : post,
    })


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        messages.success(request, '포스팅을 삭제했습니다.')
        return redirect('instagram:post_list')
    return render(request, 'instagram/post_confirm_delete.html', {
        'post': post,
    })
    
    
# ?page = 2 -> 하면 2페이지로 이동
# decorator 장식 선택 1
# post_list = login_required(ListView.as_view(model=Post, paginate_by=10))

# decorator 장식 선택 2
# @method_decorator(login_required, name='dispatch')
# decorator 장식 선택 3


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    paginate_by = 10

post_list = PostListView.as_view()

# @login_required
# def post_list(request):
#     qs = Post.objects.all()
#     q = request.GET.get('q', '')
#     if q:
# Post.objects.all()에 filter을 써서 사용자가 쓴 검색어 q를 대입해서 검색 구현
#         qs = qs.filter(message__icontains=q)
    
#     # 등록만 해줌 소비는 template layout.html에서 해줌
#     messages.info(request, 'messages 테스트')
    
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
# post_detail = DetailView.as_view(
#     model=Post,
#     # 공개된 포스팅 안에서 디테일뷰를 처리 
#     queryset=Post.objects.filter(is_public=True)
#     )

class PostDetailView(DetailView):
    model = Post
    
    # queryset=Post.objects.filter(is_public=True)
    # get_queryset은 DetailView의 메서드
    def get_queryset(self):
        
        # 기본 쿼리셋을 가져옴
        qs = super().get_queryset()
        # 로그인이 되어있지 않다면 공개된 글만 보여줌
        if not self.request.user.is_authenticated:
            qs = qs.filter(is_public=True)
        return qs

post_detail = PostDetailView.as_view()

# def archives_year(request, year):
#     return HttpResponse(f'{year}년 archives')


post_archive = ArchiveIndexView.as_view(model=Post, date_field='created_at', paginate_by=10)


post_year_archive = YearArchiveView.as_view(model=Post, date_field='created_at', make_object_list=True)