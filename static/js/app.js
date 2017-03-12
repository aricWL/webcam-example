var player = videojs("myVideo",
{
    controls: true,
    width: 640,
    height: 360,
    plugins: {
        record: {
            audio: true,
            video: true,
            maxLength: 60 * 30,
            debug: true
        }
    }
});

// error handling
player.on('deviceError', function() {
    console.log('device error:', player.deviceErrorCode);
});

player.on('error', function(error) {
    console.log('error:', error);
});

// user clicked the record button and started recording
player.on('startRecord', function() {
    console.log('started recording!');
});

// user completed recording and stream is available
player.on('finishRecord', function() {
    // the blob object contains the recorded data that
    // can be downloaded by the user, stored on server etc.
    console.log('finished recording: ', player.recordedData);

    var fd = new FormData();
    fd.append('fname', 'video_' + Date.now() + '.webm');
    fd.append('data', player.recordedData.video);
    $.ajax({
        type: 'POST',
        url: '/video',
        data: fd,
        processData: false,
        contentType: false
    }).done(function(data) {
        console.log(data);
    });

});
