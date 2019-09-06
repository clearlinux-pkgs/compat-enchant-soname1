#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : compat-enchant-soname1
Version  : 1.6.1
Release  : 5
URL      : https://github.com/AbiWord/enchant/releases/download/enchant-1-6-1/enchant-1.6.1.tar.gz
Source0  : https://github.com/AbiWord/enchant/releases/download/enchant-1-6-1/enchant-1.6.1.tar.gz
Summary  : An Enchanting Spell Checking Library
Group    : Development/Tools
License  : LGPL-2.1
Requires: compat-enchant-soname1-bin = %{version}-%{release}
Requires: compat-enchant-soname1-lib = %{version}-%{release}
Requires: compat-enchant-soname1-license = %{version}-%{release}
Requires: compat-enchant-soname1-man = %{version}-%{release}
BuildRequires : aspell-dev
BuildRequires : hunspell-dev
BuildRequires : pkgconfig(dbus-glib-1)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gmodule-2.0)
BuildRequires : pkgconfig(hunspell)
# Suppress generation of debuginfo
%global debug_package %{nil}

%description
A library that wraps other spell checking backends.

%package bin
Summary: bin components for the compat-enchant-soname1 package.
Group: Binaries
Requires: compat-enchant-soname1-license = %{version}-%{release}

%description bin
bin components for the compat-enchant-soname1 package.


%package dev
Summary: dev components for the compat-enchant-soname1 package.
Group: Development
Requires: compat-enchant-soname1-lib = %{version}-%{release}
Requires: compat-enchant-soname1-bin = %{version}-%{release}
Provides: compat-enchant-soname1-devel = %{version}-%{release}
Requires: compat-enchant-soname1 = %{version}-%{release}

%description dev
dev components for the compat-enchant-soname1 package.


%package lib
Summary: lib components for the compat-enchant-soname1 package.
Group: Libraries
Requires: compat-enchant-soname1-license = %{version}-%{release}

%description lib
lib components for the compat-enchant-soname1 package.


%package license
Summary: license components for the compat-enchant-soname1 package.
Group: Default

%description license
license components for the compat-enchant-soname1 package.


%package man
Summary: man components for the compat-enchant-soname1 package.
Group: Default

%description man
man components for the compat-enchant-soname1 package.


%prep
%setup -q -n enchant-1.6.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1567808163
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1567808163
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/compat-enchant-soname1
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/compat-enchant-soname1/COPYING.LIB
%make_install
## Remove excluded files
rm -f %{buildroot}/usr/share/enchant/enchant.ordering

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/enchant
/usr/bin/enchant-lsmod

%files dev
%defattr(-,root,root,-)
/usr/include/enchant/enchant++.h
/usr/include/enchant/enchant-provider.h
/usr/include/enchant/enchant.h
/usr/lib64/libenchant.so
/usr/lib64/pkgconfig/enchant.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/enchant/libenchant_aspell.so
/usr/lib64/enchant/libenchant_ispell.so
/usr/lib64/enchant/libenchant_myspell.so
/usr/lib64/enchant/libenchant_zemberek.so
/usr/lib64/libenchant.so.1
/usr/lib64/libenchant.so.1.6.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/compat-enchant-soname1/COPYING.LIB

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/enchant.1
