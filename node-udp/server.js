const udp = require('dgram');
const prompt = require("prompt-sync")();

const address = prompt("Digite o IP: ");
const port = parseInt(prompt("Digite a porta: "))

// --------------------creating a udp server --------------------//
const server = udp.createSocket('udp4');


//================ Server is listening
server.on('listening', function () {
    var address = server.address();
    var port = address.port;
    console.log('Server is listening at port' + port);
});

//================ When receiving data from client 
server.on('message', function (msg, info) {
    let buffer_string = Buffer.from(msg).toString()
    console.log("Message from client: ", buffer_string);
    var data = JSON.parse(buffer_string)
    if(data.type === "int" && parseInt(data.val)){
        var response = Buffer.from(`${data.val + 1}`)
    }
    else if(data.type === "char" && data.val.length === 1){
        if(data.val === data.val.toLowerCase()){
            var response = Buffer.from(`{"response": "${data.val.toUpperCase()}"}`)
        }
        else{
            var response = Buffer.from(`{"response": "${data.val.toLowerCase()}"}`)
        }
    }
    else if(data.type === "str"){
        var response = Buffer.from(`{"response": "${data.val.split("").reverse().join("")}"}`)
    }
    // var response = Buffer.from(`{"type": "int", "val": "${teste + 1}""`)
    // const m = Buffer.from(msg, 'utf8')
    // console.log(m['val'])
    // if (Number.isInteger(msg.val) && msg.type === 'int') {
    //     console.log('Data received from client : ' + msg.toString());
    //     console.log('Received %d bytes from %s:%d\n', msg.length, info.address, info.port);
    // }
    //sending msg to the client
    // `teste: ${var}`
    // Buffer.from(`{type: 'int', 'val': ${msg.val+1}}`);

    server.send(response, info.port, 'localhost', function (error) {
        if (error) {
            client.close();
        } else {
            console.log('Data sent !');
        }
    });
});

//================ if an error occurs
server.on('error', function (error) {
    console.log('Error: ' + error);
    server.close();
});

server.bind(port)
// server.addSourceSpecificMembership(address)