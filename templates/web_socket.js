$(document).ready(function() {
    var url = "http://" + document.domain + ":" + location.port;
    var socket = io.connect(url + "/socketio");
    $("#textform").submit(function(event) {
        socket.emit('text', {'text': $('#text').val()});
        $('#text').val('');
        return false;
    });
    socket.on('text', function(msg) {
        $("#text-list").prepend('<h3>' + msg.text + '<h3>');
    });
    socket.on('msg', function(msg) {
        $("#counter").html(msg.count);
    });
});
