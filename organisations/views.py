'''
Organisation model views.py
'''
from django.shortcuts import HttpResponse, render

from authentication.models import MyUser

from .forms import OrganisationForm, UnassociatedUserForm
from .models import Organisation


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


def add_or_edit_organisation(request):
    '''
    Returns the modal that allows addition or editing of
    an organisation
    '''
    if request.method == 'POST':
        if request.POST:
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
                'edit_organisation.html',
                {
                    'form': form
                }
            )
    return HttpResponse(status=401)

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
    return HttpResponse(status=401)

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
            return HttpResponse(request.POST['Organisation_Name'])

        edit_org = OrganisationForm(request.POST)
        new_org = edit_org.save()
        response = f'<div class="card-wrapper col-lg-4 col-md-6 col-sm 12">\
                        <div class="card text-center">\
                            <div class="card-body">\
                                <h5 class="card-title">{new_org.Organisation_Name}</h5>\
                            </div>\
                            <div class="card-footer">\
                                <a href="#" class="card-link org-edit" data-id="{ new_org.id }">\
                                    <i class="fas fa-edit"></i>\
                                    <div>Edit</div>\
                                </a>\
                                <a href="#" class="card-link org-users" data-id="{ new_org.id }">\
                                    <i class="fas fa-users"></i>\
                                    <div class="d-none d-lg-block">Show attached users</div>\
                                    <div class="d-lg-none">Show users</div>\
                                </a>\
                            </div>\
                        </div>\
                    </div>'
        return HttpResponse(response)
    return HttpResponse(status=401)

def get_unassociated_users(request):
    '''
    Return all users not associated with a user
    '''
    if request.method == 'POST':
        form = UnassociatedUserForm()
        org_id = request.POST['org_id']
        return render(request, 'unassociated_users.html',
                      {'form': form, 'org_id': org_id})
    return HttpResponse(status=401)

def associate_users(request):
    '''
    Associate user(s) to an organisation
    '''
    if request.method == 'POST':
        organisation_id = request.POST['org_id']
        organisation = Organisation.objects.get(id=organisation_id)
        if organisation:
            list_of_users = request.POST.getlist('users')
            initialstring = list_of_users.pop(0)
            initial_user_list = initialstring.split('&')
            user_list = []
            for user in initial_user_list:
                if 'users=' in user:
                    user_list.append(user.strip('users='))
            response = ''
            for assoc_user in user_list:
                current_user = MyUser.objects.get(user_id=assoc_user)
                if current_user:
                    current_user.organisation = organisation
                    current_user.save()
                    if current_user.user.email is not None:
                        user_email_text = current_user.user.email
                    else:
                        user_email_text = 'No Email listed'
                    response = response + \
                        f'<div id="user-{ current_user.user.id }" class="card">\
                            <div class="card-body">\
                                <h5 class="card-title">\
                                    {current_user.user.username}\
                                </h5>\
                                <h6 class="card-subtitle mb-2 text-muted">\
                                    {user_email_text}\
                                </h6>\
                                <a class="card-link modal-remove btn\
                                btn-remove" href="#" \
                                data-id={ current_user.user.id }>\
                                    Remove from organisation\
                                </a>\
                            </div>\
                        </div>'
            return HttpResponse(content=response, status=200)
        return HttpResponse(status=403)
    return HttpResponse(status=403)


def unassocate_user(request):
    '''
    Unassociate a user from a organisation
    '''
    if request.method == 'POST':
        user_to_be_unassociated = request.POST['user']
        if user_to_be_unassociated:
            affected_user = MyUser.objects.get(user_id=user_to_be_unassociated)
            affected_user.organisation = None
            affected_user.save()

        return HttpResponse(status=200)

    return HttpResponse(status=403)
