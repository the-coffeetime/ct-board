from django.db import models


class Jobs(models.Model):
    jobID = models.AutoField(db_column='jobID', primary_key=True)
    fieldID = models.ForeignKey('Fields', models.CASCADE, db_column='fieldID')
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'jobs'
        unique_together = (('fieldID', 'name'),)


class JobCreationRequest(models.Model):
    userID = models.PositiveBigIntegerField(db_column='userID')
    fieldName = models.CharField(db_column='fieldName', max_length=255)
    jobName = models.CharField(db_column='jobName', max_length=255)
    note = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jobCreationRequest'
        unique_together = (('userID', 'fieldName', 'jobName'),)
