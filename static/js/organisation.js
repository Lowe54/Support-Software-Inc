$('.org-edit').on('click', function(e) {
    e.preventDefault();
    let id = $(this).data('id');
    console.log(id);
    get_organisation_info(id);
})

function get_organisation_info(id) {
    console.info("Get Organisation info called with id " + id);
    $.ajax({
        url: 'http://127.0.0.1:8000/organisations/edit/',
        type: "POST",
        data: { 'org_id' : id },
        success: function(response){
            console.log(response)
            $('#edit-modal').remove();
            $('.org-OrganisationTableWrapper').append(response);
            $('#edit-modal').modal();
        }
    })
}