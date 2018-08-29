<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1,user-scalable=0">
  <title>Ghurbo Flight Search</title>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js">
  </script>
  <link rel="stylesheet" href="//res.wx.qq.com/open/libs/weui/1.1.2/weui.min.css"/>

  <style>
    .fb{
      background-color:#4080FF;
    }

    body{
      background: #efefef;
      padding: 20px;
    }

    .weui-cells__title {
      padding-left: 0px;
      padding-right: 0px;
    }

    #depart_city, #arrive_city { 
      max-width: 300px;
    }
  </style>
  <script>
    function showResult(str) {
      if (str.length==0) { 
        document.getElementById("depart_city").innerHTML="";
        document.getElementById("depart_city").style.border="0px";
        return;
      }
      if (window.XMLHttpRequest) {
    // code for IE7+, Firefox, Chrome, Opera, Safari
    xmlhttp=new XMLHttpRequest();
  } else {  // code for IE6, IE5
    xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
  xmlhttp.onreadystatechange=function() {
    if (this.readyState==4 && this.status==200) {
      document.getElementById("depart_city").innerHTML=this.responseText;
      document.getElementById("depart_city").style.border="1px solid #A5ACB2";

    }
  }
  xmlhttp.open("GET","livesearch.php?q="+str,true);
  xmlhttp.send();
}

function showResult2(str) {
  if (str.length==0) { 
    document.getElementById("arrive_city").innerHTML="";
    document.getElementById("arrive_city").style.border="0px";
    return;
  }
  if (window.XMLHttpRequest) {
    // code for IE7+, Firefox, Chrome, Opera, Safari
    xmlhttp=new XMLHttpRequest();
  } else {  // code for IE6, IE5
    xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
  xmlhttp.onreadystatechange=function() {
    if (this.readyState==4 && this.status==200) {
      document.getElementById("arrive_city").innerHTML=this.responseText;
      document.getElementById("arrive_city").style.border="1px solid #A5ACB2";
    }
  }
  xmlhttp.open("GET","livesearch2.php?q="+str,true);
  xmlhttp.send();
} 
</script>

</head>
<body>
  <div class="weui-cells__title">Ghurbo Flight Search</div>
  <form id="dropreqform" action="results.php" method="post">
   <input type="radio" value="round_trip_all_search" name="flight_type" checked="checked" id="radio1" onclick="display()"></input>
   <label for="radio1">Round trip</label>
   &nbsp; &nbsp; &nbsp; 
   <input type="radio" value="one_way_all_search" name="flight_type" id="radio2" onclick="hide()"></input>
   <label for="radio2">One way</label>
   <input type="hidden" name="fbid" value="">
   <input type="hidden" name="product_subcategory_id" value="0">

   <div class="weui-cells__title"></div>
   <input type="text" size="20" placeholder="Flying from..." onkeyup="showResult(this.value)">
   <select name="depart_city" id="depart_city" required> </select>

   <div>
     <input type="text" size="20" placeholder="Flying to..." onkeyup="showResult2(this.value)">
     <select name="arrive_city" id="arrive_city" required> </select>
   </div>
 </div>

 <div class="weui-cells__title">Depart date:
  <input name="depart_date" id="depart_date" type="date" min="2018-07-24" onchange="changeDatePicker();" required> 
</div>

<div id="ret" class="weui-cells__title">
  Return date:<input name="return_date" id="return_date" type="date" required>
</div>

<div class="weui-cells__title">Class
  <select name="class">
    <option value="economy">Economy</option>
    <option value="economy_standard">Economy Standard</option>
    <option value="economy_premium">Economy Premium</option>
    <option value="business">Business Class</option>
  </select> 
</div>

<div class="weui-cells__title">
  Adult
  <select name="adult" id="adult" onchange="changeOptAdult();">
    <option>1</option>
    <option>2</option>
    <option>3</option>
    <option>4</option>
    <option>5</option>
    <option>6</option>
    <option>7</option>
    <option>8</option>
    <option>9</option>
  </select>
  Child
  <select name="child" id="child" onchange="changeOptChild();">
   <option>0</option> 
   <option>1</option>
   <option>2</option>
   <option>3</option>
   <option>4</option>
   <option>5</option>
   <option>6</option>
   <option>7</option>
   <option>8</option>
 </select>
 Infant
 <select name="infant" id="infant" onchange="changeOptInfant();">
   <option>0</option> 
   <option>1</option>
 </select>

 <p id="passenger_count"> 1 passenger </p>
 <p id="datetest"> </p>
</div>


<div class="weui-btn-area">
  <button type="submit" form="dropreqform" class="weui-btn fb">Submit</button>
</div>
</form>

<script>
  function hide() {
    document.getElementById("ret").style.display = "none";
    document.getElementById("return_date").required = false;
  }

  function display() {
    document.getElementById("ret").style.display = "inline";
    document.getElementById("return_date").required = true;
  }

  function changeOptAdult() {
    var adultCount = $("#adult").val();
    var childCount = $("#child").val();
    var infantCount = $("#infant").val();

    if(adultCount < infantCount)
      var x = 1;

    $("#infant").empty();

    for(var i=0; i <= adultCount; i++) 
      $("#infant").append('<option>' + i + '</option>');
    
    $("#child").empty();

    for(var i=0; i <= (9 - adultCount); i++) 
      $("#child").append('<option>' + i + '</option>');
    
    $("#child").val(childCount);

    if(x) 
      $("#infant").val(0);   
    else 
      $("#infant").val(infantCount);
    

    var total = parseInt($("#child").val()) + parseInt($("#adult").val()) + parseInt($("#infant").val());
    $("#passenger_count").text(total + " passengers");
  }

  function changeOptChild() {
    var childCount = $("#child").val();
    var adultCount = $("#adult").val();
    var infantCount = $("#infant").val();

    $("#adult").empty();
    for(var i=0; i <= (9-childCount); i++)
      $("#adult").append('<option>' + i + '</option');
    
    $("#adult").val(adultCount);
    $("#infant").val(infantCount);

    var total = parseInt($("#child").val()) + parseInt($("#adult").val()) + parseInt($("#infant").val());
    $("#passenger_count").text(total + " passengers");
  }

  function changeOptInfant() {
    var total = parseInt($("#child").val()) + parseInt($("#adult").val()) + parseInt ($("#infant").val());
    if(total == 1)
      $("#passenger_count").text(total + " passenger"); 

    else 
     $("#passenger_count").text(total + " passengers");
 }
 var dateToday = new Date().toISOString().substr(0,10);
 $("#depart_date").attr("min", dateToday);

 function changeDatePicker() {
  var minDate = $("#depart_date").val();
  $("#return_date").attr("min", minDate);

  if($("#return_date").val() < minDate && $("#return_date").val() != '') 
    $("#return_date").val(minDate); 
}

</script>
</body>
</html>
