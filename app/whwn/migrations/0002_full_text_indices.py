# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models, connections


class Migration(SchemaMigration):

    def forwards(self, orm):
        cursor = connections['default'].cursor()
        cursor.execute("""
CREATE INDEX message_text_index
ON whwn_communicationmessage
USING gin(to_tsvector('english',whwn_communicationmessage.message_text));""")
        cursor.execute("""
CREATE INDEX post_name_index
ON whwn_post
USING gin(to_tsvector('english',whwn_post.name));""")

    def backwards(self, orm):
        cursor = connections['default'].cursor()
        cursor.execute("DROP INDEX message_text_index;")
        cursor.execute("DROP INDEX post_name_index;")

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
        'whwn.communication': {
            'Meta': {'object_name': 'Communication'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'hashcode': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latest_message_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'owner'", 'to': "orm['auth.User']"}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['whwn.Post']"}),
            'requester': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'requester'", 'to': "orm['auth.User']"})
        },
        'whwn.communicationmessage': {
            'Meta': {'object_name': 'CommunicationMessage'},
            'communication': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['whwn.Communication']"}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'flagged': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message_text': ('django.db.models.fields.CharField', [], {'max_length': '160'}),
            'read': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'receiver': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'message_receiver'", 'to': "orm['auth.User']"}),
            'send_type': ('django.db.models.fields.IntegerField', [], {}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'sent_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True'}),
            'type': ('django.db.models.fields.IntegerField', [], {})
        },
        'whwn.errormessage': {
            'Meta': {'object_name': 'ErrorMessage'},
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'error_type': ('django.db.models.fields.IntegerField', [], {}),
            'flagged': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message_text': ('django.db.models.fields.CharField', [], {'max_length': '160'}),
            'read': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'response': ('django.db.models.fields.CharField', [], {'max_length': '160'}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'sent_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True'}),
            'type': ('django.db.models.fields.IntegerField', [], {})
        },
        'whwn.location': {
            'Meta': {'object_name': 'Location'},
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            # 'point': ('django.contrib.gis.db.models.fields.PointField', [], {})
        },
        'whwn.notificationmessage': {
            'Meta': {'object_name': 'NotificationMessage'},
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'flagged': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message_text': ('django.db.models.fields.CharField', [], {'max_length': '160'}),
            'notify_type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'read': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'sent_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True'}),
            'type': ('django.db.models.fields.IntegerField', [], {})
        },
        'whwn.post': {
            'Meta': {'object_name': 'Post'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'categories': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['whwn.PostCategory']"}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'expiration_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'is_needed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['whwn.Location']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'post_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'posted_date': ('django.db.models.fields.DateField', [], {}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'updated_date': ('django.db.models.fields.DateField', [], {'null': 'True'})
        },
        'whwn.postcategory': {
            'Meta': {'object_name': 'PostCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'whwn.statusmessage': {
            'Meta': {'object_name': 'StatusMessage'},
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'flagged': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message_text': ('django.db.models.fields.CharField', [], {'max_length': '160'}),
            'read': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'response': ('django.db.models.fields.CharField', [], {'max_length': '160'}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'sent_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True'}),
            'status_type': ('django.db.models.fields.IntegerField', [], {}),
            'type': ('django.db.models.fields.IntegerField', [], {})
        },
        'whwn.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'communication_via': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['whwn']