# Cleanup

## Install
You can use the these editor scripts in your own project by adding this project as a [Defold library dependency](https://www.defold.com/manuals/libraries/). Open your game.project file and in the dependencies field under project add:  
https://github.com/Jerakin/editor-script-cleanup/archive/master.zip

### macOS
You need to make your python installation visible to Defolds Java VM, you need to put your path modifications in
`$HOME/.bash_profile`. This is because I `source $HOME/.bash_profile` and I opted do it this way instead of
`export PATH="$PATH:/usr/local/bin"` because if you are using `pyenv` and `pyenv-virtualenv` it would not pick up on that.
 

### Dependencies
You also need to make sure you have python 3 and [deftree](https://github.com/Jerakin/DefTree) installed.  
You can easily install deftree with  
`pip install deftree`

## Editor Script
This library adds a few scripts that are made to help you clean up your project. Remember to **ALWAYS** commit all your changes before running these commands as they are all **highly destructive**.

### Remove Unused Images From Project
This script removes all images that can not be found in any resource files

### Remove Unused Images From Atlases
This script removes image entries in your atlas that are now missing on disk. For when you have checked removed images manually from explorer.

### Remove Unused Resources from GUI
This script removes all Layers, Textures, Fonts etc from GUI files that are not using them. Beware that this is _not_ aware
about any switches happening in your lua or gui_scripts, meaning it will remove textures even if you change to them with
`gui.set_texture` or similar for other resources.

## Something went wrong
If you want some more information of what is happening create a file in the root of your project called `python_log.txt`
the script checks for that file and output any logging to it. 