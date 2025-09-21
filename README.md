# PG Labeller

GUI to label images. Uses opencv simple blob detector to help find features to label.
...
>python3 PgLabeller.py 
...


# Features
* Can set bob parameters using the gui. Blobs are detected once the detect button is pressed. Use 0 for color for detecting dark blobs and 255 for light blobs. Remember blob detector uses grayscale image.
* After the blobs are detected you can select them using left mouse click. The selected blobs can be deleted by pressing delete.
* The blobs can be dragged by using left click and drag.
* New blobs can be manually added using draw circle tool at the bottom of the app.
* You can show and hide detected blobs using the check button at the bottom of the app.
* Bilateral filter is applied to the foreground image before using blob detector. You can check the filtered image using "show filtered image" check button on the right. Filtering parameters d, sigma_color, sigma_space can be set from the right control panel as well. See Opencv Bilateral Filter for definition of these parameters.
* Once you use the File menu to load the foreground image, you can use "Load Background" button in File menu to load a background image. You can set the opacity of Fg image using slider in right control panel to see the background image, which will perhaps help in labelling. This option is not available when you are looking at filtered image.
* Can select blob using left click. Can add to the selection using ctrl+left click. Can box select as well, and ctrl+box select.
* Google map style zoom and pan. Mouse scroll to zoom in and out at cursor point, and mouse wheel click and drag to pan.
* Go to Mode and select Edit mode to edit/detect leds, and Label mode to label them.

# Updates:
* Added dark and light mode options for the app. Go to preference and select preferred mode.
* Added Scene system to switch between Edit and label mode. Edit mode will be used for detecting and editing leds(blobs) and labelling mode will be used to label the detected leds.
* Labeling mode coming soon...
* Reorganized code to fit the scene system.



# To Do:
* Have two modes: one for detecting and editing blobs, i.e. Edit mode and one for Labeling blobs, i.e. Label mode.
* Add more advanced features to minimize number of blobs(led) that we need to label manually. Have some features to automatically generate label once few blobs are labelled.
* Undo and Redo feature can be implemented, but less priority.

# Requirements
* tkinter, python, ... 
