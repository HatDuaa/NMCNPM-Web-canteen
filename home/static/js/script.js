$(document).ready(function(){

    $('#menu-bar').click(function(){
        $(this).toggleClass('fa-times');
        $('.navbar').toggleClass('nav-toggle');
    });

    $(window).on('load scroll',function(){

        $('#menu-bar').removeClass('fa-times');
        $('.navbar').removeClass('nav-toggle');

        $('section').each(function(){

            let top = $(window).scrollTop();
            let height = $(this).height();
            let id = $(this).attr('id');
            let offset = $(this).offset().top - 200;

            if(top > offset && top < offset + height){
                $('.navbar ul li a').removeClass('active');
                $('.navbar').find(`[href="#${id}"]`).addClass('active');
            }

        });

    });

    $('.list .btn').click(function(){
        $(this).addClass('active').siblings().removeClass('active');
        let src = $(this).attr('data-src');
        $('.menu .row .image img').attr('src',src);
        var listItem = ["maindish","sidedish","drink","combo"];
        function removeAll(listItem) {
            listItem.forEach(function(item) {
                $(`.box-container .${item} .box.active`).removeClass('active')
            })
        }
        if(this.id === "menu1") {
            removeAll(listItem);
            $('.box-container .maindish .box').addClass('active')
        }
        if(this.id === "menu2") {
            removeAll(listItem);
            $('.box-container .sidedish .box').addClass('active')
        }
        if(this.id === "menu3") {
            removeAll(listItem);
            $('.box-container .drink .box').addClass('active')
        }
        if(this.id === "menu4") {
            removeAll(listItem);
            $('.box-container .combo .box').addClass('active')
        }
        
    });

});