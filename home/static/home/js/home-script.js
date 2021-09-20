 // Bootstrap code to initialize carousel
//  var myCarousel = document.querySelector('#myCarousel')
//  var carousel = new bootstrap.Carousel(myCarousel, {
//      interval: 2000,
//      wrap: false
//  });


 // Display the divs when the testemony-div is in view
//  $(function(){
 
//      if ($(".testimony-div").is(":visible")) {
//          console.log("the div is visible")
//          $('.card-info').each(function(i) {
//              $(this).delay(3000*i).toggle(1850);
//          });
//     } else {
//         $('.card-info').hide()
//     }

// $(function() {
//     if ($(".testimony-div").is(":visible")) {
//         console.log("I can see you")
//         $('.card-info:hidden').each(function(index) {
//             setTimeout(function(el) {
//                 el.toggle(2000);
//             }, index * 1000, $(this));
//         });
//     }
// });

$(document).scroll(function() {
    var y = $(this).scrollTop();
    if (y > 400) {
        $('.card-info:hidden').each(function(index) {
            setTimeout(function(el) {
                el.toggle(2000);
            }, index * 1000, $(this));
        });
    } else {
        $('.card-info').hide()
    }
});
    
    