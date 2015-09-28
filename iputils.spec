Name:           iputils
Version:        s20121221
Release:        10
License:        GPL-2.0+
Summary:        Network monitoring tools
Url:            http://www.skbuff.net/iputils
Group:          console/network
Source0:        http://www.skbuff.net/iputils/%{name}-%{version}.tar.bz2
Patch0:         fix-build-command-line-argument-with-gnutls.patch
BuildRequires:  attr-dev
BuildRequires:  libcap-dev
BuildRequires:  openssl-dev
BuildRequires:  pkgconfig(zlib)

%description
Network monitoring tools.

%prep
%setup -q
%patch0 -p1

%build
make %{?_smp_mflags} all USE_GNUTLS=no

%install
install -m 0755 -d %{buildroot}/bin
#install -m 0755 -d %{buildroot}/%{_mandir}/man8
# SUID root programs
install -m 4555 ping %{buildroot}/bin/ping
install -m 4555 ping6 %{buildroot}/bin/ping6
install -m 4555 traceroute6 %{buildroot}/bin/
# Other programs
for i in arping tracepath tracepath6; do
  install -m 0755 $i %{buildroot}/bin/
done
# Manual pages for things we build packages for
#for i in tracepath.8 traceroute6.8 ping.8 arping.8; do
#  install -m 0644 doc/$i %{buildroot}/%{_mandir}/man8/ || true
#done

%files
/bin/ping
/bin/ping6
/bin/arping
/bin/tracepath
/bin/tracepath6
/bin/traceroute6
