# Cleanup

## Install
You can use the these editor scripts in your own project by adding this project as a [Defold library dependency](https://www.defold.com/manuals/libraries/). Open your game.project file and in the dependencies field under project add:  
https://github.com/Jerakin/editor-script-cleanup/archive/master.zip

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
