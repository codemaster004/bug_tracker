from django.shortcuts import render

from .models import Project


def projects_list_view(request):
	context = {}
	
	user_projects = Project.objects.all()
	context['projects'] = user_projects
	
	return render(request, 'projects/projects_list.html', context)
