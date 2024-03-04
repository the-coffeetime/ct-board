from django.db import models


class Comments(models.Model):
    commentID = models.AutoField(db_column='commentID', primary_key=True)
    postID = models.ForeignKey('post.Posts', models.CASCADE, db_column='postID')
    userID = models.PositiveBigIntegerField(db_column='userID')
    content = models.TextField()
    parentCommentID = models.IntegerField(db_column='parentCommentID', blank=True, null=True)
    anonymous = models.BooleanField()
    likes = models.IntegerField()
    reports = models.IntegerField()
    createdAt = models.DateTimeField(db_column='createdAt')
    updatedAt = models.DateTimeField(db_column='updatedAt')

    class Meta:
        managed = False
        db_table = 'comments'


class CommentFollowers(models.Model):
    commentID = models.ForeignKey('Comments', models.CASCADE, db_column='commentID')
    userID = models.PositiveBigIntegerField(db_column='userID')

    class Meta:
        managed = False
        db_table = 'commentFollowers'
        unique_together = (('commentID', 'userID'),)
