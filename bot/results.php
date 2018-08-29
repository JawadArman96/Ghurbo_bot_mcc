<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width,initial-scale=1,user-scalable=0">
	<title>Flight Search Results</title>
	<style>
		table {
			font-family: arial, sans-serif;
			border-collapse: collapse;
			width: 100%;
		}

		td, th {
			border: 1px solid #dddddd;
			text-align: left;
			padding: 8px;
		}

		tr:nth-child(even) {
			background-color: #dddddd;
		}
	</style>
</head>

<?php
$flightType = $_POST['flight_type'];
$departCity = $_POST['depart_city'];
$arriveCity = $_POST['arrive_city'];
$departDate = $_POST['depart_date'];
$returnDate = $_POST['return_date'];
$class = $_POST['class'];
$adultCount = $_POST['adult'];
$childCount = $_POST['child'];
$infantCount = $_POST['infant'];

$url = "http://dev.ghurbo.com/api/flight_search";

if($flightType == 'one_way_all_search')
	$postFields = "secret_key=123456&search_type=".$flightType."&depart_city=".$departCity."&arrive_city=".$arriveCity."&depart_date=".$departDate."&adult_count=".$adultCount."&child_count=".$childCount."&infant_count=".$infantCount."&seat_type_class=".$class;

elseif ($flightType == 'round_trip_all_search')
	$postFields = "secret_key=123456&search_type=".$flightType."&depart_city=".$departCity."&arrive_city=".$arriveCity."&depart_date=".$departDate."&return_date=".$returnDate."&adult_count=".$adultCount."&child_count=".$childCount."&infant_count=".$infantCount."&seat_type_class=".$class;

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $postFields);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
$result = curl_exec($ch);

$result = json_decode($result);

if($flightType == 'one_way_all_search') {
	$nonStopFlights = $result->data->nostop; ?>
	<h3> Non-stop Flights: </h3>
	<table>
		<tr>
			<th> Flight No. </th>
			<th> Departure </th>
			<th> Arrival </th>
			<th> Total Fare </th>
		</tr>
		<?php
		if(sizeof($nonStopFlights) == 0)
			echo " N/A <br />" ;
		else {
			for($i=0; $i < sizeof($nonStopFlights); $i++) { 
				$arrival = $nonStopFlights[$i]->arrival;
				echo "<tr> <td>" . '<img width="70px" height="70px" src="' . $arrival->airlinesIcon . '"> <br> <i>' . $arrival->airlinesName . "<br>" . $arrival->flightName . " " . $arrival->flightNo . "</i> </td>";

				echo "<td> <p>" . $arrival->departureDate . "<br>" . $arrival->departureTime . "</p>";
				echo "<p>" . $arrival->departureCity . "<br>" .$arrival->departAirport . " (".$arrival->departFrom.")" . "</p> </td>";

				echo "<td> <p>" . $arrival->arrivalDate . "<br>" . $arrival->arrivalTime . "</p>";
				echo "<p>" . $arrival->arrivalCity . "<br>" .$arrival->arriveAirport . " (".$arrival->arriveTo.")" . "</p> </td>";


				echo "<td>" . $arrival->flightPriceCurrency . " " . $arrival->flightPrice . "</td> </tr>";
			}
			echo "</table>";	
		}

		echo "<br />";	

		$multiStopFlights = $result->data->multistop;
		echo "<h3> Multi-stop Flights: </h3>";
		for($i=0; $i < sizeof($multiStopFlights); $i++) {
			echo "<h3> Route#" . ($i+1) . ": </h3>";
			echo "<p> <i>" . $multiStopFlights[$i]->arrival[0]->flightPriceCurrency . " " . $multiStopFlights[$i]->arrival[0]->flightPrice . "</i> </p>";
			echo "<table> <tr> <th> Flight No. </th> <th> Departure </th> <th> Arrival </th> </tr>";
			for($j=0; $j < sizeof($multiStopFlights[$i]->arrival); $j++) {
				$arrival = $multiStopFlights[$i]->arrival[$j];

				echo "<tr> <td>" . '<img width="70px" height="70px" src="' . $arrival->airlinesIcon . '"> <br> <i>' . $arrival->airlinesName . "<br>" . $arrival->flightName . " " . $arrival->flightNo . "</i> </td>";

				echo "<td> <p>" . $arrival->departureDate . "<br>" . $arrival->departureTime . "</p>";
				echo "<p>" . $arrival->departureCity . "<br>" .$arrival->departAirport . " (".$arrival->departFrom.")" . "</p> </td>";

				echo "<td> <p>" . $arrival->arrivalDate . "<br>" . $arrival->arrivalTime . "</p>";
				echo "<p>" . $arrival->arrivalCity . "<br>" .$arrival->arriveAirport . " (".$arrival->arriveTo.")" . "</p> </td>";

			}
			echo "</table>";
			echo "<br> <hr>";
		}
	}

	if($flightType == 'round_trip_all_search') {
		$nonStopFlights = $result->data->nostop;
		echo "<h3> Non-stop Flights: </h3>"; 
		if(sizeof($nonStopFlights) == 0)
			echo " N/A <br />";
		else {
			echo "
			<table>
				<tr>
					<th> Outbound Flight </th>
					<th> Return Flight </th>
					<th> Total Fare </th>
				</tr>";
				for($i=0; $i < sizeof($nonStopFlights); $i++) {
					$arrival = $nonStopFlights[$i]->arrival;
					$return = $nonStopFlights[$i]->return;
					
					echo "<tr> <td>" . '<img width="70px" height="70px" src="' . $arrival->airlinesIcon . '"> <br> <i>' . $arrival->airlinesName . "<br>" . $arrival->flightName . " " . $arrival->flightNo . "</i> <br> <br>";

					echo "<b>" . $arrival->departFrom . "</b> <sub>" . $arrival->departureDate . " - " . $arrival->departureTime . "</sub>" . " &#9992; <b>" . $arrival->arriveTo . "</b> <sub>" . $arrival->arrivalDate . " - " . $arrival->arrivalTime . "</sub> <br> <br>";

					echo "<b> Departure: </b>".$arrival->departureCity.". ".$arrival->departAirport;
					echo "<br />";
					echo "<b> Arrival: </b>".$arrival->arrivalCity.", ".$arrival->arriveAirport . "</td>";


					echo "<td>" . '<img width="70px" height="70px" src="' . $return->airlinesIcon . '"> <br> <i>' . $return->airlinesName . "<br>" . $return->flightName . " " . $return->flightNo . "</i> <br> <br>";

					echo "<b>" . $return->departFrom . "</b> <sub>" . $return->departureDate . " - " . $return->departureTime . "</sub>" . " &#9992; <b>" . $return->arriveTo . "</b> <sub>" . $return->arrivalDate . " - " . $return->arrivalTime . "</sub> <br> <br>";

					echo "<b> Departure: </b>" . $return->departureCity.". ".$return->departAirport;
					echo " (".$return->departFrom.")";
					echo "<br />";
					echo "<b> Arrival: </b>".$return->arrivalCity.", ".$return->arriveAirport . "</td>";

					echo "<td>" . $arrival->flightPriceCurrency . " " .$arrival->flightPrice . "</td> </tr>";
				}
				echo "</table>";
			}
			echo "<br />";

			$multiStopFlights = $result->data->multistop;
			echo "<h3> Multi-stop Flights: </h3>"; 
			echo "<table> <tr> <th> Outbound Flight(s) </th> <th> Return Flight(s) </th> <th> Total Fare </th> </tr>";
			for($i=0; $i < sizeof($multiStopFlights); $i++) {			
				echo "<td>";	
				for($j=0; $j < sizeof($multiStopFlights[$i]->arrival); $j++) {
					$arrival = $multiStopFlights[$i]->arrival[$j];
					if ($j==0)
						echo '<img width="70px" height="70px" src="' . $arrival->airlinesIcon . '"> <br>';

					echo "<i>" . $arrival->airlinesName . "<br>" . $arrival->flightName . " " . $arrival->flightNo . "</i> <br>";

					echo "<b>" . $arrival->departFrom . "</b> <sub>" . $arrival->departureDate . " - " . $arrival->departureTime . "</sub>" . " &#9992; <b>" . $arrival->arriveTo . "</b> <sub>" . $arrival->arrivalDate . " - " . $arrival->arrivalTime . "</sub> <br>";
					echo "<strong>" . $arrival->departureCity . " - " . $arrival->arrivalCity . "</strong> <br> <br>";
				}

				echo "</td> <td>";
				for($k=0; $k < sizeof($multiStopFlights[$i]->return); $k++) {
					if ($k==0)
						echo '<img width="70px" height="70px" src="' . $return->airlinesIcon . '"> <br>';

					echo "<i>" . $return->airlinesName . "<br>" . $return->flightName . " " . $return->flightNo . "</i> <br>";

					echo "<b>" . $return->departFrom . "</b> <sub>" . $return->departureDate . " - " . $return->departureTime . "</sub>" . " &#9992; <b>" . $return->arriveTo . "</b> <sub>" . $return->arrivalDate . " - " . $return->arrivalTime . "</sub> <br>";
					echo "<strong>" . $return->departureCity . " - " . $return->arrivalCity . "</strong> <br> <br>";
				}
				echo "<td>" . $multiStopFlights[$i]->arrival[0]->flightPriceCurrency . " " . $multiStopFlights[$i]->arrival[0]->flightPrice . "</td>";
				echo "</tr>";
			}
		}
		?>
		</html>