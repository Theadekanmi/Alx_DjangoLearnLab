# Social Media API

A robust Social Media API built with Django and Django REST Framework (DRF) that provides comprehensive social media functionality including user authentication, posts, comments, likes, follows, and notifications.

## Features

### User Management
- **Custom User Model**: Extended Django's AbstractUser with bio, profile picture, and follow relationships
- **Authentication**: Token-based authentication using DRF's TokenAuthentication
- **User Registration & Login**: Secure user registration and login endpoints
- **Profile Management**: Update user profiles and view user information
- **Follow System**: Users can follow/unfollow other users

### Posts & Comments
- **Post Management**: Create, read, update, and delete posts
- **Comment System**: Add comments to posts with full CRUD operations
- **Like System**: Like and unlike posts
- **Search & Filtering**: Search posts by title or content
- **Pagination**: Built-in pagination for large datasets

### Social Features
- **User Feed**: View posts from followed users
- **User Posts**: View all posts from a specific user
- **Follow Relationships**: Manage following/follower relationships

### Notifications
- **Real-time Notifications**: Get notified for follows, likes, and comments
- **Notification Types**: Support for different notification types
- **Read/Unread Status**: Track notification read status
- **Bulk Operations**: Mark all notifications as read

## API Endpoints

### Authentication
- `POST /api/accounts/register/` - User registration
- `POST /api/accounts/login/` - User login
- `GET /api/accounts/profile/` - Get current user profile
- `PUT /api/accounts/profile/` - Update current user profile

### User Management
- `GET /api/accounts/users/` - List all users
- `GET /api/accounts/users/{id}/` - Get specific user details
- `POST /api/accounts/follow/{user_id}/` - Follow a user
- `POST /api/accounts/unfollow/{user_id}/` - Unfollow a user

### Posts
- `GET /api/posts/` - List all posts (with pagination)
- `POST /api/posts/` - Create a new post
- `GET /api/posts/{id}/` - Get specific post details
- `PUT /api/posts/{id}/` - Update a post
- `DELETE /api/posts/{id}/` - Delete a post
- `POST /api/posts/{id}/like/` - Like a post
- `POST /api/posts/{id}/unlike/` - Unlike a post

### Comments
- `GET /api/posts/{post_id}/comments/` - List comments for a post
- `POST /api/posts/{post_id}/comments/` - Add comment to a post
- `GET /api/posts/{post_id}/comments/{id}/` - Get specific comment
- `PUT /api/posts/{post_id}/comments/{id}/` - Update a comment
- `DELETE /api/posts/{post_id}/comments/{id}/` - Delete a comment

### Feed & User Posts
- `GET /api/feed/` - Get posts from followed users
- `GET /api/users/{user_id}/posts/` - Get posts from a specific user

### Notifications
- `GET /api/notifications/` - List user notifications
- `GET /api/notifications/{id}/` - Get specific notification
- `POST /api/notifications/{id}/read/` - Mark notification as read
- `POST /api/notifications/mark-all-read/` - Mark all notifications as read
- `GET /api/notifications/unread-count/` - Get unread notifications count

## Installation & Setup

### Prerequisites
- Python 3.8+
- Django 4.2+
- Django REST Framework 3.15+

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd social_media_api
   ```

2. **Install dependencies**
   ```bash
   pip install django djangorestframework
   ```

3. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

## Usage Examples

### User Registration
```bash
curl -X POST http://localhost:8000/api/accounts/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "securepassword123",
    "password_confirm": "securepassword123",
    "bio": "Hello, I am John!"
  }'
```

### User Login
```bash
curl -X POST http://localhost:8000/api/accounts/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "password": "securepassword123"
  }'
```

### Create a Post
```bash
curl -X POST http://localhost:8000/api/posts/ \
  -H "Authorization: Token YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My First Post",
    "content": "This is the content of my first post!"
  }'
```

### Follow a User
```bash
curl -X POST http://localhost:8000/api/accounts/follow/2/ \
  -H "Authorization: Token YOUR_TOKEN_HERE"
```

### Like a Post
```bash
curl -X POST http://localhost:8000/api/posts/1/like/ \
  -H "Authorization: Token YOUR_TOKEN_HERE"
```

## Project Structure

```
social_media_api/
├── accounts/                 # User management app
│   ├── models.py            # Custom user model
│   ├── serializers.py       # User serializers
│   ├── views.py             # User views
│   └── urls.py              # User URL patterns
├── posts/                    # Posts and comments app
│   ├── models.py            # Post, Comment, Like models
│   ├── serializers.py       # Post serializers
│   ├── views.py             # Post views
│   └── urls.py              # Post URL patterns
├── notifications/            # Notifications app
│   ├── models.py            # Notification model
│   ├── serializers.py       # Notification serializers
│   ├── views.py             # Notification views
│   ├── utils.py             # Notification utilities
│   └── urls.py              # Notification URL patterns
├── social_media_api/         # Main project settings
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL configuration
│   └── wsgi.py              # WSGI configuration
└── manage.py                 # Django management script
```

## Security Features

- **Token Authentication**: Secure API access using DRF tokens
- **Permission Classes**: Proper permission checks for all endpoints
- **User Validation**: Users can only modify their own content
- **Input Validation**: Comprehensive serializer validation
- **CSRF Protection**: Built-in Django CSRF protection

## Testing

The API can be tested using tools like:
- **Postman**: For manual API testing
- **cURL**: For command-line testing
- **Django Test Framework**: For automated testing

## Deployment

### Production Settings
- Set `DEBUG = False`
- Configure `ALLOWED_HOSTS`
- Use production database (PostgreSQL recommended)
- Set up static file serving
- Configure HTTPS

### Recommended Hosting
- **Heroku**: Easy deployment with Git integration
- **AWS**: Scalable cloud hosting
- **DigitalOcean**: VPS hosting with Django support

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For support and questions, please open an issue in the repository or contact the development team.