$(document).ready(function() {
    document.session = $('#session').val();
    
    setTimeout(requestInventory, 100);

    $('#send-button').click(function(event) {
        event.preventDefault();
        document.message = $('#message-text').val();
        jQuery.ajax({
            url: '//localhost:8888/chat',
            type: 'POST',
            data: {
                message: document.message,
                session: document.session,
                action: 'send'
            },

            dataType: 'json',
        
            beforeSend: function(xhr, settings) {
                
            },
            success: function(data, status, xhr) {
                $("#message-text").val('')
            }
        });
    });
});

function requestInventory() {
    var host = 'ws://localhost:8888/chat/status';
    var websocket = new WebSocket(host);
    websocket.onopen = function (evt) { };
    websocket.onmessage = function(evt) {
      console.log($.parseJSON(evt.data)['messageReturn'])
        var html = 
        '<li class="d-flex justify-content-between mb-4">' + 
                       
            '<div class="card">' +
              '<div class="card-header d-flex justify-content-between pb-2 px-3">' +
                '<p class="fw-bold mb-0" style="color:#aa5e81">'+ $.parseJSON(evt.data)['user'] +'</p>' + 
                  
              '</div>' + 
              '<div class="card-body pt-2 px-3">' + 
                '<p class="mb-0">' + 
                  $.parseJSON(evt.data)['messageReturn']
                '</p>' + 
              '</div>' +
            '</div>' +

          '</li>'
        $("#contain-message").append(html);
    };
    websocket.onerror = function (evt) { };
}