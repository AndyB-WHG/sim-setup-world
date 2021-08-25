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
    document.getElementById('submit-setup-button').click() 
});

$("#car_name").on('change', function() {
    // the following line of code was found at https://www.codegrepper.com/code-examples/javascript/how+to+get+the+option+text+from+dropdown+with+option+value+javascript
    var car_name = this.options[this.selectedIndex].text;
    console.log(car_name);    

    // $("#pageTitle").html("<h1>Hello, World!</h1>");

    // $("#car-name").html("<option value='' disabled selected></i>Select Car</option>" +
    //     "{% set car_count = {'total': 0} %} + 
    //     "{%- for car in cars -%}" +
    //     "{% if car.sim_name =" + sim_name + "%}" +
    //         "{% if car_count.update({'total': car_count.total + 1}) %}{% endif %}" +
    //             "<option value='{{count.total}}'>{{ car.car_name }}</option>" +
    //     "{%- endfor -%}");
});
