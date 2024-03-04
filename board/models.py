from django.db import models


class Boards(models.Model):
    boardID = models.AutoField(db_column='boardID', primary_key=True)
    fieldID = models.ForeignKey('field.Fields', models.CASCADE, db_column='fieldID')
    jobID = models.ForeignKey('job.Jobs', models.CASCADE, db_column='jobID')
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'boards'
        unique_together = (('fieldID', 'jobID', 'name'),)


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
