# Advanced Features & Security Django Project

This project demonstrates the implementation of a custom user model, a robust permissions and groups system, and various security best practices in Django.

## Project Structure

\`\`\`
advanced_features_and_security/
├── manage.py
├── advanced_features_and_security/       # Project settings folder
│   ├── settings.py                       # Main settings, including security configs
│   ├── urls.py                           # Main URL configurations
│   └── ...
└── accounts/                             # Custom User and Document App
    ├── models.py                         # CustomUser and Document models with custom permissions
    ├── admin.py                          # Custom admin interfaces for CustomUser and Document
    ├── forms.py                          # Forms for user registration and document management
    ├── views.py                          # Views with permission checks and secure data handling
    ├── urls.py                           # App-specific URL patterns
    └── templates/accounts/               # HTML templates for user and document interfaces
        ├── base.html
        ├── profile.html
        ├── register.html
        ├── document_list.html
        ├── document_detail.html
        ├── document_form.html
        ├── document_confirm_delete.html
        └── permission_denied.html
\`\`\`

## Setup and Installation

1.  **Clone the repository:**
    \`\`\`bash
    git clone https://github.com/Alx_DjangoLearnLab/advanced_features_and_security.git
    cd advanced_features_and_security
    \`\`\`
2.  **Create a virtual environment (recommended):**
    \`\`\`bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    \`\`\`
3.  **Install dependencies:**
    \`\`\`bash
    pip install Django Pillow django-csp
    \`\`\`
4.  **Run database migrations:**
    \`\`\`bash
    python manage.py makemigrations accounts
    python manage.py migrate
    \`\`\`
5.  **Set up groups and permissions:**
    \`\`\`bash
    python manage.py setup_groups
    \`\`\`
6.  **Create a superuser:**
    \`\`\`bash
    python manage.py createsuperuser
    \`\`\`
7.  **Run the development server:**
    \`\`\`bash
    python manage.py runserver
    \`\`\`

## Security Best Practices Implemented

This project incorporates the following security measures:

### 1. Secure Settings (`settings.py`)
-   `DEBUG = False` (for production): Prevents sensitive information leakage.
-   `SECURE_BROWSER_XSS_FILTER = True`: Activates browser's XSS filter.
-   `X_FRAME_OPTIONS = 'DENY'`: Prevents clickjacking attacks by disallowing embedding in iframes.
-   `SECURE_CONTENT_TYPE_NOSNIFF = True`: Prevents MIME-sniffing vulnerabilities.
-   `CSRF_COOKIE_SECURE = True` & `SESSION_COOKIE_SECURE = True`: Ensures session and CSRF cookies are only sent over HTTPS.
-   `CSRF_COOKIE_HTTPONLY = True` & `SESSION_COOKIE_HTTPONLY = True`: Prevents client-side JavaScript from accessing cookies, mitigating XSS.
-   `SECURE_SSL_REDIRECT = True`, `SECURE_HSTS_SECONDS`, `SECURE_HSTS_INCLUDE_SUBDOMAINS`, `SECURE_HSTS_PRELOAD`: Configures HTTP Strict Transport Security (HSTS) to enforce HTTPS.

### 2. CSRF Protection (`templates`)
-   All forms include `{% csrf_token %}` to protect against Cross-Site Request Forgery attacks.

### 3. Secure Data Access (`views.py`)
-   **SQL Injection Prevention**: All database interactions use Django's ORM, which automatically parameterizes queries, preventing SQL injection.
-   **Input Validation & Sanitization**: User inputs are handled via Django Forms (`form.is_valid()`), ensuring data is validated and sanitized before processing or saving to the database.

### 4. Content Security Policy (CSP)
-   Implemented using `django-csp` middleware.
-   `CSP_DEFAULT_SRC`, `CSP_SCRIPT_SRC`, `CSP_STYLE_SRC`, `CSP_IMG_SRC`, etc., are configured in `settings.py` to restrict content sources, significantly reducing XSS attack vectors.

## Testing Security Measures

### Manual Testing:

1.  **CSRF Protection**:
    *   Try to submit a form (e.g., create a document) after removing the `{% csrf_token %}` line from the template. It should result in a "CSRF verification failed" error.
2.  **XSS Protection (Basic)**:
    *   Try entering `<script>alert('XSS');</script>` into a text field (e.g., document content). The script should not execute when the content is displayed. Django's template engine escapes HTML by default.
3.  **X-Frame-Options**:
    *   Attempt to embed your site in an iframe on a different domain (e.g., create a simple HTML file on your local machine with `<iframe src="http://127.0.0.1:8000/"></iframe>`). The browser should block it.
4.  **CSP**:
    *   Open your browser's developer tools (F12) and go to the "Network" tab. Load a page. Check the response headers for `Content-Security-Policy`.
    *   If you try to load an external script or image not allowed by your CSP, you should see errors in the browser console.
5.  **SQL Injection**:
    *   Since ORM is used, direct SQL injection attempts through form fields should fail gracefully (e.g., `'; DROP TABLE users; --`). Django's ORM handles this.

This comprehensive setup significantly enhances the security posture of your Django application.
