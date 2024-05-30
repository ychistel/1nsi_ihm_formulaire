Exercices
=========

.. exercice::

    #.  Créer le formulaire ci-dessous qui contient un champ de type ``text`` et un bouton de validation:

        .. image:: ../img/formulaire_2.png
            :alt: image
            :align: center
            :width: 480

    #.  Ajouter au champ de saisie du prénom, les attributs suivants:
    
        -   l'attribut ``name`` qui a pour valeur ``prenom``
        -   l'attribut ``id`` qui a pour valeur ``prenom``

    #.  Ajouter au formulaire un champ de type ``number`` pour saisr un âge. On ajoutera aussi des attributs ``name`` et ``id``.

        .. image:: ../img/formulaire_3.png
            :alt: image
            :align: center
            :width: 480

    #.  Un formulaire peut contenir des boutons radios. L’ajout de ces boutons se fait avec des balises ``<input>`` de type ``radio``. Chaque ``input`` a les attributs suivants:

        - L’attribut ``name`` qui a la même valeur ``pet`` pour chaque bouton radio. 
        - L'attribut ``value`` qui a la valeur correspondant au type d'animal à sélectionner.

        De plus, le premier bouton radio contient la valeur ``checked`` dans sa balise ``input``.

        .. image:: ../img/formulaire_4.png
            :alt: image
            :align: center
            :width: 480

.. exercice::

    .. _liste déroulante: https://developer.mozilla.org/fr/docs/Web/HTML/Element/select

    On reprend le formulaire de l'activité pour cet exercice.

    Une liste déroulante contient plusieurs valeurs et permet de faire un choix parmi les valeurs proposées. En html, la liste déroulante est implémentée par:

    - la balise ``<select>`` et ``</select>`` qui contient l'attribut ``name`` pour nommer la liste;
    - entre ces 2 balises, les balises ``<option>`` et ``</option>`` contenant l'attribut ``value`` associée à chaque valeur de la liste.

    On a donc un code qui ressemble à:

    .. code-block:: html

        <select name='ma_liste'>
            <option value='valeur 1'>Ma première valeur</option>
            <option value='valeur 2'>Ma seconde valeur</option>
        </select>

    Vous trouverez une documentation plus complète sur le site de la fondation Mozilla à propos de la `liste déroulante`_.

    Vous devez compléter le formulaire avec une liste déroulante contenant 5 couleurs.

    .. figure:: ../img/formulaire_liste_deroulante.png
        :align: center

.. exercice::

    .. _zone de texte: https://developer.mozilla.org/fr/docs/Web/HTML/Element/textarea

    On reprend le formulaire de l'activité pour cet exercice.

    Une zone de texte permet de saisir un message sur plusieurs lignes.

    En html, une zone de texte est implémentée par:

    -   la balise ``<textarea>`` et ``</textarea>`` qui contient les attributs ``name`` pour nommer la zone, ``rows`` qui définit le nombre de ligne de la zone et ``cols`` qui définit le nombre de colonnes de la zone de texte;
    -   entre ces 2 balises se trouve un exemple de texte (non obligatoire).

    On a donc un code qui ressemble à:

    .. code-block:: html

        <textarea name="message" rows="4" cols="40">Le message par défaut</textarea>

    Vous trouverez une documentation plus complète sur le site de la fondation Mozilla à propos de la `zone de texte`_.

    Vous devez compléter le formulaire avec une zone de texte contenant de 4 lignes et 40 colonnes pour la saisie.

    .. figure:: ../img/formulaire_textarea.png
        :align: center
    
.. exercice::

    Il faut au préalable récupérer sur l'ENT l’archive ``formulaire.zip`` et la décompresser dans votre espace de travail. Le dossier est organisé pour utiliser le module Pyhon ``Flask`` qui permet d'avoir un serveur web nécessaire au traitement des données d'un formulaire.

    Dans le dossier ``serveur_HTTP``, faire un clic droit sur le fichier ``serveur.py`` puis ouvrir avec ``python``. Si tout se passe correctement, la fenêtre de commande exécute le script et on a l'affichage suivant:

    .. figure:: ../img/serveur_http_run.png
        :align: center

    On peut se connecter au serveur web que l'on vient de lancer avec un navigateur en saisissant l'url ``localhost:5000/``.

    Le formulaire à créer a pour adresse ``localhost:5000/formulaire``.

    #.  Éditer le fichier ``formulaire.html`` placé dans le dossier ``templates``.
    #.  Ajouter au formulaire l'attribut ``action`` qui a pour valeur ``localhost:5000/reponse``.
    #.  Ajouter au formulaire la méthode ``get`` à votre formulaire puis valider celui-ci après l'avoir rempli. Que remarquez-vous au niveau de l'url ?
    #.  Modifier la méthode d’envoi par ``post`` puis soumettre à nouveau le formulaire. Quelle est la différence avec l’envoi précédent ?
