$('#request-take-me').on('click', function(e){
    e.preventDefault();
    $.ajax({
        url: '/ticket/assigntouser/',
        type: "POST",
        data: {
        't_id' : $(this).data('id'),
        'assignee': $(this).data('user')
        },
        success: function(response){
            $('.ticket-assigned-to').text(response);
            Swal.fire({
                'icon': 'success',
                'toast': true,
                'timer': 5000,
                'position': 'top-right',
                'text':'Ticket has been assigned to you',
            });
        },
        error: function(){
            Swal.fire({
                'icon': 'error',
                'toast': true,
                'timer': 5000,
                'position': 'top-right',
                'text':'Something went wrong, please try again',
            });
        }
    });
});

$('#edit-ticket').on('click', function(e){
    e.preventDefault();
    get_ticket_information(id=$(this).data('id'));
});

$('#add-comment').on('click', function(e){
    e.preventDefault();
    show_comment_form(id=$(this).data('id'));
});

$('#mark-ticket-closed').on('click', function(e){
    e.preventDefault();
});

function get_ticket_information(id=None){
$.ajax({
    url: '/ticket/edit/',
    type: "POST",
    data: { 't_id' : id },
    success: function(response){
        $('#edit-modal').remove();
        $('#content-wrapper').append(response);
        $('#edit-modal').modal();
    },
    error: function(response){
        Swal.fire({
            'icon': 'error',
            'toast': true,
            'timer': 5000,
            'position': 'top-right',
            'text':'Something went wrong, please try again',
        });
    }
    });
}

function save_ticket(){
    $.ajax({
        url: '/ticket/save/',
        type: "POST",
        data: {
            't_id': $('#id_t_id').val(),
            'title': $('#id_title').val(),
            'description':$('#id_description').val() ,
            'status' : $('#id_status').val(),
            'priority': $('#id_priority').val(),
            'associated_users': $('#id_associated_users').val()
        },
        success: function(data){
            $('#edit-modal').modal('hide');
            let response = data;
            $('.ticket-header').text(response.title);
            $('.ticket-description').text(response.description);
            Swal.fire({
                'icon': 'success',
                'toast': true,
                'timer': 5000,
                'position': 'top-right',
                'text':'Ticket has been updated',
            });
           

        }
    });
}

function close_ticket(){
    Swal.mixin({
        confirmButtonText: 'Next &rarr;',
        showCancelButton: true,
      }).queue([
        {
            title: 'Please enter the closure reason',
            input: 'textarea',  
        },
        { 
            title: 'Confirm Closure',
            text: "Closed tickets can no longer be edited or updated",
            icon: 'warning',
            confirmButtonText: 'Confirm',
        },
      ]).then((result) => {
            if (result.value) {
                $.ajax({
                    url: '/ticket/close/',
                    type: "POST",
                    data: {
                        't_id': $('#mark-ticket-closed').data('id'),
                        'closure_message': result.value[0]
                    },
                    success: function(response){
                        $('.tck-Ticket_Header').prepend('<div id="ticket-closure-banner" class="alert alert-dark">' + response + '</div>');
                        $('#edit-ticket, #mark-ticket-closed').remove();
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
      });
}

function show_comment_form(id=None){
    $.ajax({
        url: '/comment/new/',
        type: "POST",
        data: { 't_id' : id },
        success: function(response){
            $('#comment-modal').remove();
            $('#content-wrapper').append(response);
            $('#comment-modal').modal();
        },
        error: function(){
            Swal.fire({
                'icon': 'error',
                'toast': true,
                'timer': 5000,
                'position': 'top-right',
                'text':'Something went wrong, please try again',
            });
        }
        });
    }


function post_comment() {
        let internal_comment;
        
        if ($('#id_is_internal_comment').prop('checked')) {
            internal_comment = $('#id_is_internal_comment').prop('checked');
        }
        else {
            internal_comment = false;
        }

        $.ajax({
            url: '/comment/post/',
            method: 'POST',
            data: {
                'comment_content': $('#id_comment_content').val(),
                'is_internal_comment': internal_comment,
                'rel_ticket': $('#id_related_ticket').val()
            },
            success: function(response){
                $('.tck-Ticket-CommentSection').append(response);
                const Toast = Swal.mixin({
                    toast: true,
                    position: 'top-end',
                    showConfirmButton: false,
                    timer: 10000,
                    timerProgressBar: true,
                });
                Toast.fire(
                    'success',
                    'Comment Posted',
                    'success'
                );
            }
        });
    }