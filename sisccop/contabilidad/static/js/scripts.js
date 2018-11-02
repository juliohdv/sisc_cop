//Script para cargar vistas en el template
$(document).ready(function(){
	$("#catalogoCuentas").on('click',function(e){
		//alert("Hola");
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

//Script para limpiar formularios en la página
$(document).ready(function(){
    $("#btnCerrarMdlGuardar").on('click', function(e){
    	$(':input').not(':button, :submit, :reset, :hidden, :checkbox, :radio').val('');
        $(':checkbox, :radio').prop('checked', false);
    	e.preventDefault();
    	$.ajax({
    		url:"catalogoCuentas/",
    		type:"POST",
    		data:"",
    		success:function(response){
    			$("#content").html(response);
    		}
    	});
    });
});
//Script para enviar nueva cuenta a BD
$(document).ready(function(){
    $("#formGuardarCuenta").on('submit',function(e){
    	e.preventDefault();
    	var datos = $("#formGuardarCuenta").serialize();
    	alert(datos);
    	$.ajax({
    		url: "guardarCuenta/",
    		type: "POST",
    		data: $("#formGuardarCuenta").serialize(),
    		success: function(data){
    			$("#respuestaGuardar").append(data);
    		}
    	});
    });
});

//Script para eliminar cuenta en BD
$(document).ready(function(){
    $("#btnEliminarCuenta").on('click',function(e){
        e.preventDefault();
        var datos = $("#tdCuenta".text());
        alert(datos);
    });
});