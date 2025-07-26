"""
Django management command to set up groups and permissions

Run this command after migrations to create the necessary groups:
python manage.py setup_groups
"""

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Book

class Command(BaseCommand):
    help = 'Create groups and assign permissions for the bookshelf app'

    def handle(self, *args, **options):
        # Get content type for Book model
        book_content_type = ContentType.objects.get_for_model(Book)
        
        # Get or create custom permissions
        can_view, created = Permission.objects.get_or_create(
            codename='can_view',
            name='Can view book',
            content_type=book_content_type,
        )
        
        can_create, created = Permission.objects.get_or_create(
            codename='can_create',
            name='Can create book', 
            content_type=book_content_type,
        )
        
        can_edit, created = Permission.objects.get_or_create(
            codename='can_edit',
            name='Can edit book',
            content_type=book_content_type,
        )
        
        can_delete, created = Permission.objects.get_or_create(
            codename='can_delete',
            name='Can delete book',
            content_type=book_content_type,
        )

        # Create groups and assign permissions
        
        # Viewers group - can only view books
        viewers_group, created = Group.objects.get_or_create(name='Viewers')
        viewers_group.permissions.set([can_view])
        if created:
            self.stdout.write(
                self.style.SUCCESS('Created "Viewers" group with view permissions')
            )
        
        # Editors group - can view, create, and edit books
        editors_group, created = Group.objects.get_or_create(name='Editors') 
        editors_group.permissions.set([can_view, can_create, can_edit])
        if created:
            self.stdout.write(
                self.style.SUCCESS('Created "Editors" group with view, create, edit permissions')
            )
        
        # Admins group - can do everything
        admins_group, created = Group.objects.get_or_create(name='Admins')
        admins_group.permissions.set([can_view, can_create, can_edit, can_delete])
        if created:
            self.stdout.write(
                self.style.SUCCESS('Created "Admins" group with all permissions')
            )
        
        self.stdout.write(
            self.style.SUCCESS('Successfully configured groups and permissions!')
        )
        
        # Display summary
        self.stdout.write('\nGroups and their permissions:')
        for group in Group.objects.filter(name__in=['Viewers', 'Editors', 'Admins']):
            perms = [p.codename for p in group.permissions.all()]
            self.stdout.write(f'  {group.name}: {", ".join(perms)}')