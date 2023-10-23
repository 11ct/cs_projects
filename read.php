<?php
// Check if id is available | is used to read the data from table rows
if (isset($_GET["id"]) && !empty(trim($_GET["id"]))) {

    //Access database config
    require_once("config.php");

    $sql = "SELECT * FROM employee_data WHERE id = ?";

    if ($stmt = $conn->prepare($sql)) {
        // bind variable to prepare statement as parameters
        $stmt->bind_param("i", $param_id);

        // setting parameter
        $param_id = trim($_GET["id"]);

        // attempt to execute the prepared statement
        if ($stmt->execute()) {
            $result = $stmt->get_result();

            if ($result->num_rows == 1) {
                $row = $result->fetch_array(MYSQLI_ASSOC);

                $name = $row['name'];
                $address = $row['address'];
                $salary = $row['salary'];
            } else {
                header('location: error.php');
                exit();
            }

        } else {
            echo "Oops, something went wrong!";
        }
    }
    //Close the statement to free up memory
    $stmt->close();

    $conn->close();
} else {
    header("location: error.php");
    exit();
}

?>


<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css"
        integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">

    <title>
        <?php echo $name ?> - Page
    </title>
    <style>
        .wrapper {
            max-width: 800px;
            margin: 0 auto;
        }
    </style>
</head>

<body>

    <div class="wrapper">
        <div class="container-fluid">
            <div class="row">
                <div class="col-md-12">
                    <div class="mt-5 mb-3 clearfix">
                        <h2 class="pull-left">
                            <?php echo $name ?>'s Details
                        </h2>
                        <table class="table table-striped">
                            <tr>
                                <td>Name</td>
                                <td>
                                    <?php echo $name; ?>
                                </td>
                            </tr>
                            <tr>
                                <td>Address</td>
                                <td>
                                    <?php echo $address; ?>
                                </td>
                            </tr>
                            <tr>
                                <td>Salary</td>
                                <td>
                                    <?php echo $salary; ?>
                                </td>
                            </tr>
                        </table>

                        <br>
                        <a href="index.php" class="btn btn-primary">Back</a>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-Fy6S3B9q64WdZWQUiU+q4/2Lc9npb8tCaSX9FK7E8HnRr0Jz8D6OP9dO5Vg3Q9ct" crossorigin="anonymous"></script>

</body>

</html>