// Loop through all the plus buttons and increment the quantity
const addQuantity = document.querySelectorAll('.add-quantity')
console.log(addQuantity)
for (var i = 0; i < addQuantity.length; i++) { 
    $(addQuantity[i]).click(function(e) {
        e.preventDefault();
        let input = $(this).closest('.input-group').find('.qty_input')[0];
        let value = parseInt($(input).val());
        $(input).val(value + 1);
        console.log($(input).val())
        if ( $(input).val() > 7) {
            $(this).fadeOut()
            $(this).delay(5000).fadeIn()
            alert("You cannot add more than 9 adults. Please get in touch for large group bookings")
        }

        let itemId = $(this).data('item_id');
        

    });
}


// Remove quantity
const removeQuantity = document.querySelectorAll('.decrease-quantity')
for (var i = 0; i < removeQuantity.length; i++) { 
    $(removeQuantity[i]).click(function(e) {
        e.preventDefault();
        let input = $(this).closest('.input-group').find('.qty_input')[0];
        let value = parseInt($(input).val());
        
        if ( $(input).val() < 2) {
            $(this).fadeOut()
            $(this).delay(5000).fadeIn()
            alert("You need to have at least 1 adult selected!")
        }
        else {
            $(input).val(value - 1);
        }

        let itemId = $(this).data('item_id');
    });
}



