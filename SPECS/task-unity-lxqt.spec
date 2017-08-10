Name:		task-unity-lxqt
Version:	0.1.0
Release:	6%{?dist}
Summary:	Metapackage to build a Unity-Linux LXQt install
Group:		Graphical desktop/Other
License:	GPL
URL:		http://lxqt.org/
Requires:	%{name}-minimal
Recommends:	task-pulseaudio
Recommends:	mageiawelcome
Requires:	lxqt-openssh-askpass
Requires:	sddm
Requires:	mageia-theme
#requires system-tools-backend + liboobs
#Recommends:	lxqt-admin
Recommends:	lximage-qt
Recommends:	obconf-qt
Recommends:	qastools
Recommends:	qbittorrent
Recommends:     notepadqq	
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

#Recommends:	xarchiver
#Recommends:	scrot
#Recommends:	xmessage
#Recommends:	networkmanager-applet
#Recommends:	parcellite
#Recommends:	volumeicon
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
BuildRequires:	systemd-devel
Requires:	basesystem-uml
Requires:	xmessage
Requires:	gpm
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
#window manager is required to login - require openbox, suggest kwin?
Requires:	openbox
#Recommends:	kdebase4-workspace
#require at least one terminal emulator
Requires:	qterminal
Requires:	task-x11
Requires:	dbus-x11
Requires: x11-driver-video
#Needed for vbox package below
Requires: dkms-minimal
Requires:	x11-driver-video-vboxvideo
Recommends:	drakx-finish-install
Recommends:	drakconf
Recommends:	fonts-ttf-dejavu
Recommends:	lxde-icon-theme
Recommends:	oxygen-icon-theme
Obsoletes:	task-razorqt < 1-13
Obsoletes:	lxqt-appswitcher < 0.7.0-5
Obsoletes:	compton-conf < 0.1.1-1

%description minimal
This package is a meta-package, meaning that its purpose is to contain
minimal dependencies for running LXQT, the Qt port of the upcoming version
of LXDE, the Lightweight Desktop Environmen.

%post
/usr/bin/systemctl set-default graphical.target
/usr/bin/systemctl enabled sddm

%files

%files minimal
