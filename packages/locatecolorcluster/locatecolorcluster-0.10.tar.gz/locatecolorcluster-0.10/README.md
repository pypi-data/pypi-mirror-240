# Lightning-fast image color clustering with C-based RGB localization/euclidean distance calculation. Supports DBSCAN/HDBSCAN, Shapely geometry. 

## pip install locatecolorcluster

### Tested against Python 3.11 / Windows 10

## Important: A C/C++ compiler is necessary!

## Advantages:


### Flexibility:

The module supports both DBSCAN and HDBSCAN clustering algorithms, allowing users to choose the method that best fits their needs.


### Parallelization:

The code leverages parallelization capabilities in clustering algorithms, specifically in DBSCAN, HDBSCAN and cythoneuclideandistance, by allowing users to specify the number of parallel jobs.


### Speed Optimization:

The module exhibits exceptional speed, outperforming standard libraries like SciPy in Euclidean distance calculations by a factor of four. This performance boost is crucial for large-scale image processing tasks.


### RGB Localization with C:

The module includes efficient C implementations for RGB localization (300x faster than Python - search_colors method), enhancing the speed and accuracy of color identification in images.


### Visualization:

The module includes methods (draw_results and draw_results_real_size) for visualizing the clustered results, making it easier for users to interpret and analyze the outcomes.


### Shapely Geometry:

The module provides Shapely geometry information for each cluster, offering additional insights into the spatial characteristics of the clusters.

![](https://avatars.githubusercontent.com/u/77182807?s=400&u=b3398787384abf38d62c6f080195550df64f3990&v=4)
![](https://github.com/hansalemaos/screenshots/blob/main/colorcluster/0.png?raw=true)
![](https://github.com/hansalemaos/screenshots/blob/main/colorcluster/1.png?raw=true)

```python
Dependencies:
	- Cython and a C/C++ compiler!
	- os.path
	- sys
	- cv2
	- scipy.spatial.distance.pdist, squareform
	- cythoneuclideandistance
	- a_cv_imwrite_imread_plus
	- locate_pixelcolor_c
	- numpy
	- shapely.geometry
	- sklearn.cluster.DBSCAN, HDBSCAN
	- numexpr
	- a_cv2_easy_resize

Usage:
	- Create an instance of ColorCluster by providing an image path, optional parameters for resizing,
	  and interpolation method.
	- Use the find_colors method to search for specific colors in the image.
	- Calculate the Euclidean distance matrix using the calculate_euclidean_matrix method with the desired backend.
	- Apply clustering algorithms (DBSCAN or HDBSCAN) using the get_dbscan_labels or get_hdbscan_labels methods.
	- Extract clusters and visualize results using get_clusters, draw_results, and draw_results_real_size methods.
	- Obtain Shapely geometry information for each cluster using get_shapely method.

Example:

	import cv2

	from locatecolorcluster import ColorCluster, get_range_of_colors
	# Some valid color inputs
	colors = get_range_of_colors(
		start=(0, 0, 0),
		end=(10, 10, 10),
		rgb_or_bgr="bgr",
		min_r=0,
		max_r=10,
		min_g=0,
		max_g=10,
		min_b=0,
		max_b=10,
	)
	colors = ((0, 0, 0),)
	colors = get_range_of_colors(
		start=(100, 0, 0),
		end=(255, 0, 0),
		rgb_or_bgr="bgr",
		min_r=100,
		max_r=255,
		min_g=0,
		max_g=10,
		min_b=0,
		max_b=10,
	)
	cbackend = (
		ColorCluster(
			img=r'https://avatars.githubusercontent.com/u/77182807?s=400&u=b3398787384abf38d62c6f080195550df64f3990&v=4',
			max_width=200,
			max_height=200,
			interpolation=cv2.INTER_NEAREST,
		)
		.find_colors(colors=colors, reverse_colors=False)
		.calculate_euclidean_matrix(backend="C", memorylimit_mb=10000) # Define a memory limit for the C backend - It's 4x faster than scipy, but if the array is too big for the memory, the process crashes with 0xc0000005
		.get_dbscan_labels(eps=3, min_samples=10, algorithm="auto", leaf_size=30, n_jobs=5)
		.get_clusters()
		.draw_results(folder=r"C:\myimageresults\1", color=(255, 0, 255))
		.draw_results_real_size(folder=r"C:\myimageresults\2", color=(255, 255, 0))
		.get_shapely()
	)
	shapelydata = cbackend.shapelydata
	print(shapelydata)



```