(function dashboard() {

    submitListener = function(e) {
        var classes = document.getElementById('classes');
        var classnames = classes.value.split(',');

        var fd = new FormData();
        for (var i = 0; i < classnames.length; i++){
            fd.append('class', classnames[i]);
        }

        window.apiRequest(fd, 'spawnInstance', function(){window.location.reload()});
    },
        
    init = function() {
        document.getElementById('submitNewModel').addEventListener('click', this.submitListener);
    },

    init();
})()