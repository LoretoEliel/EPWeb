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
    var ti = new Date().getTime();
    $.ajax({
        data : { 'id': arg },
        url: '/messages/',
        type:'GET',
        success: function(data) {
            if(data.validar === undefined){
                var i; 
                for (i in data){
                    if(i > arg){
                        arg = i;
                    }
                    crearCaja(1, data[i].user, data[i].mesage, data[i].enviado); 
                }

                var charlist = document.getElementById('msg-list-div');
                charlist.scrollTop = charlist.scrollHeight;
            }
            var tf = new Date().getTime();
            var time = 1000 * 10;
            time -= tf - ti;
            if(time < 0) {
                message(arg);   
            }else{
                setTimeout(function (){ message(arg); }, time);
            }
        }
    });

}
function crearCaja(orientacion, usuario, mensaje, fecha){
    var tipo = "enviado";
    var tipo2 = "right";
    if(orientacion == 1){
        tipo="recibido";
        tipo2 = "left";
    }
    var x = fecha.substring(0, 10);
    var h = fecha.substring(11, 19);
    var text = "<div class='chat-caja__mensaje "+tipo+"'><div class='chat-caja__nombre'><h2>" +  usuario + "</h2></div><p class='chat-caja__content "+tipo2+"'> "+ mensaje + "</p>"  + "<p class='chat-caja__fecha'> Ultima vez el " + x +  " a las " + h +"</p>" + "</div>";
    document.getElementById('msg-list').innerHTML += text;
}


function enviar(user) {
    var msg = document.getElementById("id_mensaje").value;   
    if(msg != ""){
        var time = new Date().getTime(); 
        acti = "<p class='chat-caja__fecha' id = '"+ time +"'></p>"
        var text = "<div class='chat-caja__mensaje enviado'><div class='chat-caja__nombre'><h2>" +  user + "</h2></div> <p class='chat-caja__content right'> "+ msg + "</p>"  + acti + "</div>"
        $('#msg-list').append(text);
        $('#id_mensaje').val('');
        $.ajax({
            url: '/createbox/',
            type:'POST',
            datatype:'json',
            data:{
                'csrfmiddlewaretoken': document.getElementsByName("csrfmiddlewaretoken")[0].value ,
                'ced':msg
            },
            success:function(data){
                ver = data.ver
                text = " "
                if(data.validar){
                   va = ver.enviado
                   x = va.substring(0, 10)
                   h = va.substring(11, 19)
                   document.getElementById(time).innerHTML= "Ultima vez el"  + x +  " a las "  + h;
               }               
               var charlist = document.getElementById('msg-list-div');
               charlist.scrollTop = charlist.scrollHeight;
           }
       })
    }             
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
