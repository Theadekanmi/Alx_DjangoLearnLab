from .models import Notification
from django.contrib.contenttypes.models import ContentType


def create_notification(recipient, actor, verb, notification_type, target=None):
    """
    Create a notification for a user.
    
    Args:
        recipient: User receiving the notification
        actor: User performing the action
        verb: Description of the action
        notification_type: Type of notification (follow, like, comment, mention)
        target: Optional object related to the notification
    """
    target_content_type = None
    target_object_id = None
    
    if target:
        target_content_type = ContentType.objects.get_for_model(target)
        target_object_id = target.id
    
    notification = Notification.objects.create(
        recipient=recipient,
        actor=actor,
        verb=verb,
        notification_type=notification_type,
        target_content_type=target_content_type,
        target_object_id=target_object_id
    )
    
    return notification


def create_follow_notification(follower, followed_user):
    """Create notification when someone follows a user."""
    verb = f"started following you"
    return create_notification(
        recipient=followed_user,
        actor=follower,
        verb=verb,
        notification_type='follow'
    )


def create_like_notification(liker, post):
    """Create notification when someone likes a post."""
    verb = f"liked your post '{post.title}'"
    return create_notification(
        recipient=post.author,
        actor=liker,
        verb=verb,
        notification_type='like',
        target=post
    )


def create_comment_notification(commenter, comment, post):
    """Create notification when someone comments on a post."""
    verb = f"commented on your post '{post.title}'"
    return create_notification(
        recipient=post.author,
        actor=commenter,
        verb=verb,
        notification_type='comment',
        target=comment
    )