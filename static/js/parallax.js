$(window).on('scroll', parallax);

function parallax(){
    //Obtener el nivel del scroll

    var s = $(window).scrollTop();

    //Efecto parallax para los fondos

    function parallaxBg(el,t){
        $(el).css({
            'background-attachment': 'fixed',
            'background-position': 'center ' + -(s*t) + 'px'
        })
    }

    //Efecto parallax para los Textos

    function parallaxFront(el,t){
        $(el).css({
            'position': 'relative',
            'top': -(s*t) + 'px'
        })
    }
    parallaxBg('body',.1);
    parallaxBg('footer',.1);
    parallaxFront('h1',2);
    parallaxFront('h2',.5);
    parallaxFront('.page',.4);
}
