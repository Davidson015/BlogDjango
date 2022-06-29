from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):

  name = models.CharField(max_length=50)
  slug = models.SlugField(max_length=100, unique=True, blank=True)

  class Meta:
    verbose_name = ("Category")
    verbose_name_plural = ("Categories")

  def __str__(self):
    return self.name

  def save(self, *args, **kwargs):
    slug = self.name
    self.slug = slugify(slug, allow_unicode=True)
    super().save(*args, **kwargs)

  def get_absolute_url(self):
    return reverse("Category_detail", kwargs={"pk": self.pk})


class Blog(models.Model):

  title = models.CharField(max_length=500)
  content = models.TextField()
  image = models.ImageField(upload_to="BlogImages/")
  author = models.CharField(max_length=150)
  category = models.ForeignKey("Category", on_delete=models.CASCADE)
  slug = models.SlugField(max_length=500, unique=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name = ("Blog")
    verbose_name_plural = ("Blogs")

  def __str__(self):
    return self.title

  def save(self, *args, **kwargs):
    slug = self.title
    self.slug = slugify(slug, allow_unicode=True)
    super().save(*args, **kwargs)

  def get_absolute_url(self):
    return reverse("Blog_detail", kwargs={"pk": self.pk})

class Comment(models.Model):

  post = models.ForeignKey(Blog, on_delete=models.CASCADE)
  full_name = models.CharField(max_length=100)
  phone_number = models.CharField(max_length=50)
  email = models.EmailField(max_length=254)
  comment = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name = ("Comment")
    verbose_name_plural = ("Comments")

  def __str__(self):
    return f"{self.full_name} - {self.phone_number}"

  def get_absolute_url(self):
    return reverse("Comment_detail", kwargs={"pk": self.pk})
