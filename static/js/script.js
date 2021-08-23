$(document).ready(function () {
    $('.sidenav').sidenav({edge: "right"});
    $('.collapsible').collapsible();
    $('.tooltipped').tooltip();
    $('select').formSelect();
});

// function getCarList()
// var instance = M.FormSelect.getInstance(elem);


$("#sim-name").on('change', function() {
    console.log($(this));
    console.log("option selected!")
    
});
