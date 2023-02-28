from django.db import models

# Create your models here.
class Contact(models.Model):

    name = models.CharField(max_length=512)
    email = models.EmailField()
    subject = models.CharField(max_length=512)
    message = models.TextField()

    def __str__(self) -> str:
        return f"{self.name}"

class Company(models.Model):

    image = models.ImageField(upload_to="images/", default="images/company_default.jpg")
    name = models.CharField(max_length=512)
    email = models.EmailField()
    address = models.CharField(max_length=1024)
    phone = models.CharField(max_length=1024)
    website = models.URLField()
    description = models.TextField()

    def __str__(self) -> str:
        return f"{self.name}"

class Certificate(models.Model):

    image = models.ImageField(upload_to="images/", default="images/certificate.jpg")
    name = models.CharField(max_length=512)
    issuing_organization = models.CharField(max_length=1024)
    certificate_id = models.IntegerField()
    certificate_url = models.URLField()
    
    def __str__(self) -> str:
        return f"{self.name}"

class Post(models.Model):
    
    image = models.ImageField(upload_to="images/", default="images/post_default.jpg")
    title = models.CharField(max_length=512)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    certificate = models.ManyToManyField(Certificate,  related_name="certificates", null=True)

    def __str__(self) -> str:
        return f"{self.title}"