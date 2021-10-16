#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kget
Version  : 21.08.2
Release  : 33
URL      : https://download.kde.org/stable/release-service/21.08.2/src/kget-21.08.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/21.08.2/src/kget-21.08.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/21.08.2/src/kget-21.08.2.tar.xz.sig
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
BuildRequires : gpgme-dev
BuildRequires : gpgme-dev gpgme-extras
BuildRequires : knotifyconfig-dev
BuildRequires : plasma-workspace-dev
BuildRequires : qca-qt5-dev
BuildRequires : sqlite-autoconf-dev

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
%setup -q -n kget-21.08.2
cd %{_builddir}/kget-21.08.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1634413934
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1634413934
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kget
cp %{_builddir}/kget-21.08.2/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kget/29fb05b49e12a380545499938c4879440bd8851e
cp %{_builddir}/kget-21.08.2/COPYING %{buildroot}/usr/share/package-licenses/kget/3860f7708aae6a8ddfe8483263b2a5f29b83c975
cp %{_builddir}/kget-21.08.2/COPYING.DOC %{buildroot}/usr/share/package-licenses/kget/bd75d59f9d7d9731bfabdc48ecd19e704d218e38
cp %{_builddir}/kget-21.08.2/COPYING.LIB %{buildroot}/usr/share/package-licenses/kget/9a1929f4700d2407c70b507b3b2aaf6226a9543c
cp %{_builddir}/kget-21.08.2/cmake/modules/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/kget/ff3ed70db4739b3c6747c7f624fe2bad70802987
pushd clr-build
%make_install
popd
%find_lang kget
%find_lang kgetplugin
%find_lang plasma_applet_kget
%find_lang plasma_runner_kget

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kget

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kget.desktop
/usr/share/config.kcfg/kget.kcfg
/usr/share/config.kcfg/kget_checksumsearchfactory.kcfg
/usr/share/config.kcfg/kget_mirrorsearchfactory.kcfg
/usr/share/config.kcfg/kget_multisegkiofactory.kcfg
/usr/share/dbus-1/services/org.kde.kget.service
/usr/share/dolphinpart/kpartplugins/kget_plug_in.desktop
/usr/share/dolphinpart/kpartplugins/kget_plug_in.rc
/usr/share/icons/hicolor/128x128/apps/kget.png
/usr/share/icons/hicolor/16x16/apps/kget.png
/usr/share/icons/hicolor/22x22/apps/kget.png
/usr/share/icons/hicolor/32x32/apps/kget.png
/usr/share/icons/hicolor/48x48/apps/kget.png
/usr/share/icons/hicolor/64x64/apps/kget.png
/usr/share/kconf_update/kget.upd
/usr/share/kconf_update/kget_limitdownloads.pl
/usr/share/kconf_update/kget_sensitive.pl
/usr/share/kget/pics/kget_splash.png
/usr/share/khtml/kpartplugins/kget_plug_in.desktop
/usr/share/khtml/kpartplugins/kget_plug_in.rc
/usr/share/knotifications5/kget.notifyrc
/usr/share/kservices5/ServiceMenus/kget_download.desktop
/usr/share/kservices5/kget_checksumsearchfactory_config.desktop
/usr/share/kservices5/kget_metalinkfactory_config.desktop
/usr/share/kservices5/kget_mirrorsearchfactory_config.desktop
/usr/share/kservices5/kget_multisegkiofactory_config.desktop
/usr/share/kservicetypes5/kget_plugin.desktop
/usr/share/kwebkitpart/kpartplugins/kget_plug_in.desktop
/usr/share/kwebkitpart/kpartplugins/kget_plug_in.rc
/usr/share/kxmlgui5/kget/kgetui.rc
/usr/share/metainfo/org.kde.kget.appdata.xml
/usr/share/qlogging-categories5/kget.categories

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
/usr/share/doc/HTML/sr/kget/index.cache.bz2
/usr/share/doc/HTML/sr/kget/index.docbook
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
/usr/lib64/libkgetcore.so.5
/usr/lib64/libkgetcore.so.5.0.0
/usr/lib64/qt5/plugins/kcm_kget_checksumsearchfactory.so
/usr/lib64/qt5/plugins/kcm_kget_metalinkfactory.so
/usr/lib64/qt5/plugins/kcm_kget_mirrorsearchfactory.so
/usr/lib64/qt5/plugins/kcm_kget_multisegkiofactory.so
/usr/lib64/qt5/plugins/kget/kget_checksumsearchfactory.so
/usr/lib64/qt5/plugins/kget/kget_kio.so
/usr/lib64/qt5/plugins/kget/kget_metalinkfactory.so
/usr/lib64/qt5/plugins/kget/kget_mirrorsearchfactory.so
/usr/lib64/qt5/plugins/kget/kget_multisegkiofactory.so
/usr/lib64/qt5/plugins/kget_browser_integration.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kget/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/kget/3860f7708aae6a8ddfe8483263b2a5f29b83c975
/usr/share/package-licenses/kget/9a1929f4700d2407c70b507b3b2aaf6226a9543c
/usr/share/package-licenses/kget/bd75d59f9d7d9731bfabdc48ecd19e704d218e38
/usr/share/package-licenses/kget/ff3ed70db4739b3c6747c7f624fe2bad70802987

%files locales -f kget.lang -f kgetplugin.lang -f plasma_applet_kget.lang -f plasma_runner_kget.lang
%defattr(-,root,root,-)

