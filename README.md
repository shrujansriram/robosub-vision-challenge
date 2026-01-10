# robosub-vision-challenge
ROBOSUB UCI RECRUITMENT 2026
This project implements a real-time computer vision system using OpenCV to detect red-colored objects from a live webcam feed. The program uses HSV color space for robust color detection and YCrCb color space for skin-tone filtering to reduce false positives caused by human skin.

Detected objects are highlighted with bounding circles, making the output intuitive and visually clear.


FUTURE IMPROVEMENTS
 - Noise filtering with morphology to reduce false positives caused by small objects.
 - Focus on only the largest object
 - Add object tracking by maintaining identity between frames to add features like velocity tracking
