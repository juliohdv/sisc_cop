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
    $("#btnAgregarDetalle").on('click',function(e){
        e.preventDefault();
        var fecha = $("#fechaD").val();
        var cuenta = $("#cuentaD").val();
        var descripcion = $("#descripcionD").val();
        var debe = $("#debeD").val();
        var haber = $("#haberD").val();
        var filaNueva = "<tr><td>" + fecha + "</td><td>" + cuenta + "</td><td>" + descripcion + "</td><td class='celdaDebe'>" + debe + "</td><td class='celdaHaber'>" + haber + "</td></tr>";
        $("#tblDetalleTransaccion tbody").append(filaNueva);
        $(':input').not(':button, :submit, :reset, :hidden, :checkbox, :radio').val('');
        $(':checkbox, :radio').prop('checked', false);
        
        function getColumnTotal(selector) {
            return Array.from( $(selector) ).reduce(sumReducer, 0);
        } 
        function sumReducer(total, cell) {
            return total += parseInt(cell.innerHTML, 10);
        }
        function toMoney(number) {
            return '$' + number.toFixed(2);
        };   
        function actualizarTotales(){
            var celdaTotalDebe = $("#totalDebe");
            var celdaTotalHaber = $("#totalHaber");
            var totalDebe = getColumnTotal('.celdaDebe');
            var totalHaber = getColumnTotal('.celdaHaber');
            celdaTotalDebe.text(toMoney(totalDebe));
            celdaTotalHaber.text(toMoney(totalHaber));
        };
        actualizarTotales();
    });
});

$(document).ready(function(){
    $("#btnLimparTablaDetalle").on('click',function(e){
        e.preventDefault();
        $("#tblDetalleTransaccion tbody").empty();
        $("#tblDetalleTransaccion tfoot").empty();
        $(':input').not(':button, :submit, :reset, :hidden, :checkbox, :radio').val('');
        $(':checkbox, :radio').prop('checked', false);
    });
});