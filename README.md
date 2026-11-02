# Python Games

A collection of games made with Python and pygame (when I was 10-13). 



Featured games:

|Game|File|
|-|-|
|Platformer where you propel yourself using explosives|`bomber.py`|
|Game where you carefully position black holes and blocks in order to make a ball go through a hoop|`gravity hoop.py`|
|Alien shooter|`aliens 4.0.py`|
|Evolution simulators|`sim.py` and `sim2.py`|
|Educational game|Removed; contains personal info|

The other `.py` files in this repository are additional games and earlier versions.

## Requirements

* **Python 3.** These games were originally written for Python 3.6 (2018), and they also run on current versions of Python 3.
* **pygame**, the only outside library the games use.

## How to run

1. **Install Python 3** from [python.org](https://www.python.org/downloads/) if you don't already have it.
2. **Install pygame** by running this in a terminal (Command Prompt on Windows):

```bash
   pip install pygame
   ```

   On macOS or Linux, you may need `python3 -m pip install pygame` instead.

3. **Download this repository.** Click the green **Code** button near the top of this page, choose **Download ZIP**, and unzip it. Or clone it:

```bash
   git clone https://github.com/webgoatguy/PythonGames.git
   ```

4. **Open a terminal inside the downloaded folder.** This matters: the games load their images, sounds, and level files from this folder, so they need to be run from inside it.

```bash
   cd PythonGames
   ```

5. **Run a game.** Some file names contain spaces, so put them in quotes:

```bash
   python bomber.py
   python "gravity hoop.py"
   python "aliens 4.0.py"
   python sim.py
   python sim2.py
   ```

   On macOS or Linux, use `python3` instead of `python`.

## Files that aren't code

* `images/` contains the pictures and sound effects the games use
* `hooplevels`, `pickles`, `pickles1`, `duel`, `td\_mapx`, and `td\_mapy` are saved game data (levels, maps, scores)

