# Baraton Tribune

Baraton Tribune is a web application that provides a platform for users to share and discover news articles, blog posts, and other content.
It allows users to create accounts, submit articles, and interact with the community through comments and likes.
The application is built using Django, a high-level Python web framework, and is designed to be user-friendly and responsive.
It features a clean and modern design, making it easy for users to navigate and find the content they are interested in. 
The application also includes social media integration, allowing users to share articles on their favorite platforms. 
Overall, Baraton Tribune aims to be a go-to source for news and information, fostering a sense of community among its users. 




## How it Works




## Running Locally
Clone the repository to your local machine:
```bash
git clone <repository-url>
cd django-hello-world
# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
# Install dependencies
pip install -r requirements.txt
# Create a .env file and add your environment variables
touch .env
# Add your environment variables to the .env file
```
```bash
#Run migrations
python manage.py migrate
# then run the server
python manage.py runserver```

Your Django application is now available at `http://127.0.0.1:8000`.


