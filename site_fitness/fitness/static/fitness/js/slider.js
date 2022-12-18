$(document).ready(function(){
    $('.slider').slick({
        dots: true,
        adaptiveHeight: true,
        slidesToShow: 3,
        speed: 1000,
        variableWidth: true,    
        centerMode: true,

        responsive: [
            {
              breakpoint: 1200,
              settings: {
                arrows: false
              }
            }
        ]
    });

});