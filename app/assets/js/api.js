window.apiRequest = function(file, endpoint, callback) {
    var xhr = new XMLHttpRequest();
    var endpoint = "/v1/" + endpoint;
    xhr.open('POST', endpoint, true);

    xhr.onload = callback;
    
    // Listen to the upload progress.
    xhr.upload.onprogress = function(e) {
        if (e.lengthComputable) {
            var prog = (e.loaded / e.total) * 100;
            console.log("Progress: " + prog.toString());
        }
    };
    
    xhr.send(file);
}