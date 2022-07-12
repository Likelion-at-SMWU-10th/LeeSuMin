from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:30]

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self): #객체를 문자열로 표현한 것을 반환해주는 함수
        return self.content
