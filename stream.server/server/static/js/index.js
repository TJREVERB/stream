let currfile = "";
let filenames = [];
let live = true;
var slider, button, display, output, recording, playbutton, speedinput;
let playing = false;
let speed = 0.0;
let counter = 0;
function updateDisplay(){
    let url = 'https://cubesat-stream.sites.tjhsst.edu/captures'
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", url, false); // false for synchronous request
    xmlHttp.send();
    let json = JSON.parse(xmlHttp.responseText);
//    console.log(json);
    if(json.status != 0){
        console.log("ERROR REEE");
        return;
    }
    let filepaths = json.image;
    filepaths = filepaths.sort();
    for(let i = 0; i < filepaths.length; i++){
        let filepath = filepaths[i];
        if(!filenames.includes(filepath)){
            filenames.push(filepath);            
        }
    }
    let slider = document.getElementById("myRange");
    slider.max = filenames.length;
    if(live){
        slider.value = slider.max;
        change();
        counter = 0;
    }
    else{
        counter += 0.1;
        if(counter * speed >= 1){
            slider.value = parseInt(slider.value) + 1;
            change();
            counter = 0;
        }
    }
}

function change() {
    output.innerHTML = "Frame: " + slider.value;
    display.src = filenames[parseInt(slider.value) - 1];
}

function play(){
    if(playing){
        // Pause
        speed = 0.0;
        playbutton.innerHTML = "Play";
        playing = false;
    }
    else{
        // Play
        playing = true;
        speed = speedinput.value;
        playbutton.innerHTML = "Pause";
    }
}


function switchMode(){
    console.log(live);
    live = !live;
    if(live){
        button.innerHTML = "Switch to recording mode";
        recording.style.display = "none";
    }
    else{
        button.innerHTML = "Switch to live mode";
        slider.value = slider.max;
        recording.style.display = "block";
        change();
    }
}


window.onload = function(){
    slider = document.getElementById("myRange");
    button = document.getElementById("mode");
    display = document.getElementById("display");
    output = document.getElementById("label");
    recording = document.getElementById("recording");
    playbutton = document.getElementById("play");
    speedinput = document.getElementById("speed");
    setInterval(updateDisplay, 100);
    slider.onchange = change;
    slider.value = 1;
    change();
};