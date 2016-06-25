/**
 * Created by snouto on 25/06/16.
 */

$(document).ready(function(){



    $("#addField-btn").click(function(){
        var unique_id = 'id' + (new Date()).getTime();
        var html = '<div class="col-sm-3 m-b-30"> <label for="field_name[]">Field Name</label> <input type="text" name="field_name[]" id="field_name[]" value="" class="form-control input-sm"> </div> <div class="col-sm-3 m-b-30"> <label for="field_value[]">Field Value</label> <input type="text" name="field_value[]" id="field_value[]" value="" class="form-control input-sm"> </div> <div class="col-sm-3 m-b-30"> <label for="field_type[]">Field Type</label> <select id="field_type[]" name="field_type[]" value="" class="form-control"> <option value="Text">Text</option> <option value="Password">Password</option> </select> </div>';
        var smaller_html = ' <div class="col-sm-1 m-b-30"> <a href="#"  to-remove-id="'+unique_id+'" class="btn bgm-cyan btn-icon waves-effect waves-circle waves-float ui-item-deleter"> <i class="md md-close"></i> </a> </div>';
        var div_el = document.createElement('div');
        div_el.id = unique_id;
        div_el.setAttribute('class','fg-line');
        div_el.innerHTML = html;
        div_el.innerHTML += smaller_html;
        var fields = document.getElementById('fields');

        if(fields != undefined && fields != null)
        {
            //add them to the fields
            fields.appendChild(div_el);
        }
    });

    $('body').on('click','a.ui-item-deleter',function(){

        to_delete = this.attributes['to-remove-id'];
        var delete_element = document.getElementById(to_delete.value);
        delete_element.remove();
    });
});