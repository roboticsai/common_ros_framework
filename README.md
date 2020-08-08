# common_ros_framework
To launch the hector_slam without odometry
1. Launch rplidar node to read the laser data
roslaunch rplidar_ros rplidar.launch
2. Launch the hectormap launch file for mapping given area
roslaunch hector_slam_launch tutorial.launch

To run the object classification with real time images from usb camera:
1. Run the tf lite python script 
cd ~/common_ros_framework/src/tf_lite
./run_label_video.sh
