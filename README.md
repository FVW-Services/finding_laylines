# Thank you for downloading the plugin.

# Plugin for Qgis : finding_laylines

## Function : 
This plugin “Finding_ Laylines" is used for creating drain nets (consisting of contour lines and surface flow pathways called LAYLINES that are at right angles to
each other), using a DEM and a boundary file.

Basically, the plugin is developed for the following reasons:

a.Used to help visualize surface features, and thereby simplify drainage system layout, particularly for inexperienced designers.
b.Used for steady state subsurface flow visualization.

This plugin exacts a LiDAR DEM data out of an input boundary layer and then performs analysis such as:
 Performs terrain analysis to fill in all surface depressions in DEM for hydrologic analysis and modeling.
 Creates contour lines and laylines within the boundary layer extent on the map canvas of the DEM file Note: uncheck all web map layers from QuickMapServives like Google Satellite or Google Hybrid or OSM in the layers panel before pressing the OK button in the plugin.
 All operations are saved in your specified folder. After all the tasks have been executed and analyzed, go to the specified folder and there you will see in the subfolders where all saved files are as “Fill”, "Unfill“ or "Both“ files depending on the desired output selected. The entire task of the plugin takes few
seconds depending on the extent of the boundary layer extracted.

## Issues
You can report a issue [here](https://github.com/FVW-Services/finding_laylines/issues/new) and check the current [issues](https://github.com/FVW-Services/finding_laylines/issues).

## Developers :
Compile `ressources.py` with OSGeo4W Shell and the command : `pyrcc5 -o resources.py resources.qrc`

Edit `finding_laylines_dialog_base.ui` with QT designer (in Qt Creator).

## Feedbacks
Feel free to contact us: fvw.services@gmail.com

## User Guide :
ILLINOIS DRAINAGE GUIDE (ONLINE) : (http://www.wq.illinois.edu/DG/extraction/LAYLINES_User_Guide.pdf) 