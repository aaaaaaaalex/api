(function overrideForm(){

    var fileInput = document.getElementById('fileInput');
    fileInput.addEventListener('change', function(e){
        var formData = new FormData();
        formData.append('image', fileInput.files[0]);

        window.apiRequest(formData, 'newImage', function(e) {
            response = e.target;
    
            console.log(response);
            if (response.status === 200){
                var classification = JSON.parse(response.response);
                var imgID = classification.imgID;
                var viewImgURL = "/images/" + imgID;
                window.location.href = viewImgURL;
            }
        });
    }, false);

})()