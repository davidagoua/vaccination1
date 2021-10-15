from django.shortcuts import render
from django.views import View, generic
from django.contrib.auth import mixins
from django.contrib import messages
from usermanager.models import User


class HomeView(mixins.LoginRequiredMixin, generic.TemplateView):
    template_name = 'home.html'


class UserUpdateView(mixins.LoginRequiredMixin, mixins.UserPassesTestMixin, generic.UpdateView):
    model = User
    fields = ['email','contact','first_name','last_name']
    success_url = '/'
    template_name = 'registration/update_profile.html'

    def test_func(self):
        return self.request.user.pk == int(self.kwargs['pk'])

    def form_valid(self, form):
        messages.success(self.request, "Profile modifié !")
        return super(UserUpdateView, self).form_valid(form)