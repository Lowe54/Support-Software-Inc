'''
Organisation model views.py
'''
from django.shortcuts import render
from .models import Organisation
from .forms import OrganisationForm


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


def add_or_edit_organisation(request, org_id=None):
    '''
    Returns the modal that allows addition or editing of
    an organisation
    '''
    if request.method == 'POST':
        org = Organisation.objects.get(id=request.POST['org_id'])
        if org:
            form = OrganisationForm(instance=org)
            return render(
                request,
                'partials/edit_organisation.html',
                {'org': org, 'form': form}
            )
        else:
            form = OrganisationForm()
            return render(
                request,
                'partials/edit_organisation.html',
                {'org': org}
            )
