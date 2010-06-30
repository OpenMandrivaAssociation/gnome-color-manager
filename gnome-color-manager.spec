%define dbus_glib_version               0.73
%define unique_version                  1.0.0

Summary:   Color management tools for GNOME
Name:      gnome-color-manager
Version:   2.30.1
Release:   %mkrel 2
License:   GPLv2+
Group:     Graphical desktop/GNOME
URL:       http://projects.gnome.org/gnome-color-manager/
Source0:   ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires:  gnome-icon-theme
Requires:  packagekit
Requires:  shared-color-profiles
Requires:  ldetect-lst >= 0.1.282

BuildRequires: gtk2-devel
BuildRequires: rarian
BuildRequires: gnome-doc-utils >= 0.3.2
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: libtool
BuildRequires: vte-devel
BuildRequires: gnome-doc-utils
BuildRequires: unique-devel >= %{unique_version}
BuildRequires: libnotify-devel
BuildRequires: libsane-devel gphoto2-devel libv4l-devel
BuildRequires: intltool
BuildRequires: libgudev-devel
BuildRequires: dbus-glib-devel >= %{dbus_glib_version}
BuildRequires: libxxf86vm-devel
BuildRequires: libxrandr-devel
BuildRequires: gnome-desktop-devel
BuildRequires: packagekit
BuildRequires: lcms-devel
BuildRequires: libcanberra-devel
BuildRequires: libtiff-devel
BuildRequires: cups-devel
BuildRequires: docbook-utils
BuildRequires: docbook-dtd41-sgml

%description
gnome-color-manager is a session framework that makes it easy to manage, 
install and generate color profiles in the GNOME desktop.

%prep
%setup -q

%build
%configure2_5x --disable-scrollkeeper --disable-schemas-install --enable-packagekit
%make 

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %name --with-gnome --all-name
for omf in %buildroot%_datadir/omf/*/*-??*.omf;do 
echo "%lang($(basename $omf|sed -e s/.*-// -e s/.omf//)) $(echo $omf|sed -e s!%buildroot!!)" >> %name.lang
done

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS README
/lib/udev/rules.d/*.rules
%{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/gcm-*
%{_sbindir}/*
%{_datadir}/gnome-color-manager
%{_datadir}/man/man1/*
%dir %{_datadir}/omf/*
%{_datadir}/omf/*/*-C.omf
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/scalable/*/*.svg*
%{_datadir}/applications/*.desktop
%config(noreplace) %{_sysconfdir}/xdg/autostart/*.desktop
%{_datadir}/dbus-1/services/org.gnome.ColorManager.service
%{_datadir}/polkit-1/actions/*.policy
