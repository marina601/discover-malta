 //jshint esversion: 6
 /*globals $:false */

 $( document ).ready(function() {
  
  // Code taken from https://api.jqueryui.com/datepicker/
  let today = new Date();
  let tomorrow = new Date(today);
  tomorrow.setDate(tomorrow.getDate() + 1);

  $(function () {
    $(".calendar").datepicker({
      dateFormat: 'yy-mm-dd',
      minDate: tomorrow,
      firstDay: 1,
    });
  });

  /**Prevent the user from manually adusting the date to past dates
   * and set the default date to tomorrow
   * This code has been sorced from 
   * https://stackoverflow.com/questions/8356358/jquery-date-picker-disable-past-dates
   */
  $(".calendar").change(function () {
    let updatedDate = $(this).val();
    let instance = $(this).data("datepicker");
    let date = $.datepicker.parseDate(instance.settings.dateFormat || $.datepicker._defaults.dateFormat, updatedDate, instance.settings);
  
    if (date < today) {
        alert("You must pick a date in the future");
        $(this).datepicker("setDate", tomorrow);
    }
  });

});