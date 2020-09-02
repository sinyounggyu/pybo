from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200)  # 제목을 나타내는 속성, 최대 200자까지 가능하게 설정했고 이렇게 길이가 제한된 텍스트는 CharField를 사용해야함.
    content = models.TextField()  # 내용을 나타내는 속성, 글자수 제한이 없으므로 TextField를 사용함.
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question')  # voter 추가

    def __str__(self): # id 대신 제목을 표시하게 해주는 메서드
        return self.subject


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # 질문에 대한 답변이므로 Question 모델을 속성으로 가져간 것, 기존 모델을 속성으로 가져갈 때 ForeignKey를 사용한다. on_delete=models.CASCADE의 의미는 연결된 질문이 삭제되면 이 답변도 삭제된다는 의미.
    content = models.TextField()
    modify_date = models.DateTimeField(null=True, blank=True)
    create_date = models.DateTimeField()
    voter = models.ManyToManyField(User, related_name='voter_answer')


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)


