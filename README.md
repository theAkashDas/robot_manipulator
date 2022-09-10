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

#### 0.0.4
- Saved the rviz configs in the launch folder as config.rviz 
- For showing the saved rviz config during roslaunch we have to add some lines in ros launch file
```
<node name="rviz" pkg="rviz" type="rviz" args=" -d $(find arm_a)/launch/config.rviz"/>
```
- After that
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
- After that
```
roslaunch arm_a arm_rviz.launch
```
- Refer to the Video 2.

#### 0.0.6
- Added a file named robot_parameters.xacro.
- this file contains the name of the links and joints as parameters.
- used "${link_name}" to get the link name from the xacro file.
- So if we need to change the name or the parameters we have to that in that specific file only.

---
### Images :

#### Image 1 :
<img src="Images/a1.png" width="840"/>

### Vidoes :

#### Video 1 :
![A](https://github.com/theAkashDas/robot_manipulator/blob/master/Videos/v1.gif) 

#### Video 2 :
![A](https://github.com/theAkashDas/robot_manipulator/blob/master/Videos/v2.mp4) 