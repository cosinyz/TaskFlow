from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Category(models.Model):
    name = models.CharField('Название категории', max_length=100, unique=True)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['name']

    def __str__(self):
        return self.name


class Task(models.Model):
    class Status(models.TextChoices):
        NEW = 'new', 'Новая'
        IN_PROGRESS = 'in_progress', 'В работе'
        COMPLETED = 'completed', 'Завершена'

    title = models.CharField('Название задачи', max_length=150)
    description = models.TextField('Описание', blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='tasks',
    )
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.SET_NULL,
        related_name='tasks',
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    due_date = models.DateField('Срок выполнения', null=True, blank=True)
    status = models.CharField(
        'Статус',
        max_length=20,
        choices=Status.choices,
        default=Status.NEW,
    )
    priority = models.PositiveSmallIntegerField(
        'Приоритет',
        default=3,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )

    class Meta:
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'
        ordering = ['-created_at']

    def __str__(self):
        return self.title
