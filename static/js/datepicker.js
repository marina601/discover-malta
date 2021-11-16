 //jshint esversion: 6
 /*globals $:false */

 
 // Code taken from https://api.jqueryui.com/datepicker/
 const today = new Date()
 const tomorrow = new Date(today)
 tomorrow.setDate(tomorrow.getDate() + 1) 

$(function () {
  $(".calendar").datepicker({
    dateFormat: 'yy-mm-dd',
    minDate: tomorrow,
    firstDay: 1,
  });
});