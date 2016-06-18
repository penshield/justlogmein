/**
 * Created by snouto on 16/06/16.
 */

//this script will read from chrome storage api , the account details
$(document).ready(function(){

    var email = $(".ui-icon-power");
    var sites_count = $("#numSites");

    chrome.storage.local.get('account',function(data){

        //alert(data.account.email);
        email.text(data.account.email);

    });

    chrome.storage.local.get('sites',function(data){

        sites_count.text(data.sites.length);
    });
});