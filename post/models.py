from django.db import models


class Posts(models.Model):
    objects = models.Manager()
    postID = models.AutoField(db_column='postID', primary_key=True)
    boardID = models.ForeignKey('board.Boards', models.CASCADE, db_column='boardID')
    userID = models.PositiveBigIntegerField(db_column='userID')
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=10000)
    pictureUrl = models.CharField(db_column='pictureURL', max_length=255, blank=True, null=True)
    viewCount = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    reports = models.IntegerField(default=0)
    anonymous = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'posts'


class PostFollowers(models.Model):
    objects = models.Manager()
    postID = models.ForeignKey('Posts', models.CASCADE, db_column='postID')
    userID = models.PositiveBigIntegerField(db_column='userID')

    class Meta:
        managed = False
        db_table = 'postFollowers'
        unique_together = (('postID', 'userID'),)
