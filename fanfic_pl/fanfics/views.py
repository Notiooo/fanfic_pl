from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404
from django.template.defaultfilters import slugify
from django.db.models import Q


from . import models
from .forms import FanficForm
# Create your views here.


class FandomsHomeView(ListView):
    model = models.Fandom
    context_object_name = 'fandoms'
    template_name = 'fanfics/fandom_list.html'

    def get_queryset(self):
        query = self.request.GET.get('search')
        if(query):
            tags_list = [slugify(x.strip()) for x in self.request.GET['search'].split(',')]
            return self.model.objects.filter(Q(tags__slug__in=tags_list) | Q(fandom_name__icontains=tags_list[0])).distinct()
        else:
            return super(FandomsHomeView, self).get_queryset()

class FandomView(DetailView):
    model = models.Fandom
    context_object_name = 'fandom'
    template_name = 'fanfics/fandom_detail.html'
    slug_url_kwarg = 'slug_fandom'
    slug_field = 'slug'


class AddFanfic(CreateView):
    model = models.Fanfic
    form_class = FanficForm
    template_name = 'fanfics/add_fanfic.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.fandom = get_object_or_404(models.Fandom, slug=self.kwargs['slug_fandom'])
        return super().form_valid(form)