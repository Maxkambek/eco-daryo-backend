from django.db import models


class Slider(models.Model):
    title = models.TextField()
    content = models.TextField()
    background_image = models.ImageField(upload_to='sliders/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Slayder'
        verbose_name_plural = 'Slayderlar'
        ordering = ['-id']


class News(models.Model):
    title = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to='news/')
    created_at = models.DateTimeField(auto_now_add=True)
    image_main = models.ImageField(upload_to='news/', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Yangilik'
        verbose_name_plural = 'Yangiliklar'
        ordering = ['-id']


class Video(models.Model):
    title = models.TextField()
    video_file = models.FileField(upload_to='videos/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videolar'
        ordering = ['-id']


class Links(models.Model):
    name = models.CharField(max_length=222)
    logo = models.ImageField(upload_to='links/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Foydali havola'
        verbose_name_plural = 'Foydali havolalar'


class Leaders(models.Model):
    name = models.CharField(max_length=222)
    image = models.ImageField(upload_to='leaders/')
    created_at = models.DateTimeField(auto_now_add=True)
    position = models.CharField(max_length=222, verbose_name="Lavozimi")
    phone = models.CharField(max_length=222)
    email = models.CharField(max_length=222)
    work_time = models.CharField(max_length=222, verbose_name="Ish vaqti")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Rahbariyat'
        verbose_name_plural = 'Rahbariyat'


class RegionUnit(models.Model):
    name = models.CharField(max_length=222)
    image = models.ImageField(upload_to='region_units/')
    created_at = models.DateTimeField(auto_now_add=True)
    position = models.CharField(max_length=222, verbose_name="Lavozimi")
    phone = models.CharField(max_length=222)
    email = models.CharField(max_length=222)
    work_time = models.CharField(max_length=222, verbose_name="Ish vaqti")
    date_birth = models.CharField(max_length=222, verbose_name="Tug'ilgan vaqti")
    place_birth = models.CharField(max_length=222, verbose_name="Tug'ilgan joyi")
    specialty = models.CharField(max_length=222, verbose_name="Mutaxasisligi")
    nationality = models.CharField(max_length=222, verbose_name="Millati")
    party = models.CharField(max_length=222, verbose_name="Partiyaviyligi")
    malumoti = models.CharField(max_length=222, verbose_name="Ma'lumoti")
    tamomlagan = models.CharField(max_length=222, verbose_name="Tamomlagan")
    ilmiy_daraja = models.CharField(max_length=222, verbose_name="Ilmiy Darajasi")
    ilmiy_unvon = models.CharField(max_length=222, verbose_name="Ilmiy unvoni")
    language = models.CharField(max_length=222, verbose_name="Qaysi chet tillarini bilishi?")
    davlat_mukofoti = models.CharField(max_length=222, verbose_name="Davlar mukofotlari?")
    xald_deputatlari = models.CharField(max_length=222, verbose_name="Xald deputatlari, organlar a'zosimi?")

    def __str__(self):
        return self.name


class LegalDocs(models.Model):
    name = models.CharField(max_length=222)
    link = models.URLField(max_length=222)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Huquqiy Hujjat'
        verbose_name_plural = 'Huquqiy Hujjatlar'
