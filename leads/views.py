from multiprocessing import context
from django.shortcuts import render, get_object_or_404, redirect
from leads.forms import LeadForm

from leads.models import Lead


def landing_page(request):
    return render(request, 'landing.html')

# Create your views here.
def home(request):
    leads = Lead.objects.all().order_by('-email')
    context = {
        'leads':leads
    }
    return render(request, 'leads/homepage.html', context)


def lead_detail(request,pk):
    lead_detail = get_object_or_404(Lead, id=pk)
    context = {
        'lead': lead_detail
    }
    return render(request, 'leads/lead_details.html', context)

def lead_create(request):
    form = LeadForm
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form' : form
    }
    return render(request, 'leads/create_lead.html', context)



# def lead_create(request):
#     form = LeadForm
#     if request.method == 'POST':
#          form = LeadForm(request.POST)
#          if form.is_valid():
#             first_name = form.cleaned_data["first_name"]
#             last_name = form.cleaned_data["last_name"]
#             age = form.cleaned_data["age"]
#             email = form.cleaned_data["email"]
#             source = form.cleaned_data["source"]
#             agent = form.cleaned_data["agent"]
#             lead = Lead.objects.create(first_name = first_name, last_name=last_name,age=age,email=email,source=source,agent=agent)
#             return redirect('home')
#     context = {
#         'form': form
#     }
#     return render(request, 'leads/create_lead.html', context)


def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadForm(instance = lead)
    if request.method == 'POST':
        form = LeadForm(request.POST, instance=lead)
        if form.is_valid():
            
            lead.save()
            return redirect('home')
    context = {
        'lead': lead,
        'form': form
    }
    return render(request, 'leads/lead_update.html', context)

def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('home')
    