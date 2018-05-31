Name:           iputils
Version:        s20151218
Release:        22
License:        GPL-2.0+
Summary:        Network monitoring tools
Url:            http://www.skbuff.net/iputils
Group:          console/network
Source0:        http://www.skbuff.net/iputils/iputils-s20151218.tar.bz2
BuildRequires:  attr-dev
BuildRequires:  libcap-dev
BuildRequires:  openssl-dev
BuildRequires:  pkgconfig(zlib)

Patch1: cflags.patch

%description
Network monitoring tools.

%prep
%setup -q
%patch1 -p1

%build
export CFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used -fPIE "
make %{?_smp_mflags} all USE_GNUTLS=no USE_GCRYPT=no 

%install
install -m 0755 -d %{buildroot}/usr/bin
#install -m 0755 -d %{buildroot}/%{_mandir}/man8
# SUID root programs
install -m 4555 ping %{buildroot}/usr/bin/ping
install -m 4555 ping6 %{buildroot}/usr/bin/ping6
install -m 4555 traceroute6 %{buildroot}/usr/bin/
# Other programs
for i in arping tracepath tracepath6; do
  install -m 0755 $i %{buildroot}/usr/bin/
done
# Manual pages for things we build packages for
#for i in tracepath.8 traceroute6.8 ping.8 arping.8; do
#  install -m 0644 doc/$i %{buildroot}/%{_mandir}/man8/ || true
#done

%files
/usr/bin/ping
/usr/bin/ping6
/usr/bin/arping
/usr/bin/tracepath
/usr/bin/tracepath6
/usr/bin/traceroute6
