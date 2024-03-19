import numpy as np
import tifffile
from scipy.io import savemat
import glob
import os


def main():
    tiff_paths = []
    for i in range(1,10):
        tiff_paths.append("C:/Users/bkotl/PycharmProjects/DeePoreCollab/Fiber_Files/35e.{}c.tiff".format(i))
    print(tiff_paths)
    def tiff_to_binary_voxels(tiff_path):
        """
        Convert a TIFF file to a binary 3D numpy array (voxels), with 1s for solids and 0s for voids.

        Parameters:
        - tiff_path: Path to the TIFF file.

        Returns:
        - binary_voxels: 3D numpy array representing the voxelized image in binary format.
        """
        # Using tifffile to handle potentially large tiff files more efficiently
        with tifffile.TiffFile(tiff_path) as tif:
            images = tif.asarray()
            # Convert to binary: 1 for solid structures (nonzero), 0 for voids (zero)
            binary_voxels = np.where(images > 1, 1, 0).astype(np.uint8)

        return binary_voxels

    for i, tiff_file in enumerate(tiff_paths):
        i+=1
        binary_voxels = tiff_to_binary_voxels(tiff_file)
        print(binary_voxels.shape)
        mat_data = {'A': binary_voxels}
        # Save the binary voxel data to a .mat file
        savemat('C:/Users/bkotl/PycharmProjects/DeePoreCollab/Data/voxelized_images/35e.{}c.mat'.format(i), mat_data)

if __name__ == '__main__':
    main()
