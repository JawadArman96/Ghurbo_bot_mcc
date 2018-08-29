<?php

//get the q parameter from URL
$q=$_GET["q"];
$url = "http://dev.ghurbo.com/api/city_search?airport_search=".$q;

$ch = curl_init(); 
curl_setopt($ch, CURLOPT_URL, $url); 
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
$result = curl_exec($ch);
$result = json_decode($result);
curl_close($ch);

if (strlen($q)>2) {
  $hint = "";
  for ($i=0; $i < sizeof($result); $i++) {
    if($hint == "") {
      $hint = '<option value="' . $result[$i]->iata_code . '">' . $result[$i]->municipality . ", " . $result[$i]->country_name . " - " . 
      $result[$i]->name . " (" . $result[$i]->iata_code . ")" . "</option>"; 
    }
    else {
      $hint = $hint . '<option value="' . $result[$i]->iata_code . '">' . $result[$i]->municipality . ", " . $result[$i]->country_name . " - " . 
      $result[$i]->name . " (" . $result[$i]->iata_code . ")" . "</option>"; 
    }
  }
}

if (strlen($q) > 2)
  $response=$hint;


//output the response
echo $response;
?>