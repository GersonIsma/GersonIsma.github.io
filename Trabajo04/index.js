var app = require('express')();
var server = require('http').createServer(app);
var socket = require('socket.io');

// App setup
server.listen(3000, function(){
    console.log('listening for requests on port 3000,');
});

// Static files
app.use(express.static('public'));

// Socket setup & pass server
var io = socket(server);

io.on('connection', function(socket){
    console.log('made socket connection', socket.id);

    socket.on('chat',function(data){
        io.sockets.emit('chat',data);
    });

    socket.on('typing',function(data){
        socket.broadcast.emit('typing',data);
    });
});