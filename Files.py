"""
Files module

Files Class [ Files.py ]

@author      Eric Potvin
@package     PythonLib
@subpackage  Files
@link        https://github.com/ericpotvin/PythonLib
"""
import codecs
import binascii
from os import path, remove, walk, makedirs

# File extensions
FILE_EXT_HTML = ".html"
FILE_EXT_JSON = ".json"

ERROR_FILE_NOT_FOUND = "The file %s cannot be found"


class Files(object):
    """ Files module class
    """

    @staticmethod
    def get_file_list(folder, exclude=None):
        """ Get the file list for a path
            :param folder: The path
            :param exclude: a list of file to exclude
            :return: List
        """
        my_list = []

        if exclude is None:
            exclude = []

        # add files we never use
        exclude.append("__init__.py")
        exclude.append(".pyc")

        for root, dirs, files in walk(folder):
            del (root, dirs)
            for filename in files:
                if Files.can_include_file(filename, exclude):
                    my_list.append(filename)
        return my_list

    @staticmethod
    def can_include_file(filename, excludes):
        """ Check if a filename is allowed
            :param filename: the filename
            :param excludes: the filename to exclude
        """
        _filename, ext = path.splitext(filename)
        del _filename
        for exclude in excludes:
            if ext == exclude:
                return False
            if filename == exclude:
                return False
        return True

    @staticmethod
    def get_raw_contents(filename, folder=""):
        """ Get the raw content of a file
            :param filename: The filename
            :param folder: The path
            :return: String
        """
        with codecs.open(folder + filename, "r", "utf8") as my_file:
            data = my_file.read()
        return data

    @staticmethod
    def write(data, file_name, folder):
        """ Write the data to a file
            :param data: The data
            :param file_name: the filename
            :param folder: The path
            :return: null
        """
        with open(folder + file_name, 'w') as filename:
            filename.write(data)

    @staticmethod
    def write_binary(data, filename, folder="./"):
        """ Write the data to a file in binary mode
            :param data: The data to save
            :param filename: The file name
            :param folder: The folder where to save the file
        """
        data = data.encode('UTF8')
        with open(folder + filename, 'wb') as file_data:
            file_data.write(binascii.hexlify(data))

    @staticmethod
    def read_binary_file(file_name, position, length):
        """ Read x characters from a binary file starting at a position
            :param file_name: The filename
            :param position: The starting position
            :param length: The length
            :return string
        """
        with open(file_name, "rb") as my_file:
            my_file.seek(position * 2)
            content = my_file.read(length * 2)
            return binascii.unhexlify(content)

    @staticmethod
    def file_exists(filename):
        """ Check if the file exists
            :param filename: The filename
            :return boolean
        """
        return path.exists(filename)

    @staticmethod
    def create_folder(folder):
        """ Creates a folder
            :param folder: The folder name
        """
        if Files.file_exists(folder):
            return
        makedirs(folder)

    @staticmethod
    def delete_files(filename):
        """ Delete a file
            :param filename: The filename (full path)
        """
        if path.isfile(filename):
            remove(filename)

    @staticmethod
    def delete_folder(folder):
        """ Delete a folder and its files
            :param folder: The folder
        """
        if not path.exists(folder):
            return False

        files = Files.get_file_list(folder)
        for filename in files:
            Files.delete_files(folder + "/" + filename)
