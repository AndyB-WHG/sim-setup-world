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

enterSettingsButton = document.getElementById('enter-settings-button');

enterSettingsButton.addEventListener('click', function() {
    console.log("'Enter Settings' button clicked")
    car_name = document.getElementsByName('car_name')
    track_name = document.getElementsByName('track_name')
    console.log(car_name.text)
    console.log(track_name.text)
    if (car_name == "" || track_name == "") {
        getElementById('settings-section').innerHTML = "<h2>Please enter both a car name and and a track name</h2>"
    }

}, false);


