# BlogLite Web Application

This is the initial setup for the **BlogLite** web application project.

## Project Overview
BlogLite is a web application that allows users to:
- Create posts
- Like, comment, and interact with posts
- Follow and unfollow other users
- Access RESTful APIs for engagement data

This application is built using the following technologies:
- **Flask**: For building the web application
- **SQLite**: For database management
- **Flask-SQLAlchemy**: For ORM and database operations
- **Flask-RESTful**: For building REST APIs
- **Flask-Login**: For user authentication and authorization
- **Werkzeug**: For password hashing

## Current Status
The project is in its **initial phase**, with the following setup completed:
1. Folder structure created.
2. Basic `.gitignore` file added to exclude unnecessary files.
3. README created with project overview and setup details.


## Database Schema Design

The database used in this project is a SQLite database. The following tables were created:

- Users: Stores information about users, including their name, email, and password hash.
- Posts: Stores information about posts, including the text of the post and the user who created it.
- Comments: Stores information about comments, including the text of the comment and the user who created it.
- Likes: Stores information about likes, including the user who liked the post and the post that was liked.
- Followers: Stores information about followers, including the user who is following and the user who is being followed.

The relationships between these tables are as follows:

- Users has many Posts, Comments, and Likes
- Posts has many Comments and Likes
- Comments has many Likes
- Followers has many Users


