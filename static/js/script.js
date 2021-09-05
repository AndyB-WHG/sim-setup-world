$(document).ready(function () {
    $('.sidenav').sidenav({edge: "right"});
    $('.collapsible').collapsible();
    $('.tooltipped').tooltip();
    $('select').formSelect();
});


// Adds a submit button to the page when a 'Sim' name is selected.

$("#sim_name").on('change', function() {
    // the following line of code was found at https://www.codegrepper.com/code-examples/javascript/how+to+get+the+option+text+from+dropdown+with+option+value+javascript
    var sim_name = this.options[this.selectedIndex].text;
    console.log(sim_name);
    document.getElementById('submit-setup-button-div').innerHTML = '<div class="col s12 center-align"><button id="submit-setup-button" type="submit" class="btn-large light-blue text-shadow">Automated Button Click<i class="fas fa-plus-square right"></i></button></div>'
    document.getElementById('submit-setup-button').click();
});

$("#car_name").on('change', function() {
    // the following line of code was found at https://www.codegrepper.com/code-examples/javascript/how+to+get+the+option+text+from+dropdown+with+option+value+javascript
    var car_name = this.options[this.selectedIndex].text;
    console.log(car_name);
});

$("#enter-settings-button").onclick, function() {
    console.log("Settings section ready to be rendered.")
    document.getElementById("settings-section").innerHTML = '<h1>Settings Go Here!</h1>'
};

