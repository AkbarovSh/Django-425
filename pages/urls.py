from django.urls import path
from pages.views import *
from products.views import products_page_view

app_name = "pages"

urlpatterns = [
    path("blogs/", blog_page_view, name="blogs"),
    path("contact/", contact_page_view, name="contact"),
    path("about/", about_page_view, name="about"),
    path("email/", email_post, name="email"),
    path("", home_page_view, name="home")
]
