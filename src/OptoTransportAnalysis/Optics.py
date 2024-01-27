from os import path
import string
from .Data import Data

class OpticsData(Data):
    """
    Class containing spectral data and associated metadata.

    Contains specific methods pertinent to optical signals, 
    e.g., averaging spectra to elimiinate cosmic ray signals, converting 
    wavelength units to photon energy, etc.

    Attributes
    ----------
    data : pandas DataFrame
        Inherited from Data class. Dataframe containing spectral data, 
        collection wavelength, and other relevant information.

    metadata : dict, optional
        Inherited from Data class. dict containing relevant experimental
        information, e.g., exposure time, excitation laser, optical
        components used, etc.

    filename, filename_md : path or path-like str
        Inherited from Data class. A reference to the file used to 
        initialize the data or metadata attributes (if given).

    metadata_flag : bool


    Methods
    -------
    add_average_signal()
        Appends the average intensity of spectra contained in data to data.
    
    """

    #### Constructor ---------------------------------------------------------

    def __init__(self, filename: path or string = None, filename_md: path or string = None,
        init_dir: path or string = "", metadata_flag = False) -> None: 
        super().__init__(filename=filename, filename_md=filename_md, init_dir=init_dir, 
                         metadata_flag=metadata_flag)
        return

    #### Methods -------------------------------------------------------------

    def add_average_signal(self, num_frames=None) -> None:
        """
        Adds an entry to the data attribute containing the average of all intensities.
        Does so without correcting for cosmic rays.
        """
        int_col_names = [names for names in self.data.columns if names.startswith('Intensity')]
        num_frames = len(int_col_names)
        self.data['Average Intensity'] = self.data[int_col_names].sum(axis=1).values / num_frames
        return

    
    

