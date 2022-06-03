var loadJS = function(url, implementationCode, location){
    var scriptTag = document.createElement('script');
    scriptTag.src = url;

    scriptTag.onload = implementationCode;
    scriptTag.onreadystatechange = implementationCode;

    location.appendChild(scriptTag);
}; 
$(window).on('load', function() {
    if (/Android|webOS|iPhone|iPad|iPod|BlackBerry/i.test(navigator.userAgent)) {
      $('body').addClass('ios');   
    } else {
      $('body').addClass('web');
    };

    setTimeout(function(){
        $(".js-bg").each(function () {
          $(this).css('background-image', 'url(' + $(this).data("preload") + ')');
        });
        $(".js-img").each(function () {
          $(this).attr('src', $(this).data("src"));
        });
    }, 700);       
    setTimeout(function() {
        loadJS('js/components/jquery.maskedinput.min.js',maskedInput, document.body);
        loadJS('js/components/jquery.validate.min.js',validateInput, document.body);
    }, 800);
    setTimeout(function() {  
      $('body').removeClass('loaded');      
    }, 1000); 
    setTimeout(function() {
        $("head").append( '<link rel="preload preconnect" href="https://fonts.gstatic.com" as="style">' );
        $("head").append( '<link href="https://fonts.googleapis.com/css2?family=Jost:wght@300;400;500;600;700&family=Spartan:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">' );   
    }, 1100); 

    function maskedInput() {  
        if ($('input[type="tel"]').length) {
            $('input[type="tel"]').mask("+1 (999) 999-99-99");
            $.fn.setCursorPosition = function(pos) {
                if ($(this).get(0).setSelectionRange) {
                  $(this).get(0).setSelectionRange(pos, pos);
                } else if ($(this).get(0).createTextRange) {
                  var range = $(this).get(0).createTextRange();
                  range.collapse(true);
                  range.moveEnd('character', pos);
                  range.moveStart('character', pos);
                  range.select();
                }
            };
        
            $('input[type="tel"]').click(function(){
                $(this).setCursorPosition(4);
            });
        }
    }
    function validateInput() {  
      $("#form").validate({
        rules: {
          name: {
            required: true
          },
          tel: {
            required: true, 
           // minlength:9,
           // maxlength:15
          },
          email: {
            required: true, 
          },
          comment: {
            required: true, 
          },
        },        
        messages: {
            name: "Enter your name",  
            tel: "Enter your phone",
            email: "Enter your email",
            comment: "Enter your message", 
        }, 
      });
    }

});


/* viewport width */
function viewport() {
    var e = window,
        a = 'inner';
    if (!('innerWidth' in window)) {
        a = 'client';
        e = document.documentElement || document.body;
    }
    return {
        width: e[a + 'Width'],
        height: e[a + 'Height']
    }
};
/* viewport width */
$(function() {
    /* placeholder*/
    $('input, textarea').each(function() {
        var placeholder = $(this).attr('placeholder');
        $(this).focus(function() {
            $(this).attr('placeholder', '');
        });
        $(this).focusout(function() {
            $(this).attr('placeholder', placeholder);
        });
    });
    /* placeholder*/
    /*button open main nav begin*/
    $('.button-nav').on('click', function () {
        $('.header_nav').toggleClass('opened');
        $('html').toggleClass('noscroll-tablet');
        $(this).toggleClass('active');
        $('.navoverlay').toggleClass('active');
        return false;
    });
    $('.navoverlay').on('click', function () {
        $('.header_nav').removeClass('opened');
        $('html').removeClass('noscroll-tablet');
        $('.button-nav').removeClass('active');
        $('.navoverlay').removeClass('active');
    });
    /*button open main nav end*/

    if($('.js-welcome_slider').length){ 
        $('.js-welcome_slider').slick({
            dots: false,
            arrows:false,
            infinite: true,
            fade: false,
            speed: 500,
            slidesToShow: 1,
            slidesToScroll: 1, 
            prevArrow:'<button type="button" data-role="none" class="slick-prev slick-arrow" aria-label="Previous" role="button"><span class="icon-arr"></span</button>',
            nextArrow:'<button type="button" data-role="none" class="slick-next slick-arrow" aria-label="Next" role="button"><span class="icon-arr"></span></button>',  
            responsive: [
              {
                breakpoint: 1023,
                settings: {
                  arrows:true,
                  prevArrow:'<button type="button" data-role="none" class="slick-prev slick-arrow" aria-label="Previous" role="button"><span class="icon-arr"></span</button>',
            nextArrow:'<button type="button" data-role="none" class="slick-next slick-arrow" aria-label="Next" role="button"><span class="icon-arr"></span></button>',  
                }
              }
            ]
        });
    }

    //header_categ_opener
    $('.header_categ_opener').on('click', function () {
        $('.header_categ_drop').toggleClass('opened');
        $(this).toggleClass('active');
        return false;
    });

    //
    $(document).mouseup(function(e) {
        var container = $(".header_categ");
        if (!container.is(e.target) && container.has(e.target).length === 0)     {
            $('.header_categ_opener').removeClass('active');
            $('.header_categ_drop').removeClass('opened');
        }
    });

    //js-local
    $('.js-local').on('click', function () {
        var target = $(this).attr('href');
        $('html, body').animate({
            scrollTop: $(target).offset().top 
        }, 700);
        $('.header_nav').removeClass('opened');
        $('html').removeClass('noscroll-tablet');
        $('.button-nav').removeClass('active');
        $('.navoverlay').removeClass('active');
        return false;
    });


});

var handler = function() {
    var height_footer = $('footer').height();
    var height_header = $('header').height();
    var viewport_wid = viewport().width;
    var viewport_height = viewport().height;
    $('.js-vh').css({'height': $(window).height()});

    if (viewport_wid <= 767) {
       
    } else {
        
    }

}
$(window).bind('load', handler);
$(window).bind('resize', handler);

