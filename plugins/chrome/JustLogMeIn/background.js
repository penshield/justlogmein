//Clear everything
//chrome.storage.local.clear();
chrome.browserAction.setPopup({popup:'popup.html'});

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


