# object-detector-trained-artificial-data

YOLO based object detector trained with artficially created data

This project was conducted as the final project for the post-graduation course offered by Universidad de Buenos Aires (UBA) in 2023.

It consists in a idea I had while facing difficulties when trying to build a dataset for images, in an application where it was hard to acquire images relevant to the problem.

Instead of using real images, I decided to test creating a dataset with artificial data. The images created would form either the entire dataset or, at least, a significant part of it. In the end, I was able to achieve a trained model with good performance with a 100% artificial dataset.

The idea came from a few examples I had seen on the internet applied to other problems. A notable one was the example given by Tesla, where they created an entire simulation for their self-driving AI.

## File description

	.
	├── blender_files			# Folder containing the blender related files for
	|  	├── usb_v3.blend 		# Blender file containing the object to detect and the necessary 3D objects to simulate the real-world environment
	|	├── render_script.py		# Python file to render N images from terminal
	├── scripts				# Folder containing scripts to help build the dataset
	|	├── convert_images.ipynb	# Code to create labels for the real images 
	|	├── create_dataset.ipynb	# Code to create smaller datasets from artificial images
	|	├── create_tfrecord.ipynb	# Code to create a tfrecord file for each dataset
	|	├── generate_yolo_labels.ipynb	# Code to create labels from rendered masks for the artificial images

