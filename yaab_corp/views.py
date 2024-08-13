from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404





class DashboardView(TemplateView):
     pass
     
index_view = DashboardView.as_view(template_name="index.html")

