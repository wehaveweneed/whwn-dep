# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Conversation'
        db.delete_table('whwn_conversation')

        # Deleting model 'MessageSentVia'
        db.delete_table('whwn_messagesentvia')

        # Deleting model 'ConversationMessage'
        db.delete_table('whwn_conversationmessage')

        # Deleting model 'Participant'
        db.delete_table('whwn_participant')

        # Deleting model 'Location'
        db.delete_table('whwn_location')

        # Deleting model 'StatusMessage'
        db.delete_table('whwn_statusmessage')

        # Deleting model 'NotificationMessage'
        db.delete_table('whwn_notificationmessage')

        # Deleting model 'ErrorMessage'
        db.delete_table('whwn_errormessage')

        # Deleting model 'Region'
        db.delete_table('whwn_region')

        # Deleting model 'MessageReadBy'
        db.delete_table('whwn_messagereadby')

        # Adding model 'Message'
        db.create_table('whwn_message', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('contents', self.gf('django.db.models.fields.TextField')(default='')),
            ('flagged', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['whwn.Team'])),
        ))
        db.send_create_signal('whwn', ['Message'])

        # Adding model 'Item'
        db.create_table('whwn_item', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True)),
            # ('point', self.gf('django.contrib.gis.db.models.fields.PointField')(null=True, blank=True)),
            ('sku', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['whwn.ItemSKU'])),
            ('quantity', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('requested', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('possessor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
        ))
        db.send_create_signal('whwn', ['Item'])

        # Adding model 'ItemSKU'
        db.create_table('whwn_itemsku', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True)),
            ('upc', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['whwn.Team'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['whwn.ItemCategory'])),
        ))
        db.send_create_signal('whwn', ['ItemSKU'])

        # Adding unique constraint on 'ItemSKU', fields ['upc', 'team']
        db.create_unique('whwn_itemsku', ['upc', 'team_id'])

        # Deleting field 'Team.conversation'
        db.delete_column('whwn_team', 'conversation_id')

        # Deleting field 'Team.location'
        db.delete_column('whwn_team', 'location_id')

        # Adding field 'Team.created_at'
        db.add_column('whwn_team', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True),
                      keep_default=False)

        # Adding field 'Team.updated_at'
        db.add_column('whwn_team', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True),
                      keep_default=False)

        # Adding field 'Team.point'
        # db.add_column('whwn_team', 'point',
        #               self.gf('django.contrib.gis.db.models.fields.PointField')(null=True, blank=True),
        #               keep_default=False)


        # Changing field 'Team.primary_user'
        db.alter_column('whwn_team', 'primary_user_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['auth.User']))
        # Adding field 'ItemCategory.created_at'
        db.add_column('whwn_itemcategory', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True),
                      keep_default=False)

        # Adding field 'ItemCategory.updated_at'
        db.add_column('whwn_itemcategory', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True),
                      keep_default=False)

        # Deleting field 'UserProfile.location'
        db.delete_column('whwn_userprofile', 'location_id')

        # Deleting field 'UserProfile.communication_via'
        db.delete_column('whwn_userprofile', 'communication_via')

        # Adding field 'UserProfile.created_at'
        db.add_column('whwn_userprofile', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.updated_at'
        db.add_column('whwn_userprofile', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.point'
        # db.add_column('whwn_userprofile', 'point',
        #               self.gf('django.contrib.gis.db.models.fields.PointField')(null=True, blank=True),
        #               keep_default=False)


        # Changing field 'UserProfile.team'
        db.alter_column('whwn_userprofile', 'team_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['whwn.Team'], null=True))

    def backwards(self, orm):
        # Removing unique constraint on 'ItemSKU', fields ['upc', 'team']
        db.delete_unique('whwn_itemsku', ['upc', 'team_id'])

        # Adding model 'Conversation'
        db.create_table('whwn_conversation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('team', self.gf('django.db.models.fields.related.OneToOneField')(related_name='team', unique=True, to=orm['whwn.Team'])),
        ))
        db.send_create_signal('whwn', ['Conversation'])

        # Adding model 'MessageSentVia'
        db.create_table('whwn_messagesentvia', (
            ('web', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sms', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('message', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['whwn.ConversationMessage'])),
            ('email', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('whwn', ['MessageSentVia'])

        # Adding model 'ConversationMessage'
        db.create_table('whwn_conversationmessage', (
            ('conversation', self.gf('django.db.models.fields.related.ForeignKey')(related_name='messages', to=orm['whwn.Conversation'])),
            ('sent_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True)),
            ('sender', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('received_via', self.gf('django.db.models.fields.IntegerField')(default=2)),
            ('flagged', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('contents', self.gf('django.db.models.fields.TextField')(default='')),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('whwn', ['ConversationMessage'])

        # Adding model 'Participant'
        db.create_table('whwn_participant', (
            ('conversation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['whwn.Conversation'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('whwn', ['Participant'])

        # Adding model 'Location'
        db.create_table('whwn_location', (
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            # ('point', self.gf('django.contrib.gis.db.models.fields.PointField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal('whwn', ['Location'])

        # Adding model 'StatusMessage'
        db.create_table('whwn_statusmessage', (
            ('received_via', self.gf('django.db.models.fields.IntegerField')(default=2)),
            ('sent_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True)),
            ('sender', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('status_type', self.gf('django.db.models.fields.IntegerField')()),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('response', self.gf('django.db.models.fields.CharField')(max_length=160)),
            ('flagged', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('contents', self.gf('django.db.models.fields.TextField')(default='')),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('whwn', ['StatusMessage'])

        # Adding model 'NotificationMessage'
        db.create_table('whwn_notificationmessage', (
            ('received_via', self.gf('django.db.models.fields.IntegerField')(default=2)),
            ('sent_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True)),
            ('sender', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('notify_type', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('flagged', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('contents', self.gf('django.db.models.fields.TextField')(default='')),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('whwn', ['NotificationMessage'])

        # Adding model 'ErrorMessage'
        db.create_table('whwn_errormessage', (
            ('received_via', self.gf('django.db.models.fields.IntegerField')(default=2)),
            ('sent_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True)),
            ('sender', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('response', self.gf('django.db.models.fields.CharField')(max_length=160)),
            ('error_type', self.gf('django.db.models.fields.IntegerField')()),
            ('flagged', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('contents', self.gf('django.db.models.fields.TextField')(default='')),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('whwn', ['ErrorMessage'])

        # Adding model 'Region'
        db.create_table('whwn_region', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('whwn', ['Region'])

        # Adding model 'MessageReadBy'
        db.create_table('whwn_messagereadby', (
            ('message', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['whwn.ConversationMessage'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('whwn', ['MessageReadBy'])

        # Deleting model 'Message'
        db.delete_table('whwn_message')

        # Deleting model 'Item'
        db.delete_table('whwn_item')

        # Deleting model 'ItemSKU'
        db.delete_table('whwn_itemsku')

        # Adding field 'Team.conversation'
        db.add_column('whwn_team', 'conversation',
                      self.gf('django.db.models.fields.related.OneToOneField')(related_name='conversation', unique=True, null=True, to=orm['whwn.Conversation']),
                      keep_default=False)

        # Adding field 'Team.location'
        db.add_column('whwn_team', 'location',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['whwn.Location'], null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Team.created_at'
        db.delete_column('whwn_team', 'created_at')

        # Deleting field 'Team.updated_at'
        db.delete_column('whwn_team', 'updated_at')

        # Deleting field 'Team.point'
        # db.delete_column('whwn_team', 'point')


        # Changing field 'Team.primary_user'
        db.alter_column('whwn_team', 'primary_user_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['whwn.UserProfile']))
        # Deleting field 'ItemCategory.created_at'
        db.delete_column('whwn_itemcategory', 'created_at')

        # Deleting field 'ItemCategory.updated_at'
        db.delete_column('whwn_itemcategory', 'updated_at')

        # Adding field 'UserProfile.location'
        db.add_column('whwn_userprofile', 'location',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['whwn.Location'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.communication_via'
        db.add_column('whwn_userprofile', 'communication_via',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Deleting field 'UserProfile.created_at'
        db.delete_column('whwn_userprofile', 'created_at')

        # Deleting field 'UserProfile.updated_at'
        db.delete_column('whwn_userprofile', 'updated_at')

        # Deleting field 'UserProfile.point'
        # db.delete_column('whwn_userprofile', 'point')


        # Changing field 'UserProfile.team'
        db.alter_column('whwn_userprofile', 'team_id', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['whwn.Team']))

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
            # 'point': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            # 'point': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'primary_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'primary_user'", 'null': 'True', 'to': "orm['auth.User']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        'whwn.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'email_verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'phone_verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            # 'point': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['whwn.Team']", 'null': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['whwn']