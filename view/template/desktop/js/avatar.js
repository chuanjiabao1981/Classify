<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.6.2/jquery.min.js"></script> 
<script src="http://ajax.googleapis.com/ajax/libs/jqueryui/1.8/jquery-ui.min.js"></script>
<link rel="stylesheet" type="text/css" href="/static_file/js/imagereaselect/css/imgareaselect-animated.css" /> 
<script type="text/javascript" src="/static_file/js/jquery.form.js"></script> 
<script type="text/javascript" src="/static_file/js/imagereaselect/scripts/jquery.imgareaselect.pack.js"></script> 

<script type="text/javascript">
        $(document).ready(function() { 
            var options = { 
                type:       'POST',
                url:        '/uploadimage',
		dataType:    'json',
		success:       showResponse
            }; 

	    var options_image_save = {
		type: 'POST',
		url : '/setavatar',
		dataType:'json',
		success:showImageSaveResult,
		error: function(xhr, textStatus, errorThrown) {
			alert("系统错误");
    		}
	    };
		
	    $('#submit_post_button').click(function(){
		$('#tt_tt_tt').imgAreaSelect({remove:true});
                $('#image_upload').ajaxSubmit(options);
		$('#error_upload').hide();
                return false;
            });
	   $('#image_save_submit').click(function(){
		$('#error_upload').hide();
                $('#image_save').ajaxSubmit(options_image_save);
                return false;
            });

	   $('#image_save_submit').hide();
	   $('#error_upload').hide();
	}
	);
	function preview(img, selection) {
    		if (!selection.width || !selection.height)
        	return;
 
    		var scaleX = 100 / selection.width;
    		var scaleY = 100 / selection.height;
 		
    		$('#preview img').css({
        		width: Math.round(scaleX * 200 ),
        		height: Math.round(scaleY * 200 ),
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
	function showImageSaveResult(responseText,statusText,xhr,$form)
	{
		if (responseText.status){
			document.getElementById('error_upload').innerHTML = responseText.err;
			$('#error_upload').show();
			$('#error_upload').hide("fade",{},2000);
			
		}else{
			document.getElementById('error_upload').innerHTML = responseText.err;
			$('#error_upload').show();
			alert(responseText.err);

		}
	}

	function showResponse(responseText, statusText, xhr, $form)
	{ 
		if (responseText.status)
		{
			
			document.getElementById('image_output').innerHTML = 
			'<img id="tt_tt_tt" src='+responseText.img+' width="200px" height="200px" style="margin:5px 5px 2px 5px"/>';
			document.getElementById('preview').innerHTML = '<img src='+responseText.img+' style="position: relative;" />';
			$('#tt_tt_tt').imgAreaSelect({ handles: true,onInit:preview,onSelectChange: preview,x1:30,y1:30,x2:150,y2:150});
			$('#image_save_submit').show(500);
			//$("#submit_post_button").hide();
			$("#image_save_img").val(responseText.img);

		}else{
			document.getElementById('error_upload').innerHTML=responseText.img;
			$('#error_upload').show(500);
		}
	}
     </script>


