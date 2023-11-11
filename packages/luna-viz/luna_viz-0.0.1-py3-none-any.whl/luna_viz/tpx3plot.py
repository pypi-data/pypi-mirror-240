import argparse
import logging
import os
from luna_viz.tpx3data import Timepix3Data

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)


def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error(f"The file {arg} does not exist!")
    else:
        return arg

def add_layout_argument(parser):
    """This is needed by multiple subgroups."""
    parser.add_argument('--layout', type=lambda s: s.lower(), choices=['single', 'quad'], required=True,
                        help='Layout for the TIFF image output.')

def add_units_argument(parser):
    """This is needed by multiple subgroups."""
    parser.add_argument('--units', type=str, choices=['ns', 'ps', 'fs100'], required=True,
                            help='Units for the Time of Arrival data.')



def handle_tiff(args):
    tpx_data = Timepix3Data(args.hdf5_path)

    # quad default.
    x_max, y_max = 512, 512

    # overwrite if Single
    if args.layout == 'Single':
        x_max, y_max = 256, 256

    # Check which data type was chosen for TIFF creation and call the appropriate function
    if args.pixel:
        logger.info(f"Creating TIFF for pixel data with layout {args.layout} from file {args.hdf5_path}")
        tpx_data.create_tiff_from_pixel_data(x_max=x_max, y_max=y_max, scale_factor=32,
                                             output_directory=args.output_directory)
    elif args.cluster:
        logger.info(f"Creating TIFF for cluster data with layout {args.layout} from file {args.hdf5_path}")
        tpx_data.create_tiff_from_cluster_data(x_max=x_max, y_max=y_max, scale_factor=32,
                                               output_directory=args.output_directory)


def handle_toa(args):
    # Implement the function to handle the 'toa' subcommand
    logger.info(f"Processing ToA data in {args.units} units from file {args.hdf5_path}")


def handle_hist(args):
    tpx_data = Timepix3Data(args.hdf5_path, layout=args.layout, units=args.units, output_directory=args.output_directory)
    tpx_data.plot_toa_histogram()
    tpx_data.plot_tot_histogram()
    tpx_data.plot_pixel_hits_histogram()
    tpx_data.plot_weighted_pixel_hits_histogram()


def main():
    # Create the top-level parser
    parser = argparse.ArgumentParser(description='Process and visualize data from Timepix3 detector.')
    parser.add_argument('hdf5_path', type=lambda x: is_valid_file(parser, x),
                        help='Path to the HDF5 file to process.')

    # Create subparsers for the "tiff" and "toa" command groups

    subparsers = parser.add_subparsers(dest='command', required=True, help='Sub-command help.')

    # Create the parser for the "tiff" command
    parser_tiff = subparsers.add_parser('tiff', help='Create TIFF images from the data.')
    add_layout_argument(parser_tiff)
    add_units_argument(parser_tiff)

    # Add arguments to specify the data type to process for TIFF
    group = parser_tiff.add_mutually_exclusive_group(required=True)
    group.add_argument('--pixel', action='store_true', help='Process pixel hit data for TIFF output.')
    group.add_argument('--cluster', action='store_true', help='Process cluster data for TIFF output.')

    # Create the parser for the "toa" command
    # parser_toa = subparsers.add_parser('toa', help='Process Time of Arrival (ToA) data.')


    parser_hist = subparsers.add_parser('hist', help='Plot data histograms from the Timepix3 data.')
    add_layout_argument(parser_hist)
    add_units_argument(parser_hist)

    # Parse the arguments
    args = parser.parse_args()

    h5_directory = os.path.dirname(args.hdf5_path)
    output_directory = os.path.join(h5_directory, "Tpx3DataPlots")
    os.makedirs(output_directory, exist_ok=True)
    args.__setattr__("output_directory", output_directory)

    # Based on the subcommand, call the appropriate function/handler
    if args.command == 'tiff':
        handle_tiff(args)
    elif args.command == 'toa':
        handle_toa(args)
    elif args.command == "hist":
        handle_hist(args)


if __name__ == '__main__':
    main()
