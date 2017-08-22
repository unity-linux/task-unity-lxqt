Name:		task-unity-lxqt
Version:	0.1.2
Release:	1%{?dist}
Summary:	Metapackage to build a Unity-Linux LXQt install
Group:		Graphical desktop/Other
License:	GPL
URL:		http://lxqt.org/
Requires:	%{name}-live
Recommends:	task-pulseaudio
Recommends:	mageiawelcome
Requires:	lxqt-openssh-askpass
#requires system-tools-backend + liboobs
#Recommends:	lxqt-admin
Recommends:	lximage-qt
Recommends:	obconf-qt
Recommends:	qastools
Recommends:	qbittorrent
Recommends:	notepadqq	
Recommends:	qlipper
Recommends:	xarchiver
Recommends:	silicon-image-burner
Recommends:	silicon-data-disc
Recommends:	silicon-audio-disc
Recommends:	silicon-converter
Recommends:	silicon-copy-disc
Recommends:	silicon-plugin-system-tray
Recommends:	silicon-plugin-single-inner-dialog
Recommends:	xscreensaver
Recommends:	qupzilla
Recommends:	trojita
Recommends:	qpdfview
Recommends:	vlc
Recommends:	meteo-qt
#was suggested via https://bugs.mageia.org/show_bug.cgi?id=13321#c33
# but pulls in quite a lot of KDE dependencies - do we really want this?
#Recommends:	quassel

#Recommends:	scrot
#Recommends:	networkmanager-applet
#Recommends:	parcellite
#Recommends:	catfish
#Recommends:	fskbsetting
BuildArch:	noarch

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for running LXQT, the Qt port of the upcoming version of LXDE,
the Lightweight Desktop Environmen.


%package minimal
Summary:	Minimal dependencies needed for LXQt
Group:		Graphical desktop/Other
Requires:	desktop-common-data
# components listed at http://wiki.lxde.org/en/Build_LXDE-Qt_From_Source
Requires:	lxqt-globalkeys
Requires:	lxqt-notificationd
Requires:	lxqt-panel
Requires:	pcmanfm-qt
Requires:	lxqt-session
Requires:	lxqt-runner
Requires:	lxqt-qtplugin
Requires:	lxqt-policykit
Requires:	lxqt-powermanagement
Requires:	lxqt-about
Requires:	lxqt-common
Requires:	lxmenu-data
Requires:	lxqt-config
Requires:	openbox
#require at least one terminal emulator
Requires:	qterminal
Recommends:	drakx-finish-install
Recommends:	drakconf
Recommends:	fonts-ttf-dejavu
Recommends:	lxde-icon-theme

%description minimal
This package is a meta-package, meaning that its purpose is to contain
minimal dependencies for running LXQT, the Qt port of the upcoming version
of LXDE, the Lightweight Desktop Environmen.

%package live
Summary:	Minimal dependencies needed for LXQt
Group:		Graphical desktop/Other
Requires:	desktop-common-data
# components listed at http://wiki.lxde.org/en/Build_LXDE-Qt_From_Source
BuildRequires:	systemd-devel
Requires: 	%{name}-minimal
Requires: 	unity-theme
Requires: 	sddm
Requires: 	cpupower
Requires: 	volumeicon
Requires: 	basesystem-uml
Requires: 	xmessage
Requires: 	gpm
Requires: 	task-x11
Requires: 	dbus-x11
Requires: 	x11-driver-video
#Needed for vbox package below
Requires:	dkms-minimal
Requires:	dkms-vboxadditions
Requires:	dnfdragora-qt

# We need Icons, but 32M worth?
Requires:	oxygen-icons5

Requires:	drakx-finish-install
Requires:	drakconf
Requires:	alsa-utils

%description live
This package is a meta-package, meaning that its purpose is to contain
dependencies for running LXQT, the Qt port of the upcoming version
of LXDE, the Lightweight Desktop Environment in a Live Environment.
This package assures that the minimal needed packages are installed
for a viable desktop environment.

%post live
/usr/bin/systemctl set-default graphical.target
/usr/bin/systemctl enable sddm

%files

%files minimal

%files live
%changelog
* Thu Aug 17 2017 JMiahMan <jmiahman@unity-linux.org> 0.1.2-1
- Implamented Tito
