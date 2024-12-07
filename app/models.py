from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title

class Video(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='videos',
        null=True  # Bu yerda null=True qo'shilmoqda
    )
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='videos/', verbose_name='Video fayl')

    def __str__(self):
        return self.title
