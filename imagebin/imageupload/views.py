from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Photo
from .forms import PhotoForm
from django.views.generic.detail import DetailView
from django.http.response import HttpResponseRedirect
from django.utils.encoding import force_text


class PhotoUploadView(CreateView):
    model = Photo
    form_class = PhotoForm

    def get_success_url(self):
        if self.object:
            print self.object.photo
            return force_text(self.object.get_absolute_url())

    def form_invalid(self, form):
        print form.error
        return CreateView.form_invalid(self, form)


class PhotoDetailView(DetailView):
    model = Photo
