$(document).ready(function(){
    

    var myurl = document.getElementById('url').getAttribute("name");
    $('.btn-ExitSystem').on('click', function(e){
        e.preventDefault();
        swal({ 
            title: "Quieres Eliminar este Elemento?",   
            text: "Se eliminara todo su contenido",   
            type: "warning",   
            showCancelButton: true,   
            confirmButtonColor: "#DD6B55",   
            confirmButtonText: "Si",
            animation: "slide-from-top",   
            closeOnConfirm: false,
            cancelButtonText: "Cancelar"
        }, function(){   
            window.location= myurl ; 
        });
    }); 
})(jQuery);