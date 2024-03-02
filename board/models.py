from django.db import models


class Fields(models.Model):
    fieldID = models.AutoField(db_column='fieldID', primary_key=True)
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        managed = False
        db_table = 'fields'


class Jobs(models.Model):
    jobID = models.AutoField(db_column='jobID', primary_key=True)
    fieldID = models.ForeignKey('Fields', models.CASCADE, db_column='fieldID')
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'jobs'
        unique_together = (('fieldID', 'name'),)


class Boards(models.Model):
    boardID = models.AutoField(db_column='boardID', primary_key=True)
    fieldID = models.ForeignKey('Fields', models.CASCADE, db_column='fieldID')
    jobID = models.ForeignKey('Jobs', models.CASCADE, db_column='jobID')
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'boards'
        unique_together = (('fieldID', 'jobID', 'name'),)


class Posts(models.Model):
    postID = models.AutoField(db_column='postID', primary_key=True)
    boardID = models.ForeignKey(Boards, models.CASCADE, db_column='boardID')
    userID = models.PositiveBigIntegerField(db_column='userID')
    title = models.CharField(max_length=255)
    content = models.TextField()
    pictureUrl = models.CharField(db_column='pictureURL', max_length=255, blank=True, null=True)
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


class Comments(models.Model):
    commentID = models.AutoField(db_column='commentID', primary_key=True)
    postID = models.ForeignKey('Posts', models.CASCADE, db_column='postID')
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


class FieldCreationRequest(models.Model):
    userID = models.PositiveBigIntegerField(db_column='userID')
    fieldName = models.CharField(db_column='fieldName', max_length=255)
    note = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fieldCreationRequest'
        unique_together = (('userID', 'fieldName'),)


class JobCreationRequest(models.Model):
    userID = models.PositiveBigIntegerField(db_column='userID')
    fieldName = models.CharField(db_column='fieldName', max_length=255)
    jobName = models.CharField(db_column='jobName', max_length=255)
    note = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jobCreationRequest'
        unique_together = (('userID', 'fieldName', 'jobName'),)


class BoardCreationRequest(models.Model):
    userID = models.PositiveBigIntegerField(db_column='userID')
    fieldName = models.CharField(db_column='fieldName', max_length=255)
    jobName = models.CharField(db_column='jobName', max_length=255)
    boardName = models.CharField(db_column='boardName', max_length=30)
    note = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'boardCreationRequest'
        unique_together = (('userID', 'fieldName', 'jobName', 'boardName'),)
