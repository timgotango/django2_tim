# user가 "views.py"에 request를 하면, 
# "views.py"가 models.py에게 찾아달라고 하면 모델이 DB를 찾아서 다시 "views.py"에 전달하고, 
# "뷰"는 템플릿한테 이렇게 보여줘~하면 템플릿이 "뷰"에게 보여주고 최종적으로 "뷰"가 유저에게 보여주는 원리!!

from django.shortcuts import redirect, render
from .models import Blog
from django.utils import timezone

# Create your views here.

def home(request):
    blogs = Blog.objects # Blog 클래스 안 객체를 blogs 변수에 담겠다~
    return render(request, "home.html", {'blogs':blogs}) # blogs라는 이름으로 템플릿에서 사용하겠다~

def detail(request, blog_id): # 인자를 블로그 id까지 2개 받음
    blog_detail = Blog.objects.get(id = blog_id) # 블로그 안 객체를 찾아서 변수에 집어넣음
    return render(request, 'detail.html', {'blog': blog_detail}) # 특정 디테일 페이지를 띄워줘라

def new(request):
    return render(request, 'new.html')

def create(request): # 글쓰기 함수
    blog = Blog()                               # 블로그 클래스에서 객체 생성
    blog.title = request.GET['title']           # new.html파일에 있는 name ='title' 에서 찾아가지고 넣어주겠다~
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()                                 # save해야 DB에 저장!!!
    return redirect('/blog/' + str(blog.id))

def delete(request, blog_id):
    Blog.objects.get(id = blog_id).delete()
    return redirect('/') # homepage로 리턴

def edit(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render(request, 'edit.html', {'blog':blog})

def update(request, blog_id):
    blog = Blog.objects.get(id = blog_id)
    blog.title = request.POST.get('title')
    blog.body = request.POST.get('body')
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))

def introduce(request):
    return render(request, 'introduce.html')