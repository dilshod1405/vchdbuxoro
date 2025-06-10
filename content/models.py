from django.db import models

class Information(models.Model):
    title_uz = models.CharField(max_length=255, verbose_name='Sarlavha')
    title_ru = models.CharField(max_length=255, verbose_name='Sarlavha')
    content_uz = models.TextField(verbose_name='Matn')
    content_ru = models.TextField(verbose_name='Matn')
    photo = models.ImageField(upload_to='photos/', blank=True, null=True, verbose_name='Rasm')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqt')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Yangilangan vaqt')

    class Meta:
        verbose_name = 'Yangilik'
        verbose_name_plural = 'Yangiliklar'

    def __str__(self):
        return self.title



class Service(models.Model):
    title_uz = models.CharField(max_length=255, verbose_name='Sarlavha')
    title_ru = models.CharField(max_length=255, verbose_name='Sarlavha')
    description_uz = models.TextField(verbose_name='Tavsif', blank=True, null=True)
    description_ru = models.TextField(verbose_name='Tavsif', blank=True, null=True)
    picture = models.ImageField(upload_to='services/', blank=True, null=True, verbose_name='Rasm')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqt')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Yangilangan vaqt')

    class Meta:
        verbose_name = 'Xizmat'
        verbose_name_plural = 'Xizmatlar'

    def __str__(self):
        return self.title


class Message(models.Model):
    name = models.CharField(max_length=255, verbose_name='Ism')
    phone = models.CharField(max_length=9, verbose_name='Telefon raqami')
    message = models.TextField(verbose_name='Xabar')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqt')

    class Meta:
        verbose_name = 'Xabar'
        verbose_name_plural = 'Xabarlar'

    def __str__(self):
        return f"{self.name} - {self.phone}"