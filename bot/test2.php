<?php

/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
    exec('C:/wamp64/bin/php/php5.6.35/php.exe C:/wamp64/www/bot/test.php one_way_all_search DAC CCU 2018-09-6 2018-09-10 economy 1 0 0',$output);
    file_put_contents('C:\wamp64\www\bot\out.html', $output);        
    #flightType=one_way_all_search&departCity=DAC&$arriveCity=SIN&departDate=2018-09-06&returnDate=2018-09-10&class=economy&adultCount=1&childCount=0&infantCount=0
?>