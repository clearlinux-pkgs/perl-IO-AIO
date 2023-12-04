#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-IO-AIO
Version  : 4.8
Release  : 25
URL      : https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/IO-AIO-4.8.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/IO-AIO-4.8.tar.gz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-IO-AIO-bin = %{version}-%{release}
Requires: perl-IO-AIO-license = %{version}-%{release}
Requires: perl-IO-AIO-man = %{version}-%{release}
Requires: perl-IO-AIO-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Canary::Stability)
BuildRequires : perl(common::sense)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
IO::AIO - Asynchronous/Advanced Input/Output
SYNOPSIS
use IO::AIO;
aio_open "/etc/passwd", IO::AIO::O_RDONLY, 0, sub {
my $fh = shift
or die "/etc/passwd: $!";
...
};

%package bin
Summary: bin components for the perl-IO-AIO package.
Group: Binaries
Requires: perl-IO-AIO-license = %{version}-%{release}

%description bin
bin components for the perl-IO-AIO package.


%package dev
Summary: dev components for the perl-IO-AIO package.
Group: Development
Requires: perl-IO-AIO-bin = %{version}-%{release}
Provides: perl-IO-AIO-devel = %{version}-%{release}
Requires: perl-IO-AIO = %{version}-%{release}

%description dev
dev components for the perl-IO-AIO package.


%package license
Summary: license components for the perl-IO-AIO package.
Group: Default

%description license
license components for the perl-IO-AIO package.


%package man
Summary: man components for the perl-IO-AIO package.
Group: Default

%description man
man components for the perl-IO-AIO package.


%package perl
Summary: perl components for the perl-IO-AIO package.
Group: Default
Requires: perl-IO-AIO = %{version}-%{release}

%description perl
perl components for the perl-IO-AIO package.


%prep
%setup -q -n IO-AIO-4.8
cd %{_builddir}/IO-AIO-4.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-IO-AIO
cp %{_builddir}/IO-AIO-%{version}/COPYING %{buildroot}/usr/share/package-licenses/perl-IO-AIO/9a56f3b919dfc8fced3803e165a2e38de62646e5 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/treescan

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/IO::AIO.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-IO-AIO/9a56f3b919dfc8fced3803e165a2e38de62646e5

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/treescan.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
