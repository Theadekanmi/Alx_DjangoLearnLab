"""
Management command to set up groups and permissions.
Run with: python manage.py setup_groups
"""
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from accounts.models import Document


class Command(BaseCommand):
    help = 'Create groups and assign permissions'

    def handle(self, *args, **options):
        # Get the content type for Document model
        document_content_type = ContentType.objects.get_for_model(Document)
        
        # Get or create permissions
        can_view, created = Permission.objects.get_or_create(
            codename='can_view',
            name='Can view document',
            content_type=document_content_type,
        )
        
        can_create, created = Permission.objects.get_or_create(
            codename='can_create',
            name='Can create document',
            content_type=document_content_type,
        )
        
        can_edit, created = Permission.objects.get_or_create(
            codename='can_edit',
            name='Can edit document',
            content_type=document_content_type,
        )
        
        can_delete, created = Permission.objects.get_or_create(
            codename='can_delete',
            name='Can delete document',
            content_type=document_content_type,
        )
        
        # Create groups and assign permissions
        
        # Viewers group - can only view documents
        viewers_group, created = Group.objects.get_or_create(name='Viewers')
        viewers_group.permissions.set([can_view])
        
        # Editors group - can view, create, and edit documents
        editors_group, created = Group.objects.get_or_create(name='Editors')
        editors_group.permissions.set([can_view, can_create, can_edit])
        
        # Admins group - can do everything
        admins_group, created = Group.objects.get_or_create(name='Admins')
        admins_group.permissions.set([can_view, can_create, can_edit, can_delete])
        
        self.stdout.write(
            self.style.SUCCESS('Successfully created groups and permissions:')
        )
        self.stdout.write('- Viewers: can_view')
        self.stdout.write('- Editors: can_view, can_create, can_edit')
        self.stdout.write('- Admins: can_view, can_create, can_edit, can_delete')
