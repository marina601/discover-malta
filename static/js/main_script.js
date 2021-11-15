//jshint esversion: 6
//Initiates the toasts and hides the contentent within 5 seconds
let toastElList = [].slice.call(document.querySelectorAll('.toast'));
toastElList.map(function (toastEl) {
    let option = {
        animation: true,
        autohide: true,
        delay: 5000,
    };
let bsToast = new bootstrap.Toast(toastEl, option);
bsToast.show();
});


 /**Code for this function has been sourced from 
  * https://www.codegrepper.com/code-examples/javascript/auto+update+copyright+year+html
 */
// Sets copyright date in footer to current year
function getCurrentYear() {
    return new Date().getFullYear();
};
document.getElementById("copyright-year").innerHTML = getCurrentYear(); 
    