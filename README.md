# PG Labeller

GUI to label images. Uses opencv simple blob detector to help find features to label.
...
>python3 main.py (main.py will be renamed to represent the app name in the end)
...


# Features
* Can set bob parameters using the gui. Blobs are detected once the detect button is pressed. Use 0 for color for detecting dark blobs and 255 for light blobs. Remember blob detector uses grayscale image.
* After the blobs are detected you can select them using left mouse click. The selected blobs can be deleted by pressing delete.
* The blobs can be dragged by using left click and drag.
* New blobs can be manually added using draw circle tool at the bottom of the app.
* You can show and hide detected blobs using the check button at the bottom of the app.
* Bilateral filter is applied to the foreground image before using blob detector. You can check the filtered image using "show filtered image" check button on the right. Filtering parameters d, sigma_color, sigma_space can be set from the right control panel as well. See Opencv Bilateral Filter for definition of these parameters.
* Once you use the menu bar to load the foreground image, you can use "Load Background" button on right control panel to load a background image. You can set the opacity of Fg image so that you can see background image which will perhaps help in labelling. This option is not available when you are looking at filtered image.
* Can select blob using left click. Hold left ctrl and click to select multiple, or click in the background and drag to select multiple blobs, or ctrl+click and drag to add. 

# To Do:
* Have two modes: one for detecting and editing blobs, i.e. Edit mode and one for Labeling blobs, i.e. Label mode.
* Add more advanced features to minimize number of blobs(led) that we need to label manually. Have some features to automatically generate label once few blobs are labelled.
* Undo and Redo feature can be implemented, but less priority.

# Requirements
* tkinter, python, ... 
