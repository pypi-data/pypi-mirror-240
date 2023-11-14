import os.path
import sys
from collections import defaultdict
import cv2
from scipy.spatial.distance import pdist, squareform
import cythoneuclideandistance
from a_cv_imwrite_imread_plus import open_image_in_cv, save_cv_image
from locate_pixelcolor_c import search_colors
import numpy as np
from shapely import geometry
from sklearn.cluster import DBSCAN, HDBSCAN
import numexpr
from a_cv2_easy_resize import add_easy_resize_to_cv2

add_easy_resize_to_cv2()


class ColorCluster:
    r"""
    ColorCluster - A class for clustering colors in an image and analyzing the clusters.

    The ColorCluster class can be used to perform color clustering on an image
    and visualize the results. It utilizes various libraries and methods for color analysis and clustering.

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


    """

    def __init__(
        self, img, max_width=200, max_height=200, interpolation=cv2.INTER_NEAREST
    ):
        r"""
        Initialize the ColorCluster object.

        Parameters:
        - img (str): Path to the image file.
        - max_width (int): Maximum width after resizing the image.
        - max_height (int): Maximum height after resizing the image.
        - interpolation (cv2 interpolation method): Interpolation method for resizing.

        Returns:
        - ColorCluster: An instance of the ColorCluster class.
        """
        self.image_original = open_image_in_cv(img, channels_in_output=3)
        self.image = self.image_original.copy()
        if self.image.shape[0] > max_height:
            self.image = cv2.easy_resize_image(
                self.image,
                width=None,
                height=max_height,
                percent=None,
                interpolation=interpolation,
            )
        if self.image.shape[1] > max_width:
            self.image = cv2.easy_resize_image(
                self.image,
                width=max_width,
                height=None,
                percent=None,
                interpolation=interpolation,
            )
        self.image_factor = self.image_original.shape[0] / self.image.shape[0]
        self.color_search_results = np.array([], dtype=np.int32)
        self.distance_matrix = np.array([], dtype=np.float32)
        self.labels = np.array([], dtype=np.int64)
        self.clusters = {}
        self.drawn_results = {}
        self.drawn_results_real_size = {}
        self.interpolation = interpolation
        self.cv2_cnts = defaultdict(list)
        self.shapelydata = {}

    def find_colors(self, colors, reverse_colors=True):
        """
        Find specific colors in the image.

        Parameters:
        - colors (list of tuples): List of RGB or BGR color tuples.
        - reverse_colors (bool): Flag to reverse the order of RGB values.

        Returns:
        - ColorCluster: Updated instance with color search results.
        """
        if reverse_colors:
            colors = np.ascontiguousarray(
                np.array([list(reversed(col)) for col in colors], dtype=np.uint8)
            )
        else:
            colors = np.ascontiguousarray(np.asarray(colors, dtype=np.uint8))
        coords = search_colors(pic=self.image, colors=colors)
        self.color_search_results = np.ascontiguousarray(coords.astype(np.int32))

        return self

    def calculate_euclidean_matrix(self, backend, memorylimit_mb=None):
        """
        Calculate the Euclidean distance matrix based on color search results.

        Parameters:
        - backend (str): Backend for distance matrix calculation ("scipy" or "C").
        - memorylimit_mb (int, optional): # Define a memory limit for the C backend - It's 4x faster than scipy, but if the array is too big for the memory, the process crashes with 0xc0000005
          the process crashes with 0xc0000005

        Returns:
        - ColorCluster: Updated instance with the calculated distance matrix.
        """
        if backend == "scipy":
            distances = pdist(self.color_search_results, metric="euclidean")
            self.distance_matrix = squareform(distances)
        elif backend in ["c", "C", "cython", "Cython"]:
            if not memorylimit_mb:
                memorylimit_mb = sys.maxsize
                sys.stderr.write(
                    'It\'s better to specify "memorylimit_mb" if not using scipy\n'
                )
                sys.stderr.flush()
            if (
                self.color_search_results.shape[0]
                * self.color_search_results.shape[0]
                * self.color_search_results.shape[1]
                * 4
                // (1024**2)
                > memorylimit_mb
            ):
                raise MemoryError("Result would be too big!")
            self.distance_matrix = cythoneuclideandistance.calculate_euc_distance(
                self.color_search_results, self.color_search_results
            )
        return self

    def get_dbscan_labels(
        self, eps=0.5, min_samples=5, algorithm="auto", leaf_size=30, n_jobs=5, **kwargs
    ):
        """
        Apply DBSCAN clustering to the distance matrix.
        https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html

        Parameters:
        - eps (float): The maximum distance between two samples for one to be considered as in the neighborhood of the other.
        - min_samples (int): The number of samples in a neighborhood for a point to be considered as a core point.
        - algorithm (str): The algorithm to be used ("auto", "ball_tree", "kd_tree", "brute").
        - leaf_size (int): Leaf size passed to BallTree or KDTree.
        - n_jobs (int): The number of parallel jobs to run for DBSCAN.

        Returns:
        - ColorCluster: Updated instance with DBSCAN labels.
        """

        dbscan = DBSCAN(
            leaf_size=leaf_size,
            algorithm=algorithm,
            n_jobs=n_jobs,
            eps=eps,
            min_samples=min_samples,
            metric="precomputed",
            **kwargs,
        )
        self.labels = dbscan.fit_predict(self.distance_matrix)
        return self

    def get_hdbscan_labels(
        self,
        min_cluster_size=5,
        min_samples=None,
        cluster_selection_epsilon=0.0,
        max_cluster_size=None,
        alpha=1.0,
        algorithm="auto",
        leaf_size=40,
        n_jobs=5,
        cluster_selection_method="eom",
        allow_single_cluster=False,
        store_centers=None,
        copy=False,
        **kwargs,
    ):
        """
        Apply HDBSCAN clustering to the distance matrix.

        Parameters:
        - min_cluster_size (int): Minimum size of clusters.
        - min_samples (int): The number of samples in a neighborhood for a point to be considered as a core point.
        - cluster_selection_epsilon (float): Determines the tightness of cluster assignment.
        - max_cluster_size (int): Maximum size of clusters.
        - alpha (float): Constant that balances hierarchy height and size of clusters.
        - algorithm (str): The algorithm to be used ("auto", "ball_tree", "kd_tree", "brute").
        - leaf_size (int): Leaf size passed to BallTree or KDTree.
        - n_jobs (int): The number of parallel jobs to run for HDBSCAN.
        - cluster_selection_method (str): Method for choosing the best clusters ("eom", "leaf").
        - allow_single_cluster (bool): Flag to allow a single cluster as output.
        - store_centers (bool): Flag to store cluster centers.
        - copy (bool): Flag to copy the data before fitting.

        Returns:
        - ColorCluster: Updated instance with HDBSCAN labels.
        """
        hdbscan_cluster = HDBSCAN(
            min_cluster_size=min_cluster_size,
            min_samples=min_samples,
            cluster_selection_epsilon=cluster_selection_epsilon,
            max_cluster_size=max_cluster_size,
            alpha=alpha,
            algorithm=algorithm,
            leaf_size=leaf_size,
            n_jobs=n_jobs,
            cluster_selection_method=cluster_selection_method,
            allow_single_cluster=allow_single_cluster,
            store_centers=store_centers,
            copy=copy,
            metric="precomputed",
            **kwargs,
        )
        self.labels = hdbscan_cluster.fit_predict(self.distance_matrix)
        return self

    def get_clusters(self):
        """
        Extract clusters based on the obtained labels.

        Returns:
        - ColorCluster: Updated instance with extracted clusters.
        """
        self.clusters = {}
        for l in np.sort(np.unique(self.labels)):
            self.clusters[l] = self.color_search_results[
                (
                    numexpr.evaluate(
                        "labels==l",
                        local_dict={"labels": self.labels, "l": l},
                        global_dict={},
                    )
                )
            ]
        cv2_cnts = defaultdict(list)
        for cluk, cluv in self.clusters.items():
            if cluk == -1:
                continue
            ax = np.zeros_like(self.image)
            ax[cluv[..., 0], cluv[..., 1]] = 255
            ax = cv2.easy_resize_image(
                ax,
                width=self.image_original.shape[1],
                height=self.image_original.shape[0],
                percent=None,
                interpolation=self.interpolation,
            )
            cnts = cv2.findContours(
                ax[..., 0], cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE
            )
            fi = cnts[0] if len(cnts) == 2 else cnts[1]
            cv2_cnts[cluk].append(fi)

        indi = 0
        for k, v in cv2_cnts.items():
            for fi in v:
                for ff in fi:
                    self.cv2_cnts[indi] = ff
                    indi = indi + 1

        return self

    def draw_results(self, folder=None, color=(255, 0, 255)):
        """
        Draw color-coded results for each cluster and save images.

        Parameters:
        - folder (str, optional): Folder path to save the drawn results.
        - color (tuple): RGB color for drawing.

        Returns:
        - ColorCluster: Updated instance with drawn results.
        """
        col = np.array(list(reversed(color)), dtype=np.uint8)
        for k, v in self.clusters.items():
            image2 = self.image.copy()
            image2[self.clusters[k][:, 0], self.clusters[k][:, 1]] = col
            if folder:
                save_cv_image(os.path.join(folder, f"{k}.png"), image2)
            self.drawn_results[k] = image2
        return self

    def draw_results_real_size(self, folder=None, color=(255, 0, 255)):
        """
        Draw color-coded results on the original-sized image and save images.

        Parameters:
        - folder (str, optional): Folder path to save the drawn results.
        - color (tuple): RGB color for drawing.

        Returns:
        - ColorCluster: Updated instance with drawn results on the original-sized image.
        """
        ino = 0
        for k, ff in self.cv2_cnts.items():
            im = self.image_original.copy()
            cv2.fillPoly(im, [ff], color)
            cv2.polylines(im, [ff], isClosed=True, color=color, thickness=2)

            if folder:
                save_cv_image(os.path.join(folder, f"{ino}.png"), im)

            self.drawn_results_real_size[ino] = im
            ino = ino + 1
        return self

    def get_shapely(self):
        r"""
        Obtain Shapely geometry information for each cluster.

        Returns:
        - ColorCluster: Updated instance with Shapely geometry data.
        """
        for k, v in self.cv2_cnts.items():
            shapelyobject = geometry.Polygon(v.squeeze())
            convexhull = np.dstack(shapelyobject.convex_hull.boundary.coords.xy).astype(
                np.int32
            )
            centroid = np.dstack(shapelyobject.centroid.xy).astype(np.uint32)[0][0]
            boundary = np.dstack(shapelyobject.boundary.coords.xy).astype(np.int32)
            bounds = list(map(int, shapelyobject.bounds))
            exterior = np.dstack(shapelyobject.exterior.coords.xy).astype(np.int32)
            area = shapelyobject.area
            representative_point = np.dstack(
                shapelyobject.representative_point().xy
            ).astype(np.uint32)[0][0]
            self.shapelydata[k] = {
                "shapelyobject": shapelyobject,
                "convexhull": convexhull,
                "centroid": centroid,
                "boundary": boundary,
                "bounds": bounds,
                "exterior": exterior,
                "area": area,
                "representative_point": representative_point,
            }
        return self


def get_range_of_colors(
    start,
    end,
    rgb_or_bgr="bgr",
    min_r=0,
    max_r=255,
    min_g=0,
    max_g=255,
    min_b=0,
    max_b=255,
):
    """
    Generate a range of RGB or BGR colors within specified limits.

    Parameters:
    - start (tuple): Starting RGB or BGR color.
    - end (tuple): Ending RGB or BGR color.
    - rgb_or_bgr (str): Color format ("rgb" or "bgr").
    - min_r, max_r, min_g, max_g, min_b, max_b (int): Minimum and maximum values for each color channel.

    Returns:
    - np.ndarray: Array of generated colors within the specified range.
    """

    def rgb_to_int(rgb):
        r, g, b = rgb
        return (r << 16) + (g << 8) + b

    startint = rgb_to_int(start)
    endint = rgb_to_int(end) + 1
    integer_value = np.arange(startint, endint)
    if rgb_or_bgr.lower() == "bgr":
        corrange = np.dstack(
            [
                integer_value & 255,
                (integer_value >> 8) & 255,
                (integer_value >> 16) & 255,
            ]
        )
        return np.ascontiguousarray(
            corrange[
                ((corrange[..., 0] <= max_b) & (corrange[..., 0] >= min_b))
                & ((corrange[..., 1] <= max_g) & (corrange[..., 1] >= min_g))
                & ((corrange[..., 2] <= max_r) & (corrange[..., 2] >= min_r))
            ].astype(np.uint8)
        )

    else:
        corrange = np.dstack(
            [
                (integer_value >> 16) & 255,
                (integer_value >> 8) & 255,
                integer_value & 255,
            ]
        )
        return np.ascontiguousarray(
            corrange[
                ((corrange[..., 2] <= max_b) & (corrange[..., 2] >= min_b))
                & ((corrange[..., 1] <= max_g) & (corrange[..., 1] >= min_g))
                & ((corrange[..., 0] <= max_r) & (corrange[..., 0] >= min_r))
            ].astype(np.uint8)
        )
