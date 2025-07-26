from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Book, Author

class Command(BaseCommand):
    help = 'Create user groups with appropriate permissions'

    def handle(self, *args, **options):
        # Get content types
        book_content_type = ContentType.objects.get_for_model(Book)
        author_content_type = ContentType.objects.get_for_model(Author)

        # Create or get groups
        editors, created = Group.objects.get_or_create(name='Editors')
        viewers, created = Group.objects.get_or_create(name='Viewers')
        admins, created = Group.objects.get_or_create(name='Admins')

        # Book permissions
        book_permissions = Permission.objects.filter(content_type=book_content_type)
        author_permissions = Permission.objects.filter(content_type=author_content_type)

        # Assign permissions to groups
        # Viewers - can only view
        viewers.permissions.set([
            Permission.objects.get(codename='view_book'),
            Permission.objects.get(codename='view_author'),
        ])

        # Editors - can add, change, view
        editor_perms = [
            Permission.objects.get(codename='view_book'),
            Permission.objects.get(codename='add_book'),
            Permission.objects.get(codename='change_book'),
            Permission.objects.get(codename='view_author'),
            Permission.objects.get(codename='add_author'),
            Permission.objects.get(codename='change_author'),
        ]
        editors.permissions.set(editor_perms)

        # Admins - all permissions
        all_perms = list(book_permissions) + list(author_permissions)
        admins.permissions.set(all_perms)

        self.stdout.write(
            self.style.SUCCESS('Successfully created groups and permissions')
        )
