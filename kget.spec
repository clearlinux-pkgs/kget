#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: 5424026
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kget
Version  : 24.12.0
Release  : 80
URL      : https://download.kde.org/stable/release-service/24.12.0/src/kget-24.12.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.12.0/src/kget-24.12.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.12.0/src/kget-24.12.0.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.2 GPL-2.0 LGPL-2.1
Requires: kget-bin = %{version}-%{release}
Requires: kget-data = %{version}-%{release}
Requires: kget-lib = %{version}-%{release}
Requires: kget-license = %{version}-%{release}
Requires: kget-locales = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : gpgme-dev
BuildRequires : gpgme-extras
BuildRequires : kconfig-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kcrash-dev
BuildRequires : kdbusaddons-dev
BuildRequires : ki18n-dev
BuildRequires : kio-dev
BuildRequires : knotifications-dev
BuildRequires : knotifyconfig-dev
BuildRequires : kstatusnotifieritem-dev
BuildRequires : kwallet-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
KGet is included in the kdenetwork module.
If you just want to install KGet alone, please read
the instructions below.

%package bin
Summary: bin components for the kget package.
Group: Binaries
Requires: kget-data = %{version}-%{release}
Requires: kget-license = %{version}-%{release}

%description bin
bin components for the kget package.


%package data
Summary: data components for the kget package.
Group: Data

%description data
data components for the kget package.


%package dev
Summary: dev components for the kget package.
Group: Development
Requires: kget-lib = %{version}-%{release}
Requires: kget-bin = %{version}-%{release}
Requires: kget-data = %{version}-%{release}
Provides: kget-devel = %{version}-%{release}
Requires: kget = %{version}-%{release}

%description dev
dev components for the kget package.


%package doc
Summary: doc components for the kget package.
Group: Documentation

%description doc
doc components for the kget package.


%package lib
Summary: lib components for the kget package.
Group: Libraries
Requires: kget-data = %{version}-%{release}
Requires: kget-license = %{version}-%{release}

%description lib
lib components for the kget package.


%package license
Summary: license components for the kget package.
Group: Default

%description license
license components for the kget package.


%package locales
Summary: locales components for the kget package.
Group: Default

%description locales
locales components for the kget package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n kget-24.12.0
cd %{_builddir}/kget-24.12.0
pushd ..
cp -a kget-24.12.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1735261374
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1735261374
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kget
cp %{_builddir}/kget-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kget/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/kget-%{version}/COPYING %{buildroot}/usr/share/package-licenses/kget/3860f7708aae6a8ddfe8483263b2a5f29b83c975 || :
cp %{_builddir}/kget-%{version}/COPYING.DOC %{buildroot}/usr/share/package-licenses/kget/bd75d59f9d7d9731bfabdc48ecd19e704d218e38 || :
cp %{_builddir}/kget-%{version}/COPYING.LIB %{buildroot}/usr/share/package-licenses/kget/9a1929f4700d2407c70b507b3b2aaf6226a9543c || :
cp %{_builddir}/kget-%{version}/cmake/modules/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/kget/ff3ed70db4739b3c6747c7f624fe2bad70802987 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang kget
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kget
/usr/bin/kget

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kget.desktop
/usr/share/config.kcfg/kget.kcfg
/usr/share/config.kcfg/kget_checksumsearchfactory.kcfg
/usr/share/config.kcfg/kget_mirrorsearchfactory.kcfg
/usr/share/config.kcfg/kget_multisegkiofactory.kcfg
/usr/share/dbus-1/services/org.kde.kget.service
/usr/share/icons/hicolor/128x128/apps/kget.png
/usr/share/icons/hicolor/16x16/apps/kget.png
/usr/share/icons/hicolor/22x22/apps/kget.png
/usr/share/icons/hicolor/32x32/apps/kget.png
/usr/share/icons/hicolor/48x48/apps/kget.png
/usr/share/icons/hicolor/64x64/apps/kget.png
/usr/share/kget/pics/kget_splash.png
/usr/share/kio/servicemenus/kget_download.desktop
/usr/share/knotifications6/kget.notifyrc
/usr/share/metainfo/org.kde.kget.appdata.xml
/usr/share/qlogging-categories6/kget.categories

%files dev
%defattr(-,root,root,-)
/usr/lib64/libkgetcore.so

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kget/index.cache.bz2
/usr/share/doc/HTML/ca/kget/index.docbook
/usr/share/doc/HTML/cs/kget/index.cache.bz2
/usr/share/doc/HTML/cs/kget/index.docbook
/usr/share/doc/HTML/de/kget/index.cache.bz2
/usr/share/doc/HTML/de/kget/index.docbook
/usr/share/doc/HTML/de/kget/kget_Advanced.png
/usr/share/doc/HTML/de/kget/kget_Appearance.png
/usr/share/doc/HTML/de/kget/kget_Network.png
/usr/share/doc/HTML/de/kget/kget_Web_Interface.png
/usr/share/doc/HTML/de/kget/kget_drop_target.png
/usr/share/doc/HTML/de/kget/kget_groups.png
/usr/share/doc/HTML/de/kget/kget_plugins.png
/usr/share/doc/HTML/de/kget/kget_verification.png
/usr/share/doc/HTML/en/kget/file.png
/usr/share/doc/HTML/en/kget/import_link.png
/usr/share/doc/HTML/en/kget/index.cache.bz2
/usr/share/doc/HTML/en/kget/index.docbook
/usr/share/doc/HTML/en/kget/kget_Advanced.png
/usr/share/doc/HTML/en/kget/kget_Appearance.png
/usr/share/doc/HTML/en/kget/kget_Network.png
/usr/share/doc/HTML/en/kget/kget_Web_Interface.png
/usr/share/doc/HTML/en/kget/kget_drop_target.png
/usr/share/doc/HTML/en/kget/kget_group.png
/usr/share/doc/HTML/en/kget/kget_groups.png
/usr/share/doc/HTML/en/kget/kget_plugins.png
/usr/share/doc/HTML/en/kget/kget_transfer_hostory.png
/usr/share/doc/HTML/en/kget/kget_verification.png
/usr/share/doc/HTML/en/kget/metalink0.png
/usr/share/doc/HTML/en/kget/metalink1.png
/usr/share/doc/HTML/en/kget/metalink2.png
/usr/share/doc/HTML/en/kget/metalink3.png
/usr/share/doc/HTML/en/kget/pluginsettings.png
/usr/share/doc/HTML/es/kget/file.png
/usr/share/doc/HTML/es/kget/import_link.png
/usr/share/doc/HTML/es/kget/index.cache.bz2
/usr/share/doc/HTML/es/kget/index.docbook
/usr/share/doc/HTML/es/kget/kget_Advanced.png
/usr/share/doc/HTML/es/kget/kget_Appearance.png
/usr/share/doc/HTML/es/kget/kget_Network.png
/usr/share/doc/HTML/es/kget/kget_Web_Interface.png
/usr/share/doc/HTML/es/kget/kget_drop_target.png
/usr/share/doc/HTML/es/kget/kget_group.png
/usr/share/doc/HTML/es/kget/kget_groups.png
/usr/share/doc/HTML/es/kget/kget_plugins.png
/usr/share/doc/HTML/es/kget/kget_transfer_hostory.png
/usr/share/doc/HTML/es/kget/kget_verification.png
/usr/share/doc/HTML/es/kget/metalink0.png
/usr/share/doc/HTML/es/kget/metalink1.png
/usr/share/doc/HTML/es/kget/metalink2.png
/usr/share/doc/HTML/es/kget/metalink3.png
/usr/share/doc/HTML/et/kget/index.cache.bz2
/usr/share/doc/HTML/et/kget/index.docbook
/usr/share/doc/HTML/fr/kget/index.cache.bz2
/usr/share/doc/HTML/fr/kget/index.docbook
/usr/share/doc/HTML/fr/kget/kget1.png
/usr/share/doc/HTML/fr/kget/kget2.png
/usr/share/doc/HTML/fr/kget/kget3.png
/usr/share/doc/HTML/fr/kget/kget4.png
/usr/share/doc/HTML/fr/kget/kget5.png
/usr/share/doc/HTML/id/kget/index.cache.bz2
/usr/share/doc/HTML/id/kget/index.docbook
/usr/share/doc/HTML/it/kget/file.png
/usr/share/doc/HTML/it/kget/import_link.png
/usr/share/doc/HTML/it/kget/index.cache.bz2
/usr/share/doc/HTML/it/kget/index.docbook
/usr/share/doc/HTML/it/kget/kget_Advanced.png
/usr/share/doc/HTML/it/kget/kget_Appearance.png
/usr/share/doc/HTML/it/kget/kget_Network.png
/usr/share/doc/HTML/it/kget/kget_Web_Interface.png
/usr/share/doc/HTML/it/kget/kget_drop_target.png
/usr/share/doc/HTML/it/kget/kget_group.png
/usr/share/doc/HTML/it/kget/kget_groups.png
/usr/share/doc/HTML/it/kget/kget_plugins.png
/usr/share/doc/HTML/it/kget/kget_transfer_hostory.png
/usr/share/doc/HTML/it/kget/kget_verification.png
/usr/share/doc/HTML/it/kget/metalink0.png
/usr/share/doc/HTML/it/kget/metalink1.png
/usr/share/doc/HTML/it/kget/metalink2.png
/usr/share/doc/HTML/it/kget/metalink3.png
/usr/share/doc/HTML/nl/kget/index.cache.bz2
/usr/share/doc/HTML/nl/kget/index.docbook
/usr/share/doc/HTML/pl/kget/index.cache.bz2
/usr/share/doc/HTML/pl/kget/index.docbook
/usr/share/doc/HTML/pl/kget/kget1.png
/usr/share/doc/HTML/pl/kget/kget2.png
/usr/share/doc/HTML/pl/kget/kget3.png
/usr/share/doc/HTML/pl/kget/kget4.png
/usr/share/doc/HTML/pl/kget/kget5.png
/usr/share/doc/HTML/pt/kget/index.cache.bz2
/usr/share/doc/HTML/pt/kget/index.docbook
/usr/share/doc/HTML/pt_BR/kget/file.png
/usr/share/doc/HTML/pt_BR/kget/import_link.png
/usr/share/doc/HTML/pt_BR/kget/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kget/index.docbook
/usr/share/doc/HTML/pt_BR/kget/kget_Advanced.png
/usr/share/doc/HTML/pt_BR/kget/kget_Appearance.png
/usr/share/doc/HTML/pt_BR/kget/kget_Network.png
/usr/share/doc/HTML/pt_BR/kget/kget_Web_Interface.png
/usr/share/doc/HTML/pt_BR/kget/kget_drop_target.png
/usr/share/doc/HTML/pt_BR/kget/kget_group.png
/usr/share/doc/HTML/pt_BR/kget/kget_groups.png
/usr/share/doc/HTML/pt_BR/kget/kget_plugins.png
/usr/share/doc/HTML/pt_BR/kget/kget_transfer_hostory.png
/usr/share/doc/HTML/pt_BR/kget/kget_verification.png
/usr/share/doc/HTML/pt_BR/kget/metalink0.png
/usr/share/doc/HTML/pt_BR/kget/metalink1.png
/usr/share/doc/HTML/pt_BR/kget/metalink2.png
/usr/share/doc/HTML/pt_BR/kget/metalink3.png
/usr/share/doc/HTML/ru/kget/file.png
/usr/share/doc/HTML/ru/kget/import_link.png
/usr/share/doc/HTML/ru/kget/index.cache.bz2
/usr/share/doc/HTML/ru/kget/index.docbook
/usr/share/doc/HTML/ru/kget/kget_Advanced.png
/usr/share/doc/HTML/ru/kget/kget_Appearance.png
/usr/share/doc/HTML/ru/kget/kget_Network.png
/usr/share/doc/HTML/ru/kget/kget_Web_Interface.png
/usr/share/doc/HTML/ru/kget/kget_drop_target.png
/usr/share/doc/HTML/ru/kget/kget_group.png
/usr/share/doc/HTML/ru/kget/kget_groups.png
/usr/share/doc/HTML/ru/kget/kget_plugins.png
/usr/share/doc/HTML/ru/kget/kget_transfer_hostory.png
/usr/share/doc/HTML/ru/kget/kget_verification.png
/usr/share/doc/HTML/ru/kget/metalink0.png
/usr/share/doc/HTML/ru/kget/metalink1.png
/usr/share/doc/HTML/ru/kget/metalink2.png
/usr/share/doc/HTML/ru/kget/metalink3.png
/usr/share/doc/HTML/sl/kget/index.cache.bz2
/usr/share/doc/HTML/sl/kget/index.docbook
/usr/share/doc/HTML/sr/kget/index.cache.bz2
/usr/share/doc/HTML/sr/kget/index.docbook
/usr/share/doc/HTML/sr@latin/kget/index.cache.bz2
/usr/share/doc/HTML/sr@latin/kget/index.docbook
/usr/share/doc/HTML/sv/kget/index.cache.bz2
/usr/share/doc/HTML/sv/kget/index.docbook
/usr/share/doc/HTML/sv/kget/kget1.png
/usr/share/doc/HTML/sv/kget/kget2.png
/usr/share/doc/HTML/sv/kget/kget3.png
/usr/share/doc/HTML/sv/kget/kget4.png
/usr/share/doc/HTML/sv/kget/kget5.png
/usr/share/doc/HTML/uk/kget/file.png
/usr/share/doc/HTML/uk/kget/import_link.png
/usr/share/doc/HTML/uk/kget/index.cache.bz2
/usr/share/doc/HTML/uk/kget/index.docbook
/usr/share/doc/HTML/uk/kget/kget_Advanced.png
/usr/share/doc/HTML/uk/kget/kget_Appearance.png
/usr/share/doc/HTML/uk/kget/kget_Network.png
/usr/share/doc/HTML/uk/kget/kget_Web_Interface.png
/usr/share/doc/HTML/uk/kget/kget_drop_target.png
/usr/share/doc/HTML/uk/kget/kget_group.png
/usr/share/doc/HTML/uk/kget/kget_groups.png
/usr/share/doc/HTML/uk/kget/kget_plugins.png
/usr/share/doc/HTML/uk/kget/kget_transfer_hostory.png
/usr/share/doc/HTML/uk/kget/kget_verification.png
/usr/share/doc/HTML/uk/kget/metalink0.png
/usr/share/doc/HTML/uk/kget/metalink1.png
/usr/share/doc/HTML/uk/kget/metalink2.png
/usr/share/doc/HTML/uk/kget/metalink3.png

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libkgetcore.so.6.0.0
/V3/usr/lib64/qt6/plugins/kget/kget_checksumsearchfactory.so
/V3/usr/lib64/qt6/plugins/kget/kget_kio.so
/V3/usr/lib64/qt6/plugins/kget/kget_metalinkfactory.so
/V3/usr/lib64/qt6/plugins/kget/kget_mirrorsearchfactory.so
/V3/usr/lib64/qt6/plugins/kget/kget_multisegkiofactory.so
/V3/usr/lib64/qt6/plugins/kget_kcms/kcm_kget_checksumsearchfactory.so
/V3/usr/lib64/qt6/plugins/kget_kcms/kcm_kget_metalinkfactory.so
/V3/usr/lib64/qt6/plugins/kget_kcms/kcm_kget_mirrorsearchfactory.so
/V3/usr/lib64/qt6/plugins/kget_kcms/kcm_kget_multisegkiofactory.so
/usr/lib64/libkgetcore.so.6
/usr/lib64/libkgetcore.so.6.0.0
/usr/lib64/qt6/plugins/kget/kget_checksumsearchfactory.so
/usr/lib64/qt6/plugins/kget/kget_kio.so
/usr/lib64/qt6/plugins/kget/kget_metalinkfactory.so
/usr/lib64/qt6/plugins/kget/kget_mirrorsearchfactory.so
/usr/lib64/qt6/plugins/kget/kget_multisegkiofactory.so
/usr/lib64/qt6/plugins/kget_kcms/kcm_kget_checksumsearchfactory.so
/usr/lib64/qt6/plugins/kget_kcms/kcm_kget_metalinkfactory.so
/usr/lib64/qt6/plugins/kget_kcms/kcm_kget_mirrorsearchfactory.so
/usr/lib64/qt6/plugins/kget_kcms/kcm_kget_multisegkiofactory.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kget/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/kget/3860f7708aae6a8ddfe8483263b2a5f29b83c975
/usr/share/package-licenses/kget/9a1929f4700d2407c70b507b3b2aaf6226a9543c
/usr/share/package-licenses/kget/bd75d59f9d7d9731bfabdc48ecd19e704d218e38
/usr/share/package-licenses/kget/ff3ed70db4739b3c6747c7f624fe2bad70802987

%files locales -f kget.lang
%defattr(-,root,root,-)

