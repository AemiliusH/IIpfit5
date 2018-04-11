from EWFImgInfo import *


class Image():
    # Aanmaken van class variable
    ewf_img_info = None

    def __init__(self, image_path):
        '''
        Image object, laad automatisch alle files en partities
        :param image_path: Pad naar image
        '''
        DebugLog("Loading image from: " + image_path)

        # Opslaan belangrijke parameter
        self.image_path = image_path

        try:
            # Opening Image in pyEWF
            self.image_files = pyewf.glob(self.image_path)
            self.ewf_handle = pyewf.handle()
            self.ewf_handle.open(self.image_files)

            # Aanmaken van EWFImage Class, deze combineert EWF met Pytsk3
            self.ewf_img_info = EWFImgInfo(self.ewf_handle, self)
            DebugLog("Image succesfully loaded!")
        except IOError:
            try:
                print "Error opening image with EWF... Attempting raw mode"
                self.ewf_img_info = EWFImgInfo(self.image_path, self, True)
                DebugLog("Image succesfully loaded!")
            except:
                raise Exception(
                    'Unable to open image as filesystem: Cannot determine file system type')

    def get_all_files(self):
        '''
        Ophalen van alle bestanden uit image.
        :return: Arraylist met bestanden
        '''
        files = []
        # Voor iedere image, alle files toevoegen aan de files array
        for partitie in self.ewf_img_info.get_partitions():
            files.extend(partitie.files)
        return files
