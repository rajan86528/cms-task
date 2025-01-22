# CMS API

A RESTful API for a Content Management System built with Django REST Framework.

## Setup

1.  Clone the repository: `git clone https://github.com/rajan86528/cms-task.git`
2.  Navigate to the project directory: `cd cms_api`
3.  Create a virtual environment: `python -m venv venv`
4.  Activate the virtual environment: `source venv/bin/activate` (or `venv\Scripts\activate` on Windows)
5.  Install requirements: `pip install -r requirements.txt`
6.  Apply migrations: `python manage.py migrate`
7.  Create an admin user: `python manage.py seed_admin`
8.  Run the development server: `python manage.py runserver`

## API Endpoints

### User

*   `POST /users/register/`: Register a new author.
*   `POST /users/login/`:  Login with email and password and get token
*   `GET /users/admins/`: List admin users (admin only)

### Content (Author)

*   `GET /content/author/`: List content created by the author.
*   `POST /content/author/`: Create new content.
*   `GET /content/author/<int:pk>/`: View content by its id
*   `PUT /content/author/<int:pk>/`: Edit content by its id
*   `DELETE /content/author/<int:pk>/`: Delete content by its id

### Content (Admin)

*   `GET /content/admin/`: List all content (admin only).
*   `POST /content/admin/`: Create new content (admin only).
*   `GET /content/admin/<int:pk>/`: View content by its id (admin only)
*   `PUT /content/admin/<int:pk>/`: Edit content by its id (admin only)
*   `DELETE /content/admin/<int:pk>/`: Delete content by its id (admin only)

### Search

*   `GET /content/search/?q=<search_term>`: Search content by title, body, summary, and categories

## Notes

*   Authentication is based on JWT Tokens.
*   All endpoints require token for authorization.
*   Admin endpoints are available to admin users only.
*   Coverage files are included in the `coverage` folder.