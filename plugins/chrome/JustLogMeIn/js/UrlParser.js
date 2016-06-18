/**
 * Created by snouto on 16/06/16.
 */

function UrlParser(location){

   this.location = location;
    //init the current object
    this.init();
};

UrlParser.prototype.init = function(){

    this.link = document.createElement('a');
    this.link.href = this.location;
    //get the hostname
    UrlParser.prototype.hostname = this.link.hostname;
    UrlParser.prototype.found = null;
};

UrlParser.prototype.isSavedURL = function(){


    done = false;
    //get all the available sites from the chrome storage
    chrome.storage.local.get('sites',function(data){

        /*sites = data.sites;

        storedSites = [];
        for(i=0;i<sites.length;i++){

            lnk = document.createElement('a');
            lnk.href = sites[i].url;
            var current = {host:lnk.hostname,settings:sites[i].settings,credentials:{username:sites[i].username,password:sites[i].password}};
            reg = new RegExp(current.host);

            matched = UrlParser.prototype.hostname.match(reg);

            UrlParser.prototype.found = (matched != null && matched.length > 0);

            if (UrlParser.prototype.found) {

                UrlParser.prototype.found = current;
                break;
            }
        }*/
        UrlParser.prototype.done = true;
    });

    while(!UrlParser.prototype.done);
    return this.found;
};

//This function will return the settings like favourite , auto-login and auto-fill for the specified url
UrlParser.prototype.getURLSettings = function(){

    if (this.found != null || this.found != false) return this.found.settings;
    else return null;

};

//This function will return the username and password stored in the user's account for the specified url
UrlParser.prototype.getCredentials = function(){

    if (this.found != null || this.found != false) return this.found.credentials;
    else return null;

};