from django.db import models


class Boards(models.Model):
    objects = models.Manager()
    boardID = models.AutoField(db_column='boardID', primary_key=True)
    fieldID = models.ForeignKey('field.Fields', models.CASCADE, db_column='fieldID')
    jobID = models.ForeignKey('job.Jobs', models.CASCADE, db_column='jobID')
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'boards'
        unique_together = (('fieldID', 'jobID', 'name'),)


class BoardCreationRequest(models.Model):
    objects = models.Manager()
    userID = models.PositiveBigIntegerField(db_column='userID')
    fieldName = models.CharField(db_column='fieldName', max_length=255)
    jobName = models.CharField(db_column='jobName', max_length=255)
    boardName = models.CharField(db_column='boardName', max_length=30)
    note = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'boardCreationRequest'
        unique_together = (('userID', 'fieldName', 'jobName', 'boardName'),)


class BoardFollowers(models.Model):
    objects = models.Manager()
    id = models.AutoField(auto_created=True, primary_key=True, db_column='id')
    boardID = models.ForeignKey(Boards, models.CASCADE, db_column='boardID')
    userID = models.PositiveBigIntegerField(db_column='userID')
    createdAt = models.DateTimeField(db_column='createdAt', auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'boardFollowers'
        unique_together = (('boardID', 'userID'),)