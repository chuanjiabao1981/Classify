function preview(img, selection) {
    if (!selection.width || !selection.height)
        return;
 
    var scaleX = 100 / selection.width;
    var scaleY = 100 / selection.height;
 		
    $('#preview img').css({
        width: Math.round(scaleX * 300 ),
        height: Math.round(scaleY * 300 ),
        marginLeft: -Math.round(scaleX * selection.x1),
        marginTop: -Math.round(scaleY * selection.y1)
    });
		
    $('#x1').val(selection.x1);
    $('#y1').val(selection.y1);
    $('#x2').val(selection.x2);
    $('#y2').val(selection.y2);
    $('#w').val(selection.width);
    $('#h').val(selection.height); 
}

$(document).ready(function() { 
    var options = { 
        //target:        '#output1',   // target element(s) to be updated with server response 
        beforeSubmit:  	showRequest,  // pre-submit callback 
        success:       	showResponse,  // post-submit callback 
	url:	       	'/uploadimage',
	type:	       	'post',
 	dataType:	'json'
        // other available options: 
        //url:       url         // override for form's 'action' attribute 
        //type:      type        // 'get' or 'post', override for form's 'method' attribute 
        //dataType:  html        // 'xml', 'script', or 'json' (expected server response type) 
        //clearForm: true        // clear all form fields after successful submit 
        //resetForm: true        // reset the form after successful submit 
        // $.ajax options can be used here too, for example: 
        //timeout:   3000 
    }; 
    var options1 = { 
	url:'/',
	type:'get'
        // other available options: 
        //url:       url         // override for form's 'action' attribute 
        //type:      type        // 'get' or 'post', override for form's 'method' attribute 
        //dataType:  null        // 'xml', 'script', or 'json' (expected server response type) 
        //clearForm: true        // clear all form fields after successful submit 
        //resetForm: true        // reset the form after successful submit 
 
        // $.ajax options can be used here too, for example: 
        //timeout:   3000 
    }; 
    $('#submit1').click(function(){
	//alert("12334")
	$('#myForm').ajaxSubmit(options); 
	return false; 
    }
    )
    $('#submit2').click(function(){
	$('#myForm').attr({action:"/",method:"GET"})
	$('#myForm').submit();
    }
    );
}); 
// post-submit callback 
function showResponse(responseText, statusText, xhr, $form)  { 
    // for normal html responses, the first argument to the success callback 
    // is the XMLHttpRequest object's responseText property 
 
    // if the ajaxSubmit method was passed an Options Object with the dataType 
    // property set to 'xml' then the first argument to the success callback 
    // is the XMLHttpRequest object's responseXML property 
 
    // if the ajaxSubmit method was passed an Options Object with the dataType 
    // property set to 'json' then the first argument to the success callback 
    // is the json data object returned by the server 
    if (responseText.img != '') {
	document.getElementById('output1').innerHTML = '<img id="tt" src='+responseText.img+' style="float:left;margin-right:20px" width="300px" height="300px"/>';
	document.getElementById('preview').innerHTML = '<img src='+responseText.img+' style="position: relative;" />';
	//alert(responseText.img)
	//document.getElementById('message').innerHTML = data.error;
    }
    $('#tt').imgAreaSelect({ handles: true, onSelectChange: preview,aspectRatio: '1:1'});
    //alert('status: ' + statusText + '\n\nresponseText: \n' + responseText + '\n\nThe output div should have already been updated with the responseText.'); 
}
// pre-submit callback 
function showRequest(formData, jqForm, options) { 
    // formData is an array; here we use $.param to convert it to a string to display it 
    // but the form plugin does this for you automatically when it submits the data 
    var queryString = $.param(formData); 
 
    // jqForm is a jQuery object encapsulating the form element.  To access the 
    // DOM element for the form do this: 
    // var formElement = jqForm[0]; 
 
    //alert('About to submit: \n\n' + queryString); 
 
    // here we could return false to prevent the form from being submitted; 
    // returning anything other than false will allow the form submit to continue 
    return true; 
} 




