#globals for vid.stab-0.98a-20150424-4ec5be1.tar
%global gitdate 20150424
%global gitversion 4ec5be1
%global snapshot %{gitdate}-%{gitversion}
%global gver .%{gitdate}git%{gitversion}

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


%prep
%setup -q

%build
%cmake .
make

%install
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%{_includedir}/vid.stab/
%{_libdir}/libvidstab.so
%{_libdir}/libvidstab.so.*
%{_libdir}/pkgconfig/vidstab.pc

%changelog

* Fri Apr 24 2015 David Vasquez <davidjeremias82 at gmail dot com> 0.98a-20150424-4ec5be1-1
- Updated to 0.98a-20150424-4ec5be1
- Included snapshot

* Mon Sep 1 2014 David Vasquez <davidjeremias82 at gmail dot com> 0.98b-1
- Initial build rpm
