<?php
header("Content-Type: application/json");
include "cnx.php";
$Cnx=new SqlitePDO();
      $sql="";
//$_SERVER["REQUEST_METHOD"];
switch($_SERVER["REQUEST_METHOD"]){
    case 'GET':
       if(isset($_GET["id"]))
        $sql="SELECT * FROM EPS WHERE IDEPS=".$_GET["id"];
      else
        $sql="SELECT * FROM EPS";
        $Cnx->EjecutarJSON($sql);
        echo $Cnx->CargarJSON();
        break;
    case 'POST':
         $_POST=json_decode( file_get_contents("php://input"),true);
         $sql="insert into eps(nombre,estadoeps) 
        values('".$_POST["nombre"]."',".$_POST["estadoeps"].")";
        $Cnx->Ejecutar($sql);
        break;
    case 'PUT':
        $_POST=json_decode( file_get_contents("php://input"),true);
        $sql="update eps set nombre='".$_POST["nombre"]."',
        estadoeps=".$_POST["estadoeps"]." where ideps=".$_POST["id"];
        $Cnx->Ejecutar($sql);       
        break;
    case 'DELETE':
        $sql="DELETE FROM EPS WHERE IDEPS=".$_GET["id"];
        $Cnx->Ejecutar($sql);
        break;
    }
?>
        



