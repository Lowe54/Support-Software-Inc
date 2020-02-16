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
            return HttpResponse(request.POST['Organisation_Name'])
        else:
            edit_org = OrganisationForm(request.POST)
            new_org = edit_org.save()
            response = '<tr><td>{}</td>\
                        <td colspan="2">\
                        <a href="#" class="org-edit btn btn-info"\
                        data-id="{}">\
                        Edit</a> <a href="#" class="org-users btn btn-info"\
                        data-id="{}">Show all Users</a>\
                        </td></tr>'.format(
                            new_org.Organisation_Name,
                            new_org.id,
                            new_org.id
                            )
            return HttpResponse(response)


def get_unassociated_users(request):
    if request.method == 'POST':
        form = UnassociatedUserForm()
        # userlist = MyUser.objects.filter(organisation_id=None)
        org_id = request.POST['org_id']
        print(org_id)
        return render(request, 'unassociated_users.html',
                      {'form': form, 'org_id': org_id})


def associate_users(request):
    if request.method == 'POST':
        organisation_id = request.POST['org_id']
        organisation = Organisation.objects.get(id=organisation_id)
        if organisation:
            list_of_users = request.POST.get('users')
            user_list = []
            # Go through each user parameter, and remove all text apart from
            # '&' characters
            for letter in list_of_users:
                if letter == '&' or letter.isdigit():
                    user_list.append(letter)
            # Join the resulting array to a string var
            userstring = ','.join(user_list)
            # Remove the commas
            userstring = userstring.replace(',', '')    
            # Finally split by the '&'
            user_list = userstring.split('&')
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
                        '<div id="user-{}" class="org-modal-userrow row" data-user="{}">\
                            <div class="org-modal-username col-lg-4">\
                                {}\
                            </div>\
                            <div class="org-modal-useremail col-lg-4">\
                                {}\
                            </div>\
                            <div class="org-modal-useractions col-lg-4">\
                                <a class="btn btn-danger modal-remove\
                                col-lg-12" href="#" data-id={}>Remove from\
                                organisation</a>\
                            </div>\
                        </div>'.format(
                            current_user.user.id,
                            current_user.user.id,
                            current_user.user.username,
                            user_email_text,
                            current_user.user.id
                            )
            return HttpResponse(content=response, status=200)
        return HttpResponse(status=403)


def unassocate_user(request):
    if request.method == 'POST':
        user_to_be_unassociated = request.POST['user']
        if user_to_be_unassociated:
            Affected_User = MyUser.objects.get(user_id=user_to_be_unassociated)
            Affected_User.organisation = None
            Affected_User.save()

        return HttpResponse(status=200)

    return HttpResponse(status=403)