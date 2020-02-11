from django.shortcuts import render
from django.views.generic import ListView
from django.template.defaultfilters import slugify
from django.db.models import Q


from . import models
# Create your views here.


class FandomsView(ListView):
    model = models.Fandom
    context_object_name = 'fandoms'
    template_name = 'fanfics/fanfic_list.html'

    def get_queryset(self):
        query = self.request.GET.get('search')
        if(query):
            tags_list = [slugify(x.strip()) for x in self.request.GET['search'].split(',')]
            return self.model.objects.filter(Q(tags__slug__in=tags_list) | Q(fandom_name__icontains=tags_list[0])).distinct()
        else:
            return super(FandomsView, self).get_queryset()