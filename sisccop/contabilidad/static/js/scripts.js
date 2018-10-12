//Script para cargar vistas en el template
$(document).ready(function(){
	$("#catalogoCuentas").on('click',function(e){
		alert("Hola");
		e.preventDefault();
		$.ajax({
			url:"catalogoCuentas/",
			type:"POST",
			data:"",
			success:function(response){
				$("#content").html(response);
			},
		});
	});
});