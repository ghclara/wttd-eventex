from django.db import models

from django.shortcuts import resolve_url


class Speaker(models.Model):
    name = models.CharField('Nome', max_length=255)
    slug = models.SlugField('Slug')
    photo = models.URLField('Foto')
    website = models.URLField('Website', blank=True)
    description = models.TextField('Descrição', blank=True)

    class Meta:
        verbose_name = 'Palestrante'
        verbose_name_plural = 'Palestrantes'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return resolve_url('speaker_detail', slug=self.slug)


class Contact(models.Model):

    EMAIL = 'E'
    PHONE = 'P'
    KINDS = (
        (EMAIL, 'Email'),
        (PHONE, 'telefone'),
    )

    speaker = models.ForeignKey(Speaker, verbose_name='Palestrante')
    king = models.CharField('Tipo', max_length=1, choices=KINDS)
    value = models.CharField('Valor', max_length=255)

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return self.value


class Talk(models.Model):
    title = models.CharField('Título', max_length=200)
    start = models.TimeField('Início', null=True, blank=True)
    description = models.TextField('Descrição', blank=True)
    speakers = models.ManyToManyField('Speaker', verbose_name='Palestrantes', blank=True)

    class Meta:
        verbose_name = 'Palestra'
        verbose_name_plural = 'Palestras'

    def __str__(self):
        return self.title
