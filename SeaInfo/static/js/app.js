
var dropdown_options = document.querySelectorAll("#map_dates")
var image = document.getElementById("map")
var dropdown_button = document.querySelector("#dropdownMenuButton")
var animate_button = document.querySelector("#animate")

var end_url = ".windir.gif";
var res = image.src.slice(0, 84);
var cur_index = 0;

dropdown_button.textContent = dropdown_options[0].text

animate_button.addEventListener('click',go_anim)

for (let index = 0; index < dropdown_options.length; index++) {
    dropdown_options[index].addEventListener("click", function () {
        animate(this);
        cur_index = index;
    });
}

function animate(object,some_index){
    var v = object.name;
    dropdown_button.textContent = object.text
    image.src = res + v + end_url;
}


function go_anim() {
    if (animate_button.textContent == "Animate") {
        animate_button.textContent = "Stop";
        clock();
    }
    else {
        animate_button.textContent = "Animate";
    }
}

function clock() {
    if (animate_button.textContent=="Stop") {
        if (cur_index < dropdown_options.length ) {
            animate(dropdown_options[cur_index]);
            cur_index++
        }
        else {
            cur_index = 0;
            animate(dropdown_options[cur_index]);
        }
        setTimeout("clock()", 1000);          
    }
}


