"""Main Function."""
from scipy.misc import imread, imsave
from utilities import perform_alteration, new_file_name, get_args


def main(choice):
    """Script to run."""
    path = 'resources/Michael.JPG'
    alt_image = perform_alteration(imread(path), choice)
    imsave(new_file_name(path, choice), alt_image)
    print('\rDone!')

if __name__ == '__main__':
    main(get_args())
