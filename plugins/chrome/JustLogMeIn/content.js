//chrome.browserAction.setPopup({popup:'popup.html'});

//alert(document.location.href);
//inputs  = document.getElementsByTagName("input");

mystyle = 'cursor:pointer;background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAACh0lEQVQ4T2NkwAEKjz3mDFcTvynDxSq78+m3xmRV7gZsShlxGTD/5pcHSqLc8p///WewEWZkePTh39kb75icw5QZPyLrwWpAw9FXq9x0RUKffPzN0Hr4dYYg4z+dDjfJHAMhFoamsx+N20wEzsEMwTCAN3hjknOey1wtYQYGQ0FWhhUnXk5ZGyybazTtelqug9TMBE0+hilXvjTk6vI2ggzBMEC2/tJ/AUNphv8/fzOI8LIy+ChzMjx9/OFJv4uULIPeEpncZqtLnX6Kgkef/tzrKsPhgmEAX/75XyJWKqycPz8yMLMwMzCyszA4qHMz8L98z9BUtsNW3Vqmdmqnm5v87/+vVfmYxDDDQLPViMHabK+QmYmAMNNnBnZ2RoafTCwMVip8DDaCfxlYmJkZxHjZGV49+7Q00UAoBmsg9jZ2zKp4bJb6W16FQVaMkYGLmYHhOyMjg4UyD0OEDg/D+ctvDjQ7SjhiDYP58+cn8LD9n3/s2GmGy8KRDHs+iTCIqPIwcP//z/CTg5XBU57lI6ugqOgsE8bfGAZERUXJJyWnP5gxZx5DYXYag5Wx3L/Atjv1G17xNgsYSDEwvf3G8G7TMVOGU3FnsEbj1m07Hy1ftVrWy8ODwczMnEFZUTCGkZFnKYNosyqDmXYxw8uXKxjOZB7AmpCu37q3ZO7cedHCQsIMgYF+DHx8nO1SElJVuFIq3AWenp7sFha2CWLiIjMuXbnOkJ6W+l1YmH+OrLR0HiHN4DBoamrP0tPTLdu0dZt8QkI8g4ykaK2SklILMZrBBkRGxxfb2zsUKykrSSoryjHw8fKViIoK9xJtQFVt4w55OXk7S0uzBj4ertUKCgr3idUMUgcAYQbEEdUqXKkAAAAASUVORK5CYII="); background-attachment: scroll; background-size: 16px 18px; background-position: 98% 50%; background-repeat: no-repeat;';
auto_style='cursor:auto;background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAACh0lEQVQ4T2NkwAEKjz3mDFcTvynDxSq78+m3xmRV7gZsShlxGTD/5pcHSqLc8p///WewEWZkePTh39kb75icw5QZPyLrwWpAw9FXq9x0RUKffPzN0Hr4dYYg4z+dDjfJHAMhFoamsx+N20wEzsEMwTCAN3hjknOey1wtYQYGQ0FWhhUnXk5ZGyybazTtelqug9TMBE0+hilXvjTk6vI2ggzBMEC2/tJ/AUNphv8/fzOI8LIy+ChzMjx9/OFJv4uULIPeEpncZqtLnX6Kgkef/tzrKsPhgmEAX/75XyJWKqycPz8yMLMwMzCyszA4qHMz8L98z9BUtsNW3Vqmdmqnm5v87/+vVfmYxDDDQLPViMHabK+QmYmAMNNnBnZ2RoafTCwMVip8DDaCfxlYmJkZxHjZGV49+7Q00UAoBmsg9jZ2zKp4bJb6W16FQVaMkYGLmYHhOyMjg4UyD0OEDg/D+ctvDjQ7SjhiDYP58+cn8LD9n3/s2GmGy8KRDHs+iTCIqPIwcP//z/CTg5XBU57lI6ugqOgsE8bfGAZERUXJJyWnP5gxZx5DYXYag5Wx3L/Atjv1G17xNgsYSDEwvf3G8G7TMVOGU3FnsEbj1m07Hy1ftVrWy8ODwczMnEFZUTCGkZFnKYNosyqDmXYxw8uXKxjOZB7AmpCu37q3ZO7cedHCQsIMgYF+DHx8nO1SElJVuFIq3AWenp7sFha2CWLiIjMuXbnOkJ6W+l1YmH+OrLR0HiHN4DBoamrP0tPTLdu0dZt8QkI8g4ykaK2SklILMZrBBkRGxxfb2zsUKykrSSoryjHw8fKViIoK9xJtQFVt4w55OXk7S0uzBj4ertUKCgr3idUMUgcAYQbEEdUqXKkAAAAASUVORK5CYII="); background-attachment: scroll; background-size: 16px 18px; background-position: 98% 50%; background-repeat: no-repeat;';

//get the location of the current page
//var location = document.location;
//create a new url parser
//var parser = new UrlParser(location);
/*
 if( bb.ix <= p.x && p.x <= bb.ax && bb.iy <= p.y && p.y <= bb.ay ) {
 // Point is in bounding box
 }
 bb is the bounding box, (ix,iy) are its top-left coordinates, and (ax,ay) its bottom-right coordinates.  p is the point and (x,y) its coordinates.
 */
var isPointInside = function(rect,x,y){

    return (rect.top <= x && x <= rect.bottom && rect.left <= y && y <= rect.right);

}

var inject_pattern = function(input,obj,type){


    //set a badge
    /*
     x>=this.x
     && x<=this.x+this.width
     && y>=this.y
     && y<=this.y+this.height
     */
    input.style = auto_style;
    //inputs[i].class ="";
    //inputs[i].value = "snouto";
    input.ondblclick = function(event){

        rect = input.getBoundingClientRect();

            var iframe_style = "display: block !important; position: absolute !important; visibility: visible !important; z-index: 2147483647 !important; border-style: none !important; opacity: 1 !important; margin: 0px !important;";
            iframe_style += "padding: 0px !important; width: 345px !important; height: 210px !important;" + "top:" + rect.bottom.toString() +"px !important; left:"+rect.left.toString() + "px  !important;";
        var iframe_obj = document.getElementById('embeddedFrame');

        if(iframe_obj != undefined && iframe_obj != null){

            iframe_obj.style = iframe_style;

        }else{
            iframe_obj = document.createElement('iframe');
            iframe_obj.style = iframe_style;
            iframe_obj.document.open();
            iframe_obj.document.write("Hello World");
            iframe_obj.document.close();
            iframe_obj.id ="embeddedFrame";
            iframe_obj.name = "embeddedFrame";
            document.body.appendChild(iframe_obj);
        }

    };

    input.onmouseout = function(){

        input.style = auto_style;
    };


    if(obj.settings.autofill){

        //get the credential and put it into the value of the text
        if(type =="username"){
            username = obj.credentials.username;
            input.value = username;
        }else if (type == "password"){

            password = obj.credentials.password;
            input.value = password;
        }
    }
};

var inject = function(obj){

    u_tags =['user','username','user_name','user-name','email','loginname','name','logon','login_name','email_address'];
    pass_tags = ['pass','password','secret','secret_word','secretword','pass_word'];
    inputs = document.getElementsByTagName("input");

    for(i=0;i<inputs.length;i++){

        input = inputs[i];

        if(u_tags.includes(input.name.toLowerCase()) || u_tags.includes(input.id.toLowerCase())){
            inject_pattern(input,obj,"username");
        }else if (input.type == "password" || pass_tags.includes(input.name.toLowerCase()) || pass_tags.includes(input.id.toLowerCase()))
        {
            inject_pattern(input,obj,"password");
        }


    }

};



chrome.storage.local.get('sites',function(data){


    var location = (document.location.origin + document.location.pathname);
    var current_site = null;
    sites = data.sites;
    var totalMatched = 0;

    for(i=0;i<sites.length;i++){

        lnk = document.createElement('a');
        lnk.href = sites[i].url;
        var current = {host:(lnk.origin+lnk.pathname),settings:sites[i].settings,credentials:{username:sites[i].username,password:sites[i].password}};
        reg = new RegExp(current.host);

        matched = location.match(reg);

        if ((matched != null && matched.length > 0)) {

            totalMatched = totalMatched +  1;
            inject(current);

            current_site = current;

            break;
        }
    }


    chrome.runtime.sendMessage({message:'update_badge',payload:totalMatched});


    if(current_site != null && current_site != undefined){

        //check to see if the current site needs to be autologin
        if(current_site.settings.autologin)
        {
            //now submit the form of the document dom
            //get the form
            form = document.forms[0];

            if(form != null && form != undefined){

                //now submit it
                form.submit();
            }
        }
    }

});
/*
if (parser.isSavedURL()){

    //get the inputs
    inputs = document.getElementsByTagName("input");

    for (i =0;i<inputs.length;i++){

        //width : 16px
        //height : 18px
        //alert('yes we have a password field in this page');
        if(inputs[i].type == "password")
        {
            inputs[i].onmouseover = function(event){

                rect = this.getBoundingClientRect();

                var polygon = new Polygon();

            };
            inputs[i].style = auto_style;
            //inputs[i].class ="";
            //inputs[i].value = "snouto";
            inputs[i].ondblclick = function(){

                alert('you have clicked me');
            };
        }

    }
}*/


/*
 display: block !important; position: absolute !important; visibility: visible !important; z-index: 2147483647 !important;
 border-style: none !important; opacity: 1 !important; margin: 0px !important;
 padding: 0px !important; width: 345px !important; height: 210px !important; top: 214px !important; left: 769px !important;
 */

/*
 display: block !important; position: absolute !important; visibility: visible !important; z-index: 2147483647 !important;
  border-style: none !important; opacity: 1 !important; margin: 0px !important; padding: 0px !important;
 width: 345px !important; height: 210px !important; top: 269px !important; left: 769px !important;
 */

/*for (i =0 ; i < inputs.length;i++){

    if(inputs[i].type == "password"){
        //width : 16px
        //height : 18px
        //alert('yes we have a password field in this page');
       inputs[i].onmouseover = function(event){

           rect = this.getBoundingClientRect();

           var polygon = new Polygon();

       };
        inputs[i].style = auto_style;
        //inputs[i].class ="";
        //inputs[i].value = "snouto";
        inputs[i].ondblclick = function(){

            alert('you have clicked me');
        };

    }
}*/
