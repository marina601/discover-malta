//jshint esversion: 6


// Modal from bootstrap adding focus to an input element
var myModal = document.getElementById('exampleModal');
var myInput = document.getElementById('total_adults');

myModal.addEventListener('shown.bs.modal', function () {
    myInput.focus();
});
