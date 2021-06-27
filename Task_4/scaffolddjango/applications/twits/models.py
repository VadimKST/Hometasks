from django.db import models


class Movie(models.Model):
    """Фильм"""
    title = models.CharField("Название", max_length=200, blank=False, null=False)
    description = models.TextField("Описание", blank=False, null=False, default='')
    year = models.SmallIntegerField("Дата выхода")

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movie'

    def __str__(self):
        return self.title


class Review(models.Model):
    """Рецензия"""
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Текст рецензии", max_length=5000)
    movie = models.ForeignKey(Movie, verbose_name="фильм", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Review"

    def __str__(self):
        return f"{self.name} - {self.movie}"


class Comment(models.Model):
    """Комментарий к рецензии"""
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Текст комментария", max_length=500)
    review = models.ForeignKey(Review, verbose_name="рецензия", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comment"

    def __str__(self):
        return f"{self.name} - {self.review}"

