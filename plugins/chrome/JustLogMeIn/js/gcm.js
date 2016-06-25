/**
 * Created by snouto on 25/06/16.
 */
//registration callback


chrome.gcm.onMessage.addListener(function(request){
    payload = request.data;

    if(payload.command =='reload_sites'){

        //now reloading all sites available
        chrome.storage.local.get('account',function(data){

            var account = data.account;

            $.ajax({
                type:'POST',
                async:true,
                url:"http://127.0.0.1:5000/rest/account/reload",
                data:{username:account.username,authorizationId:account.authorization}
            })
                .done(function(response){

                    if(response.success){



                        chrome.storage.local.set({'sites':response.sites});

                    }

                });
        });
    }

});

chrome.runtime.onMessage.addListener(function(request,sender,senderResponse){

    var msg = request.msg;


    if(msg =='gcm_register'){
        chrome.storage.local.get("registered", function(result) {
            // If already registered, bail out.
            if (result["registered"])
                return;

            // Register in GCM using our Sender Id for the project
            var senderIds = ["903241980341"];
            chrome.gcm.register(senderIds, registrationCallBack);
        });
    }
});

function registrationCallBack(registrationId){
    if(chrome.runtime.lastError){

        console.log("Received an error , during registration : %s".format(chrome.runtime.lastError));
        return;
    }

    chrome.storage.local.get('account',function(account){

        var account_details = account.account;
        sendRegistrationId(account_details,registrationId,function(succeed) {
            // Once the registration token is received by your server,
            // set the flag such that register will not be invoked
            // next time when the app starts up.
            if (succeed){

                console.log("Registration Successful . ");
                chrome.storage.local.set({registered: true});
            }

        });

    });



};

function sendRegistrationId(account,registrationId,callback) {
    // Send the registration token to your application server
    // in a secure way.
    console.log("Received Registration Token : " + registrationId);
    response = $.ajax({
        type:'POST',
        async:true,
        url:"http://127.0.0.1:5000/rest/gcm/register",
        data:{username:account.username,registrationId:registrationId,appType:'chrome_plugin',authorizationId:account.authorization}
    }).done(function(data){

        if(data.status == 200){

            //jsonify the result
            var result_payload = JSON.parse(data.responseText);

            callback(result_payload.success);

        }else{
            callback(false);
        }

    });



};

