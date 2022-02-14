<?php
  $peticion=$_GET["peticion"];
  $opcion=$_GET["opcion"];
  $parte=$_GET["parte"];
  //include "../../rutinas.php";
    // echo "peticion=".$peticion."<br>";
    // echo "opcion=".$opcion."<br>";
    // echo "PARTE=".$parte."<br>";
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

