# last-file-modif

## FRANÇAIS

Cette application en ligne de commande affiche le nom et le moment de la
dernière modification de chaque élément du dossier spécifié.

### Arguments

* `-d`/`--directory`: le chemin d'un dossier.
* `-f`/`--files-only`: ne considérer que les fichiers, pas les dossiers.
* `-p`/`--parents`: le nombre de dossiers parents à afficher avant les noms de
fichier.

### Exécution

Lancez la commande depuis de dossier **parent** du dépôt. Exemple:

```
python last-file-modif -d last-file-modif
```

Si vous exécutez l'application depuis le dépôt, lancez le script `__main__.py`.
Exemple:

```
python __main__.py -d .
```

Afficher l'aide:
```
python last-file-modif -h
```

## ENGLISH

This command line application displays the name and the moment of the last
modification of each item in the specified directory.

### Arguments

* `-d`/`--directory`: the path to a directory.
* `-f`/`--files-only`: consider only the files, not the directories.
* `-p`/`--parents`: the number of parent directories to display before the file.
names

### Execution

Run the command from the repository's **parent** directory. Example:

```
python last-file-modif -d last-file-modif
```

If you execute the application from the repository, run script `__main__.py`.
Example:

```
python __main__.py -d .
```

Display the help:
```
python last-file-modif -h
```
