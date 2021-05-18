# user가 views.py에 request를 하면, 
# views.py가 "models.py"에게 찾아달라고 하면 "모델"이 DB를 찾아서 다시 views.py에 전달하고, 
# 뷰는 템플릿한테 이렇게 보여줘~하면 템플릿이 뷰에게 보여주고 최종적으로 뷰가 유저에게 보여주는 원리!!

# models.py는 DB를 저장하는 기능!!
# 모델을 변경한 후에 migrate해주어야.
# django가 models.py에 처리하고자 하는 데이터 알려주는 기능


from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    def __str__(self):
        return self.title # 블로그 title이 보여지게 하기 위해
    def summary(self):
        return self.body[:100] # body의 글자수 100자 제한 함수.