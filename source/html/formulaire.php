<?php
  /*****************************************
  *  Constantes et variables
  *****************************************/
  define('LOGIN','bob');  // Login correct
  define('PASSWORD','eponge');  // Mot de passe correct
  $message = '';      // Message à afficher à l'utilisateur
  $auth = false;
 
  /*****************************************
  *  Vérification du formulaire
  *****************************************/
  // Si le tableau $_POST existe alors le formulaire a été envoyé
  if(!empty($_POST))
  {
    // Le login est-il rempli ?
    if(empty($_POST['login']))
    {
      //$message = 'Veuillez indiquer votre login svp !';
	  $message = 'Vous devez saisir un login !';
    }
      // Le mot de passe est-il rempli ?
      elseif(empty($_POST['motDePasse']))
    {
      $message = 'Veuillez indiquer votre mot de passe svp !';
    }
      // Le login est-il correct ?
      elseif($_POST['login'] !== LOGIN)
    {
      $message = 'Votre login est faux !';
    }
      // Le mot de passe est-il correct ?
      elseif($_POST['motDePasse'] !== PASSWORD)
    {
      $message = 'Votre mot de passe est faux !';
    }
      else
    {
      // L'identification a réussi
      $message = 'Bienvenue '. LOGIN .' !';
	  $auth = true;
    }
  }
?>

<!DOCTYPE html>
<html>
<head>
<title>Formulaire web</title>
<meta charset='utf-8' />
	<link type="text/css" href="css/style.css" rel="stylesheet">	
</head>
<body>

<!-- script php pour la gestion des erreurs ou de succes du formulaire -->
<?php if(!empty($message) and $auth==true) {
      echo '<p class="succes centre">'.$message.'</p>';
	  exit();
	} elseif (!empty($message)){
	  echo '<p class="erreur centre">'.$message.'</p>';
	}
?>

<form action="formulaire.php" method="post" class="form-example">
  <div class="form-example">
    <label for="login">Saisir votre nom: </label>
    <input type="text" name="login" id="login">
  </div>
  <div class="form-example">
    <label for="password">Mot de passe :</label> 
    <input type="password" name="motDePasse" id="password" value="" /> 
  </div>
  <div class="form-example top">
    <input class="bouton" type="submit" value="Envoyer!">
  </div>
</form>

</body >
</html>
