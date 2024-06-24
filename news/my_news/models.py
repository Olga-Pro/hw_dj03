from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class News_post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name='Автор новости' , default=1)
    # Поле `user` связывает модель `News_post` с моделью `User`.
    # Параметр `on_delete=models.CASCADE` обеспечивает удаление новостей,
    # если пользователь будет удален из базы данных.
    # Параметр `verbose_name` используется для более дружественного отображения
    # имени поля в административной панели.
    # ID пользователя по умолчанию

    title = models.CharField('Название новости', max_length=50)
    short_description = models.CharField('Краткое описание новости', max_length=200)
    text = models.TextField('Новость')
    pub_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
