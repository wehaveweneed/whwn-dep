# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'CommunicationMessage'
        db.delete_table('whwn_communicationmessage')

        # Deleting model 'Communication'
        db.delete_table('whwn_communication')

        # Adding model 'ConversationMessage'
        db.create_table('whwn_conversationmessage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sender', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('contents', self.gf('django.db.models.fields.CharField')(default='', max_length=160)),
            ('sent_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True)),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('flagged', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('read', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sent_via', self.gf('django.db.models.fields.IntegerField')(default=2)),
            ('conversation', self.gf('django.db.models.fields.related.ForeignKey')(related_name='messages', to=orm['whwn.Conversation'])),
        ))
        db.send_create_signal('whwn', ['ConversationMessage'])

        # Deleting field 'StatusMessage.message_text'
        db.delete_column('whwn_statusmessage', 'message_text')

        # Deleting field 'StatusMessage.type'
        db.delete_column('whwn_statusmessage', 'type')

        # Adding field 'StatusMessage.contents'
        db.add_column('whwn_statusmessage', 'contents',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=160),
                      keep_default=False)

        # Adding field 'StatusMessage.sent_via'
        db.add_column('whwn_statusmessage', 'sent_via',
                      self.gf('django.db.models.fields.IntegerField')(default=2),
                      keep_default=False)

        # Deleting field 'NotificationMessage.message_text'
        db.delete_column('whwn_notificationmessage', 'message_text')

        # Deleting field 'NotificationMessage.type'
        db.delete_column('whwn_notificationmessage', 'type')

        # Adding field 'NotificationMessage.contents'
        db.add_column('whwn_notificationmessage', 'contents',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=160),
                      keep_default=False)

        # Adding field 'NotificationMessage.sent_via'
        db.add_column('whwn_notificationmessage', 'sent_via',
                      self.gf('django.db.models.fields.IntegerField')(default=2),
                      keep_default=False)

        # Deleting field 'ErrorMessage.message_text'
        db.delete_column('whwn_errormessage', 'message_text')

        # Deleting field 'ErrorMessage.type'
        db.delete_column('whwn_errormessage', 'type')

        # Adding field 'ErrorMessage.contents'
        db.add_column('whwn_errormessage', 'contents',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=160),
                      keep_default=False)

        # Adding field 'ErrorMessage.sent_via'
        db.add_column('whwn_errormessage', 'sent_via',
                      self.gf('django.db.models.fields.IntegerField')(default=2),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'CommunicationMessage'
        db.create_table('whwn_communicationmessage', (
            ('read', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('communication', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['whwn.Communication'])),
            ('sent_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True)),
            ('send_type', self.gf('django.db.models.fields.IntegerField')()),
            ('sender', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('message_text', self.gf('django.db.models.fields.CharField')(max_length=160)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('receiver', self.gf('django.db.models.fields.related.ForeignKey')(related_name='message_receiver', to=orm['auth.User'])),
            ('type', self.gf('django.db.models.fields.IntegerField')()),
            ('flagged', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('whwn', ['CommunicationMessage'])

        # Adding model 'Communication'
        db.create_table('whwn_communication', (
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='owner', to=orm['auth.User'])),
            ('latest_message_on', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('requester', self.gf('django.db.models.fields.related.ForeignKey')(related_name='requester', to=orm['auth.User'])),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['whwn.Post'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hashcode', self.gf('django.db.models.fields.CharField')(max_length=32, null=True)),
        ))
        db.send_create_signal('whwn', ['Communication'])

        # Deleting model 'ConversationMessage'
        db.delete_table('whwn_conversationmessage')

        # Adding field 'StatusMessage.message_text'
        db.add_column('whwn_statusmessage', 'message_text',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=160),
                      keep_default=False)

        # Adding field 'StatusMessage.type'
        db.add_column('whwn_statusmessage', 'type',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'StatusMessage.contents'
        db.delete_column('whwn_statusmessage', 'contents')

        # Deleting field 'StatusMessage.sent_via'
        db.delete_column('whwn_statusmessage', 'sent_via')

        # Adding field 'NotificationMessage.message_text'
        db.add_column('whwn_notificationmessage', 'message_text',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=160),
                      keep_default=False)

        # Adding field 'NotificationMessage.type'
        db.add_column('whwn_notificationmessage', 'type',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'NotificationMessage.contents'
        db.delete_column('whwn_notificationmessage', 'contents')

        # Deleting field 'NotificationMessage.sent_via'
        db.delete_column('whwn_notificationmessage', 'sent_via')

        # Adding field 'ErrorMessage.message_text'
        db.add_column('whwn_errormessage', 'message_text',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=160),
                      keep_default=False)

        # Adding field 'ErrorMessage.type'
        db.add_column('whwn_errormessage', 'type',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'ErrorMessage.contents'
        db.delete_column('whwn_errormessage', 'contents')

        # Deleting field 'ErrorMessage.sent_via'
        db.delete_column('whwn_errormessage', 'sent_via')


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
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hashcode': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['whwn.Post']"}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'through': "orm['whwn.Participant']", 'symmetrical': 'False'})
        },
        'whwn.conversationmessage': {
            'Meta': {'object_name': 'ConversationMessage'},
            'contents': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '160'}),
            'conversation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'messages'", 'to': "orm['whwn.Conversation']"}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'flagged': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'read': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'sent_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True'}),
            'sent_via': ('django.db.models.fields.IntegerField', [], {'default': '2'})
        },
        'whwn.errormessage': {
            'Meta': {'object_name': 'ErrorMessage'},
            'contents': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '160'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'error_type': ('django.db.models.fields.IntegerField', [], {}),
            'flagged': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'read': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'response': ('django.db.models.fields.CharField', [], {'max_length': '160'}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'sent_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True'}),
            'sent_via': ('django.db.models.fields.IntegerField', [], {'default': '2'})
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
            'contents': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '160'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'flagged': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notify_type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'read': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'sent_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True'}),
            'sent_via': ('django.db.models.fields.IntegerField', [], {'default': '2'})
        },
        'whwn.participant': {
            'Meta': {'object_name': 'Participant'},
            'conversation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['whwn.Conversation']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
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
            'contents': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '160'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'flagged': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'read': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'response': ('django.db.models.fields.CharField', [], {'max_length': '160'}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'sent_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True'}),
            'sent_via': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'status_type': ('django.db.models.fields.IntegerField', [], {})
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