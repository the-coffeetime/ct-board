from django.db import models


class Fields(models.Model):
    fieldID = models.AutoField(db_column='fieldID', primary_key=True)
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        managed = False
        db_table = 'fields'


class FieldCreationRequest(models.Model):
    userID = models.PositiveBigIntegerField(db_column='userID')
    fieldName = models.CharField(db_column='fieldName', max_length=255)
    note = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fieldCreationRequest'
        unique_together = (('userID', 'fieldName'),)
