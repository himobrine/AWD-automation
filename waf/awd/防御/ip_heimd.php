<?php 
// $ip=$_SERVER["REMOTE_ADDR"]; 
// $ban=file_get_contents("ip"); //需要创建一个ip文件，里面是黑名单
// if(stripos($ban,$ip)) 
// { 
//   die("No");   
// }
//黑名单
$banned_ip = array (
"172.18.140.13","172.18.140.14","172.18.140.15"
);
if (!in_array( getenv("REMOTE_ADDR"), $banned_ip ) )
{
die ("No");
}
?>