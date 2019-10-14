# Monarch

## Install
You can use the these editor scripts in your own project by adding this project as a [Defold library dependency](https://www.defold.com/manuals/libraries/). Open your game.project file and in the dependencies field under project add:  
https://github.com/Jerakin/editor-script-monarch/archive/master.zip

### Dependencies
You also need to make sure you have python 3 and [deftree](https://github.com/Jerakin/DefTree) installed.  
You can easily install deftree with  
`pip install deftree`

## Editor Script
This script adds a menu option when bringing up the context menu on a gui scene. When used it creates a collection and a gui_script (which adds the "require monarch" and "acquire_input_focus" automatically). It adds the gui_script to the selected gui scene and adds the gui scene to the newly created collection.
