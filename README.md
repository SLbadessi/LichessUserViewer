# LichessUserViewer
<h1>But de l'application</h1>
<p>Dans l'objectif de fournir des informations détaillées sur les performances d'un utilisateur de Lichess, cette application a été développée en utilisant  l'API de Lichess. Les principales fonctionnalités de l'application incluent :
Fonctionnalités

    Type de Parties : Découvrez les différentes catégories de parties auxquelles le joueur a participé, telles que Blitz, Bullet, Rapid ou Classique.

    Taux de Victoires : Obtenez le taux de victoires du joueur, calculé en fonction du nombre total de parties jouées, de victoires, de défaites et de matchs nuls.

    Visualisation Graphique : Une représentation graphique claire est générée pour illustrer la distribution des types de parties jouées par le joueur.</p>
docker build -t project . <br />
docker run -p 8003:8003 --name contchess project
