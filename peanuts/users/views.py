# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.views.generic import RedirectView
from rest_framework import viewsets
from braces.views import LoginRequiredMixin

# Import the customized User model
from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail",
                       kwargs={"username": self.request.user.username})


