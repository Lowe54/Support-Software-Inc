$(document).ready(function(){
    $('#content-wrapper').addClass('col-lg-12');
});

$('#toggle_sidebar').on('click', function(){
    let sidebar = $('#sidebar-navigation');

    if (sidebar.hasClass('closed')){
        $(sidebar).removeClass('closed');
        $(sidebar).addClass('transition');
        $('#content-wrapper').removeClass('col-lg-12').addClass('col-lg-10'); 
               
        setTimeout(function(){
                $(sidebar).removeClass('transition');
                $(sidebar).addClass('open'); 
        }, 100);
    }
    else{
        $(sidebar).removeClass('open');
        $(sidebar).addClass('transition'); 
        setTimeout(function(){
                $(sidebar).removeClass('transition');
                $(sidebar).addClass('closed');
                $('#content-wrapper').removeClass('col-lg-10').addClass('col-lg-12'); 
        }, 500);
        
        
        
    }
});
