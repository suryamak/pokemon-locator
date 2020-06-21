# Pokemon Locator
Find out if you can _really_ catch 'em all.

## About
* ```find.py```: webcrawler for [Serebii.net](https://serebii.net/) that finds complete and accurate methods of obtaining a Pokemon for a single game version only. Fully supports core-series games from generations 5-7.
* ```fetch.py```: uses the [PokeAPI](https://pokeapi.co/) to look up a Pokemon and how it is obtained across a wider range of core-series games, but location information may be incomplete

## Usage

### find.py
* Run ```python find.py``` with two command line arguments

* Command Line Arguments
 1. the Pokemon's name
 2. a specific core-series game to filter by

* Examples
    * ```python find.py greninja y``` _(lists all the ways to obtain Greninja in Pokemon Y)_
    * ```python find.py cacturne firered``` _(lists the ways to obtain Cacturne in Pokemon FireRed)_

### fetch.py
* Run ```python fetch.py``` with up to two command line arguments

* Command Line Arguments
 1. the Pokemon's name OR national dex number (required)
 2. a specific core-series game to filter by (optional)

* Examples 
    * ```python fetch.py 217 soulsilver``` _(lists all the ways to obtain Ursaring in SoulSilver)_
    * ```python fetch.py mantine``` _(lists all the ways to obtain Mantine across all games)_