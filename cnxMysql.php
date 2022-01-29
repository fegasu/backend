<?php
date_default_timezone_set('Etc/GMT-5');

class DBMysql{
 var $f;
 var $t;
 var $e;
function __construct($base){
 $this->f=mysqli_connect("","root","",$base);
 //mysqli_select_db($this->f,$bd);
}

function Ejecutar($sentencia){
   $this->t=mysqli_query($this->f,$sentencia);
   
}
   function EjecutarArray($Sentencia){
    try{
     $this->Rs = $this->f->query($Sentencia);
     }catch (Exception $e){ die($e);}
   }
   function CargarArray(){
       $i=0;
       $rawdata = array();
       $rows = $this->Rs -> fetch_assoc();
       foreach ($rows as $row =>$valor) {
               $rawdata[$row] = $valor;
             }
          //echo json_encode($rawdata);
          return ($rawdata);

   }
   function CargarCSV(){
       $i=0;
       $raw="";
       while($rows = $this->e=mysqli_fetch_array($this->t,MYSQLI_NUM)){
       foreach ($rows as $valor) {
               $raw .= $valor.";";
             }
          //echo json_encode($rawdata);
             $raw=substr($raw,0,strlen($raw)-1);
             $raw.="|";
           }
           $raw=substr($raw,0,strlen($raw)-1);
          return ($raw);

   }

function Cargar(){
 return($this->e=mysqli_fetch_array($this->t,MYSQLI_NUM));
}

function getdato($col){
   return $this->e[$col];
}
    function Datos($col){
	    //die(chr(34).$col.chr(34));
        return ($this->e["$col"]);
    }
}

class Dame{
    function getId($Ced){
        
    }
    
}
