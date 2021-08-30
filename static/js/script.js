$(document).ready(function () {
    $('.sidenav').sidenav({edge: "right"});
    $('.collapsible').collapsible();
    $('.tooltipped').tooltip();
    $('select').formSelect();
});

// function getCarList()
// var instance = M.FormSelect.getInstance(elem);


$("#sim_name").on('change', function() {
    // the following line of code was found at https://www.codegrepper.com/code-examples/javascript/how+to+get+the+option+text+from+dropdown+with+option+value+javascript
    var sim_name = this.options[this.selectedIndex].text;
    console.log(sim_name);
    // document.getElementById('submit-setup-button').click() 
});

$("#car_name").on('change', function() {
    // the following line of code was found at https://www.codegrepper.com/code-examples/javascript/how+to+get+the+option+text+from+dropdown+with+option+value+javascript
    var car_name = this.options[this.selectedIndex].text;
    console.log(car_name);


});