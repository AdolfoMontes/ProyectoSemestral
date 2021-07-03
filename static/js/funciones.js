$("#btn_registro").click(function() {
        $("#errores").empty();
        usuario = $("#txt_nombre").val();
        validador=0;
        if(usuario == "") {
                validador= validador + 1;
                $("#errores").append('<li> Debe ingresar un usuario </li>');
                $('#txt_nombre').removeClass('is-valid')
                $('#txt_nombre').addClass('is-invalid');
        }
        else{  
                $('#txt_nombre').removeClass('is-invalid')
                $('#txt_nombre').addClass('is-valid');
        };

        apellido = $("#txt_apellido").val();
        if(apellido == "") {
                validador= validador + 1;
                $("#errores").append('<li> Debe ingresar un apellido </li>');
                $('#txt_apellido').removeClass('is-valid')
                $('#txt_apellido').addClass('is-invalid');
        }else{  
                $('#txt_apellido').removeClass('is-invalid')
                $('#txt_apellido').addClass('is-valid');
        };


        mail = $("#txt_mail").val();
        if(mail == "") {
                validador= validador + 1;
                $("#errores").append('<li> Debe ingresar un mail </li>');
                $('#txt_mail').removeClass('is-valid')
                $('#txt_mail').addClass('is-invalid');
        }else{  
                $('#txt_mail').removeClass('is-invalid')
                $('#txt_mail').addClass('is-valid');
        };

        direccion = $("#txt_direccion").val();
        if(direccion == "") {
                validador= validador + 1;
                $("#errores").append('<li> Debe ingresar una direccion </li>');
                $('#txt_direccion').removeClass('is-valid')
                $('#txt_direccion').addClass('is-invalid');
        }else{  
                $('#txt_direccion').removeClass('is-invalid')
                $('#txt_direccion').addClass('is-valid');
        };



        comuna = $("#cmb_comuna option:selected").text();
        if(comuna == "Elegir...") {
                validador= validador + 1;
                $("#errores").append('<li> Debe seleccionar una comuna </li>');
                $('#cmb_comuna').removeClass('is-valid')
                $('#cmb_comuna').addClass('is-invalid');
        }else{  
                $('#cmb_comuna').removeClass('is-invalid')
                $('#cmb_comuna').addClass('is-valid');
        };

        telefono = $("#txt_telefono").val();
        if(telefono == "") {
                validador= validador + 1;
                $("#errores").append('<li> Debe ingresar un teléfono </li>');
                $('#txt_telefono').removeClass('is-valid')
                $('#txt_telefono').addClass('is-invalid');
        }else{  
                $('#txt_telefono').removeClass('is-invalid')
                $('#txt_telefono').addClass('is-valid');
        };

        rut = $("#txt_rut").val();
        if(rut == "") {
                validador= validador + 1;
                $("#errores").append('<li> Debe ingresar un RUT </li>');
                $('#txt_rut').removeClass('is-valid')
                $('#txt_rut').addClass('is-invalid');
        }else{  
                $('#txt_rut').removeClass('is-invalid')
                $('#txt_rut').addClass('is-valid');
        };


        pass1 = $("#txt_pass1").val();
        pass2 = $("#txt_pass2").val();
        if(pass1 == "" && pass2==""){
                validador= validador + 1;
                $("#errores").append('<li> Debe ingresar las contraseñas </li>');
                $('#txt_pass1').removeClass('is-valid')
                $('#txt_pass1').addClass('is-invalid');
                $('#txt_pass2').removeClass('is-valid')
                $('#txt_pass2').addClass('is-invalid');

                
        }
        else if(pass1.lenght >15) {
                validador= validador + 1;
                $("#errores").append('<li> La contraseña no cumple con los requisitos </li>');
                $('#txt_pass1').removeClass('is-valid')
                $('#txt_pass1').addClass('is-invalid');
        }
        else if(pass1 != pass2){
                validador= validador + 1;
                $("#errores").append('<li> Las contraseñas no son idénticas </li>');
                $('#txt_pass1').removeClass('is-valid')
                $('#txt_pass1').addClass('is-invalid');
                $('#txt_pass2').removeClass('is-valid')
                $('#txt_pass2').addClass('is-invalid');

        }
        

        else{  
                $('#txt_pass1').removeClass('is-invalid')
                $('#txt_pass1').addClass('is-valid');
                $('#txt_pass2').removeClass('is-invalid')
                $('#txt_pass2').addClass('is-valid');
                
        };

        var checkBox = document.getElementById("chk_terminos");

        if (checkBox.checked == false){
                validador= validador + 1;
                alert("Debe aceptar los términos y condiciones");
               
        } 
        if(validador == 0){
                alert("Registro correcto"); 
        }
       

        
});


$("#menu-toggle").click(function (e) {
    e.preventDefault();
    $("#wrapper").toggleClass("toggled");
});


$("#tarjeta1").click(function() {
        var tarjeta = $('#tarjeta1').text();
        $("#dropdown_tar").empty();
        console.log(tarjeta);
        $("#dropdown_tar").append(tarjeta);
        $("#txt_numero").val(tarjeta);
        $("#txt_tipocomb").val('GAS95');
        $("#txt_tipodoc").val('Factura');
        $("#txt_nick").val('Nissan');
        $("#txt_patente").text('Patente: HJ1434');
        $("#txt_tipoveh").val('Auto');
        $("#titulo_tarj").text('Tarjeta Xpress');
        $("#saldo").text('215893');
        $("#moneda").text('CLP');
        

});

$("#tarjeta2").click(function() {
        var tarjeta = $('#tarjeta2').text();
        $("#dropdown_tar").empty();
        console.log(tarjeta);
        $("#dropdown_tar").append(tarjeta);
        $("#txt_numero").val(tarjeta);
        $("#txt_tipocomb").val('DIESEL');
        $("#txt_tipodoc").val('Boleta');
        $("#txt_nick").val('Peugeot');
        $("#txt_patente").text('Patente :PK1886');
        $("#txt_tipoveh").val('Camioneta');
        $("#titulo_tarj").text('Tarjeta Flota');
        $("#saldo").text('512318');
        $("#moneda").text('CLP');

});

function limpiarTxt(){
        $("#txt_numero").val('');
        $("#txt_tipocomb").val('');
        $("#txt_tipodoc").val('');
        $("#txt_nick").val('');
        $("#txt_patente").text('Patente: ');
        $("#txt_tipoveh").val('');
        $("#titulo_tarj").text('');
        $("#saldo").text('0');
};

$("#btn_usd").click(function() {
        $.getJSON('https://mindicador.cl/api', function(data) {
        var indicadores = data;
        var valor = '';
        var moneda = $('#moneda').text();
        var saldo = $('#saldo').text();
        if(moneda =='CLP'){
                valor = Math.round(saldo/indicadores.dolar.valor) ;
        }if (moneda=='EUR'){
                valor =  Math.round(saldo/0.83)
        }if(moneda=='USD'){
                valor = saldo;
        }

        $('#saldo').text(valor);
        $('#moneda').text('USD');
        })
        
});

$("#btn_eur").click(function() {
        $.getJSON('https://mindicador.cl/api', function(data) {
        var indicadores = data;
        var valor = '';
        var saldo = $('#saldo').text();
        var moneda = $('#moneda').text();
        if(moneda =='CLP'){
                valor = Math.round(saldo/indicadores.euro.valor) ;
        }if (moneda=='EUR'){
                valor =  saldo;
        }if(moneda=='USD'){
                valor = saldo * 0.83;
        }
        $('#saldo').text(valor);
        $('#moneda').text('EUR');
        })
        
});







$("#btn_clp").click(function() {
        var saldo = 0;
        var patente =  $("#txt_patente").text();

        if (patente == 'Patente: HJ1434'){
                saldo = 215893;
        }else if (patente =='Patente :PK1886'){
                saldo = 512318;
        }

        $('#saldo').text(saldo);
        $('#moneda').text('CLP');

});
        



