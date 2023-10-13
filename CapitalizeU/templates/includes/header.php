<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>CapitalizeU</title>

   <!-- Bootstrap core CSS -->
    <link href="templates/css/bootstrap.css" rel="stylesheet">
    <!-- Custom styles for this template -->
    <link href="templates/css/custom.css" rel="stylesheet">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <script src="templates/js/bootstrap.js"></script>
	<script src="templates/js/ckeditor/ckeditor.js"></script>
  <link rel="stylesheet" href="main.css">
	<?php
    //Check if title is set, if not assign it
    if(!isset($title)){
    	$title = SITE_TITLE;
    }
    ?>
  </head>

  <body>

    <div class="navbar navbar-inverse navbar-fixed-top" role="navigation" style="padding: 2%;">
      <div class="container">
        <div class="navbar-header">
          <a class="navbar-brand" href="index.php" style="font-size: 30px; padding-bottom: 90px; padding-top:0px; padding-left: 0px; "><b>CapitalizeU</b></a>
        </div>
        <div class="collapse navbar-collapse" >
          <ul class="nav navbar-nav navbar-right">
            <li><a href="index.html"><b>Home</b></a></li>
            <li class="dropdown"><a href="#"><span><b>Services</b></span> <i class="bi bi-chevron-down"></i></a>
            <ul>
              <li><a href="video.html">Video Connect</a></li>
              <li><a href="vs.html">Resources</a></li>
              <li><a href="index.php">Discussion forum</a></li>
            </ul>
          </li>
			<?php if(!isLoggedIn()) : ?>
				<li><a href="register.php"><b>Create An Account</b></a></li>
			<?php else : ?>
				<li><a href="create.php"><b>Create Topic</b></a></li>
			<?php endif; ?>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </div>

    <br>
    <br>


    <div class="container">
		<div class="row">
			<div class="col-md-8">
				<div class="main-col">
					<div class="block">
						<h1 class="pull-left"><?php echo $title; ?></h1>
						<h4 class="pull-right">A simple PHP forum engine</h4>
						<div class="clearfix"></div>
						<hr>
						<?php displayMessage(); ?>