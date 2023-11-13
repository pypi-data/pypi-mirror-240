# pictriage

A lightweight image manager.

![Screenshot](https://i.imgur.com/dQtoPfj.gif)

Fast way to manually organize & clean-up a folder of images. First, select your image 1-click action:

-   Delete
-   Move to a different folder
-   Rotate left
-   Rotate right
-   (more coming soon)

Then, clicking on an image executes that action.
You can also click on a whole subfolder (e.g. delete the subfolder).

Also features a zoom pane (zoom in on the current image)

## Installation

`pip install pictriage`

For image modifications such as rotating, you must have ffmpeg installed.

## Usage

usage: pictriage DIR [--move-dir MOVE_DIR]

manually organize & clean-up a folder of images

positional arguments:
  DIR                   Root folder containing images (can contain subfolders). Defaults to current dir.

optional arguments:
  --move-dir MOVE_DIR   Directory to move images to (if the 'move' action is selected)


## Extra configuration flags

  --thumbnail-width THUMBNAIL_WIDTH
                        Width of thumbnails, in pixels (when in thumbnail
                        mode)
  --zoom-pane-width ZOOM_PANE_WIDTH
                        Width of the zoom pane, in pixels
  --zoom-image-width ZOOM_IMAGE_WIDTH
                        Width of the zoomed image, in pixels
  




