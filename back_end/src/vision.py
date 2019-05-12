import argparse
import io

from google.cloud import vision
from google.cloud.vision import types

"""
"""

def annotate(path):
    """
    Returns web annotations given the path to an image.

    Taken from tutorial https://cloud.google.com/vision/docs/internet-detection
    """
    client = vision.ImageAnnotatorClient()

    if path.startswith('http') or path.startswith('gs:'):
        image = types.Image()
        image.source.image_uri = path

    else:
        with io.open(path, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)

    web_detection = client.web_detection(image=image).web_detection

    return web_detection


def get_large_from_thumbnail(url):
    """
    Gets the large image URL from a given thumbnail

    :param url: The thumbnail url
    :return: The URL of the large image
    """
    a = annotate(url)
    r = return_large(a)

    # If there are no large equivalents, return None
    if not r:
        return None
    return r


def return_large(web_detection_result):
    """
    Returns the single exact match large image

    :param web_detection_result: The result given by the web detection engine
    :return: The large image url (or None if none exists)
    """
    if web_detection_result.full_matching_images:
        return web_detection_result.full_matching_images[0].url
    elif web_detection_result.partial_matching_images:
        return web_detection_result.partial_matching_images[0].url
    else:
        return None

if __name__ == '__main__':
    # parser = argparse.ArgumentParser(
    #     description=__doc__,
    #     formatter_class=argparse.RawDescriptionHelpFormatter)
    # path_help = str('The image to detect, can be web URI, '
    #                 'Google Cloud Storage, or path to local file.')
    # parser.add_argument('image_url', help=path_help)
    # args = parser.parse_args()
    #
    # report(annotate(args.image_url))

    a = get_large_from_thumbnail("https://s3-eu-west-1.amazonaws.com/property.adzuna.co.uk/e3dafc5f824674cb70bea8d375caaf4dc5eff714f678b67574f6f9f689a6def7.jpeg")
    print(a)