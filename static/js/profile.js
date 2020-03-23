$('#edit').on('click', function(e) {
    e.preventDefault();
    console.log('Editing Profile');
    let id = $(this).data('id');
    get_profile(id);
});

function get_profile(id=None){
    profile_id = id;
    $.ajax({
        url: 'profile/edit/',
        type: "POST",
        data: { 'profile_id' : profile_id },
        success: function(response){
            $('#edit-modal').remove();
            $('.usr-profile-container').append(response);
            $('#edit-modal').modal();
        }
    });
}

function save_profile(){
    let user_id = $('#user_id').val();
    $.ajax({
        url: 'profile/save/',
        type: "POST",
        data: {
            'user_id' : user_id,
            'username': $('#id_username').val(),
            'email': $('#id_email').val(),
            'first_name': $('#id_first_name').val(),
            'last_name': $('#id_last_name').val(),
        },
        success: function(response){
            $('#edit-modal').modal('hide');
            $('.user-profile-core-info:first').remove();
            $('.user-profile-secondary-info').parent().prepend(response);
            Swal.fire({
                'icon': 'success',
                'toast': true,
                'timer': 5000,
                'position': 'top-right',
                'text':'Profile Updated Successfully',
            });
        }
    });
}