const udp = require('dgram');
const prompt = require("prompt-sync")();

let DEFAULT_IP_ADDRESS = "152.92.236.11"
let DEFAULT_IP_PORT = 9929

let address = prompt("Digite o IP: ");
address = address ? address : DEFAULT_IP_ADDRESS
let port = parseInt(prompt("Digite a porta: "))
port = port ? port : DEFAULT_IP_PORT

// --------------------creating a udp server --------------------//
const server = udp.createSocket('udp4');


//================ Server is listening
server.on('listening', function () {
    var address = server.address();
    var port = address.port;
    console.log('Server is listening at port ' + port);
});

//================ When receiving data from client 
server.on('message', function (msg, info) {
    let buffer_string = Buffer.from(msg).toString()
    console.log("Message from client: ", buffer_string);
    var data = JSON.parse(buffer_string)
    if (data.tipo === "int" && parseInt(data.val)) {
        var response = Buffer.from(`{"response": ${data.val + 1}}`)
    }
    else if (data.tipo === "char" && data.val.length === 1) {
        if (data.val === data.val.toLowerCase()) {
            var response = Buffer.from(`{"response": "${data.val.toUpperCase()}"}`)
        }
        else {
            var response = Buffer.from(`{"response": "${data.val.toLowerCase()}"}`)
        }
    }
    else if (data.tipo === "str") {
        var response = Buffer.from(`{"response": "${data.val.split("").reverse().join("")}"}`)
    }
    // var response = Buffer.from(`{"type": "int", "val": "${teste + 1}""`)
    // const m = Buffer.from(msg, 'utf8')
    // console.log(m['val'])
    // if (Number.isInteger(msg.val) && msg.tipo === 'int') {
    //     console.log('Data received from client : ' + msg.toString());
    //     console.log('Received %d bytes from %s:%d\n', msg.length, info.address, info.port);
    // }
    //sending msg to the client
    // `teste: ${var}`
    // Buffer.from(`{type: 'int', 'val': ${msg.val+1}}`);

    server.send(response, info.port, address, function (error) {
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