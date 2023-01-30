from django.db import models

# Create your models here.
class Chapter(models.Model):
    number = models.IntegerField(verbose_name="Номер главы")
    name = models.CharField(verbose_name="Название главы", max_length=100)
    class Meta:
        verbose_name = "Глава"
        verbose_name_plural = "Главы"
    def __str__(self) -> str:
        return f"Глава {self.number} - {self.name}"

class Theme(models.Model):
    number = models.IntegerField(verbose_name="Номер темы")
    name = models.CharField(verbose_name="Название темы", max_length=30)
    chapter = models.ForeignKey(Chapter, models.CASCADE)
    slug = models.SlugField(verbose_name="Ссылка",null=True, unique=True, help_text="Отображается в url поле в верху браузера")
    text = models.TextField(verbose_name="Содержание", null=True, help_text="Тут можно указать разметку используя готовые стили bootstrap")

    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = "Темы"
    def __str__(self) -> str:
        return f"Тема {self.number}, Глава {self.chapter.number} - {self.name}"