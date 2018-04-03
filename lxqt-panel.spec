%define rel 4

Name: lxqt-panel
Version: 0.12.0
Release: %mkrel %rel
Source0: http://downloads.lxqt.org/lxqt/%{version}/%{name}-%{version}.tar.xz
# (doktor5000) add a custom panel configuration as default
Source1: panel.conf
Summary: Panel for the LXQt desktop
URL: http://lxqt.org/
License: LGPLv2+
Group: Graphical desktop/KDE
BuildRequires: cmake
# https://github.com/lxde/lxqt-panel/issues/73
#Patch1:	lxqt-panel-0.9-mga-lxqtmount-includes.patch
BuildRequires: pkgconfig(lxqt)
BuildRequires: pkgconfig(lxqt-globalkeys) >= 0.10.0
BuildRequires: pkgconfig(lxqt-globalkeys-ui) >= 0.10.0
BuildRequires: pkgconfig(lxqtmount)
BuildRequires: pkgconfig(sysstat-qt5)
BuildRequires: pkgconfig(Qt5Help)
BuildRequires: pulseaudio-devel
BuildRequires: pkgconfig(icu-uc)
BuildRequires: pkgconfig(libstatgrab)
BuildRequires: pkgconfig(libmenu-cache)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: lm_sensors-devel
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(alsa)
BuildRequires: kguiaddons-devel
BuildRequires: pkgconfig(xcb-util)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xkbcommon-x11)
BuildRequires: pkgconfig(libmenu-cache)
BuildRequires: pkgconfig(dbusmenu-qt5)
BuildRequires: solid-devel >= 5.5.0 
BuildRequires: lxqt-build-tools

Obsoletes: razorqt-panel < 0.5.3-1
# (doktor5000) require qt5 plugins as otherwise menu and tasklist misbehave and display incorrectly
Requires: kwindowsystem
Requires: lxqt-themes

Conflicts:  lxqt-common < 0.12.0

%description
Panel for the LXQt desktop.

%prep
%setup -q %{name}-%{version}
%autopatch -p1

%build
%cmake_qt5 -DPULL_TRANSLATIONS=NO
%make

%install
%make_install -C build

# fix the default menu file, we want to use new upstream lxqt menu definition (cloned from lxmenu-data)
sed -i 's|menu_file=.*|menu_file=%{_sysconfdir}/xdg/menus/lxqt-applications.menu|g' %{buildroot}/%{_sysconfdir}/xdg/lxqt/panel.conf

# (doktor5000) add a custom panel configuration as default
cp %{SOURCE1} %{buildroot}/%{_sysconfdir}/xdg/lxqt/panel.conf

%files
%{_sysconfdir}/xdg/autostart/lxqt-panel.desktop
%{_sysconfdir}/xdg/menus/lxqt-applications.menu
%{_sysconfdir}/xdg/lxqt/panel.conf
%{_bindir}/%{name}
%{_datadir}/lxqt/%{name}/
%{_datadir}/desktop-directories/lxqt-leave.directory
%{_datadir}/desktop-directories/lxqt-settings.directory
%{_includedir}/lxqt
%{_libdir}/%{name}
%{_mandir}/man1/lxqt-panel.1.*

