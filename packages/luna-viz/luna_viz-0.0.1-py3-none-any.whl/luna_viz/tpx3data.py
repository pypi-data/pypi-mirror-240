import os
import h5py
import numpy as np
import pandas as pd
import tifffile
import matplotlib.pyplot as plt
import seaborn as sns
from typing import *
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

sns.set_style(style="white")
sns.set_context(context="talk", font_scale=1)


class TiffPlotter:

    def __init__(self):
        pass

    @staticmethod
    def create_tiff_from_pixel_data(pixel_data: pd.DataFrame, x_max: int = 512, y_max: int = 512,
                                    scale_factor: int = 32, output_directory: Optional[str] = None) -> str:
        """
        Create a TIFF image from the pixel data.

        Parameters:
            x_max (int): The max value of the x dimension of the image. Defaults to 256.
            y_max (int): The max value of the y dimension of the image. Defaults to 256.
            scale_factor (int): The factor to scale the 'tot' values by. Defaults to 32.

        Returns:
            str: The file name of the created TIFF file.
        """
        image = np.zeros((y_max, x_max), dtype=np.uint16)
        grouped = pixel_data.groupby(['x', 'y'])['tot'].sum().reset_index()
        image[grouped['y'].values, grouped['x'].values] = grouped['tot'].values * scale_factor
        if output_directory is not None:
            fname = os.path.join(output_directory, "pixel_data.tiff")
        else:
            fname = os.path.join(os.path.dirname(__file__), "pixel_data.tiff")
        tifffile.imwrite(fname, image)
        return fname

    @staticmethod
    def create_tiff_from_cluster_data(cluster_data: pd.DataFrame, x_max: int = 512, y_max: int = 512,
                                      scale_factor: int = 32, output_directory: Optional[str] = None) -> str:
        """
        Create a TIFF image from the cluster data.

        Parameters:
            x_max (int): The max value of the x dimension of the original image
            y_max (int): The max value of the y dimension of the original image
            scale_factor (int): The factor to scale the 'sum_tot' values by. Defaults to 32.

        Returns:
            str: The file name of the created TIFF file.
        """
        new_x_max, new_y_max = 4 * x_max, 4 * y_max
        image = np.zeros((new_y_max, new_x_max), dtype=np.uint16)
        grouped = cluster_data.groupby(['average_x', 'average_y'])['sum_tot'].sum().reset_index()
        x_values = np.round(grouped['average_x'].values * 4).astype(int)
        y_values = np.round(grouped['average_y'].values * 4).astype(int)
        image[y_values, x_values] = grouped['sum_tot'].values * scale_factor
        if output_directory is not None:
            fname = os.path.join(output_directory, "cluster_data.tiff")
        else:
            fname = os.path.join(os.path.dirname(__file__), "cluster_data.tiff")
        tifffile.imwrite(fname, image)
        return fname


class HistogramPlotter:
    def __init__(self, pixel_data, layout, units, output_directory=None):
        self.pixel_data = pixel_data
        self.layout = layout.lower()
        self.units = units
        self.output_directory = output_directory

    def plot_toa_histogram(self):
        sns.set(style="white")
        dt = self.get_conversion_factor()
        toa = self.pixel_data["toa"]
        fig = plt.figure(figsize=(6, 4))
        sns.histplot(toa * dt, bins=30, kde=False)
        sns.despine(fig=fig)
        plt.xlabel(f'ToA (seconds)')
        plt.ylabel('Count')
        self.save_figure('toa_histogram.png')

    def plot_tot_histogram(self):
        sns.set(style="white")
        dtot = 25  # ToT conversion factor
        tot = self.pixel_data["tot"]
        fig = plt.figure(figsize=(6, 4))
        sns.histplot(tot / dtot, log_scale=(False, True))  # log_scale on y-axis
        sns.despine(fig)
        plt.xlabel('ToT (counts)')
        plt.ylabel('Frequency')
        self.save_figure('tot_histogram.png')

    def plot_pixel_hits_histogram(self):
        x_max, y_max = self.get_layout_boundaries()
        xpix = self.pixel_data["x"]
        ypix = self.pixel_data["y"]
        fig = plt.figure(figsize=(6, 4))
        plt.hist2d(xpix, ypix, bins=(x_max, y_max), range=[[0, x_max], [0, y_max]])
        sns.despine(fig)
        plt.xlabel('xpix')
        plt.ylabel('ypix')
        self.save_figure('pixel_hits_histogram.png')

    def plot_weighted_pixel_hits_histogram(self):
        dt = self.get_conversion_factor()
        x_max, y_max = self.get_layout_boundaries()
        xpix = self.pixel_data["x"]
        ypix = self.pixel_data["y"]
        tot = self.pixel_data["tot"]
        dtot = 25  # ToT conversion factor
        fig = plt.figure(figsize=(6, 4))
        plt.hist2d(xpix, ypix, bins=(x_max, y_max), weights=tot / dtot, range=[[0, x_max], [0, y_max]],
                   vmax=1000000 / dtot)
        sns.despine(fig)
        plt.xlabel('xpix')
        plt.ylabel('ypix')
        self.save_figure('weighted_pixel_hits_histogram.png')

    def get_conversion_factor(self):
        conversion_factors = {
            'ns': 1e-9,
            'ps': 1e-12,
            'fs100': 1e-13
        }
        return conversion_factors[self.units]

    def get_layout_boundaries(self):
        boundaries = {
            'single': (256, 256),
            'quad': (512, 512)
        }
        return boundaries[self.layout]

    def save_figure(self, filename: Optional[str] = None):
        if self.output_directory is None:
            fname = os.path.join(os.getcwd(), filename)
        else:
            fname = os.path.join(self.output_directory, filename)

        plt.savefig(fname, dpi=150, bbox_inches="tight")
        logger.info(f"Plot saved to \"{fname}\"")
        plt.close()


class Timepix3Data:
    """
    A class to manage the data from Timepix3 detector stored in an HDF5 file.

    Attributes:
        hdf5_path (str): The file path to the HDF5 file containing the detector data.
        pixel_data (pd.DataFrame): DataFrame containing the pixel hit data.
        cluster_data (pd.DataFrame): DataFrame containing the cluster data.
        tdc_data (pd.DataFrame): DataFrame containing the TDC events data.
    """

    def __init__(self, hdf5_path: str, layout: str, units: str, output_directory: Optional[str] = None) -> None:
        """
        The constructor for Timepix3Data class.

        Parameters:
            hdf5_path (str): The file path to the HDF5 file containing the detector data.
        """
        self.hdf5_path = hdf5_path
        self.pixel_data: pd.DataFrame
        self.cluster_data: pd.DataFrame
        self.tdc_data: pd.DataFrame
        self.layout = layout
        self.units = units
        self.output_directory = output_directory

        self._load_data()

    def _load_data(self) -> None:
        """Private method to load data from the HDF5 file into DataFrames."""
        with h5py.File(self.hdf5_path, 'r') as h5f:
            self.pixel_data = pd.DataFrame(h5f["PixelHits"][:])
            self.cluster_data = pd.DataFrame(h5f["Clusters"][:])
            self.tdc_data = pd.DataFrame(h5f["TDCEvents"][:])

    def get_pixel_data(self) -> pd.DataFrame:
        """Return the pixel hit data as a pandas DataFrame."""
        return self.pixel_data

    def get_cluster_data(self) -> pd.DataFrame:
        """Return the cluster data as a pandas DataFrame."""
        return self.cluster_data

    def get_tdc_data(self) -> pd.DataFrame:
        """Return the TDC events data as a pandas DataFrame."""
        return self.tdc_data

    def create_tiff_from_pixel_data(self, x_max: int = 512, y_max: int = 512, scale_factor: int = 32):
        """
        Create a TIFF image from the pixel data.

        Parameters:
            x_max (int): The max value of the x dimension of the image. Defaults to 256.
            y_max (int): The max value of the y dimension of the image. Defaults to 256.
            scale_factor (int): The factor to scale the 'tot' values by. Defaults to 32.

        Returns:
            str: The file name of the created TIFF file.
        """
        TiffPlotter.create_tiff_from_pixel_data(self.pixel_data, x_max, y_max, scale_factor, self.output_directory)

    def create_tiff_from_cluster_data(self, x_max: int = 512, y_max: int = 512, scale_factor: int = 32):
        """
        Create a TIFF image from the cluster data.

        Parameters:
            x_max (int): The max value of the x dimension of the original image
            y_max (int): The max value of the y dimension of the original image
            scale_factor (int): The factor to scale the 'sum_tot' values by. Defaults to 32.

        Returns:
            str: The file name of the created TIFF file.
        """
        TiffPlotter.create_tiff_from_cluster_data(self.cluster_data, x_max, y_max, scale_factor, self.output_directory)

    def plot_toa_histogram(self):
        hist_plotter = HistogramPlotter(self.pixel_data, self.layout, self.units, self.output_directory)
        hist_plotter.plot_toa_histogram()

    def plot_tot_histogram(self):
        hist_plotter = HistogramPlotter(self.pixel_data, self.layout, self.units, self.output_directory)
        hist_plotter.plot_tot_histogram()

    def plot_pixel_hits_histogram(self):
        hist_plotter = HistogramPlotter(self.pixel_data, self.layout, self.units, self.output_directory)
        hist_plotter.plot_pixel_hits_histogram()

    def plot_weighted_pixel_hits_histogram(self):
        hist_plotter = HistogramPlotter(self.pixel_data, self.layout, self.units, self.output_directory)
        hist_plotter.plot_weighted_pixel_hits_histogram()
