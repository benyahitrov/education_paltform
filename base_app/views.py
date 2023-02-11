from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from django.urls import reverse_lazy
from base_app.models import Course


class PageTitleMixin:
    title = None

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['title'] = self.title
        return context


class CourseListView(PageTitleMixin, ListView):
    model = Course
    template_name = 'base_app/index.html'
    title = 'Главная'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Course.objects.all().select_related('category')
        return context


class CourseDetailView(PageTitleMixin, DetailView):
    model = Course
    title = 'Страница курса'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students_count'] = self.object.students.all().count()
        context['lectors'] = self.object.lectors.all()
        return context


class CourseCreateView(CreateView):
    model = Course
    fields = ['title', 'description', 'duration', 'price', 'category']


class CourseUpdateView(UpdateView):
    model = Course
    fields = ['title', 'description', 'duration', 'price', 'category']
    template_name_suffix = '_update_form'


class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('base_app:index')


class CourseReportView(PageTitleMixin, ListView):
    model = Course
    template_name = 'base_app/index.html'
    title = 'Главная'
