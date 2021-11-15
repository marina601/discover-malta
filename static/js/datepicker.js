 //jshint esversion: 6
 /*globals $:false */

 
 // Code taken from https://api.jqueryui.com/datepicker/
 $(function () {
   $(".calendar").datepicker({
     dateFormat: 'yy-mm-dd',
     minDate: new Date(),
     firstDay: 1,
   });
 });