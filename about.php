<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>黃子鑒個人網頁</title>
		<style type="text/css">
		* { font-family:"標楷體"; margin-left:auto; margin-right:auto;}
		h1 {color:blue; font-size:60px;}
		h2 {color:#33ff33; font-size:40px;}
	</style>

</head>


<body>
	<?php echo date("Y-m-d") ?>
	<h1>黃子鑒</h1>

	<br>個人網頁</br>
	<br><a href="https://www.facebook.com/">FB</a></br>
	<a href="https://www.youtube.com/">youtube</a>
	E-Mail: AA@pu.edu.tw
	<iframe src="https://www.youtube.com/embed/pW88QFpHXa8" allowfullscreen></iframe>

	<audio controls>
		<source src="elephant.mp3" type="audio/mP3">
	</audio><br>

<table width="70%">
		<tr>
			<td>
				<img src="Image/th.jpg" width="110%" alt="jfisfjo" id="pic" onmouseover="change1()" onmouseout="change2()">
			</td>>

			<td>
				<h1 id="h2text">黃子鑒</h1>
				<h2>Garen</h2>
			</td>
		</tr>
	</table>
	<script>
			function change1() {
  			document.getElementById("pic").src = "Image/apple.jpg";
  			document.getElementById("h2text").innerText = "靜宜資管";
		}

		function change2() {
  			document.getElementById("pic").src = "Image/guava.jpg";
  			document.getElementById("h2text").innerText = "帥哥黃子鑒";
		}
	</script>


</body>
</html>