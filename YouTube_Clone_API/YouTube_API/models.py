from django.db import models


class Comment(models.Model):
    comment_body = models.CharField(max_length=300)
    videoid = models.CharField(max_length=100)
    like = models.IntegerField()
    dislike = models.IntegerField()


class Reply(models.Model):
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)
    reply_body = models.CharField(max_length=300)
