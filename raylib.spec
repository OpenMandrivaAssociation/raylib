%define major 1
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Name:		raylib
Version:	5.5
Release:	1
Source0:	https://github.com/raysan5/raylib/archive/%{version}/%{name}-%{version}.tar.gz
Summary:	raylib
URL:		https://www.raylib.com
License:	zlib
Group:		System/Libraries	
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glfw3)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(vulkan)
BuildSystem:	cmake
BuildOption:	-D BUILD_EXAMPLES=OFF
BuildOption:	-D BUILD_SHARED_LIBS=ON
BuildOption:	-D PLATFORME=Desktop
BuildOption:	-D USE_EXTERNAL_GLFW=ON
BuildOption:	-D WITH_PIC=ON	

#-------------------------------------------------------------------------------

%description
raylib is highly inspired by Borland BGI graphics lib and by XNA framework and
it's especially well suited for prototyping, tooling, graphical applications,
embedded systems and education.

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries

%description -n %{libname}
This package contains the %{name} library needed for programs that are 
dynamically linked to it.

%files -n %{libname}
%doc README.md
%doc FAQ.md 
%license LICENSE
%{_libdir}/libraylib.so.5*
%{_libdir}/libraylib.so

#-------------------------------------------------------------------------------

%package -n %{devname}
Summary:	Headers for development with %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains the headers for development with %{name}

%files -n %{devname}
%{_includedir}/raylib.h
%{_includedir}/rlgl.h
%{_includedir}/raymath.h
%{_libdir}/pkgconfig/raylib.pc
%{_libdir}/cmake/raylib/raylib-config-version.cmake
%{_libdir}/cmake/raylib/raylib-config.cmake

