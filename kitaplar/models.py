from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models import User 
# Create your models here.
class Kitap(models.Model):
    isim = models.CharField(max_length=150)
    yazar = models.CharField(max_length=150)
    aciklama = models.TextField(max_length=150,null=True,blank=True)
    yaratilma_tarihi = models.DateTimeField(auto_now_add=True) # bir kerelik gelecek biz değiştirmicez o yüzden otomatik yapsın kendisi
    güncellenme_tarihi = models.DateField(auto_now_add=True)
    yayın_tarihi = models.DateTimeField()

    def __str__(self):
        return f'{self.isim} - {self.yazar}'

class Yorum(models.Model):
    kitap= models.ForeignKey(Kitap,on_delete=models.CASCADE,related_name='yorumlar')
    # yorum_sahibi = models.CharField(max_length=255)
    yorum_sahibi= models.ForeignKey(User,on_delete=models.CASCADE,related_name='kullanici_yorumlari')
    yorum = models.TextField(blank=True,null=True)
    yaratilma_tarihi = models.DateTimeField(auto_now_add=True) # bir kerelik gelecek biz değiştirmicez o yüzden otomatik yapsın kendisi
    güncellenme_tarihi = models.DateField(auto_now_add=True)

    degerlendirme = models.PositiveIntegerField(
        validators= [MinValueValidator(1),MaxValueValidator(5)],
    )

    def __str__(self):
        return str(self.degerlendirme)
