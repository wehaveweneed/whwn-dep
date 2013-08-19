# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Volunteer'
        db.delete_table('whwn_volunteer')

        # Removing M2M table for field regions on 'Volunteer'
        db.delete_table('whwn_volunteer_regions')

        # Removing M2M table for field skills on 'Volunteer'
        db.delete_table('whwn_volunteer_skills')

        # Deleting model 'Skill'
        db.delete_table('whwn_skill')


    def backwards(self, orm):
        # Adding model 'Volunteer'
        db.create_table('whwn_volunteer', (
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('confirmed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('email_verification', self.gf('django.db.models.fields.CharField')(default='cd358cae5e6ae4ca51157966f3d4e829b61a8a35', max_length=40)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True)),
            ('vehicle', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=254)),
        ))
        db.send_create_signal('whwn', ['Volunteer'])

        # Adding M2M table for field regions on 'Volunteer'
        db.create_table('whwn_volunteer_regions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('volunteer', models.ForeignKey(orm['whwn.volunteer'], null=False)),
            ('region', models.ForeignKey(orm['whwn.region'], null=False))
        ))
        db.create_unique('whwn_volunteer_regions', ['volunteer_id', 'region_id'])

        # Adding M2M table for field skills on 'Volunteer'
        db.create_table('whwn_volunteer_skills', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('volunteer', models.ForeignKey(orm['whwn.volunteer'], null=False)),
            ('skill', models.ForeignKey(orm['whwn.skill'], null=False))
        ))
        db.create_unique('whwn_volunteer_skills', ['volunteer_id', 'skill_id'])

        # Adding model 'Skill'
        db.create_table('whwn_skill', (
            ('skill', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('whwn', ['Skill'])


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
        'whwn.conversation': {
            'Meta': {'object_name': 'Conversation'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'hashcode': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['whwn.Post']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "'dfgs'", 'max_length': '50'}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'through': "orm['whwn.Participant']", 'symmetrical': 'False'})
        },
        'whwn.conversationmessage': {
            'Meta': {'object_name': 'ConversationMessage'},
            'contents': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'conversation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'messages'", 'to': "orm['whwn.Conversation']"}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'flagged': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'read': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'received_via': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'sent_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True'})
        },
        'whwn.errormessage': {
            'Meta': {'object_name': 'ErrorMessage'},
            'contents': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'error_type': ('django.db.models.fields.IntegerField', [], {}),
            'flagged': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'read': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'received_via': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'response': ('django.db.models.fields.CharField', [], {'max_length': '160'}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'sent_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True'})
        },
        'whwn.location': {
            'Meta': {'object_name': 'Location'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            # 'point': ('django.contrib.gis.db.models.fields.PointField', [], {})
        },
        'whwn.messagereadby': {
            'Meta': {'object_name': 'MessageReadBy'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['whwn.ConversationMessage']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'whwn.messagesentvia': {
            'Meta': {'object_name': 'MessageSentVia'},
            'email': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['whwn.ConversationMessage']"}),
            'sms': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'web': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'whwn.notificationmessage': {
            'Meta': {'object_name': 'NotificationMessage'},
            'contents': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'flagged': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notify_type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'read': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'received_via': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'sent_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True'})
        },
        'whwn.participant': {
            'Meta': {'object_name': 'Participant'},
            'conversation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['whwn.Conversation']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'whwn.post': {
            'Meta': {'object_name': 'Post'},
            'amount': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'categories': ('django.db.models.fields.related.ForeignKey', [], {'default': '5', 'to': "orm['whwn.PostCategory']", 'null': 'True'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'expiration_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'is_needed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['whwn.Location']", 'null': 'True', 'on_delete': 'models.DO_NOTHING', 'blank': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'post_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'posted_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "'384u7zns'", 'max_length': '50'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'updated_date': ('django.db.models.fields.DateField', [], {'null': 'True'})
        },
        'whwn.postcategory': {
            'Meta': {'object_name': 'PostCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "'1wmx6r63'", 'max_length': '50'})
        },
        'whwn.region': {
            'Meta': {'object_name': 'Region'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'whwn.statusmessage': {
            'Meta': {'object_name': 'StatusMessage'},
            'contents': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'flagged': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'read': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'received_via': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'response': ('django.db.models.fields.CharField', [], {'max_length': '160'}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'sent_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True'}),
            'status_type': ('django.db.models.fields.IntegerField', [], {})
        },
        'whwn.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'communication_via': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'default_location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['whwn.Location']", 'null': 'True', 'blank': 'True'}),
            'email_verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'phone_verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['whwn']