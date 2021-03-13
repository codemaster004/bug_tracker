from django.shortcuts import render


def projects_list_view(request):
	return render(request, 'projects/projects_list.html', {})
