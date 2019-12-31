$('#toggle_sidebar').on('click', function(){
    let sidebar = $('#sidebar-navigation');

    if (sidebar.hasClass('closed')){
        $(sidebar).removeClass('closed');
        $(sidebar).addClass('transition-open');
        setTimeout(function(){
                $(sidebar).removeClass('transition-open');
                $(sidebar).addClass('open'); 
        }, 100);
    }
    else{
        $(sidebar).removeClass('open');
        $(sidebar).addClass('transition-close'); 
        setTimeout(function(){
                $(sidebar).removeClass('transition-close');
                $(sidebar).addClass('closed'); 
        }, 500);                     
    }
});
