function notificacion() {
    $.ajax({
        url: '/all/',
        type:'GET',
        datatype:'json',
        success: function(data) {
            ul = document.getElementById("all");
            text = ""
            aja = ""
            acti = ""
            for(i in data){
                if(data[i].activo){
                    aja = "<span class='material-icons lista-caja__activo'>wifi_tethering</span>"
                    acti = "<p class='tiempo_conexion'>Activo</p>"
                }else{
                    va = data[i].last_login
                    x = va.substring(0, 10)
                    h = va.substring(11, 19)
                    aja = "<span class='material-icons'>wifi_tethering</span>"
                    acti = "<p class='tiempo_conexion'> Ultima vez el " + x +  " a las " + h +"</p>"
                }

                text = text + "<a href='#' class='lista-caja__link'> <li class='lista-caja__user'>" + aja + data[i].username + acti + "</li></a>"
            }
            ul.innerHTML = text
            setTimeout(function (){ notificacion(); }, 1000 *30);
            }
         });
    }


function message(arg) {
    $.ajax({
    data : { 'id': arg },
    url: '/messages/',
    type:'GET',
    success: function(data) {
        console.log(data)
        if(data.validar){
          window.location.reload()
        }
        setTimeout(function (){ message(arg); }, 1000 *10);
      }
    });

}






/*
function obtenermsg() {
    if(!scrolling){
        $.get('/messages/', function(messages){
            $('#msg-list').html(messages)
            var charlist = document.getElementById('msg-list-div');
            charlist.scrollTop = charlist.scrollHeight;
        });
    }
    scrolling = false;
}

var scrolling = false;

/*
$(function(){
    $('#msg-list-div').on('scroll', function() {
        scrolling = true;
    });
    refreshTimer = setInterval(obtenermsg, 500)
});
*/
