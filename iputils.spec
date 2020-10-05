#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : iputils
Version  : s20200821
Release  : 34
URL      : https://github.com/iputils/iputils/archive/s20200821.tar.gz
Source0  : https://github.com/iputils/iputils/archive/s20200821.tar.gz
Summary  : Network monitoring tools
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0
Requires: iputils-bin = %{version}-%{release}
Requires: iputils-license = %{version}-%{release}
Requires: iputils-locales = %{version}-%{release}
Requires: iputils-man = %{version}-%{release}
Requires: iputils-services = %{version}-%{release}
Requires: iputils-setuid = %{version}-%{release}
BuildRequires : attr-dev
BuildRequires : buildreq-meson
BuildRequires : docbook-xml
BuildRequires : libcap-dev
BuildRequires : libxslt-bin
BuildRequires : openssl-dev
BuildRequires : pkgconfig(libidn2)
BuildRequires : pkgconfig(systemd)
BuildRequires : pkgconfig(zlib)

%description
[![Build Status](https://travis-ci.org/iputils/iputils.svg?branch=master)](https://travis-ci.org/iputils/iputils)
[![Coverity Status](https://scan.coverity.com/projects/1944/badge.svg?flat=1)](https://scan.coverity.com/projects/1944)

%package bin
Summary: bin components for the iputils package.
Group: Binaries
Requires: iputils-setuid = %{version}-%{release}
Requires: iputils-license = %{version}-%{release}
Requires: iputils-services = %{version}-%{release}

%description bin
bin components for the iputils package.


%package license
Summary: license components for the iputils package.
Group: Default

%description license
license components for the iputils package.


%package locales
Summary: locales components for the iputils package.
Group: Default

%description locales
locales components for the iputils package.


%package man
Summary: man components for the iputils package.
Group: Default

%description man
man components for the iputils package.


%package services
Summary: services components for the iputils package.
Group: Systemd services

%description services
services components for the iputils package.


%package setuid
Summary: setuid components for the iputils package.
Group: Default

%description setuid
setuid components for the iputils package.


%prep
%setup -q -n iputils-s20200821
cd %{_builddir}/iputils-s20200821

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1601915831
export GCC_IGNORE_WERROR=1
export CFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wformat -Wformat-security -Wno-error -Wl,-z,max-page-size=0x1000 -march=westmere -mtune=haswell"
export CXXFLAGS=$CFLAGS
export FFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wno-error -Wl,-z,max-page-size=0x1000 -march=westmere -mtune=haswell"
export FCFLAGS=$FFLAGS
unset LDFLAGS
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -DBUILD_RARPD=true \
-DBUILD_TRACEROUTE6=true \
-DBUILD_MANS=true \
-DBUILD_HTML_MANS=false \
-DBUILD_TFTPD=true  builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/iputils
cp %{_builddir}/iputils-s20200821/Documentation/LICENSE.BSD3 %{buildroot}/usr/share/package-licenses/iputils/7d9185af9b499d91e113fe752af7d9d53b9e5c6a
cp %{_builddir}/iputils-s20200821/Documentation/LICENSE.GPL2 %{buildroot}/usr/share/package-licenses/iputils/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/iputils-s20200821/ninfod/COPYING %{buildroot}/usr/share/package-licenses/iputils/894a01b2e7d7a684a85caa5bc604ed48d25d9393
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang iputils
## install_append content
mv %{buildroot}/usr/sbin/* %{buildroot}/usr/bin/
# SUID root programs
for i in ping ping traceroute6; do
chmod 4555 %{buildroot}/usr/bin/$i
done

## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/arping
/usr/bin/clockdiff
/usr/bin/ninfod
/usr/bin/rarpd
/usr/bin/rdisc
/usr/bin/tftpd
/usr/bin/tracepath

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/iputils/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/iputils/7d9185af9b499d91e113fe752af7d9d53b9e5c6a
/usr/share/package-licenses/iputils/894a01b2e7d7a684a85caa5bc604ed48d25d9393

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/arping.8
/usr/share/man/man8/clockdiff.8
/usr/share/man/man8/ninfod.8
/usr/share/man/man8/ping.8
/usr/share/man/man8/rarpd.8
/usr/share/man/man8/rdisc.8
/usr/share/man/man8/tftpd.8
/usr/share/man/man8/tracepath.8
/usr/share/man/man8/traceroute6.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/ninfod.service
/usr/lib/systemd/system/rarpd@.service
/usr/lib/systemd/system/rdisc.service

%files setuid
%defattr(-,root,root,-)
%attr(4755, root, root) /usr/bin/ping
%attr(4755, root, root) /usr/bin/traceroute6

%files locales -f iputils.lang
%defattr(-,root,root,-)

