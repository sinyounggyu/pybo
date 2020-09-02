from django.contrib import admin

from .models import Question


class QuestionAdmin(admin.ModelAdmin):  # 관리자 화면에서 제목으로 질문을 검색할 수 있게 해주는 클래스
    search_fields = ['subject']


admin.site.register(Question, QuestionAdmin)  # Question 모델과 QuestionAdmin 클래스를 관리자에 등록

# Register your models here.
