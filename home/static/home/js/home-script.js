//jshint esversion: 6
/*globals $:false */
$(document).ready(function () {
    $(document).scroll(function() {
        /**Display elements on scroll */
        var y = $(this).scrollTop();
        if (y > 400) {
            $('.card-info:hidden').each(function(index) {
                setTimeout(function(el) {
                    el.show(2000);
                }, index * 1500, $(this));
            });
        } else {
            $('.card-info').hide();
        }
    });
});
    
    