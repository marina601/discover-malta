 // Code taken from https://api.jqueryui.com/datepicker/
 $( function() {
    $( ".calendar" ).datepicker({
        dateFormat : 'dd-mm-yy',
        minDate : new Date(),
        firstDay: 1,
    });
   
  } );