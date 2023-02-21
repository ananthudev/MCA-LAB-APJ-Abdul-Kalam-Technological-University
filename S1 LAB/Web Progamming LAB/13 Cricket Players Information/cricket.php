<html>
<head>
<title> Indian Cricket Team</title>
</head>
<body>
<?php
$Indianteam = array("Rohit Sharma", "KL Rahul", 
"Shikhar Dhawan", "Virat Kohli","Rajat Patidar",
"Shreyas Iyer","Rahul Tripathi","Ravichandran Ashwin",
"Ishan Kishan","Sanju Samson","Ravindra Jadeja");
?>
<table border="1" background="cricket.jpg" style="color:RED" width="40%" height="80%" align="center">
<thead>
<tr>
	<th>
	Jersey number
	</th>
	<th>
	Player
	</th>
</tr>
</thead>
<?php
$slno=1;
foreach($Indianteam as $player)
   {
	?>  
	<tr>
	<td> <?php   echo $slno++; ?> </td>
    <td> <?php   echo $player; ?> </td>
	</tr>
   <?php
   }
?>
</table>
</body>
</html>