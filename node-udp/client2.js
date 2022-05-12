const udp = require('dgram');
const client = udp.createSocket('udp4');

client.on('message', function (msg, info) {
    console.log('Data received from server : ' + msg.toString());
    console.log('Received %d bytes from %s:%d\n', msg.length, info.address, info.port);
});

const data = Buffer.from('Hello server');

client.send(data, 7788, 'localhost', function (error) {
    if (error) {
        console.log(error);
        client.close();
    } else {
        console.log('Data is sent !');
    }
});