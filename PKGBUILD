# Script generated with Bloom
pkgdesc="ROS - Maintains a local obstacle map (point cloud, voxels or occupancy grid) from recent sensor readings within a configurable time window."
url='http://wiki.ros.org/mrpt_local_obstacles'

pkgname='ros-kinetic-mrpt-local-obstacles'
pkgver='0.1.18_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-mrpt-bridge'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
'ros-kinetic-tf'
'ros-kinetic-visualization-msgs'
)

depends=('ros-kinetic-dynamic-reconfigure'
'ros-kinetic-mrpt-bridge'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
'ros-kinetic-tf'
'ros-kinetic-visualization-msgs'
)

conflicts=()
replaces=()

_dir=mrpt_local_obstacles
source=()
md5sums=()

prepare() {
    cp -R $startdir/mrpt_local_obstacles $srcdir/mrpt_local_obstacles
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

