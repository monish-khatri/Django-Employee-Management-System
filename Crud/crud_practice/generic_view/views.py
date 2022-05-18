from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .models import GeeksModel
from django.urls import reverse
from django.core.paginator import Paginator

class GeeksCreate(CreateView):

    # specify the model for create view
    model = GeeksModel
    # specify the fields to be displayed

    fields = ['title','description']

    def get_success_url(self):
        return reverse('detail',args=(self.object.id,))

class GeeksList(ListView):

    # specify the model for list view
    model = GeeksModel
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(GeeksList, self).get_context_data(**kwargs)
        list = GeeksModel.objects.all().order_by("-id")
        paginator = Paginator(list, self.paginate_by)

        page = self.request.GET.get('page',1)
        pageList = paginator.get_page(page)
        pageList.adjusted_elided_pages = paginator.get_elided_page_range(page)

        context['object_list'] = pageList
        context['totalRecords'] = len(list)
        return context


class GeeksDetailView(DetailView):
    # specify the model to use
    model = GeeksModel

class GeeksUpdateView(UpdateView):
	# specify the model you want to use
	model = GeeksModel

	# specify the fields
	fields = ["title","description"]

class GeeksDeleteView(DeleteView):
    # specify the model you want to use
    model = GeeksModel
    # can specify success url
    def get_success_url(self):
        return reverse('list')