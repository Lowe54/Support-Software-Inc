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