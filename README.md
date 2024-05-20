# object-detector-trained-artificial-data

YOLO based object detector trained with artficially created data

This project was conducted as the final project for the post-graduation course offered by Universidad de Buenos Aires (UBA) in 2023.

It consists in a idea I had while facing difficulties when trying to build a dataset for images, in an application where it was hard to acquire images relevant to the problem.

Instead of using real images, I decided to test creating a dataset with artificial data. The images created would form either the entire dataset or, at least, a significant part of it. In the end, I was able to achieve a trained model with good performance with a 100% artificial dataset.

The idea came from a few examples I had seen on the internet applied to other problems. A notable one was the example given by Tesla, where they created an entire simulation for their self-driving AI.

This repository contains only a few of the files used in the project, mainly a sample of the real images, one of the datasets and one of the training scripts.

## File description

	.
	├── blender_files			# Folder containing the blender related files for
	|  	├── usb_v3.blend 		# Blender file containing the object to detect and the necessary 3D objects to simulate the real-world environment
	|	├── render_script.py		# Python file to render N images from terminal
	├── datasets
	|	├── real_images			# Sample of images for the final validation dataset, containing real images
	|	|	├── images		# The real images
	|	|	├── labels		# Coordinates for the real images
	|	├── size500			# Training dataset containing 500 images
	|	|	├── images		# Artificial images
	|	|	├── labels		# Coordinates for the artificial images			
	├── models				
	|	├── yolo			# This folder contains one of the notebooks used to train the YOLO model with the artificial images
	├── scripts				# Folder containing scripts to help build the dataset
	|	├── convert_images.ipynb	# Code to create labels for the real images 
	|	├── create_dataset.ipynb	# Code to create smaller datasets from artificial images
	|	├── create_tfrecord.ipynb	# Code to create a tfrecord file for each dataset
	|	├── generate_yolo_labels.ipynb	# Code to create labels from rendered masks for the artificial images
	

## Prerequisites
Running this project requires:
* tensorflow
* torch
* ultralytics
* Ipython.display
* opencv-python
* matplotlib
* numpy
