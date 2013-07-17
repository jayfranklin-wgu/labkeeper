# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'ConsoleServer', fields ['fqdn', 'lab']
        db.delete_unique(u'labs_consoleserver', ['fqdn', 'lab_id'])

        # Removing unique constraint on 'ConsoleServer', fields ['name', 'lab']
        db.delete_unique(u'labs_consoleserver', ['name', 'lab_id'])


        # Changing field 'ConsoleServer.fqdn'
        db.alter_column(u'labs_consoleserver', 'fqdn', self.gf('django.db.models.fields.CharField')(max_length=50, unique=True, null=True))

        # Changing field 'ConsoleServer.ip4_address'
        db.alter_column(u'labs_consoleserver', 'ip4_address', self.gf('django.db.models.fields.GenericIPAddressField')(max_length=39, unique=True, null=True))
        # Adding unique constraint on 'ConsoleServer', fields ['ip4_address']
        db.create_unique(u'labs_consoleserver', ['ip4_address'])


    def backwards(self, orm):
        # Removing unique constraint on 'ConsoleServer', fields ['ip4_address']
        db.delete_unique(u'labs_consoleserver', ['ip4_address'])


        # Changing field 'ConsoleServer.fqdn'
        db.alter_column(u'labs_consoleserver', 'fqdn', self.gf('django.db.models.fields.CharField')(default='', max_length=50, unique=True))

        # User chose to not deal with backwards NULL issues for 'ConsoleServer.ip4_address'
        raise RuntimeError("Cannot reverse this migration. 'ConsoleServer.ip4_address' and its values cannot be restored.")
        # Adding unique constraint on 'ConsoleServer', fields ['name', 'lab']
        db.create_unique(u'labs_consoleserver', ['name', 'lab_id'])

        # Adding unique constraint on 'ConsoleServer', fields ['fqdn', 'lab']
        db.create_unique(u'labs_consoleserver', ['fqdn', 'lab_id'])


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'labs.consoleserver': {
            'Meta': {'unique_together': "(('lab', 'ip4_address'),)", 'object_name': 'ConsoleServer'},
            'fqdn': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip4_address': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'lab': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'consoleservers'", 'to': u"orm['labs.Lab']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'secret': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'})
        },
        u'labs.consoleserverport': {
            'Meta': {'unique_together': "(('consoleserver', 'number'), ('consoleserver', 'telnet_port'), ('consoleserver', 'ssh_port'))", 'object_name': 'ConsoleServerPort'},
            'consoleserver': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ports'", 'to': u"orm['labs.ConsoleServer']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'ssh_port': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'telnet_port': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'labs.device': {
            'Meta': {'ordering': "['name']", 'unique_together': "(('pod', 'name'), ('pod', 'slug'))", 'object_name': 'Device'},
            'cs_port': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'device'", 'unique': 'True', 'to': u"orm['labs.ConsoleServerPort']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'pod': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'devices'", 'to': u"orm['labs.Pod']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '30'}),
            'type': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        u'labs.lab': {
            'Meta': {'object_name': 'Lab'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_edited': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'last_edited_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'profile': ('django_bleach.models.BleachField', [], {})
        },
        u'labs.membership': {
            'Meta': {'unique_together': "(('user', 'lab'),)", 'object_name': 'Membership'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'joined': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'lab': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'memberships'", 'to': u"orm['labs.Lab']"}),
            'role': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'memberships'", 'to': u"orm['auth.User']"})
        },
        u'labs.pod': {
            'Meta': {'ordering': "['name']", 'unique_together': "(('lab', 'name'),)", 'object_name': 'Pod'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lab': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pods'", 'to': u"orm['labs.Lab']"}),
            'max_reservation': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '6'}),
            'min_reservation': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '2'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['labs']