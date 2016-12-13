Name:           ros-jade-mrpt-local-obstacles
Version:        0.1.16
Release:        0%{?dist}
Summary:        ROS mrpt_local_obstacles package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/mrpt_local_obstacles
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-dynamic-reconfigure
Requires:       ros-jade-mrpt-bridge
Requires:       ros-jade-roscpp
Requires:       ros-jade-sensor-msgs
Requires:       ros-jade-tf
Requires:       ros-jade-visualization-msgs
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-dynamic-reconfigure
BuildRequires:  ros-jade-mrpt-bridge
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-sensor-msgs
BuildRequires:  ros-jade-tf
BuildRequires:  ros-jade-visualization-msgs

%description
A node that maintains a local obstacle map (point cloud, voxels or occupancy
grid) from recent sensor readings within a configurable time window.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Tue Dec 13 2016 Jose-Luis Blanco-Claraco <jlblanco@ual.es> - 0.1.16-0
- Autogenerated by Bloom

* Sat Sep 03 2016 Jose-Luis Blanco-Claraco <jlblanco@ual.es> - 0.1.13-0
- Autogenerated by Bloom

* Sun Aug 21 2016 Jose-Luis Blanco-Claraco <jlblanco@ual.es> - 0.1.11-0
- Autogenerated by Bloom

* Fri Aug 05 2016 Jose-Luis Blanco-Claraco <jlblanco@ual.es> - 0.1.10-0
- Autogenerated by Bloom

* Fri Aug 05 2016 Jose-Luis Blanco-Claraco <jlblanco@ual.es> - 0.1.9-0
- Autogenerated by Bloom

* Wed Jun 29 2016 Jose-Luis Blanco-Claraco <jlblanco@ual.es> - 0.1.8-0
- Autogenerated by Bloom

* Sun Mar 20 2016 Jose-Luis Blanco-Claraco <jlblanco@ual.es> - 0.1.6-0
- Autogenerated by Bloom

* Wed Apr 29 2015 Jose-Luis Blanco-Claraco <jlblanco@ual.es> - 0.1.5-0
- Autogenerated by Bloom

