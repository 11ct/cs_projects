<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css"
        integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">

    <title>Hello, world!</title>
</head>

<body>
    <?php
    require_once("config.php");
    $num = "SELECT COUNT(id) FROM employee_data";
    $morethan50 = "SELECT COUNT(id) FROM employee_data WHERE salary > 50";
    $lessthan50 = "SELECT COUNT(id) FROM employee_data WHERE salary < 50";
    $averagesalary = "SELECT AVG(salary) FROM employee_data";
    $total_employees = $conn->query($num)->fetch_array();
    $morethanfifty = $conn->query($morethan50)->fetch_array();
    $lessthanfifty = $conn->query($lessthan50)->fetch_array();
    $avgsalary = $conn->query($averagesalary)->fetch_array();

    ?>

    <div class="wrapper">
        <div class="container-fluid">
            <div class="row">
                <div class="col-md-12">
                    <div class="mt-5 mb-3 clearfix">
                        <h2 class="pull-left">Employee Details <small>(<?php echo $total_employees[0]; ?> employees)</small></h2>
                        <h3 class="pull-left"><small><b>Number of employees with salary > 50: <?php echo $morethanfifty[0]?></b></small></h3>
                        <h3 class="pull-left"><small><b>Number of employees with salary < 50: <?php echo $lessthanfifty[0]?></b></small></h3>
                        <h3 class="pull-left"><small><b>Average salary of an employee: $<?php echo $avgsalary[0]?></b></small></h3>
                        <a href="create.php" class="btn btn-success pull-right">Add New Employee</a>
                    </div>

                        <?php
                        // require_once("config.php");
                        // Fetch all employees data from database
                        $sql = "SELECT * FROM employee_data";

                        if ($result = $conn->query($sql)) {
                            if ($result->num_rows > 0) {

                                echo '<table class="table table-bordered table-striped">';
                                echo '    <thead>';
                                echo '        <tr>';
                                echo '            <th>#</th>';
                                echo '            <th>Name</th>';
                                echo '            <th>Salary</th>';
                                echo '            <th>Address</th>';
                                echo '            <th>#Actions</th>';
                                echo '        </tr>';
                                echo '    </thead>';
                                echo '    <tbody>';
                                while ($row = $result->fetch_array()) {
                                    echo "<tr>";
                                    echo "<td>" . $row['id'] . "</td>";
                                    echo "<td>" . $row['name'] . "</td>";
                                    echo "<td>" . $row['salary'] . "</td>";
                                    echo "<td>" . $row['address'] . "</td>";
                                    echo "<td>";
                                    echo "<a href='read.php?id=" . $row["id"] . "'>View</a>";
                                    echo "<a href='delete.php?id=" . $row["id"] . "'>Delete</a>";
                                    echo "</td>";

                                    echo "    <td>";
                                    echo '        <a href="view.php">View</a>';
                                    echo '        <a href="edit.php">Edit</a>';
                                    echo '        <a href="delete.php">Delete</a>';
                                    echo "    </td>";
                                    echo "</tr>";
                                }

                                echo '    </tbody>';
                                echo '</table>';
                                // Free result set
                                $result->free();
                            } else {
                                echo '<div class="alert alert-danger"><em>No records were found.</em></div>';
                            }
                        }
                        ?>
                </div>
            </div>
        </div>
    </div>





    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: jQuery and Bootstrap Bundle (includes Popper) -->
    <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js"
        integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj"
        crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-Fy6S3B9q64WdZWQUiU+q4/2Lc9npb8tCaSX9FK7E8HnRr0Jz8D6OP9dO5Vg3Q9ct"
        crossorigin="anonymous"></script>

    <!-- Option 2: Separate Popper and Bootstrap JS -->
    <!--
    <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.min.js" integrity="sha384-+sLIOodYLS7CIrQpBjl+C7nPvqq+FbNUBDunl/OZv93DB7Ln/533i8e/mZXLi/P+" crossorigin="anonymous"></script>
    -->
</body>

</html>