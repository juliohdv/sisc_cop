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

$(document).ready(function(){
    $("#agregarTransaccion").on('click',function(e){
        //alert("Hola");
        e.preventDefault();
        $.ajax({
            url:"agregarTransaccion/",
            type:"POST",
            data:"",
            success:function(response){
                $("#content").html(response);
            },
        });
    });
});

$(document).ready(function(){
    $("#formDetalle").on('submit',function(e){
        e.preventDefault();
        var datos1 = $("#formDetalle").serialize();
        alert(datos1);
        $.ajax({
            url: "agregarDetalle/",
            type: "POST",
            data: $("#formDetalle").serialize(),
            success: function(data){
                $("#respuestaDetalle").append(data);
            }
        });
    });
});