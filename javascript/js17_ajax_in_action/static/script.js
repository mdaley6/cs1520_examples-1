function makePost() {
    let xhr = new XMLHttpRequest();

    if (!xhr) {
        console.log("Could not create an XMLHttpRequest instance");
        return false;
    }
    //why is xhr being passed as a local var to logResponse instead of being global
    //	if button was clicked fast as fuck, second click would overwite prev xhr object
    //  every req we make has diff XMLHTTP object w/ data from that req encoded
    //  we need to hangle the xth req with the xth XMLHTTP object was created from the req
    xhr.onreadystatechange = () => logResponse(xhr);
    //we use arrow fn to crete a closure 
    //  bc xhr refs value in contating scope
    //  so we keep ref to XML object for req that we are currently handling
    //  and also a way to get around not beung able to pass args to fn assigned to event handlers

    xhr.open("POST", "/new_item");
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

    var data;
    data = `one=${document.getElementById("a").value}&two=${document.getElementById("b").value}&three=${document.getElementById("c").value}`;

    xhr.send(data);
}

function logResponse(xhr) {
    console.log(`readyState: ${xhr.readyState}`);
    if (xhr.readyState === XMLHttpRequest.DONE) {
        console.log(`status: ${xhr.status}`);
        if (xhr.status === 200) {
            console.log("Value sent to server!");
        } else {
            console.log("There was a problem with the request.");
        }
    }
}

function setup() {
    document.getElementById("theButton").addEventListener("click", makePost);
}

window.addEventListener("load", setup);