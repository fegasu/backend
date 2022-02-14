<?php
if(!isset($_GET["N"]))
$N=0;
else
$N=$_GET["N"];
?>

<script type="text/javascript">
function Ir(donde){
      location.href="<?php echo $_SERVER['PHP_SELF']?>?N="+donde;
}
function Ir1(donde,que){
      location.href="<?php echo $_SERVER['PHP_SELF']?>?N="+donde+"&donde="+que;
}
</script>
<button onclick="Ir(1)">Nuevo</button>
<?php
if($N==0){
$url="http://".$_SERVER["SERVER_NAME"]."/SALUD/eps/0/0";

$JSON =  file_get_contents($url,true);
$eps=json_decode($JSON);
echo "<table border=1><tr><th>Nombre</th><th>Estado</th>
<th colspan=2>Funcion</th></tr>";

foreach($eps as $key => $dato){
	echo "<tr><td>",$dato->nombre."</td><td>".$dato->estadoeps."
    </td><td onclick='Ir1(3,".$dato->ideps.")'>E</td><td onclick='Ir1(5,".$dato->ideps."
)'>X</td></tr>";
}

}
if($N==1){
echo "Nivel 1";
echo "<form name=mio method=gett >Nombre EPS:
<input type=text name=nombre><input type=submit>
<input type=hidden name=estadoeps value=1>
<input type=hidden name=N value=2></form>";
}
if($N==2){
  echo "Nivel 2<br>";

$url="http://".$_SERVER["SERVER_NAME"]."/SALUD/eps/1/".str_replace(' ','+',$_GET["nombre"]).";".$_GET["estadoeps"];
$JSON =  file_get_contents($url,true);
//echo $url."<br>";
echo "<script>
location.href='".$_SERVER['PHP_SELF']."';
</script>";
}

if($N==3){
  echo "Nivel 3<br>";
$url="http://".$_SERVER["SERVER_NAME"]."/SALUD/eps/0/".$_GET["donde"];
$eps =  file_get_contents($url,true);
$eps=explode(",",$eps);

echo "<form name=mio method=get >
Nombre EPS:<input type=text name=nombre value='".$eps[1]."'><br>
Estado:<input type=number name=estadoeps value=".$eps[2].">
<input type=hidden name=N value=4>
<input type=hidden name=id value=".$_GET["donde"].">
<input type=submit></form>";
}
if($N==4){
  echo "Nivel 4<br>";

$url = "http://".$_SERVER["SERVER_NAME"]."/SALUD/eps/2/".$_GET["id"].";".str_replace(' ','+',$_GET["nombre"]).";".$_GET["estadoeps"];
//      echo $url."<br>";
$JSON =  file_get_contents($url,true);
echo "<script>
location.href='".$_SERVER['PHP_SELF']."';
</script>";
}
if($N==5){
  echo "Nivel 5<br>";
  $url = "http://".$_SERVER["SERVER_NAME"]."/SALUD/eps/3/".$_GET["donde"];
$JSON =  file_get_contents($url,true);
echo "<script>
location.href='".$_SERVER['PHP_SELF']."';
</script>";
}
