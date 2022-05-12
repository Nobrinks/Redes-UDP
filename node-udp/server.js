const udp = require('dgram');

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
    console.log('Data received from client : ' + msg.toString());
    console.log('Received %d bytes from %s:%d\n', msg.length, info.address, info.port);
    //sending msg to the client
    var response = Buffer.from('From server : your msg is received');
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

server.bind(7788)