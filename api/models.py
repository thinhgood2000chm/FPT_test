from django.db import models


# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_column='created_at', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, db_column='modified_at', blank=True, null=True)
    created_by = models.CharField(max_length=100, db_column='created_by', blank=True, null=True, default='')
    updated_by = models.CharField(max_length=100, db_column='modified_by', blank=True, null=True, default='')

    class Meta:
        abstract = True


class UserInfo(BaseModel):
    id = models.AutoField(db_column='id', primary_key=True)
    full_name = models.CharField(max_length=100, db_column='full_name')
    user_name = models.CharField(
        max_length=100, db_column='user_name')
    password = models.CharField(max_length=100, db_column='password')

    class Meta:
        db_table = 'user_info'