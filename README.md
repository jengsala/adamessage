Script Python en Module
-----------------------

## Générer les archives de distribution sur la machine locale

Maintenant que le code du package python est presque terminé, vous pouvez commencer à créer les archives de distribution. Les archives sont des fichiers compressés qui aident votre package à être déployé sur plusieurs plates-formes et le rendent également indépendant de la plate-forme.
Afin de générer les archives de distribution, exécutez la commande suivante depuis votre terminal.

```sh
pip install --user --upgrade setuptools wheel
```


Cela mettra à niveau votre bibliothèque setuptools sur votre ordinateur pour utiliser la dernière version. Après cela, vous devez exécuter la commande suivante à partir du répertoire racine de votre package pour générer les fichiers de distribution.

```sh
python setup.py sdist bdist_wheel
```

Une fois que vous avez exécuté la commande ci-dessus, vous pouvez voir que les packages de distribution seront livrés dans les répertoires – build et dist, qui sont nouvellement créés comme ci-dessous.
En plus de cela, vous pouvez également voir que les informations du fichier egg ont également été mises à jour dans le code source du projet.


## Installer le package sur la machine locale

```sh
pip install -e .
```

Comme vous pouvez le voir dans la figure ci-dessus, dans la première étape, nous installons le package localement à l'aide de la commande et une fois installé, nous démarrons le shell python et l'importons.
Ensuite, nous appelons la méthode package et elle imprime le message sur le terminal.

```sh
...
...
Installing collected packages: setuppythonscript
  Running setup.py develop for setuppythonscript
Successfully installed setuppythonscript-1.0
```

```python
> python3
Python 3.10.12 (main, Nov  9 2023, 12:32:44) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import monscript
>>> clss = monscript.MaClasse("atr1","atr2")
>>> clss.bonjour("Antoine")
'Bonjour Antoine'
>>> 
```

# Publish the package to the TestPyPi

Une fois le package installé en local et fonctionne correctement, il est maintenant prêt à être expédié vers le référentiel TestPyPi. Il s'agit d'un référentiel de test pour tous les packages Python afin de tester et voir si tout le code fonctionne correctement et s'il n'y a aucun problème dans le code du package.
Cela le maintient isolé du référentiel officiel PyPi et garantit que seuls les packages minutieusement testés sont déployés en production.


Accédez à https://test.pypi.org/ et inscrivez-vous en tant qu'utilisateur. Une fois inscrit, ouvrez votre terminal et exécutez la commande suivante. Cela installera un package appelé « twine » sur votre machine qui aidera à expédier le package python aux référentiels.

```sh
pip install --user --upgrade twine
```

Vous pouvez lire la documentation officielle sur l'empaquetage d'applications Python ainsi que sur Twine ici. Une fois le package twine installé, exécutez la commande suivante pour envoyer d'abord le code à TestPyPi. Lorsque vous exécutez la commande, il vous sera demandé de fournir les mêmes informations d'identification avec lesquelles vous avez enregistré votre compte à l'étape précédente.

```sh
twine upload --repository testpypi dist/*
```

# Publication

Maintenant que tout fonctionne bien avec notre package, il est temps de le publier sur le référentiel officiel PyPi. Suivez les mêmes étapes pour créer un compte, puis exécutez la commande suivante pour envoyer le package au référentiel officiel.

```sh
twine upload dist/*
```

## Publier sur Nexus Repository Manager

```sh
twine upload --repository nexus dist/*
```

```sh
Uploading distributions to https://nexus.digitastuces.com/repository/pypi-internal/
Uploading setuppythonscript-1.0-py3-none-any.whl
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 14.5/14.5 kB • 00:00 • 12.4 MB/s
Uploading setuppythonscript-1.0.tar.gz
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 14.7/14.7 kB • 00:00 • 19.7 MB/s
```


## Browsing PyPI Repositories and Searching Packages

```sh
pip search mypackage
```

- resultat:

```sh
pip search setuppythonscript
User for nexus.digitastuces.com: adieng
setuppythonscript (1.0)  - A python client for setuppythonscript.
  INSTALLED: 1.0
  LATEST:    1.0
```


## Configuration de `pip.conf`

```conf
[distutils]
index-servers = 
    nexus
    testpypi
    easy_install

[nexus]
repository: https://nexus.digitastuces.com/repository/pypi-internal/
username: xxxxxxxxxxxx
password: xxxxxxxxxxxx

[global]
index = https://nexus.digitastuces.com/repository/pypi-all/pypi
index-url = https://nexus.digitastuces.com/repository/pypi-all/simple
trusted-host = nexus.digitastuces.com

[easy_install]
index-url = https://nexus.digitastuces.com/repository/pypi-proxy/simple

[testpypi]
username = jengsala #__token__
password = pypi-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```


## Mots-clés dans ``setup.py``


Exemples de quelques mots-clés utilisés lors de l'appel de la méthode `setup()`  :

- ``name``: Une chaîne contenant le nom du package.
- ``version``: Une chaîne contenant le numéro de version du package.
- ``description``: Un texte sur une seule ligne expliquant le package.
- ``author``: Une chaîne identifiant le créateur/auteur du package.
- `long_description`: Une chaîne contenant une description plus détaillée du package.
- `maintainer`: C'est une chaîne fournissant le nom du responsable actuel, sinon l'auteur. Si le responsable n'est pas indiqué, l'auteur dans PKG-INFO sera utilisé par les outils d'installation.
- `url` Une chaîne fournissant l'URL de la page d'accueil du package (généralement le référentiel GitHub ou la page PyPI).
- `download_url` Une chaîne contenant l'URL où le package peut être téléchargé.
- `package_data` Il s'agit d'un dictionnaire où les clés sont des noms de packages et les valeurs sont des listes de modèles globaux.
- `py_modules` Une liste de chaînes contenant les modules que les outils de configuration modifieront.
python_requires: Il s'agit d'une chaîne séparée par des virgules fournissant des spécificateurs de version Python pour les versions Python prises en charge par le package.
- `install_requires` Une liste de chaînes contenant uniquement les dépendances nécessaires au fonctionnement efficace du package.
- `keywords` Une chaîne ou une liste de chaînes séparées par des virgules fournissant des métadonnées descriptives.
- `entry_points` Il s'agit d'un dictionnaire avec des clés correspondant aux noms de points d'entrée et des valeurs correspondant aux points d'entrée réels indiqués dans le code source.
- `license` Une chaîne contenant les informations de licence du package.

