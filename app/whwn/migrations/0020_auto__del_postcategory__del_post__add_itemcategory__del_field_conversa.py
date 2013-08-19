# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'PostCategory'
        db.delete_table('whwn_postcategory')

        # Deleting model 'Post'
        db.delete_table('whwn_post')

        # Adding model 'ItemCategory'
        db.create_table('whwn_itemcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal('whwn', ['ItemCategory'])

        # Deleting field 'Conversation.slug'
        db.delete_column('whwn_conversation', 'slug')

        # Deleting field 'Conversation.active'
        db.delete_column('whwn_conversation', 'active')

        # Deleting field 'Conversation.post'
        db.delete_column('whwn_conversation', 'post_id')

        # Deleting field 'Conversation.hashcode'
        db.delete_column('whwn_conversation', 'hashcode')

        # Adding field 'Conversation.team'
        db.add_column('whwn_conversation', 'team',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=None, related_name='team', unique=True, to=orm['whwn.Team']),
                      keep_default=False)

        # Deleting field 'ConversationMessage.read'
        db.delete_column('whwn_conversationmessage', 'read')

        # Deleting field 'StatusMessage.read'
        db.delete_column('whwn_statusmessage', 'read')

        # Deleting field 'NotificationMessage.read'
        db.delete_column('whwn_notificationmessage', 'read')

        # Deleting field 'ErrorMessage.read'
        db.delete_column('whwn_errormessage', 'read')


    def backwards(self, orm):
        # Adding model 'PostCategory'
        db.create_table('whwn_postcategory', (
            ('slug', self.gf('django.db.models.fields.SlugField')(default='jyb9kfet', max_length=50)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal('whwn', ['PostCategory'])

        # Adding model 'Post'
        db.create_table('whwn_post', (
            ('status', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('updated_date', self.gf('django.db.models.fields.DateField')(null=True)),
            ('posted_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime.now)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('post_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_needed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('slug', self.gf('django.db.models.fields.SlugField')(default='4ue9tzbo', max_length=50)),
            ('categories', self.gf('django.db.models.fields.related.ForeignKey')(default=5, to=orm['whwn.PostCategory'], null=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('expiration_date', self.gf('django.db.models.fields.DateField')(null=True)),
            ('amount', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['whwn.Location'], null=True, on_delete=models.DO_NOTHING, blank=True)),
        ))
        db.send_create_signal('whwn', ['Post'])

        # Deleting model 'ItemCategory'
        db.delete_table('whwn_itemcategory')

        # Adding field 'Conversation.slug'
        db.add_column('whwn_conversation', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='2m5w', max_length=50),
                      keep_default=False)

        # Adding field 'Conversation.active'
        db.add_column('whwn_conversation', 'active',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Conversation.post'
        raise RuntimeError("Cannot reverse this migration. 'Conversation.post' and its values cannot be restored.")
        # Adding field 'Conversation.hashcode'
        db.add_column('whwn_conversation', 'hashcode',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True),
                      keep_default=False)

        # Deleting field 'Conversation.team'
        db.delete_column('whwn_conversation', 'team_id')

        # Adding field 'ConversationMessage.read'
        db.add_column('whwn_conversationmessage', 'read',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'StatusMessage.read'
        db.add_column('whwn_statusmessage', 'read',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'NotificationMessage.read'
        db.add_column('whwn_notificationmessage', 'read',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'ErrorMessage.read'
        db.add_column('whwn_errormessage', 'read',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'team': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'team'", 'unique': 'True', 'to': "orm['whwn.Team']"})
        },
        'whwn.conversationmessage': {
            'Meta': {'object_name': 'ConversationMessage'},
            'contents': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'conversation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'messages'", 'to': "orm['whwn.Conversation']"}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'flagged': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            'received_via': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'response': ('django.db.models.fields.CharField', [], {'max_length': '160'}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'sent_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True'})
        },
        'whwn.itemcategory': {
            'Meta': {'object_name': 'ItemCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
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
            'received_via': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'response': ('django.db.models.fields.CharField', [], {'max_length': '160'}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'sent_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True'}),
            'status_type': ('django.db.models.fields.IntegerField', [], {})
        },
        'whwn.team': {
            'Meta': {'object_name': 'Team'},
            'conversation': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'conversation'", 'unique': 'True', 'to': "orm['whwn.Conversation']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['whwn.Location']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'primary_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'primary_user'", 'to': "orm['whwn.UserProfile']"}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['whwn.UserProfile']", 'symmetrical': 'False'})
        },
        'whwn.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'communication_via': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'email_verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['whwn.Location']", 'null': 'True', 'blank': 'True'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'phone_verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'teams': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['whwn.Team']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['whwn']