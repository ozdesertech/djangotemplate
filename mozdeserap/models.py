# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.ForeignKey(AuthGroup)
    permission_id = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user_id = models.ForeignKey(AuthUser)
    group_id = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user_id = models.ForeignKey(AuthUser)
    permission_id = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class CandidateMission(models.Model):
    family_candidate_family_id = models.ForeignKey('FamilyCandidate')
    family_mission_mission_id = models.ForeignKey('FamilyMission')
    reject_case = models.CharField(max_length=100, blank=True, null=True)
    address_loc = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'candidate_mission'
        unique_together = (('family_candidate_family_id', 'family_mission_mission_id'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user_id = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FamilyCandidate(models.Model):
    family_id = models.AutoField(primary_key=True)
    family_candidate_fullname = models.CharField(max_length=45)
    family_category_type = models.CharField(max_length=45)
    family_candidate_age = models.IntegerField()
    family_candidate_passport = models.CharField(unique=True, max_length=11)
    product_tbl_product_id = models.ForeignKey('ProductTbl')

    class Meta:
        managed = False
        db_table = 'family_candidate'
        unique_together = (('family_id', 'product_tbl_product_id'),)


class FamilyMission(models.Model):
    mission_id = models.AutoField(primary_key=True)
    mission_location = models.CharField(max_length=45)
    mission_duration = models.IntegerField(blank=True, null=True)
    mission_time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'family_mission'


class ProductTbl(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=45, blank=True, null=True)
    product_type = models.CharField(max_length=45, blank=True, null=True)
    product_quality = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_tbl'
