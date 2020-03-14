let currfile = "";
let filenames = [];
let live = true;
function updateDisplay(){
    let url = 'https://cubesat-stream.sites.tjhsst.edu/captures'
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", url, false); // false for synchronous request
    xmlHttp.send();
    let json = JSON.parse(xmlHttp.responseText);
    console.log(json);
    if(json.status != 0){
        console.log("ERROR REEE");
        return;
    }
    let filepaths = json.image;
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
    }
}

function change() {
    let slider = document.getElementById("myRange");
    let output = document.getElementById("demo");
    output.innerHTML = slider.value;
    let display = document.getElementById("display");
    display.src = filenames[parseInt(slider.value) - 1];
} 

function switchMode(){
    console.log(live);
    live = !live;
    let slider = document.getElementById("myRange");
    let button = document.getElementById("mode");
    if(live){
        button.innerHTML = "Switch to recording mode";
    }
    else{
        button.innerHTML = "Switch to live mode";
        slider.value = slider.max;
        change();
    }
}


window.onload = function(){
    setInterval(updateDisplay, 500);
    var slider = document.getElementById("myRange");
    var output = document.getElementById("demo");
    output.innerHTML = slider.value; // Display the default slider value
    slider.oninput = change;
};