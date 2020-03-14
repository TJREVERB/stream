let currfile = "";
let filenames = [];
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
    slider.value = slider.max;
}


window.onload = function(){
    setInterval(updateDisplay, 500);
    var slider = document.getElementById("myRange");
    var output = document.getElementById("demo");
    output.innerHTML = slider.value; // Display the default slider value

    // Update the current slider value (each time you drag the slider handle)
    slider.oninput = function() {
      output.innerHTML = this.value;
      let display = document.getElementById("display");
      display.src = filenames[parseInt(this.value) - 1];
    } 
};