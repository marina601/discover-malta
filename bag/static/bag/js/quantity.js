//jshint esversion: 6
/*globals $:false */


/**Loop through all the plus buttons
 * Add event listener on click and prevent default behaviour
 * Find the closest input element
 * Do not allow more than 8 adult tickets booked in one time
 */
const addQuantity = document.querySelectorAll('.add-quantity');
for (var i = 0; i < addQuantity.length; i++) { 
    $(addQuantity[i]).click(function(e) {
        e.preventDefault();
        let input = $(this).closest('.input-group').find('.qty_input')[0];
        let value = parseInt($(input).val());
        $(input).val(value + 1);
        if ( $(input).val() > 7) {
            $(this).fadeOut();
            $(this).delay(5000).fadeIn();
            alert("You cannot add more than 8 adults. Please get in touch for large group bookings");
            $(input).val() = 8;
        }
    });
}


/**Remove quantity
 * Loop through all the minus buttons
 * Find the closest input element
 * If the value is less than 1 
 * Hide the button for 5 sec
 */
const removeQuantity = document.querySelectorAll('.decrease-quantity');
for (var i = 0; i < removeQuantity.length; i++) { 
    $(removeQuantity[i]).click(function(e) {
        e.preventDefault();
        let input = $(this).closest('.input-group').find('.qty_input')[0];
        let value = parseInt($(input).val());
        
        if ( $(input).val() < 1) {
            $(this).fadeOut();
            $(this).delay(5000).fadeIn();
            alert("You need to have at least 1 adult selected!");
        }
        else {
            $(input).val(value - 1);
        }
    });
}


/**Allow the child value to decrease to 0 */
const removeChildQty = document.querySelectorAll('.decrease-quantity-child');
for (var i = 0; i < removeChildQty.length; i++) { 
    $(removeChildQty[i]).click(function(e) {
        e.preventDefault();
        let input = $(this).closest('.input-group').find('.qty_input')[0];
        let value = parseInt($(input).val());
        
        if ( $(input).val() < 1) {
            $(this).fadeOut();
            $(this).delay(5000).fadeIn();
        }
        else {
            $(input).val(value - 1);
        }
    });
}

// Update link
$('.update-link').click(function(e) {
    const form = $(this).prev('.update-form');
    form.submit();
});

