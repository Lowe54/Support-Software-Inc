$('.cardset-wrapper').on('click', '.org-edit', function(e) {
    e.preventDefault();
    let id = $(this).data('id');
    get_organisation_info(id);
})

$('.addOrg').on('click', function(e){
    e.preventDefault();
    add_organisation_form()
})

$('.cardset-wrapper').on('click', '.org-users', function(e) {
    e.preventDefault();
    let id = $(this).data('id');
    get_organisation_users(id);
})

function add_organisation_form() {
    $.ajax({
        url: '/organisations/add/',
        type: "POST",
        success: function(response){
            $('#edit-modal').remove();
            $('.organisation-content').append(response);
            $('#edit-modal').modal();
        }
    })
}

function get_organisation_info(id=None) {
    $.ajax({
        url: '/organisations/edit/',
        type: "POST",
        data: { 'org_id' : id },
        success: function(response){
            $('#edit-modal').remove();
            $('.organisation-content').append(response);
            $('#edit-modal').modal();
        }
    })
}

function get_organisation_users(id) {
    $.ajax({
        url: '/organisations/userlist/',
        type: "POST",
        data: { 'org_id' : id },
        success: function(response){
            $('#user-list-modal').remove();
            $('.organisation-content').append(response);
            $('#user-list-modal').modal();
        }
    })
}

function save_organisation() {
    let org_id = $('#org_id').val();
    let action = $('#action').val();
    $.ajax({
        url: '/organisations/save/',
        type: "POST",
        data: {
            'org_id' : org_id,
            'action': action,
            'Organisation_Name': $('#id_Organisation_Name').val()
        },
        success: function(response){
            $('#edit-modal').modal('hide');
            if (action === 'update'){
            $('td [data-id="'+org_id+'"]').closest('td').prev().text(response);
            Swal.fire(
                "Success!",
                "Organisation Updated",
                "success"
                )
            }
            else {
                $('table').append(response)
                Swal.fire(
                    "Success!",
                    "Organisation has been added",
                    "success"
                    )
                }
            }
        });
}


function associate_user_modal(id){
    let org_id = $('#asoc-user').attr('data-id')
    $.ajax({
        url: '/organisations/getunassociated/',
        type: "POST",
        data: {
            'org_id': org_id
        },
        success: function(response){
            $('#unassociated-user-list-modal').remove()
            $('#user-list-modal').append(response)
            $('#unassociated-user-list-modal').modal()
        }
    })
}

function assocate_user(){
    let organisation_iden = $('#org_ident').val()
    $.ajax({
        url: '/organisations/associate/',
        type: "POST",
        data: {
            'org_id': organisation_iden,
            'users': $('#organisation_form').serialize()
        },
        success: function(response){
            $('#unassociated-user-list-modal').modal('hide')
            $('#user-list-modal .modal-body').append(response)
            Swal.fire(
                'success',
                'User\'s associated',
                'success'
            )
        }
    })
}

$('div').on('click', '.modal-remove', function(){
    let organisation_ident = $(this).data('orgid')
    let user = $(this).data('id')
    $.ajax({
        url: '/organisations/unassociate/',
        type: "POST",
        data: {
            'org_id': organisation_ident,
            'user': user
        },
        success: function(){
            $('#user-'+user).remove()
            const Toast = Swal.mixin({
                toast: true,
                position: 'top-end',
                showConfirmButton: false,
                timer: 10000,
                timerProgressBar: true,
            })
            Toast.fire(
                'success',
                'User disassociated',
                'success'
            )
        }
    })
})
function disassocate_user(){
    let organisation_iden = $('#org_ident').val()
    console.log(organisation_iden)
    
}