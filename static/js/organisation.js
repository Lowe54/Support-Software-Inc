$('.org-edit').on('click', function(e) {
    e.preventDefault();
    let id = $(this).data('id');
    console.log(id);
    get_organisation_info(id);
})

$('.addOrg').on('click', function(e){
    e.preventDefault();
    add_organisation_form()
})

$('.org-users').on('click', function(e) {
    e.preventDefault();
    let id = $(this).data('id');
    console.log(id);
    get_organisation_users(id);
})

function add_organisation_form() {
    $.ajax({
        url: '/organisations/add/',
        type: "POST",
        success: function(response){
            $('#edit-modal').remove();
            $('.org-OrganisationTableWrapper').append(response);
            $('#edit-modal').modal();
        }
    })
}

function get_organisation_info(id=None) {
    console.info("Get Organisation info called with id " + id);
    $.ajax({
        url: '/organisations/edit/',
        type: "POST",
        data: { 'org_id' : id },
        success: function(response){
            $('#edit-modal').remove();
            $('.org-OrganisationTableWrapper').append(response);
            $('#edit-modal').modal();
        }
    })
}

function get_organisation_users(id) {
    console.info("Get Organisation Users called with id " + id);
    $.ajax({
        url: '/organisations/userlist/',
        type: "POST",
        data: { 'org_id' : id },
        success: function(response){
            $('#user-list-modal').remove();
            $('.org-OrganisationTableWrapper').append(response);
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