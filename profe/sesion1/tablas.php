<?php
$peticion=$_GET["peticion"];
  $opcion=$_GET["opcion"];
  $parte=$_GET["parte"];
//  echo "peticion=".$peticion."<br>";
//  echo "opcion=".$opcion."<br>";
//  echo "PARTE=".$parte."<br>";
include "cnx.php";
function ListarEps(){
	$cn=new SqlitePDO("SALUD.db");
	$sql="select *from eps";
	$cn->EjecutarJSON($sql);
	echo $cn->CargarJSON();
}

function ListarUnaEps($id){
	$cn=new SqlitePDO("SALUD.db");
	$sql="select * from eps where ideps=".$id;
	$cn->Ejecutar($sql);
	//echo $cn->numcols."<br>";
	$cn->Cargar();
	echo $cn->Resultado();
}

function InsertarEps($Cual){
	$cn=new SqlitePDO("SALUD.db");
	$a=explode(";",$Cual);
	$sql="INSERT INTO EPS(NOMBRE,ESTADOEPS) 
	VALUES('".$a[0]."',".$a[1].")";
	$cn->Ejecutar($sql);

}

function ActualizarEps($Cual){
	$cn=new SqlitePDO("SALUD.db");
	$a=explode(";",$Cual);
	$sql="UPDATE EPS SET NOMBRE='".$a[1]."',ESTADOEPS=".$a[2].
	" WHERE IDEPS=".$a[0];
	$cn->Ejecutar($sql);

}

function BorrarEps($Cual){
	$cn=new SqlitePDO("SALUD.db");
	$sql="DELETE FROM EPS WHERE IDEPS=".$Cual;
	$cn->Ejecutar($sql);

}

if($peticion=="eps" && $opcion==0 && $parte==0){
    ListarEps();
}

if($peticion=="eps" && $opcion==0 && $parte>0){
    ListarUnaEps($parte);
}

if($peticion=="eps" && $opcion==1){
    InsertarEps($parte);
}

if($peticion=="eps" && $opcion==2){
    ActualizarEps($parte);
}

if($peticion=="eps" && $opcion==3){
    BorrarEps($parte);
}
