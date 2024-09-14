%define url_ver %(echo %{version}|cut -d. -f1,2)
%define _disable_rebuild_configure 1

Summary:	Color management tools for GNOME
Name:		gnome-color-manager
Version:	3.36.0
Release:	11
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		https://projects.gnome.org/gnome-color-manager/
Source0:	https://ftp.gnome.org/pub/GNOME/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	desktop-file-utils
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	docbook-utils
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	pkgconfig(clutter-gtk-1.0)
BuildRequires:	pkgconfig(colord)
BuildRequires:	pkgconfig(colord-gtk)
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnome-desktop-3.0)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(libcanberra-gtk3)
BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(vte-2.91)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xrandr)
#BuildRequires:	pkgconfig(mash-0.2)
BuildRequires:	libxml2-utils
BuildRequires:	yelp-tools
BuildRequires:	gnome-common
BuildRequires:	meson

Requires:	colord
Requires:	gnome-icon-theme
Requires:	shared-color-profiles

%description
gnome-color-manager is a session framework that makes it easy to manage,
install and generate color profiles in the GNOME desktop.

%prep
%setup -q
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name --with-gnome --all-name

for file in %{buildroot}%{_datadir}/applications/*.desktop; do
	desktop-file-edit "$file"
done

%files -f %{name}.lang
%doc AUTHORS README
%{_bindir}/gcm-*
#%{_libexecdir}/gcm-helper-exiv
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
#{_datadir}/appdata/gcm-viewer.appdata.xml
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/scalable/*/*.svg
%{_datadir}/metainfo/*.appdata.xml
%{_mandir}/man1/*

