$(document).ready(function(){
    $('#content-wrapper').addClass('col-lg-12');
    if (!localStorage.getItem('demositeagreed')) {
        Swal.fire({
            text: 'This is a demo version of the site, emails are DISABLED',
            icon: 'warning',
            timer: 5000,
            confirmButtonText: 'Understood',
            toast: true,
            position: 'top-right',
            show_timer: true,

        }).then((result) => {
            if (result.value) {
              localStorage.setItem('demositeagreed', '1');
            }
          });
    }

    $(function() {
        $('.btn-group-fab').on('click', '.btn', function() {
          $('.btn-group-fab').toggleClass('active');
        });
        $('has-tooltip').tooltip();
      });
});

$('#intro-start').on('click', function(){
    $('.btn-group-fab').toggleClass('active');
    introJs().start();
});

$('#toggle_sidebar').on('click', function(){
    let sidebar = $('#sidebar-navigation');

    if (sidebar.hasClass('closed')){
        $(this).addClass('open');
        $(sidebar).removeClass('closed');
        $(sidebar).addClass('transition');
        $('#toggle_sidebar i').addClass('fa-times');
        $('#toggle_sidebar i').removeClass('fa-bars');
        $('#content-wrapper').removeClass('col-lg-12').addClass('col-lg-10'); 
               
        setTimeout(function(){
                $(sidebar).removeClass('transition');
                $(sidebar).addClass('open'); 
        }, 100);
    }
    else{
        $(this).removeClass('open');
        $(sidebar).removeClass('open');
        $(sidebar).addClass('transition'); 
        setTimeout(function(){
                $(sidebar).removeClass('transition');
                $(sidebar).addClass('closed');
                $('#toggle_sidebar i').addClass('fab fa-bars');
                $('#toggle_sidebar i').removeClass('fa-times');
                $('#content-wrapper').removeClass('col-lg-10').addClass('col-lg-12'); 
        }, 500);
        
        
        
    }
});

$('.purchase-toggle').on('click', function(e){
    e.preventDefault();

    $.ajax({
        url: '/payment/form/',
        type: "POST",
        success: function(response){
            $('#payment-modal').remove();
            $('body').append(response);
            $('#payment-modal').modal();
            stripe_init();
        }
    });
});


// CSRF PROTECTION - REQUIRED FOR AJAX CALLS

$(function() {


    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});