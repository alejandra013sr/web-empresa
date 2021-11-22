from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required #tambien esta login_required o permission_required
from django.utils.decorators import method_decorator

from django.shortcuts import redirect
from django.urls import reverse_lazy

from .models import Page
from .forms import PageForm


"""
#Mixin creado
class StaffRequiredMixin(object):
    ##Este mixin requerira que el usuario sea miembro del staff

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect(reverse_lazy('admin:login'))
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)
""" 

class PageList(ListView):
    model = Page

class PageDetail(DetailView):
    model = Page

@method_decorator(staff_member_required, name='dispatch')
class PageCreate(CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:list')


@method_decorator(staff_member_required, name='dispatch')
class PageUpdate(UpdateView):
    model=Page
    form_class = PageForm
    template_name_suffix='_update_form'
    
    def get_success_url(self):
        return reverse_lazy('pages:update',args=[self.object.id])+'?ok'

@method_decorator(staff_member_required, name='dispatch')
class PageDelete(DeleteView):
    model=Page
    success_url=reverse_lazy('pages:pages')

    def get_success_url(self):
        return reverse_lazy('pages:list')+ '?delete'