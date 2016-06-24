/**
 * Created by snouto on 19/06/16.
 */
$(document).ready(function(){
    $.mobile.changePage.defaults.changeHash = false;
    $.mobile.hashListeningEnabled = false;
    $.mobile.pushStateEnabled = false;


    $(".ui-close-me").on('click',function(event){


        //now send a message to the background page ordering it to execute a script onto the content page
        chrome.runtime.sendMessage({message:'frame_close'});
    });

});