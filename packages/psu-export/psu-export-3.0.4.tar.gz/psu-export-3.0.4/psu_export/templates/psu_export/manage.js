function toggle_app(el, app_id){
    let enabled = "N"
    if(el.prop("checked")){
        enabled = "Y"
    }
    $.ajax({
        type:   "POST",
        url:    "{%url 'export:set_app_export'%}",
        data:   {
            csrfmiddlewaretoken: '{{ csrf_token }}',
            app_id: app_id,
            enabled: enabled,
        },
        beforeSend:function(){
            el.after(getAjaxLoadImage());
        },
        success:function(app_html){
            let container = $("#app-" + app_id);
            container.html(app_html);
        },
        error:function(ee){},
        complete:function(){
            clearAjaxLoadImage(el.parent());
        }
    });
}

function toggle_model(el, model_id){
    let enabled = "N"
    if(el.prop("checked")){
        enabled = "Y"
    }
    $.ajax({
        type:   "POST",
        url:    "{%url 'export:set_model_export'%}",
        data:   {
            csrfmiddlewaretoken: '{{ csrf_token }}',
            model_id: model_id,
            enabled: enabled,
        },
        beforeSend:function(){
            el.after(getAjaxLoadImage());
        },
        success:function(model_html){
            let container = $("#model-" + model_id);
            container.html(model_html);
        },
        error:function(ee){},
        complete:function(){
            clearAjaxLoadImage(el.parent());
        }
    });
}

function toggle_field(el, field_id){
    let enabled = "N"
    if(el.prop("checked")){
        enabled = "Y"
    }
    $.ajax({
        type:   "POST",
        url:    "{%url 'export:set_field_export'%}",
        data:   {
            csrfmiddlewaretoken: '{{ csrf_token }}',
            field_id: field_id,
            enabled: enabled,
        },
        beforeSend:function(){
            el.after(getAjaxLoadImage());
        },
        success:function(new_tr){
            let old_tr = $("#field-" + field_id);
            old_tr.after(new_tr);
            old_tr.remove();
        },
        error:function(ee){},
        complete:function(){
            clearAjaxLoadImage(el.parent());
        }
    });
}

function update_field(el, field_id){
    let prop = el.attr("name");
    let value = el.val();
    $.ajax({
        type:   "POST",
        url:    "{%url 'export:update_field'%}",
        data:   {
            csrfmiddlewaretoken: '{{ csrf_token }}',
            field_id: field_id,
            prop: prop,
            value: value,
        },
        beforeSend:function(){
            clearAjaxStatusClasses(el.parent());
            el.after(getAjaxLoadImage());
            el.addClass('ajax-pending');
        },
        success:function(new_tr){
            el.addClass('ajax-success');

        },
        error:function(ee){
            el.addClass('ajax-error');
        },
        complete:function(){
            el.removeClass('ajax-pending');
            clearAjaxLoadImage(el.parent());
        }
    });
}
