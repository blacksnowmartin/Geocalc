//Live Tracking with JavaScript and WebSockets
const express = require('express');
const http = require('http');
const socketIo = require('socket.io');

const app = express();
const server = http.createServer(app);
const io = socketIo(server);

io.on('connection', (socket) => {
    console.log('A user connected');
    socket.on('location', (data) => {
        console.log('Received location data:', data);
        // Handle and store location data as needed
        // You can broadcast the data to all connected clients for live tracking
        socket.broadcast.emit('newLocation', data);
    });
});

server.listen(3000, () => {
    console.log('Server is running on http://localhost:3000');
});
