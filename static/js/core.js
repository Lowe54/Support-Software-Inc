$('#toggle_sidebar').on('click', function(){
    let sidebar = $('#sidebar-navigation');

    if (sidebar.hasClass('closed')){
        $(sidebar).removeClass('closed');
        $(sidebar).addClass('transition');
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
        }, 500);                     
    }
});
