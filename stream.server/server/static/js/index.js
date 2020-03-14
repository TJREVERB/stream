let currfile = "";
function updateDisplay(){
    let url = 'https://cubesat-stream.sites.tjhsst.edu/captures'
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", url, false); // false for synchronous request
    xmlHttp.send();
    let json = JSON.parse(JSON.parse(xmlHttp.responseText));
    console.log(json);
    if(json.status != 0){
        console.log("ERROR REEE");
        return;
    }
    let filepath = json.image;
    if(filepath != currfile){
        let display = document.getElementById("display");
        display.src = filepath;
        currfile = filepath;
    }
}


window.onload = function(){
    setInterval(updateDisplay, 500);
};