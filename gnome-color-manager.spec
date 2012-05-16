Summary:   Color management tools for GNOME
Name:      gnome-color-manager
Version:   3.4.2
Release:   1
License:   GPLv2+
Group:     Graphical desktop/GNOME
URL:       http://projects.gnome.org/gnome-color-manager/
Source0:   ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz

BuildRequires:	desktop-file-utils
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	docbook-utils
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	intltool
BuildRequires:	pkgconfig(clutter-gtk-1.0)
BuildRequires:	pkgconfig(colord)
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnome-desktop-3.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(libcanberra-gtk3)
BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(mash-0.2)
BuildRequires:	pkgconfig(mx-1.0)
BuildRequires:	pkgconfig(vte-2.90)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xrandr)

Requires: colord
Requires: gnome-icon-theme
Requires: shared-color-profiles

%description
gnome-color-manager is a session framework that makes it easy to manage, 
install and generate color profiles in the GNOME desktop.

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-static \
	--disable-scrollkeeper \
	--enable-packagekit

%make 

%install
%makeinstall_std

%find_lang %name --with-gnome --all-name

%files -f %{name}.lang
%doc AUTHORS NEWS README
%{_bindir}/gcm-*
%{_libexecdir}/gcm-calibrate-helper
%{_libexecdir}/gcm-helper-exiv
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/scalable/*/*.svg
%{_datadir}/man/man1/*

