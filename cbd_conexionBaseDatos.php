
<?php
//Codigo para la conexion a la base de datos
  $con = mysqli_connect("db.inf.uct.cl", "jpacheco", "175579672", "jpacheco");
  
  if(!$con){
    print_r(mysqli_connect_error());
    return false;
  }else{
    $con->set_charset("utf8");
    return $con;
  }


?>