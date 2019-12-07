from django.db import models
from django.conf import settings
from django.utils import timezone


class PostManager(models.Manager):
    def createPost(self, author, title, text, date):
        post = self.create(author,title,text,date)
        return post
        
    def sort_by_date(self):
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("""
                    SELECT * 
                    FROM blog_post
                    ORDER BY date DESC;
                    """)
            out = []
            for row in cursor.fetchall():
                post = self.model(id=row[0], author=row[1], title=row[2], text=row[3], date=row[4])
                out.append(post)
            return  out


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    objects = PostManager()

    def __str__(self):
        return self.title
