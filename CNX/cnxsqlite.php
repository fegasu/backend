<?php
class SqlitePDO{
var $Cnx;
var $Rs;
var $u;
public $numcols;


 function __construct($Bd="SALUD.db"){
 try {
    $this->Cnx= new PDO('sqlite:'.$Bd);
  } catch (Exception $e) {die ($e);}
 }

 function Ejecutar($Sentencia){

  try{
   $this->Rs = $this->Cnx->prepare($Sentencia.';') or die(SQLITE_ERROR.' '.$Sentencia);
   $this->Rs->execute();
   $this->numcols=$this->Rs->columnCount();
   
   }catch (Exception $e){ die($e);
   }
 }
 
   function EjecutarJSON($Sentencia){
//      $this->Rs = $this->Cnx->query($Sentencia,PDO::FETCH_OBJ);    
      $this->Rs = $this->Cnx->query($Sentencia,PDO::FETCH_OBJ);    
      return json_encode($this->Rs);
  }
   
 function CargarJSON(){
       $i=0;
       $rawdata = array();
       foreach ($this->Rs as $row) {
              $rawdata[] = $row;
             }
             return json_encode($rawdata);
   }
 function CargarArray(){
       $i=0;
       $rawdata = array();
       foreach ($this->Rs as $row) {
               $rawdata[][] = $row;
             }
        return $rawdata;
   }

 function Cargar(){
  $this->u = $this->Rs->fetch();
  return ($this->u );
 }

 function Resultado(){
    $i=0;$a="";
  for($i=0; $i<$this->numcols;$i++){
     $a.=$this->getdato($i);
     if($i<$this->numcols-1)
        $a.=",";   
    }
    return $a;
 }

  function getdato($col){
  //$a=$this->Rs->fetchColumn($col);
  $a=$this->u[$col];
  return $a;
 }
}



?>