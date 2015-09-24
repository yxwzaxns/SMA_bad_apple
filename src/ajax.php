<?php
//for ($k=1; $k < 3258; $k++) {
if(preg_match('/\w+iphone|Android\w*/i',$_SERVER['HTTP_USER_AGENT'])){echo 1;exit;}
if($_GET['id']>=3300) {echo 0;exit;}
$file='images/38030302_baofeng_'.$_GET['id'].'.jpg';
$img=imagecreatefromjpeg($file);
$imgSize=getimagesize($file);

$imgX=$imgSize[0];
$imgY=$imgSize[1];

$line=' ';
$char=' ';

for ($i=0; $i < 320; $i++) {
	$line[$i]='0';
}
for ($j=0; $j < $imgY;) {

	for ($i=0; $i < strlen($line); $i++) {
		$color=imagecolorat($img, $i, $j);
	if     ((($color >> 16) & 0xFF) >= 200){
				$line[$i]='0';
			}elseif((($color >>  8) & 0xFF) >= 200) {
				$line[$i]='0';
			}elseif(($color & 0xFF) >= 200) {
				$line[$i]='0';
			}else
				$line[$i]='1';
	}
		for ($t=0; $t < strlen($line);) {
			$line[$t+1]='';
			$line[$t+3]='';
			//$line[$t+2]='';
			//$line[$t+4]='';
			$t+=5;
		}
	echo $line;
	echo "<br>";
	$j+=3;
	}
//}
?>
