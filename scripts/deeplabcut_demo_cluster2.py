import deeplabcut
import time
import os

current_path = os.getcwd()
project_name = 'demo-openfield-Pranav'
experimenter_name = 'cluster_icm'
date = '2018-12-31' # time.strftime("%Y-%m-%d")

video_path = current_path+'/videos/m3v1mp4.mp4'
config_path = current_path+'/'+project_name+'-'+experimenter_name+'-'+date+'/config.yaml'


# Create Training Dataset
deeplabcut.create_training_dataset(config_path)

# Train The Network
deeplabcut.train_network(config_path)

# Evaluate the Trained Network
deeplabcut.evaluate_network(config_path)

# Video Analysis and Plotting Results
deeplabcut.analyze_videos(config_path, video_path)
deeplabcut.create_labeled_video(config_path, [video_path])
deeplabcut.plot_trajectories(config_path, [video_path])
