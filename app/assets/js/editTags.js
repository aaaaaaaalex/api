
(function(){

    IMG_ID = document.getElementById('imageView').getAttribute('data-imgID'),
    ADDED_TAGS = [],
    REMOVED_TAGS = [],
    
    
    newTag = function (tagName, tagID){
        if (tagID === null){
            tagID = -1;
        }
    
        var tagElem = document.createElement("SPAN");
        var tagWrapper = document.createElement("DIV");
        var closeBtn = document.createElement('I');
        var imgView = document.getElementById('classView');

        tagWrapper.classList.add('row');
        tagWrapper.classList.add('card');
        tagWrapper.classList.add('imageTag');
        tagWrapper.classList.add('deep-orange');
        tagWrapper.classList.add('lighten-4');

        tagElem.classList.add('col');
        tagElem.classList.add('s12');
        tagElem.setAttribute('data-cID', tagID);
        tagElem.innerText = tagName;
    
        closeBtn.setAttribute('data-type', 'close')
        closeBtn.innerText = 'x'
        closeBtn.classList.add('meterial-icons');
        closeBtn.classList.add('right');
    
        tagElem.appendChild(closeBtn);
        tagWrapper.appendChild(tagElem);
        imgView.appendChild(tagWrapper);
    },
    

    attachListeners = function () {
        var self = this;

        // delete tags functionality
        var classView = document.getElementById('classView');
        classView.addEventListener("click", function(e){
            var target = e.target;

            // ensure click came from an 'X'
            if (target.getAttribute('data-type') === 'close'){
                var tagID = target.parentElement.getAttribute('data-cID');
                var tagName = target.parentElement.innerText.trim().toLowerCase().split('\n')[0];


                console.log('added tags:');
                console.log(self.ADDED_TAGS);

                console.log("removed tags:");
                console.log(self.REMOVED_TAGS);
        
                // search for added tags to remove
                var i = 0, matchingIdx = -1;
                for(i = 0; i < self.ADDED_TAGS.length; i++){
                    if ( self.ADDED_TAGS[i] === tagName ){
                        matchingIdx = i;
                        break;
                    }
                }
                if (matchingIdx > -1) self.ADDED_TAGS = self.ADDED_TAGS.splice(matchingIdx, 1);
                
                // remove the element
                var tagElem = target.parentElement.parentElement;
                tagElem.parentElement.removeChild(tagElem);
    
                // return if there is already a duplicate in 'removed' list
                for(i = 0; i < self.REMOVED_TAGS.length; i++)
                    if (self.REMOVED_TAGS[i].name === tagName) return;
    
                //otherwise push removed tag (only if it's a known one)
                if (parseInt(tagID) !== -1) self.REMOVED_TAGS.push({'name': tagName, 'id': tagID});
            }
    
            return
        });
    
        // add a tag functionality
        var addTagBox = document.getElementById('tagBox');
        addTagBox.addEventListener("submit", function(e){
            e.preventDefault();

            var input = addTagBox.querySelector('input[type=text]');
            var tagName = input.value.trim().toLowerCase().toLowerCase().split('\n')[0];
            var tagID = -1;

            if (tagName.length < 2) return;
    
            var i = 0;
            //search for duplicated added-tag, break if exists
            for (i = 0; i < self.ADDED_TAGS.length; i++){
                var tn = self.ADDED_TAGS[i];
                if (tn === tagName) return;
            }
    
            //search if the tag has been removed previously
            var matchingIdx = -1;
            for (i = 0; i < self.REMOVED_TAGS.length; i++){
                var tag = self.REMOVED_TAGS[i];
                if (tag.name === tagName) {
                    tagID = tag.id;
                    matchingIdx = i;
                    break;
                }
            }
    
            if (matchingIdx > -1) self.REMOVED_TAGS = self.REMOVED_TAGS.splice(matchingIdx, 1);
            if (tagID === -1) self.ADDED_TAGS.push(tagName);
            self.newTag(tagName, tagID);

            input.value = ''
        });
    
        // finalise changes functionality
        var saveButton = document.getElementById('saveButton');
        saveButton.addEventListener('click', function(e){
            e.preventDefault();
            var fd = new FormData();
            var i = 0;
    
            // img id
            fd.append('imgID', self.IMG_ID);
    
            // added tag IDs
            for (i = 0; i < self.ADDED_TAGS.length; i++){
                fd.append('addTag', self.ADDED_TAGS[i]);
            }
    
            // removed ones
            for (i = 0; i < self.REMOVED_TAGS.length; i++){
                fd.append('removeTag', self.REMOVED_TAGS[i].id);
            }
    
            window.apiRequest(fd, 'newTags', function(){window.location.reload()});
        });
    },

    attachListeners();
})()
