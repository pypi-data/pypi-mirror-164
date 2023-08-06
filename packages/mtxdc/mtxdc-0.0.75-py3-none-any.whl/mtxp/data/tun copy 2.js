const net = require('node:net');

console.log("tun start", process.argv)

const argv = process.argv;

argv.shift() //node
argv.shift() //tun.js
const lHost = process.argv[0]
const lPort = Number.parseInt(process.argv[1]);
const rHost = process.argv[2]
const rPort = Number.parseInt(process.argv[3]);

console.log(` args: lHost:${lHost}: lPort:${lPort}-> rHost:${rHost}:${rPort}`)

const XORKEY = 81

const Xor = (buffer) => {
    for (let i = 0; i < buffer.byteLength; i++) {
        buffer[i] = buffer[i] ^ XORKEY;
    }
    return buffer;
}

const server = net.createServer((c) => {
    // 'connection' listener.
    console.log(`client connected ${rHost} ${rPort}`)
    //接收缓存。
    const receiveBuff = []
    const client = net.createConnection(
        {
            port: rPort,
            host: rHost,
            // localAddress: lhost,
        }, () => {
            console.log("connected to remote")
        });
    // c.on("data", function (data) {
    //     console.log(`<=${data.length}`)
    //     const dec = Xor(data)
    //     // console.log(`client  decoded : \r${dec}`)
    //     server.write(dec);
    // });
    // client.on("end", function () {
    //   console.log("dest disconnected ");
    // });
    // client.on("error", function (err) {
    //   console.log("dest=" + err);
    //   // sock.destroy();
    // });
    c.on('end', () => {
        console.log('client disconnected');
    });
    // c.write('hello\r\n');
    // c.pipe(c);
});
server.on('error', (err) => {
    throw err;
});
server.listen(lPort, () => {
    console.log('server bound');
});