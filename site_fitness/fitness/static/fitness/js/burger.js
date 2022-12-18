$(document).ready(function(){
    $('.header__burger').click(function(event){
        $('.header__burger,.header__menu').toggleClass('active');
        $('body').toggleClass('lock');
    });
});
$(document).on('mouseup', function(e){
    let s = $('.header__burger,.header__menu');
    if(!s.is(e.target) && s.has(e.target).length === 0) {
      s.removeClass('active');
    }
});