from django.shortcuts import render

from .models import Organisation
from .forms import editOrganisationForm

def show_organisation_list(request):
    '''
    View that returns a list of all organisations
    '''
    organisation_list = Organisation.objects.all()

    return render(
        request,
        'organisation_list.html',
        {'organisation_list': organisation_list}
        )


# def edit_organisation(request, org_id):
#     if request.method == 'POST':
#         edit_org_form = editOrganisationForm(request.POST)

#         if edit_org_form.is_valid():
#     edit_org_form = edit_o
