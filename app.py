import sys
import os
import re


def trim(file_name):
    """Removes extra spaces and underscore from the file name.

    Keyword arguments:
    file_name -- file to be renamed

    Returns: string

    """
    pattern = '_(?!\\.)'  # match '_' if it's not followed by a '.'
    return ' '.join(re.sub(pattern, ' ', file_name).replace('_', '').split())


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if os.path.isdir(sys.argv[1]):
            for pathname, subdir, files in os.walk(sys.argv[1]):
                os.chdir(pathname)
                for f in files:
                    os.rename(f, trim(f))
        else:
            print('\'PATH\' - {} - is not valid.'.format(sys.argv[1]))
    else:
        raise ValueError(
            'Unable to proceed. The folder\'s \'PATH\' has to be provided.')
