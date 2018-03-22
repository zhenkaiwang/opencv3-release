Name:           ros-lunar-opencv3
Version:        3.3.1
Release:        2%{?dist}
Summary:        ROS opencv3 package

Group:          Development/Libraries
License:        BSD
URL:            http://opencv.org
Source0:        %{name}-%{version}.tar.gz

Requires:       ffmpeg-devel
Requires:       libjpeg-turbo-devel
Requires:       libpng-devel
Requires:       libwebp-devel
Requires:       numpy
Requires:       protobuf
Requires:       python-devel
Requires:       ros-lunar-catkin
Requires:       vtk-qt
Requires:       zlib-devel
BuildRequires:  cmake
BuildRequires:  ffmpeg-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff
BuildRequires:  libv4l-devel
BuildRequires:  libwebp-devel
BuildRequires:  numpy
BuildRequires:  protobuf-compiler
BuildRequires:  protobuf-devel
BuildRequires:  python-devel
BuildRequires:  vtk-qt
BuildRequires:  zlib-devel

%description
OpenCV 3.x

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Thu Mar 22 2018 Vincent Rabaud <vincent.rabaud@gmail.com> - 3.3.1-2
- Autogenerated by Bloom

* Sun Jan 14 2018 Vincent Rabaud <vincent.rabaud@gmail.com> - 3.3.1-1
- Autogenerated by Bloom

* Wed Nov 01 2017 Vincent Rabaud <vincent.rabaud@gmail.com> - 3.3.1-0
- Autogenerated by Bloom

* Wed Jun 07 2017 Vincent Rabaud <vincent.rabaud@gmail.com> - 3.2.0-9
- Autogenerated by Bloom

* Tue Jun 06 2017 Vincent Rabaud <vincent.rabaud@gmail.com> - 3.2.0-8
- Autogenerated by Bloom

* Mon Jun 05 2017 Vincent Rabaud <vincent.rabaud@gmail.com> - 3.2.0-7
- Autogenerated by Bloom

* Wed Mar 15 2017 Vincent Rabaud <vincent.rabaud@gmail.com> - 3.2.0-6
- Autogenerated by Bloom

* Wed Mar 15 2017 Vincent Rabaud <vincent.rabaud@gmail.com> - 3.2.0-5
- Autogenerated by Bloom

* Tue Mar 14 2017 Vincent Rabaud <vincent.rabaud@gmail.com> - 3.2.0-4
- Autogenerated by Bloom

* Mon Mar 13 2017 Vincent Rabaud <vincent.rabaud@gmail.com> - 3.2.0-3
- Autogenerated by Bloom

