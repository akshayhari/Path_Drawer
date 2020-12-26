# Path Drawer

A  small utility program for drawing path on 2D grids. Suitable for path finding algorithms implemented in 2D grids.

How it works?
- Load the image in the background. (Change 'image_loc' variable)
- Trace the path over the image. Left click to draw, Right click to clear cell and Escape key to clear everything.
- Output will be stored in the given file in 2D grid format. (Output file can be changed in 'file_loc' variable)
- Change 'block_size' variable for size of the path.

You can use this output file along with your image of your map for implementing any pathfinding algorithms (BFS, DFS, Dijkstra, A* etc.). Output file may require further processing for your algorithm.

Requires PyGame module