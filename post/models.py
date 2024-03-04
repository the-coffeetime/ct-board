from django.db import models

from ct_board.board.models import Boards


class Posts(models.Model):
    objects = models.Manager()
    postID = models.AutoField(db_column='postID', primary_key=True)
    boardID = models.ForeignKey(Boards, models.CASCADE, db_column='boardID')
    userID = models.PositiveBigIntegerField(db_column='userID')
    title = models.CharField(max_length=255)
    content = models.TextField()
    pictureUrl = models.CharField(db_column='pictureURL', max_length=255, blank=True, null=True)
    viewCount = models.IntegerField()
    likes = models.IntegerField()
    reports = models.IntegerField()
    anonymous = models.BooleanField()
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'posts'


class PostFollowers(models.Model):
    postID = models.ForeignKey('Posts', models.CASCADE, db_column='postID')
    userID = models.PositiveBigIntegerField(db_column='userID')

    class Meta:
        managed = False
        db_table = 'postFollowers'
        unique_together = (('postID', 'userID'),)
