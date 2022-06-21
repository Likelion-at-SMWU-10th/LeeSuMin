from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self): # 객체를 지정한 문자열로 표현
        return self.title
    
    def summary(self):
        return self.body[:30]
