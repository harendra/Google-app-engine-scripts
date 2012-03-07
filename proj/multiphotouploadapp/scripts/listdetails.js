function ListDetailsHandler() {
	var dataid = "detailhandlerdata";
	var maintableclass = ".formattingtable";
	var checkboxclass = ".ifselected";
	var observednumbercomboclass = ".observednumbercombos";
	var photolinkbuttonclass = ".photolinkbutton";
	var specificlocationbuttonclass = ".specificlocationbutton";
	var addbirdbutton = "#addbirdphoto";
	var phototableid = "#phototable";
	var inputphotoid = "#addbirdphotoinput";

	this.initializeEvents = function() {
		$(addbirdbutton).click(function(){
			$(inputphotoid).trigger('click');
		});
		
	}
	
	this.handlephotoupload=function(input){
		var uploadedfiles=input.files;
		var toolarge="";
		var maxsize=1024000;
		counter=1;
		for(var i=0;i<uploadedfiles.length;i++){
			if(uploadedfiles[i].size>maxsize){
				toolarge+=uploadedfiles[i].name+"\n";
			}
			else{
				var data=new FormData();
				data.append("uploadimage",uploadedfiles[i]);
			}
		    sendPhotos(data);	
		}
		if(toolarge!=""){
			alert("These images were not uploaded due to size limit of 1MB\n"+toolarge);
		}
		//alert(data);
	}
	
	function getPhotosFromLocal() {

	}

	function sendPhotos(filedata) {
	$.ajax({
    	url: 'downloader',
    	data: filedata,
    	cache: false,
    	contentType: false,
   	     processData: false,
    	type: 'POST',
    	success: function(receiveddata){
    		var data=JSON.parse(receiveddata);
    		imagelinks=data['imagelinks'];
    		for(var i=0;i<imagelinks.length;i++){
        	$('#phototable').append('<tr><td><img src='+imagelinks[i]+'/></td></tr>');
        }
        }    	
		});

	}

}
