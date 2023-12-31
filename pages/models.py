from django.db import models


class ContactModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    mesage = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "contact"
        verbose_name_plural = "contacts"


class BlogModel(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="blogs")
    short_description = models.TextField()
    long_description = models.TextField()
    author = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "blog"
        verbose_name_plural = "blogs"


class FeedbackModel(models.Model):
    feedback = models.TextField()
    name = models.CharField(max_length=255)
    job = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "feedback"
        verbose_name_plural = "feedbacks"


class EmailModel(models.Model):
    email = models.EmailField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "email"
        verbose_name_plural = "emails"
