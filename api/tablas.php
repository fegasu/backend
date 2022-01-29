<?php
  $peticion=$_GET["peticion"];
  $opcion=$_GET["opcion"];
  $parte=$_GET["parte"];
  //include "../../rutinas.php";
    // echo "peticion=".$peticion."<br>";
    // echo "opcion=".$opcion."<br>";
    // echo "PARTE=".$parte."<br>";
class Servicios{
function mostrarCategoria($que=0){
	          include "cnxbd.php";
	  	 	    $cn=new SqlitePDO("../../restaurante.sqlite");
            if($que==0)
            $cn->EjecutarArray("select * from categoria");
            else
            $cn->EjecutarArray("select * from categoria where idCategoria=".$que);
              
            $categoria=$cn->CargarArray();
            $categoria1=json_encode( $categoria);
         
      return $categoria1;     

}

function mostrarPlatos($que){
            include "cnxbd.php";
            $cn=new SqlitePDO("../../restaurante.sqlite");
            if($que==0)
            $cn->EjecutarArray("select * from platos");
            else
            $cn->EjecutarArray("select * from platos where IDCATEGORIA=".$que);
              
            $categoria=$cn->CargarArray();
            $categoria1=json_encode( $categoria);
         
      return $categoria1;     

}
function mostrarPedido($que){
            include "cnxbd.php";
            $cn=new SqlitePDO("../../restaurante.sqlite");
            
            $cn->EjecutarArray("select count(*) CANTIDAD from carrito where idmesa=".$que);
              
            $categoria=$cn->CargarArray();
            $categoria1=json_encode( $categoria);
         
      return $categoria1;     

}
 function mostrarCarrito($que){
            include "cnxbd.php";
            $cn=new SqlitePDO("../../restaurante.sqlite");
             
            $cn->Ejecutar("select COUNT(*) from vpedido where idmesa=".$que);
            $cn->Cargar();$hay=$cn->getdato(0);
            if($hay>0){
            $cn->EjecutarArray("select * from vpedido where idmesa=".$que);             
            $categoria=$cn->CargarArray();
            //$categoria["ERROR"]=$hay;
            $categoria1=json_encode( $categoria);
          }
         
      return $categoria1;     

}
 function insertarCarrito($mesa,$plato){
            include "cnxbd.php";
            $cn=new SqlitePDO("../../restaurante.sqlite");
             
            $cn->Ejecutar("INSERT INTO carrito(idplato,idmesa) values(".$plato.",".$plato.")");
            $cn->Ejecutar("select COUNT(*) from vpedido where idmesa=".$mesa);
            $cn->Cargar();$hay=$cn->getdato(0);
            if($hay>0){
            $cn->EjecutarArray("select * from vpedido where idmesa=".$mesa);
              
            $categoria=$cn->CargarArray();
            $categoria["REG"]=$hay;
            $categoria1=json_encode( $categoria);
          }else{
            $categoria["REG"]=$hay;
            $categoria1=json_encode( $categoria);
          }
         
      return $categoria1;     

}
}
$ser=new Servicios();
if($peticion == "carrito")
    echo $ser->mostrarCarrito($opcion);
elseif($peticion == "carritoi")
    echo $ser->insertarCarrito($opcion,$parte);
elseif($peticion == "categoria")
    echo $ser->mostrarCategoria($opcion);
elseif($peticion == "vpedido")
    echo $ser->mostrarPedido($opcion);
elseif($peticion == "plato")
    echo $ser->mostrarPlatos($opcion);
else{
  echo "HTTP/1.1 404 Servicio no encontrado";
  header("HTTP/1.1 404 Servicio no encontrado");
}

?>

