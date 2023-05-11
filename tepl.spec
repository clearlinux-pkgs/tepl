#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
#
Name     : tepl
Version  : 6.4.0
Release  : 17
URL      : https://download.gnome.org/sources/tepl/6.4/tepl-6.4.0.tar.xz
Source0  : https://download.gnome.org/sources/tepl/6.4/tepl-6.4.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-3.0
Requires: tepl-data = %{version}-%{release}
Requires: tepl-lib = %{version}-%{release}
Requires: tepl-license = %{version}-%{release}
Requires: tepl-locales = %{version}-%{release}
BuildRequires : amtk-dev
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : docbook-xml
BuildRequires : gtksourceview-dev
BuildRequires : pkgconfig(amtk-5)
BuildRequires : pkgconfig(gtksourceview-4)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Tepl - Text editor product line
===============================
Tepl is a library that eases the development of GtkSourceView-based text
editors and IDEs.

%package data
Summary: data components for the tepl package.
Group: Data

%description data
data components for the tepl package.


%package dev
Summary: dev components for the tepl package.
Group: Development
Requires: tepl-lib = %{version}-%{release}
Requires: tepl-data = %{version}-%{release}
Provides: tepl-devel = %{version}-%{release}
Requires: tepl = %{version}-%{release}

%description dev
dev components for the tepl package.


%package doc
Summary: doc components for the tepl package.
Group: Documentation

%description doc
doc components for the tepl package.


%package lib
Summary: lib components for the tepl package.
Group: Libraries
Requires: tepl-data = %{version}-%{release}
Requires: tepl-license = %{version}-%{release}

%description lib
lib components for the tepl package.


%package license
Summary: license components for the tepl package.
Group: Default

%description license
license components for the tepl package.


%package locales
Summary: locales components for the tepl package.
Group: Default

%description locales
locales components for the tepl package.


%prep
%setup -q -n tepl-6.4.0
cd %{_builddir}/tepl-6.4.0
pushd ..
cp -a tepl-6.4.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1683820794
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -O3" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs || :

%install
mkdir -p %{buildroot}/usr/share/package-licenses/tepl
cp %{_builddir}/tepl-%{version}/LICENSES/LGPL-3.0-or-later.txt %{buildroot}/usr/share/package-licenses/tepl/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang tepl-6
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Tepl-6.typelib
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/V3/usr/lib64/libtepl-6.so
/usr/include/tepl-6/tepl/tepl-abstract-factory.h
/usr/include/tepl-6/tepl/tepl-application-window.h
/usr/include/tepl-6/tepl/tepl-application.h
/usr/include/tepl-6/tepl/tepl-buffer.h
/usr/include/tepl-6/tepl/tepl-encoding-iconv.h
/usr/include/tepl-6/tepl/tepl-encoding.h
/usr/include/tepl-6/tepl/tepl-enum-types.h
/usr/include/tepl-6/tepl/tepl-file-chooser.h
/usr/include/tepl-6/tepl/tepl-file-loader.h
/usr/include/tepl-6/tepl/tepl-file-saver.h
/usr/include/tepl-6/tepl/tepl-file.h
/usr/include/tepl-6/tepl/tepl-fold-region.h
/usr/include/tepl-6/tepl/tepl-goto-line-bar.h
/usr/include/tepl-6/tepl/tepl-gutter-renderer-folds.h
/usr/include/tepl-6/tepl/tepl-info-bar.h
/usr/include/tepl-6/tepl/tepl-init.h
/usr/include/tepl-6/tepl/tepl-io-error-info-bars.h
/usr/include/tepl-6/tepl/tepl-iter.h
/usr/include/tepl-6/tepl/tepl-language-chooser-dialog.h
/usr/include/tepl-6/tepl/tepl-language-chooser-widget.h
/usr/include/tepl-6/tepl/tepl-language-chooser.h
/usr/include/tepl-6/tepl/tepl-line-column-indicator.h
/usr/include/tepl-6/tepl/tepl-macros.h
/usr/include/tepl-6/tepl/tepl-menu-shell.h
/usr/include/tepl-6/tepl/tepl-metadata-manager.h
/usr/include/tepl-6/tepl/tepl-metadata.h
/usr/include/tepl-6/tepl/tepl-notebook.h
/usr/include/tepl-6/tepl/tepl-overwrite-indicator.h
/usr/include/tepl-6/tepl/tepl-panel.h
/usr/include/tepl-6/tepl/tepl-pango.h
/usr/include/tepl-6/tepl/tepl-prefs-dialog.h
/usr/include/tepl-6/tepl/tepl-prefs.h
/usr/include/tepl-6/tepl/tepl-progress-info-bar.h
/usr/include/tepl-6/tepl/tepl-settings.h
/usr/include/tepl-6/tepl/tepl-signal-group.h
/usr/include/tepl-6/tepl/tepl-space-drawer-prefs.h
/usr/include/tepl-6/tepl/tepl-statusbar.h
/usr/include/tepl-6/tepl/tepl-style-scheme-chooser-widget.h
/usr/include/tepl-6/tepl/tepl-tab-group.h
/usr/include/tepl-6/tepl/tepl-tab-label.h
/usr/include/tepl-6/tepl/tepl-tab-loading.h
/usr/include/tepl-6/tepl/tepl-tab-saving.h
/usr/include/tepl-6/tepl/tepl-tab.h
/usr/include/tepl-6/tepl/tepl-utils.h
/usr/include/tepl-6/tepl/tepl-view.h
/usr/include/tepl-6/tepl/tepl-widget-list-category.h
/usr/include/tepl-6/tepl/tepl-widget-list-item.h
/usr/include/tepl-6/tepl/tepl.h
/usr/lib64/libtepl-6.so
/usr/lib64/pkgconfig/tepl-6.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/tepl-6/TeplAbstractFactory.html
/usr/share/gtk-doc/html/tepl-6/TeplApplication.html
/usr/share/gtk-doc/html/tepl-6/TeplApplicationWindow.html
/usr/share/gtk-doc/html/tepl-6/TeplBuffer.html
/usr/share/gtk-doc/html/tepl-6/TeplFile.html
/usr/share/gtk-doc/html/tepl-6/TeplFileLoader.html
/usr/share/gtk-doc/html/tepl-6/TeplFileSaver.html
/usr/share/gtk-doc/html/tepl-6/TeplFoldRegion.html
/usr/share/gtk-doc/html/tepl-6/TeplGotoLineBar.html
/usr/share/gtk-doc/html/tepl-6/TeplGutterRendererFolds.html
/usr/share/gtk-doc/html/tepl-6/TeplInfoBar.html
/usr/share/gtk-doc/html/tepl-6/TeplLanguageChooser.html
/usr/share/gtk-doc/html/tepl-6/TeplLanguageChooserDialog.html
/usr/share/gtk-doc/html/tepl-6/TeplLanguageChooserWidget.html
/usr/share/gtk-doc/html/tepl-6/TeplLineColumnIndicator.html
/usr/share/gtk-doc/html/tepl-6/TeplMetadata.html
/usr/share/gtk-doc/html/tepl-6/TeplMetadataManager.html
/usr/share/gtk-doc/html/tepl-6/TeplNotebook.html
/usr/share/gtk-doc/html/tepl-6/TeplOverwriteIndicator.html
/usr/share/gtk-doc/html/tepl-6/TeplPanel.html
/usr/share/gtk-doc/html/tepl-6/TeplPrefsDialog.html
/usr/share/gtk-doc/html/tepl-6/TeplProgressInfoBar.html
/usr/share/gtk-doc/html/tepl-6/TeplSettings.html
/usr/share/gtk-doc/html/tepl-6/TeplSpaceDrawerPrefs.html
/usr/share/gtk-doc/html/tepl-6/TeplStatusbar.html
/usr/share/gtk-doc/html/tepl-6/TeplStyleSchemeChooserWidget.html
/usr/share/gtk-doc/html/tepl-6/TeplTab.html
/usr/share/gtk-doc/html/tepl-6/TeplTabGroup.html
/usr/share/gtk-doc/html/tepl-6/TeplTabLabel.html
/usr/share/gtk-doc/html/tepl-6/TeplView.html
/usr/share/gtk-doc/html/tepl-6/annexes.html
/usr/share/gtk-doc/html/tepl-6/annotation-glossary.html
/usr/share/gtk-doc/html/tepl-6/api-breaks-1-to-2.html
/usr/share/gtk-doc/html/tepl-6/api-breaks-2-to-3-amtk.html
/usr/share/gtk-doc/html/tepl-6/api-breaks-2-to-3-tepl.html
/usr/share/gtk-doc/html/tepl-6/api-breaks-3-to-4-tepl.html
/usr/share/gtk-doc/html/tepl-6/api-breaks-4-to-5-tepl.html
/usr/share/gtk-doc/html/tepl-6/api-breaks-5-to-6-tepl.html
/usr/share/gtk-doc/html/tepl-6/api-breaks-during-tepl-6.html
/usr/share/gtk-doc/html/tepl-6/api-breaks.html
/usr/share/gtk-doc/html/tepl-6/api-index-1-0.html
/usr/share/gtk-doc/html/tepl-6/api-index-2-0.html
/usr/share/gtk-doc/html/tepl-6/api-index-3-0.html
/usr/share/gtk-doc/html/tepl-6/api-index-4-0.html
/usr/share/gtk-doc/html/tepl-6/api-index-4-4.html
/usr/share/gtk-doc/html/tepl-6/api-index-5-0.html
/usr/share/gtk-doc/html/tepl-6/api-index-6-0.html
/usr/share/gtk-doc/html/tepl-6/api-index-6-2.html
/usr/share/gtk-doc/html/tepl-6/api-index-6-4.html
/usr/share/gtk-doc/html/tepl-6/api-index-deprecated.html
/usr/share/gtk-doc/html/tepl-6/api-index-full.html
/usr/share/gtk-doc/html/tepl-6/api-reference-general-utilities.html
/usr/share/gtk-doc/html/tepl-6/api-reference-text-editor-support.html
/usr/share/gtk-doc/html/tepl-6/code-folding.html
/usr/share/gtk-doc/html/tepl-6/file-loading-and-saving.html
/usr/share/gtk-doc/html/tepl-6/framework.html
/usr/share/gtk-doc/html/tepl-6/general.html
/usr/share/gtk-doc/html/tepl-6/gio-extras-file-metadata.html
/usr/share/gtk-doc/html/tepl-6/gobject-extras.html
/usr/share/gtk-doc/html/tepl-6/gtk-extras-info-bars.html
/usr/share/gtk-doc/html/tepl-6/gtk-extras-other.html
/usr/share/gtk-doc/html/tepl-6/home.png
/usr/share/gtk-doc/html/tepl-6/index.html
/usr/share/gtk-doc/html/tepl-6/intro.html
/usr/share/gtk-doc/html/tepl-6/language-choosers.html
/usr/share/gtk-doc/html/tepl-6/left-insensitive.png
/usr/share/gtk-doc/html/tepl-6/left.png
/usr/share/gtk-doc/html/tepl-6/menus-and-toolbars.html
/usr/share/gtk-doc/html/tepl-6/misc.html
/usr/share/gtk-doc/html/tepl-6/object-tree.html
/usr/share/gtk-doc/html/tepl-6/other-extras.html
/usr/share/gtk-doc/html/tepl-6/right-insensitive.png
/usr/share/gtk-doc/html/tepl-6/right.png
/usr/share/gtk-doc/html/tepl-6/style.css
/usr/share/gtk-doc/html/tepl-6/tepl-6-IO-error-info-bars.html
/usr/share/gtk-doc/html/tepl-6/tepl-6-Tepl-Initialization-and-Finalization.html
/usr/share/gtk-doc/html/tepl-6/tepl-6-TeplEncoding.html
/usr/share/gtk-doc/html/tepl-6/tepl-6-TeplEncodingIconv.html
/usr/share/gtk-doc/html/tepl-6/tepl-6-TeplFileChooser.html
/usr/share/gtk-doc/html/tepl-6/tepl-6-TeplIter.html
/usr/share/gtk-doc/html/tepl-6/tepl-6-TeplMenuShell.html
/usr/share/gtk-doc/html/tepl-6/tepl-6-TeplPango.html
/usr/share/gtk-doc/html/tepl-6/tepl-6-TeplPrefs.html
/usr/share/gtk-doc/html/tepl-6/tepl-6-TeplSignalGroup.html
/usr/share/gtk-doc/html/tepl-6/tepl-6-TeplUtils.html
/usr/share/gtk-doc/html/tepl-6/tepl-6-TeplWidgetListCategory.html
/usr/share/gtk-doc/html/tepl-6/tepl-6-TeplWidgetListItem.html
/usr/share/gtk-doc/html/tepl-6/tepl-6.devhelp2
/usr/share/gtk-doc/html/tepl-6/up-insensitive.png
/usr/share/gtk-doc/html/tepl-6/up.png

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libtepl-6.so.2
/usr/lib64/libtepl-6.so.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/tepl/757b86330df80f81143d5916b3e92b4bcb1b1890

%files locales -f tepl-6.lang
%defattr(-,root,root,-)

