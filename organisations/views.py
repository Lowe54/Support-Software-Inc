'''
Organisation model views.py
'''
from django.shortcuts import render, HttpResponse
from .models import Organisation
from authentication.models import MyUser
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
                'edit_organisation.html',
                {'org': org, 'form': form}
            )
        else:
            form = OrganisationForm()
            return render(
                request,
                'edit_organisation.html'
            )


def get_user_list(request, org_id=None):
    '''
    Returns the list of users associated with a particular organisation
    '''
    if request.method == 'POST':
        organisation = Organisation.objects.get(id=request.POST['org_id'])
        user_list = MyUser.objects.filter(organisation=request.POST['org_id'])
        print(user_list)
        return render(
            request,
            'organisation_user_list.html',
            {
                'org': organisation,
                'user_list': user_list
            }
        )


def save_organisation(request, org_id=None, action='create'):
    '''
    Saves the organisation
    '''
    if request.method == 'POST':
        action = request.POST['action']
        if action == 'update':
            org_ins = Organisation.objects.get(id=request.POST['org_id'])
            edit_org = OrganisationForm(request.POST, instance=org_ins)
            edit_org.save()
        else:
            edit_org = OrganisationForm(request.POST)
            edit_org.save()

        return HttpResponse(request.POST['Organisation_Name'])
