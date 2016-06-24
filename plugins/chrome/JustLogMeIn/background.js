//Clear everything
//chrome.storage.local.clear();
//chrome.browserAction.setPopup({popup:'popup.html'});


//add listener for removing tabs
chrome.tabs.onRemoved.addListener(function(id,info){

    chrome.browserAction.setBadgeText({text:""});
});

chrome.runtime.onMessage.addListener(function(response,sender,senderResponse){

    if(response.message =="starting"){

        chrome.storage.local.get('sites',function(data){

            if(data != null){

                sites = data.sites;

                if (sites != null && sites.length > 0)
                {
                    chrome.browserAction.setPopup({popup:'pages/index.html'});
                }else{
                    chrome.browserAction.setPopup({popup:'popup.html'});
                }
            }else
            {
                chrome.browserAction.setPopup({popup:'popup.html'});
            }

        });

    }else if (response.message == "update_badge"){

        if(response.payload > 0)
        {

            chrome.browserAction.setBadgeText({text:response.payload.toString()});
        }else{
            chrome.browserAction.setBadgeText({text:''});
        }
    }else if (response.message == "frame_close"){

        //now execute a specific script onto the content page
        chrome.tabs.executeScript(null,{code:"var frame = document.getElementById('embeddedFrame');frame.remove();"},function(result){

            //TODO : Remove me
            console.log("Command executed successfully on the Content Page");
        });
    }else if (response.message == 'matched_website'){

        //get the iframe
        var iframe = response.iframe_obj;

        if(iframe != null && iframe != undefined){

            //access the contents of the iframe
            var iframe_document = iframe.src;

            if(iframe_document != null && iframe_document != undefined){

                //access the one div element within that document
                var one = iframe_document.getElementById('one');

                one.innerHTML = "<h2>Hello World</h2>";
            }

        }
    }else if (response.message == 'set_field'){

        //execute a specific function
        chrome.tabs.executeScript(null,{code:"setField('"+response.payload+"')"});
    }

});

chrome.browserAction.onClicked.addListener(function(tab){


    chrome.storage.local.get('sites',function(data){

        if(data != null){

            sites = data.sites;


            if (sites != null && sites.length > 0)
            {
                chrome.browserAction.setPopup({popup:'pages/index.html'});
            }else{
                chrome.browserAction.setPopup({popup:'popup.html'});
            }
        }else
        {
            chrome.browserAction.setPopup({popup:'popup.html'});
        }

    });


});


