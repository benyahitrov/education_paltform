from django.db import models


class Lector(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=30)
    last_name = models.CharField(verbose_name='Фамилия', max_length=30)
    about = models.TextField(verbose_name='О преподавателе')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def __repr__(self):
        return str(self)


class Student(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=30)
    last_name = models.CharField(verbose_name='Фамилия', max_length=30)
    email = models.EmailField(verbose_name='Электронная почта', unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def __repr__(self):
        return str(self)


class Category(models.Model):
    name = models.CharField(verbose_name='Категория', max_length=50)

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)


class Course(models.Model):
    title = models.CharField(verbose_name='Название курса', max_length=100)
    description = models.TextField(verbose_name='Описание курса')
    duration = models.PositiveSmallIntegerField(verbose_name='Длительность')
    price = models.IntegerField(verbose_name='Стоимость')
    category = models.ForeignKey(Category,
                                 verbose_name='Категория',
                                 on_delete=models.PROTECT)
    lectors = models.ManyToManyField(Lector)
    students = models.ManyToManyField(Student)

    def get_absolute_url(self):
        return f'/course/{self.id}'

    def __str__(self):
        return self.title

    def __repr__(self):
        return str(self)

