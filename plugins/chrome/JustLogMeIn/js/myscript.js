/**
 * Created by snouto on 14/06/16.
 */


$(document).ready(function(){



    $(".ui-pop-out").click(function(){

        chrome.tabs.create({url:'../pages/index.html'});

    });


    $("#mainForm").on('submit',function(event){

        var current_form = this;
        var username = $('#username');
        var password = $('#password');
        var numSites = $("#numberofSites");
        var finalResult = false;

        response = $.ajax({
            type:'POST',
            async:false,
            url:"http://127.0.0.1:5000/rest/login",
            data:{username:username.val(),password:password.val()}
        });

        if(response.status != 200){
            event.preventDefault();
            event.stopPropagation();
            alert('We are unable to log you , Please contact us or try again!');
            finalResult = false;
            return finalResult;
        }else{

            data = JSON.parse(response.responseText);

            if(!data.success){
                event.preventDefault();
                event.stopPropagation();
                alert('Incorrect username and/or password.');
                finalResult = false;
            }else
            {
                $(".ui-li-count").text(data.sites.length);
                //$("#mainListView").listview('refresh');
                //access the sites
                chrome.storage.local.set({'sites':data.sites,'account':data.account});
                chrome.browserAction.setPopup({popup:'pages/index.html'});
                finalResult= true;
            }
            return finalResult;

        }






    });

    //the saved Sites link
    $("#savedSites").click(function(){

        $.mobile.navigate("#sites",{history:true,transition:'slide'});

    });



    //bind the logout button
    $(".ui-icon-power").click(function(){



        chrome.storage.local.clear();
        chrome.browserAction.setPopup({popup:'popup.html'});
        window.close();
    });

    $("#firstPage").on('pagebeforecreate',function(event){

        chrome.storage.local.get("sites",function(obj){

            sites = obj.sites;

            $(".ui-li-count").text(sites.length);
            $("#mainListView").listview('refresh');

        });

    });

    $("#sites").on('pagebeforecreate',function(event){

        var sites = [];
        //access the sites from the storage
        sites = chrome.storage.local.get("sites",function(obj){

            sites = obj.sites;
            if(sites != null){

                for(i = 0 ;i < sites.length;i++){

                    var site = sites[i];
                    $("#siteslistview").append("<li><a href='#"+site.id+"''>"+site.name+"</a></li>");

                }

                $("#siteslistview").listview('refresh');
                $("#siteslistview").scrollview();
            }
        });



    });
});