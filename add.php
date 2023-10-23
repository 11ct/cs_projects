<?php
//Connect to the database
require_once("config.php");

//initialise variables 
$name = $address = $salary = "";

if ($_SERVER["REQUEST_METHOD"] = "POST") {
    $input_name = trim($_POST["name"]);
    $name = $input_name;
    
    $input_address = trim($_POST["address"]);
    $address = $input_address;

    $input_salary = trim($_POST["salary"]);
    $salary = $input_salary;

    $sql = "INSERT INTO employee_data (name, address, salary) VALUES(?,?,?)";

    if ($stmt = $conn->prepare($sql)) {
        $stmt->bind_param("sss", $param_name, $param_address, $param_salary);

        // Set parameters
        $param_name = $name;
        $param_address = $address;
        $param_salary = $salary;

        if ($stmt->execute()) {
            // If successful, then redirect to the index page
            header("location: index.php");
            exit();
        } else {
            echo "Something is not right";
        }
    }
    $stmt->close();
}

$conn->close();
?>