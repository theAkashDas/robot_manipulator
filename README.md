# Robot Manipulator
This Repository contains a robot manipulator from scratch.

---
### Change Logs :
#### 0.0.1
- Added the package in catkin_ ws with a package name arm_a
```
catkin_create_pkg arm_a roscpp rospy urdf
```
- Added a folder named urdf
- Added arm.xacro (xacro is xml macro)

#### 0.0.2
- Adding the links in xacro file
- started with the base link
- visual part contains collision, roll-pitch-yaw, inertia

#### 0.0.3
- Added the xacro file. 
- Added description of base link and link 1 along with there joints.
- Joints appear in the middle of links.
- Added a rviz launch file.
```
catkin build
roslaunch arm_a arm_rviz.launch
```
- Refer to the Video 1.

#### 0.0.4
- Saved the rviz configs in the launch folder as config.rviz 
- For showing the saved rviz config during roslaunch we have to add some lines in ros launch file
```
<node name="rviz" pkg="rviz" type="rviz" args=" -d $(find arm_a)/launch/config.rviz"/>
```
- After that :
```
roslaunch arm_a arm_rviz.launch
```

#### 0.0.5
- Added a xacro macro file named link_joint.xacro
- This file contains the links and joint definition as a function
- In arm_b.xacro we are just calling those function from the link_joint.xacro file and using them.
- Need to include this file in arm_b.xacro
```
<xacro:include filename = "$(find arm_a)/urdf/link_joint.xacro" />
```
- Made the file name change in the launch file.
- After that :
```
roslaunch arm_a arm_rviz.launch
```
- Refer to the Video 2.

#### 0.0.6
- Added a file named robot_parameters.xacro.
- this file contains the name of the links and joints as parameters.
- used "${link_name}" to get the link name from the xacro file.
- So if we need to change the name or the parameters we have to that in that specific file only.

#### 0.0.7
- Added the intertia and collision parameters in the xacro file
- inertia and collision properties depend on the robot model we are making.
- After that added a spawn.launch file to launch gazebo simulation.
- After that :
```
roslaunch arm_a spawn.launch
rosrun gazebo_ros gazebo
```
- Refer to Image 2.
- The links have fallen down because stil there is no controller initialized.

#### 0.0.8
- Kept only 3 links and 2 joints to apply controller.
- Added an allias in .bashrc and source .bashrc to kill th previous gzclient and gzserver since the model was not updating.
```
alias killg='killall gzclient && killall gzserver && killall rosmaster'
```
#### 0.0.9
- Added transmission in arm_b.xacro file for the joints to implement controllers.
- Made changes in the dependencies in CMakeLists.txt and package.xml
- Added dependencies of joint state publisher, robot state publisher, controller manager.
- Made changes in the spawn.launch file to include controller_manager
- Encapsulated launch file inside a group tag.
- Added joints.yaml in the config folder
- joints.yaml contains the controller properties and names.
- Added a gazebo plugin in arm_b.xacro file named gazebo_ros_control.
- After that :
```
roscore
rosrun gazebo_ros gazebo
roslaunch arm_a spawn.launch
rostopic list
rostopic pub -1 /arm/joint2_position_controller/command std_msgs/Float64 "data: 0.7"
rostopic pub -1 /arm/joint1_position_controller/command std_msgs/Float64 "data: 1"
```
- Refer to Video 3

#### 0.0.10
- Added transmission properties in link_joint.xacro file
- Added node for rqt
- Added transmission for all the other joints.
- Reduced the mass of the links and inertia.
- Added lower and upper limit of the robot movement.
- After that :
```
roscore
rosrun gazebo_ros gazebo
roslaunch arm_a spawn.launch
rostopic list
```
- Then use the rqt_publisher to give the values to links and plot juggler to view it.
- Refer to Video 4.

#### 0.0.11
- Added a mesh folder in the package
- Added a .stl file to that folder.
- Changed the link 1 with the added mesh.
- Commented out the other links.
- After that :
```
roscore
rosrun gazebo_ros gazebo
roslaunch arm_a spawn.launch
```
- Then use the rqt_publisher to give the values to links and plot juggler to view it.
- Refer to Video 5.
- Next is to add an end effector mesh.
- Add depth camera to the arm.
- Implement Forward and Inverse Kinematics on the Arm
- Study more on the Moment of Inertia along different axes.

#### 0.0.12
- Added another new link and made the joint fixed.
- This link is to hold the depth camera in position.
- Was tweeking with the pid values of the joint controller to give a efficient control.
- Refer to Image 3

#### 1.0.0
- Starting with Depth Camera Integration in the Manipulator.
- Cloned the repositories for real sense.
- Repo1 : https://github.com/pal-robotics/realsense_gazebo_plugin
- Repo2 : https://github.com/issaiass/realsense2_description
- After that :
```
cd catkin_ws
catkin build
source devel/setup.bash
roslaunch realsense2_description view_d435_model_rviz_gazebo.launch
```
- Refer to Image 4.

#### 1.0.1
- Added a new xacro file named arm_c.xacro for adding depth camera.
- Included the file from realsnse2_description package to use the depth camera in my project.
```
<xacro:include filename = "$(find realsense2_description)/urdf/_d435.urdf.xacro"
```
- Then added :
```
<xacro:sensor_d435 name="camera" topics_ns="camera" parent="${l05}" publish_pointcloud="true">
  <origin xyz="-0.2 0 0.1" rpy="0 -1.57 0" />
</xacro:sensor_d435>
```
- The origin xyz and rpy needs to be changed accordingly to fit in our previous model.

#### 1.0.2
- After making all the changes in .xacro file, we need to make changes to the launch file to launch the changed xacro.
- After that :
```
roscore
rosrun gazebo_ros gazebo
roslaunch arm_a spawn.launch
rostopic list
rosrun image_view image_view image:=/camera/depth/image_raw
roslaunch arm_a arm_rviz.launch
```
- Refer to Video 6 and Image 5,6.

#### 1.0.3
- Added two new links to the robot model which will act as grippers.
- Added the prismatic joints for the grippers.
- Made changes in the joints.yaml and also launch file.
- Added joint8_position_controller.
- Added a folder named scripts.
- Added a python script named grip.py for controlling the grippers.
```
roscore
rosrun gazebo_ros gazebo
roslaunch arm_a spawn.launch
cd catkin_ws/src/arm_a/scripts
python3 grip.py
```
- Refer to Video 7.


---
### Images :

#### Image 1 :
<img src="Images/a1.png" width="840"/>

#### Image 2 :
<img src="Images/a2.png" width="840"/>

#### Image 3:
<img src="Images/a3.png" width="840"/>

#### Image 4:
<img src="Images/a4.png" width="840"/>

#### Image 5:
<img src="Images/a5.png" width="840"/>

#### Image 6:
<img src="Images/a6.png" width="840"/>


### Vidoes :

#### Video 1 :
https://user-images.githubusercontent.com/56507553/189474051-e167d7de-ddbb-4ec2-9db9-4c5db68e6177.mp4

#### Video 2 :
https://user-images.githubusercontent.com/56507553/189452882-20b8ea90-231a-4d94-abcc-88aa335bc7a2.mp4

#### Video 3 :
https://user-images.githubusercontent.com/56507553/189517449-66ffbf97-fba4-4ae5-a48f-88f90b699c51.mp4

#### Video 4 :
https://user-images.githubusercontent.com/56507553/189584218-4586c8af-dde0-4e9b-84b3-f9caa7fadf7f.mp4

#### Video 5 :
https://user-images.githubusercontent.com/56507553/189593023-a71af6a2-bd72-45b4-9c49-204aca4e808f.mp4

#### Video 6 :
https://user-images.githubusercontent.com/56507553/190442685-eff615f6-7fe6-453d-b987-bb5805350a95.mp4

#### Video 7 :
https://user-images.githubusercontent.com/56507553/190607503-29839462-4afa-4e20-9241-54462b0ea164.mp4

