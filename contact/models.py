from django.db import models


class Contac(models.Model):
    """Контакты"""
    name = models.CharField('Имя', max_length=10)
    last_name = models.CharField('Фамилия', max_length=15)
    big_name = models.CharField('Отчество', max_length=15)
    text_01 = models.TextField('Описание', max_length=150)
    birthday = models.DateField('Дата рождение', auto_now_add = False,blank=False, )
    num_ber = models.CharField('Номер', max_length=10)
    email = models.EmailField('Gmail', max_length=254)
    cosial = models.URLField('Страница в соц сети', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Имя'
        verbose_name_plural = 'Имена'
