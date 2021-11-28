//jshint esversion: 6


/* Modal from bootstrap adding focus to an input element
 * Check if the element exists
 */
var myModal = document.getElementById('exampleModal');
var myInput = document.getElementById('total_adults');

if (myModal) {
    myModal.addEventListener('shown.bs.modal', function () {
        myInput.focus();
    });
}
