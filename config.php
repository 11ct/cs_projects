<?php
// Database config
//$db_host = "localhost";
//$db_user = "root";
//$db_pass = "";
//$db_name = "employees";
define('DB_SERVER', 'localhost');
define('DB_USER', 'root');
define('DB_PASSWORD', '');
define('DB_NAME', 'employees');

//Create database conneciton 
// $conn = new mysqli($db_host, $db_user, $db_pass)
$conn = new mysqli(DB_SERVER, DB_USER, DB_PASSWORD, DB_NAME);

//Check connection
if ($conn === false) {
    die("Connection failed: ". $conn->connect_error);
}
?>