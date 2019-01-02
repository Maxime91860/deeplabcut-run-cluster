import deeplabcut
import time
import os

current_path = os.getcwd()
project_name = 'demo'
experimenter_name = 'cluster_icm'
date = time.strftime("%Y-%m-%d")

video_path = current_path+'/videos/reachingvideo1.avi'


# Create a New Project
deeplabcut.create_new_project(project_name, experimenter_name, video_path)

# Configure the Project
# Edit the config.yaml
config_path = current_path+'/'+project_name+'-'+experimenter_name+'-'+date+'/config.yaml'

# Select Frames to Label
deeplabcut.extract_frames(config_path, 'automatic', 'kmeans') 

# Label Frames
deeplabcut.label_frames(config_path) 