# 모델 작성한 것을 admin 사이트에 반영해주어야.

from django.contrib import admin
from .models import Blog # models.py 파일이 같은 위치에 있기 때문에 .models



# Register your models here.

admin.site.register(Blog) # admin 사이트에 Blog 모델을 등록해라~