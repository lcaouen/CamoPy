<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="Loïc Caouën">
    <title>CamoPy Administration</title>


    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" />
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.2/css/all.css" rel="stylesheet" />
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/flatpickr/dist/flatpickr.min.css" />
    <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/flatpickr"></script>
    <script src="./static/index.js"></script>
  

    <style>
      .bd-placeholder-img {
        font-size: 1.125rem;
        text-anchor: middle;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
      }

      @media (min-width: 768px) {
        .bd-placeholder-img-lg {
          font-size: 3.5rem;
        }
      }
    </style>
  </head>
  <body class="bg-light">
    <div class="container">
      <div class="py-5 text-center">
        <h2>CamoPy Administration</h2>
        <p class="lead">Vous pouvez configurer votre Webcam grace à cette page d'administration.</p>
      </div>

      <div class="row">
        <div class="input-group">
          <input type="password" class="form-control" id="password" placeholder="Mot de passe">
          <div class="input-group-append">
            <button class="btn btn-secondary" onclick="loadData()" >Connexion</button>
          </div>
        </div>
      </div>
    
      <div class="collapse" id="collapseParameters">

        <hr class="mb-4">

        <img id="currentImage" src="" alt="no image">
        <div class="row">
          <div class="col-md-12 order-md-1">
              <h4 class="mb-3">Application</h4>
              <div class="row">
                <div class="col-md-3 mb-3">
                  <label for="name">Nom</label>
                  <input type="text" class="form-control" id="name" placeholder="" value="">
                </div>
                <div class="col-md-3 mb-3">
                  <label for="port">Port</label>
                  <input type="text" class="form-control" id="port" placeholder="" value="">
                </div>
                <div class="col-md-3 mb-3">
                  <label for="pwd">Mot de passe</label>
                  <input type="text" class="form-control" id="pwd" placeholder="" value="">
                </div>
                <button class="btn btn-primary btn-lg">Redémarrer</button>
              </div>

              <hr class="mb-4">

              <h4 class="mb-3">Images</h4>
              <div class="row">
                <div class="col-md-1 mb-3">
                  <label for="detection">Détection</label>
                  <input type="text" class="form-control" id="detection" placeholder="" value="">
                </div>
                <div class="col-md-2 mb-3">
                  <label for="threshold">Seuil</label>
                  <input type="text" class="form-control" id="threshold" placeholder="" value="">
                </div>
                <div class="col-md-9 mb-3">
                  <label for="path">Répertoire</label>
                  <input type="text" class="form-control" id="path" placeholder="" value="">
                </div>
              </div>

              <div class="row">
                <div class="col-md-3 mb-3">
                  <label for="width">Largeur</label>
                  <input type="text" class="form-control" id="width" placeholder="" value="">
                </div>
                <div class="col-md-3 mb-3">
                  <label for="height">Hauteur</label>
                  <input type="text" class="form-control" id="height" placeholder="" value="">
                </div>
                <div class="col-md-3 mb-3">
                  <label for="framerate">Cadence</label>
                  <input type="text" class="form-control" id="framerate" placeholder="" value="">
                </div>
                <div class="col-md-3 mb-3">
                  <label for="iso">ISO</label>
                  <input type="text" class="form-control" id="iso" placeholder="" value="">
                </div>
              </div>

              <hr class="mb-4">

              <h4 class="mb-3">Mail</h4>

              <div class="row">
                <div class="col-md-3 mb-3">
                  <label for="smtpServer">Serveur SMTP</label>
                  <input type="text" class="form-control" id="smtpServer" placeholder="" value="">
                </div>
                <div class="col-md-3 mb-3">
                  <label for="mailPort">Port</label>
                  <input type="text" class="form-control" id="mailPort" placeholder="" value="">
                </div>
                <div class="col-md-3 mb-3">
                  <label for="address">Email</label>
                  <input type="email" class="form-control" id="address" placeholder="you@example.com" value="">
                </div>
                <div class="col-md-3 mb-3">
                  <label for="mailPwd">Mot de passe</label>
                  <input type="text" class="form-control" id="mailPwd" placeholder="" value="">
                </div>
              </div>

              <div class="row">
                <div class="col-md-9 mb-3">
                  <label for="message">Message</label>
                  <textarea rows="4" cols="50" class="form-control" id="message"></textarea> 
                </div>
                <div class="col-md-3 mb-3">
                  <label for="wait">Délai envoi</label>
                  <input type="text" class="form-control" id="wait" placeholder="" value="">
                </div>
              </div>

              <hr class="mb-4">

              <h4 class="mb-3">OneDrive</h4>

              <div class="row">
                <div class="col-md-3 mb-3">
                  <label for="url">URL</label>
                  <input type="text" class="form-control" id="url" placeholder="" value="">
                </div>
                <div class="col-md-3 mb-3">
                  <label for="directory">Répertoire des images</label>
                  <input type="text" class="form-control" id="directory" placeholder="" value="">
                </div>
                <div class="col-md-3 mb-3">
                  <label for="clientSecret">clientSecret</label>
                  <input type="text" class="form-control" id="clientSecret" placeholder="" value="">
                </div>
                <div class="col-md-3 mb-3">
                  <label for="clientId">clientId</label>
                  <input type="text" class="form-control" id="clientId" placeholder="" value="">
                </div>
              </div>

              <hr class="mb-4">
              <button class="btn btn-primary btn-lg">Enregistrer</button>
          </div>
        </div>
      </div>

      <footer class="my-5 pt-5 text-muted text-center text-small">
        <p class="mb-1">&copy; 2017-2019 Company Name</p>
        <ul class="list-inline">
          <li class="list-inline-item"><a href="#">Privacy</a></li>
          <li class="list-inline-item"><a href="#">Terms</a></li>
          <li class="list-inline-item"><a href="#">Support</a></li>
        </ul>
      </footer>
    </div>
  </body>
</html>
