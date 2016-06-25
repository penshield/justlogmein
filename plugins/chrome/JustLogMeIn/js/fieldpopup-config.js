/**
 * Created by snouto on 19/06/16.
 */


    $(document).ready(function(){


        chrome.storage.local.get('matched_site',function(data){

            site = data.matched_site;
            input = data.input;
            password = data.password;

            if(site != null && site != undefined){

                //access the data
                var title  = $(".ui-site-title");
                var fieldsList = $("#fields-list").listview();
                title.innerHTML = site.host;
                /*one.innerHTML = "<h3>"+ site.host + "</h3>";
                 one.innerHTML += "<p>"+"<i>User Name</i> : " + site.credentials.username+"</p>";*/
                if (site.fields != undefined && site.fields != null){

                    //now loop over them
                    for(i =0;i<site.fields.length;i++){
                        var current_field = site.fields[i];
                        //get the field name and value
                        var item  = document.createElement('li');
                        item.setAttribute('list-field-name',current_field.name);
                        if(current_field['type'] == 'password'){
                            item.innerHTML ="<a href='#' class='ui-btn ui-btn-icon-right ui-icon-carat-r'><h3>Field : "+ current_field.name +"</h3><p>"+"**********"+"</p></a>";
                        }else{
                            item.innerHTML ="<a href='#' class='ui-btn ui-btn-icon-right ui-icon-carat-r'><h3>Field : "+ current_field.name +"</h3><p>"+current_field.value+"</p></a>";
                        }
                        item.onclick = function(){
                            var attr_value = this.attributes['list-field-name'];
                            //now send a message
                            chrome.runtime.sendMessage({message:'set_field',payload:attr_value.value});

                        };
                        //now append it into the list item
                        fieldsList.append(item);
                    }
                }


                fieldsList.refresh();


            }
        });


    });


var passwordGenerator = function(length) {
        charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
        retVal = "";
    for (var i = 0, n = charset.length; i < length; ++i) {
        retVal += charset.charAt(Math.floor(Math.random() * n));
    }
    return retVal;
};


$(document).ready(function(){

    var ranger = $("#password_generator_field");
    var initial_password_length = ranger.val();
    var initial_password_value = passwordGenerator(initial_password_length);
    var password_input_field = $("#Password_Value")[0];
    password_input_field.value = initial_password_value;
    $("#password_generator_field").bind('change',function(event,ui){

        //Get the current slider value
        var slider = $("#password_generator_field");
        var password_length = slider.val();
        //Generate the random password depending upon the current chosen length
        var password_value = passwordGenerator(password_length);
        //Now set it into the TextField
        var password_text = $("#Password_Value")[0];
        password_text.value = password_value;



    });

});


