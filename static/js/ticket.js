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
            $('.ticket-assigned-to').text(response)
            Swal.fire(
                "Success!",
                "Ticket assigned to you",
                "success"
                )
        },
        error: function(){
            Swal.fire(
                "Uh-Oh, something went wrong",
                "Please reload the page and try again",
                "error"
            )
        }
    })
});

$('#edit-ticket').on('click', function(e){
    e.preventDefault()
    get_ticket_information(id=$(this).data('id'))
})

$('#mark-ticket-closed').on('click', function(e){
    e.preventDefault()
})

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
        Swal.fire(
            "Uh-Oh, something went wrong",
            response.status + '</br>' +
            response.statusText,
            "error"
        )
    }
    })
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
            let response = data
            $('.ticket-header').text(response.title)
            $('.ticket-description').text(response.description)
            Swal.fire(
                "Success!",
                "Ticket has been updated",
                "success"
            )
           

        }
    })
}