#globals for vid.stab-0.98a-20150706-97c6ae2.tar
%global gitdate 20150706
%global gitversion 97c6ae2
%global snapshot %{gitdate}-%{gitversion}
%global gver .%{gitdate}git%{gitversion}
%global libversion 1.1

Name:           vid.stab
Version:        0.98a
Release:    	1%{?gver}%{dist}
Summary:        Video stabilize library for fmpeg, mlt or transcode

Group:          Video
License:        GPLv3
URL:            http://public.hronopik.de/vid.stab
Source:		%{name}-%{version}-%{snapshot}.tar
Source1:       	%{name}-snapshot.sh  

BuildRequires:	cmake git
Requires:	glibc

%description
Video stabilize library for ffmpeg, mlt or transcode.

%package libs_%{libversion}
Summary: vid.stab plugin library
Group: Development/Libraries

%description libs_%{libversion}
Video stabilize library for ffmpeg, mlt or transcode.
This package contains the shared library file.

%package devel
Summary: vid.stab plugin library
Group: Development/Libraries

%description devel
Video stabilize library for ffmpeg, mlt or transcode.
This package contains the development files.

%prep
%setup -q -n vid.stab-%{version}

%build
%cmake .
make

%install
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%{_libdir}/libvidstab.so

%files libs_%{libversion}
%{_libdir}/libvidstab.so.*

%files devel
%{_includedir}/vid.stab/
%{_libdir}/pkgconfig/vidstab.pc


%changelog
* Mon Jul 6 2015 Fredrik Fornstad <fredrik.fornstad@gmail.com> 0.98a-20150706-97c6ae2-1
- New upstream release
- Introduced separate devel and libs rpms to enable future API updates without breaking dependencies

* Fri Apr 24 2015 David Vasquez <davidjeremias82 at gmail dot com> 0.98a-20150424-4ec5be1-1
- Updated to 0.98a-20150424-4ec5be1
- Included snapshot

* Mon Sep 1 2014 David Vasquez <davidjeremias82 at gmail dot com> 0.98b-1
- Initial build rpm
