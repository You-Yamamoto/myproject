from django.shortcuts import render
from django.test import TestCase
from django.views.generic import ListView , DetailView
from .models import Profile
from django.urls import reverse_lazy
from tweetapp.models import BoardModel
from django.shortcuts import get_object_or_404
# Create your tests here.


class ProfileListView(ListView):
		model = Profile
		template_name = 'profiles.html'
		context_object_name = 'profiles'

		def get_queryset(self):
				return Profile.objects.all().exclude(user = self.request.user)
# Create your views here.

class ProfileDetailView(DetailView):
		model = Profile
		model = BoardModel
		template_name = 'zibun.html'
		object = get_object_or_404(BoardModel)

		def get_object(self, **kwargs):
				pk = self.kwargs.get('pk')
				view_profile = Profile.objects.get(pk=pk)
				return view_profile

		def get_context_data(self, **kwargs):
				context = super().get_context_data(**kwargs)
				view_profile = self.get_object()
				my_profile = Profile.objects.get(user=self.request.user)
				if view_profile.user in my_profile.following.all():
						follow = True
				else:
						follow = False
				context["follow"] = follow
				return context

	