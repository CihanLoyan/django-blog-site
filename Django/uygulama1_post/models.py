from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

class yazi(models.Model):
    baslik = models.CharField(max_length=120)
    metin = RichTextField()
    yayinTarihi = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)
    slug = models.SlugField(unique=True, editable=False, max_length=130)

    def __str__(self):
        return self.baslik
    
    def get_unique_slug(self):
        slug = slugify(self.baslik)
        unique_slug = slug
        counter = 1

        while yazi.objects.filter(slug=unique_slug).exists():
            unique_slug = slug + "-" + str(counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()

        return super(yazi, self).save(*args, **kwargs)

class Yorum(models.Model):
    yazi = models.ForeignKey(yazi, on_delete=models.CASCADE, related_name="yorumlar")
    metin = models.TextField()
    yayinTarihi = models.DateTimeField(auto_now_add=True)
# Create your models here.
