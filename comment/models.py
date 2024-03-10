from django.db import models


class Comments(models.Model):
    objects = models.Manager()
    commentID = models.AutoField(db_column='commentID', primary_key=True)
    postID = models.ForeignKey('post.Posts', models.CASCADE, db_column='postID')
    userID = models.PositiveBigIntegerField(db_column='userID')
    content = models.TextField(max_length=2000)
    parentCommentID = models.IntegerField(db_column='parentCommentID', blank=True, null=True)
    anonymous = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)
    reports = models.IntegerField(default=0)
    createdAt = models.DateTimeField(db_column='createdAt', auto_now_add=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', auto_now=True)

    class Meta:
        managed = False
        db_table = 'comments'


class CommentFollowers(models.Model):
    objects = models.Manager()
    id = models.AutoField(auto_created=True, primary_key=True, db_column='id')
    commentID = models.ForeignKey('Comments', models.CASCADE, db_column='commentID')
    userID = models.PositiveBigIntegerField(db_column='userID')

    class Meta:
        managed = False
        db_table = 'commentFollowers'
        unique_together = (('commentID', 'userID'),)
