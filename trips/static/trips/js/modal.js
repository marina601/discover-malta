//jshint esversion: 6
// Modal from bootstrap adding focus to an input
var myModal = document.getElementById('exampleModal');
var myInput = document.getElementById('total_adults');

myModal.addEventListener('shown.bs.modal', function () {
    myInput.focus();
});

// //Delete Modal
// $('#myModal').on('shown.bs.modal', function () {
//     $('#myInput').trigger('focus');
// });