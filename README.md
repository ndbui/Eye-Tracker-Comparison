# Tobii 4C Heatmap Generator
Branched from the following [Eye Tracking Widget](https://github.com/commanderking/EyeTrackerWidget) created by commanderking

Uses the Tobii 4C Eye Tracker to collect the X and Y-coordinates of the user's gaze while watching a prepared video clip and stores it into a csv. After the video clip ends a folder will be created in the Results folder containing all of the heatmap images as well as the heatmaps in mp4 format under timelapse.mp4.

#Prerequisites
* Tobii Eye Tracker Device. Tested with Tobii 4c.
* [Tobii Eye Tracking Core Software](https://tobiigaming.com/getstarted/)
* Windows 10
* Visual Studio 2015. Tested with Community edition.

#Getting Started
The primary solution, titled UserPresenceWpf is located at /source/WpfSamples/UserPresenceWpf. Open this file in Visual Studio to begin editing.

A release build that works out of the box can be found at /source/WpfSamples/UserPresenceWpf/bin/x86/Release. Open UserPresenceWpf (Type Application) to run the program.

You can uncomment out the code at the bottom of maketimelapse.py in order to automatically create an overlay of the heatmaps over the experiment video once the heatmaps have been created but the process takes a bit of time to complete.
