"""
Google Cloud Vision API calls
"""
import io
from google.cloud import vision
from google.cloud.vision import types


def annotate(path):
    """
    Returns web annotations given the path to an image.

    Taken from tutorial https://cloud.google.com/vision/docs/internet-detection
    """
    if not path:
        return
    
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
