# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Team.point'
        # db.delete_column('whwn_team', 'point')

        # Adding field 'Team.latitude'
        db.add_column('whwn_team', 'latitude',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=3, blank=True),
                      keep_default=False)

        # Adding field 'Team.longitude'
        db.add_column('whwn_team', 'longitude',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=3, blank=True),
                      keep_default=False)

        # Deleting field 'Item.point'
        # db.delete_column('whwn_item', 'point')

        # Adding field 'Item.latitude'
        db.add_column('whwn_item', 'latitude',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=3, blank=True),
                      keep_default=False)

        # Adding field 'Item.longitude'
        db.add_column('whwn_item', 'longitude',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=3, blank=True),
                      keep_default=False)

        # Deleting field 'UserProfile.point'
        # db.delete_column('whwn_userprofile', 'point')

        # Adding field 'UserProfile.latitude'
        db.add_column('whwn_userprofile', 'latitude',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=3, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.longitude'
        db.add_column('whwn_userprofile', 'longitude',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=3, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Team.point'
        # db.add_column('whwn_team', 'point',
        #               self.gf('django.contrib.gis.db.models.fields.PointField')(null=True, blank=True),
        #               keep_default=False)

        # Deleting field 'Team.latitude'
        db.delete_column('whwn_team', 'latitude')

        # Deleting field 'Team.longitude'
        db.delete_column('whwn_team', 'longitude')

        # Adding field 'Item.point'
        # db.add_column('whwn_item', 'point',
        #               self.gf('django.contrib.gis.db.models.fields.PointField')(null=True, blank=True),
        #               keep_default=False)

        # Deleting field 'Item.latitude'
        db.delete_column('whwn_item', 'latitude')

        # Deleting field 'Item.longitude'
        db.delete_column('whwn_item', 'longitude')

        # Adding field 'UserProfile.point'
        # db.add_column('whwn_userprofile', 'point',
        #               self.gf('django.contrib.gis.db.models.fields.PointField')(null=True, blank=True),
        #               keep_default=False)

        # Deleting field 'UserProfile.latitude'
        db.delete_column('whwn_userprofile', 'latitude')

        # Deleting field 'UserProfile.longitude'
        db.delete_column('whwn_userprofile', 'longitude')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'whwn.item': {
            'Meta': {'object_name': 'Item'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '3', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '3', 'blank': 'True'}),
            'possessor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'requested': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sku': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['whwn.ItemSKU']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        'whwn.itemcategory': {
            'Meta': {'object_name': 'ItemCategory'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        'whwn.itemsku': {
            'Meta': {'unique_together': "(('upc', 'team'),)", 'object_name': 'ItemSKU'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['whwn.ItemCategory']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['whwn.Team']"}),
            'upc': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        'whwn.message': {
            'Meta': {'object_name': 'Message'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'contents': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'flagged': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['whwn.Team']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        'whwn.team': {
            'Meta': {'object_name': 'Team'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '3', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '3', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'primary_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'primary_user'", 'null': 'True', 'to': "orm['auth.User']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        'whwn.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'email_verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '3', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '3', 'blank': 'True'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'phone_verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['whwn.Team']", 'null': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['whwn']