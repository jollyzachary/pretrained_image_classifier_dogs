# Pre-trained Image Classifier to Identify Dog Breeds

This project is part of the Udacity AI Programming with Python Nanodegree. It uses a pre-trained image classifier to identify dog breeds.

## Project Overview

In this project, we use a created image classifier to identify dog breeds. We use a package that makes use of pre-trained networks (ResNet, AlexNet, or VGG) from the [torchvision.models](https://pytorch.org/docs/0.3.0/torchvision/models.html) module. With this project, we learn how to develop Python command-line applications that will process user-supplied input.

## Prerequisites

The project requires the following software:

- Python 3
- PyTorch and TorchVision
- PIL

## Command Line Application

`python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt`

- `--dir pet_images/` specifies the directory of pet images (default is `pet_images/`)
- `--arch vgg` specifies the CNN model architecture to use (default is `vgg`, options are `resnet`, `alexnet`, or `vgg`)
- `--dogfile dognames.txt` contains the list of valid dog names that the classifier can identify (default is `dognames.txt`)

## Authors

- Zachary Jolly

## Acknowledgments

- Udacity for providing the project and the workspace for the project
