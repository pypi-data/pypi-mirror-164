from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'This package is for Selfie segmentation of image dataset'
LONG_DESCRIPTION = 'This library is used for selfie segmentation of static and live webcam feed. You ca add images or ' \
                   'a constant backgroundd colour over your image/live feed. It is usefull for projects like: ' \
                   'Face recognition, Facial expression recognition and others, where an accurate segmentation will ' \
                   'enhance the feed to the neural network therefore increasing the accuracy of the model'

# Setting up
setup(
    name="selfiesegmentation",
    version=VERSION,
    author="Sumit Singh",
    author_email="<iamsumit1904@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['opencv-python', 'numpy', 'mediapipe'],
    keywords=['python', 'augmentation', 'image', 'data augmentation', 'image dataset'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
