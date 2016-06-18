from __future__ import unicode_literals

from django.db import models
from django.core.validators import EMPTY_VALUES
import hashlib
import random
import string
from django.core.urlresolvers import reverse


class Photo(models.Model):
    photo = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.slug in EMPTY_VALUES:
            rs = ''.join(random.choice(string.lowercase) for i in range(20))
            print rs
            self.slug = hashlib.sha1(rs).hexdigest()
        return super(Photo, self).save(*args,  **kwargs)

    def get_absolute_url(self):
        if self.slug:
            return reverse('photo-see', args=[self.slug])
