from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from jobs.models import job_types, job_cities
from jobs.models import Job
def joblist(request):
    job_list = Job.objects.order_by('job_type')
    template = loader.get_template('job_list.html')
    content = {"job_list": job_list}
    for job in job_list:
        job.city_name = job_cities[job.job_city][1]
        job.type_name = job_types[job.job_type][1]
    return HttpResponse(template.render(content))
def detail(request):
    id = request.GET.get('id')
    job = Job.objects.get(pk=id)
    return render(request, 'detail.html', {'job': job})