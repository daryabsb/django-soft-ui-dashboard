from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from isbn_field import ISBNField


class Author(models.Model):
    first_name = models.CharField(max_length=30, verbose_name=_('First name'))
    last_name = models.CharField(max_length=40, verbose_name=_('Last name'))

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')


class Tag(models.Model):
    word = models.CharField(max_length=35, verbose_name=_('Word'))
    slug = models.CharField(max_length=50, verbose_name=_('Slug'))

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')


class Book(models.Model):
    title = models.CharField(max_length=40, verbose_name=_('Title'))
    cover = models.ImageField(upload_to='book-covers',
                              verbose_name=_('Cover'), blank=True)
    tags = models.ManyToManyField(
        Tag, verbose_name=_('Tags'), related_name='books')
    authors = models.ManyToManyField(
        Author, verbose_name=_('Authors'), related_name='books')
    publication_date = models.DateField(verbose_name=_('Publication date'))
    # isbn = ISBNField(verbose_name=_('ISBN code', null=True, blank=True))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Book')
        verbose_name_plural = _('Books')


class Borrow(models.Model):
    user = models.OneToOneField(get_user_model(), verbose_name=_(
        'Usuario'), on_delete=models.PROTECT)
    borrow_date = models.DateField(verbose_name=_('Borrow date'))
    returned_date = models.DateField(verbose_name=_(
        'Returned date'), blank=True, null=True)
    book = models.ForeignKey(Book, verbose_name=_(
        'Book'), on_delete=models.PROTECT)

    class Meta:
        verbose_name = _('Borrow')
        verbose_name_plural = _('Borrows')

    def __str__(self):
        return '{}_{}'.format(self.user, self.borrow_date)
