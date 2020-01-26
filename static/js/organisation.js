$('.org-edit').on('click', function(e) {
    e.preventDefault();
    let id = $(this).data('id');
    console.log(id);
    get_organisation_info(id);
})

$('.org-users').on('click', function(e) {
    e.preventDefault();
    let id = $(this).data('id');
    console.log(id);
    get_organisation_users(id);
})

$('#organisation_form').submit(function(e){
    return false;
    console.log("Form submission prevented");
    let id = $('#org_id').val();
    let action = $('#action').val();
    save_organisation(id, action)
})

function get_organisation_info(id) {
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
    $.ajax({
        url: '/organisations/save/',
        type: "POST",
        data: {
            'org_id' : org_id,
            'action': $('#action').val(),
            'Organisation_Name': $('#id_Organisation_Name').val()
        },
        success: function(response){
            $('#edit-modal').modal('hide');
            $('td [data-id="'+org_id+'"]').closest('td').prev().text(response);
            Swal.fire(
                "Success!",
                "Organisation Updated",
                "success"
                )
        }
    })
}