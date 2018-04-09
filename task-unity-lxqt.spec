Name:		task-unity-lxqt
Version:	0.1.2
Release:	34%{?dist}
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
#Requires:	lxqt-common
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
Requires: 	unity-theme-grub
Requires: 	lightdm
Requires: 	cpupower
Requires: 	volumeicon
Requires: 	xmessage
Requires: 	gpm
Requires: 	task-x11
Requires: 	dbus-x11
Requires: 	x11-driver-video
#Install wireless firmware task package
Requires:	task-wireless-firmware
Requires:	mandi
Requires: 	pulseaudio
#Needed for vbox package below
Requires:	dkms-minimal
#Requires:	vboxadditions-kernel-unity-desktop-latest
Requires:	dnfdragora-qt
Requires:	qupzilla
Requires:	os-prober
Requires:	acpid
Requires:	grub2
Requires:	grub2-common
Requires:	grub2-mageia-theme
Requires:	x11-driver-input-synaptics
Requires:	wpa_supplicant
%ifarch x86_64
Requires:	grub2-efi
%endif
Requires:	dosfstools

# We need Icons, but 32M worth?
Requires:	oxygen-icons5
Requires:	draklive-install
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
/usr/bin/systemctl enable lightdm
if [ `grep -c ^live /etc/passwd` = "0" ]; then
/usr/sbin/useradd -c 'LiveCD User' -d /home/live -p 'Unity!' -s /bin/bash live
/usr/bin/passwd -d live
mkdir -p /home/live/.config/openbox/
cp /etc/xdg/openbox/lxqt-rc.xml /home/live/.config/openbox/lxqt-rc.xml

#For SDDM if it works
#sed -i 's!\#\[Autologin\]![Autologin]!g' /etc/sddm.conf
#sed -i 's!#User=!User=live!g' /etc/sddm.conf
#sed -i 's!#Session=!Session=lxqt.desktop!g' /etc/sddm.conf

#For LightDM
sed -i 's!#autologin-user=!autologin-user=live!g' /etc/lightdm/lightdm.conf
sed -i 's!#autologin-session=!autologin-session=lxqt!g' /etc/lightdm/lightdm.conf

mkdir -p /home/live/Desktop
cp /usr/share/applications/mageia-draklive-install.desktop /home/live/Desktop/
chown -R live:live /home/live
fi

%files

%files minimal

%files live
%changelog
* Tue Apr 03 2018 Jeremiah Summers <Jeremiah.Summers@unity-linux.org> 0.1.2-34
- Use lightdm for now to replace sddm

* Mon Apr 02 2018 Jeremiah Summers <Jeremiah.Summers@unity-linux.org> 0.1.2-33
- add acpid and os-prober

* Sat Mar 03 2018 Jeremiah Summers <Jeremiah.Summers@unity-linux.org> 0.1.2-32
- add mandi as it's needed for wireless

* Sat Mar 03 2018 Jeremiah Summers <Jeremiah.Summers@unity-linux.org> 0.1.2-31
- add wpa_supplicant and synaptic Xorg driver

* Sat Mar 03 2018 Jeremiah Summers <Jeremiah.Summers@unity-linux.org> 0.1.2-30
- add back wireless driver task package

* Fri Mar 02 2018 Jeremiah Summers <Jeremiah.Summers@unity-linux.org> 0.1.2-29
- Don't require unity kernel as it's outdated at this point

* Fri Mar 02 2018 Jeremiah Summers <Jeremiah.Summers@unity-linux.org> 0.1.2-28
- Don't require wireless driver task package for now

* Tue Jan 30 2018 Jeremiah Summers <Jeremiah.Summers@unity-linux.org> 0.1.2-27
- Don't require lxqt-common

* Sat Oct 21 2017 Jeremiah Summers <Jeremiah.Summers@unity-linux.org> 0.1.2-26
- Add grub2-mageia-theme

* Sat Oct 21 2017 Jeremiah Summers <Jeremiah.Summers@unity-linux.org> 0.1.2-25
- Bump version add draklive-install

* Fri Oct 20 2017 Jeremiah Summers <Jeremiah.Summers@unity-linux.org> 0.1.2-24
- Fix typo

* Fri Oct 20 2017 Jeremiah Summers <Jeremiah.Summers@unity-linux.org> 0.1.2-23
- Attempt to auto login

* Sat Oct 14 2017 Jeremiah Summers <Jeremiah.Summers@unity-linux.org> 0.1.2-22
- Remove basesystem-uml

* Fri Oct 06 2017 Jeremiah Summers <Jeremiah.Summers@unity-linux.org> 0.1.2-21
- Pull in wireles-firmware for live package

* Fri Oct 06 2017 Jeremiah Summers <Jeremiah.Summers@unity-linux.org> 0.1.2-20
- Revert back to using Mageia grub2 but modified

* Sun Oct 01 2017 Jeremiah Summers <Jeremiah.Summers@unity-linux.org> 0.1.2-19
- Add unity-theme-grub

* Fri Sep 29 2017 Jeremiah Summers <Jeremiah.Summers@unity-linux.org> 0.1.2-18
- Add unity-grub2-pc

* Fri Sep 29 2017 Jeremiah Summers <Jeremiah.Summers@unity-linux.org> 0.1.2-17
- Only pull in efi for x86_64

* Thu Sep 28 2017 Jeremiah Summers <Jeremiah.Summers@unity-linux.org> 0.1.2-16
- Use unity-grub-efi instead of default mageia grub2 packages

* Fri Sep 08 2017 Jeremiah Summers <Jeremiah.Summers@unity-linux.org> 0.1.2-15
- Use grub-efi instead of grub2

* Thu Sep 07 2017 Jeremiah Summers <Jeremiah.Summers@unity-linux.org> 0.1.2-14
- Remove grub-efi as it conflicts with grub2

* Thu Sep 07 2017 Jeremiah Summers <Jeremiah.Summers@unity-linux.org> 0.1.2-13
- Add grub

* Thu Sep 07 2017 Jeremiah Summers <Jeremiah.Summers@unity-linux.org> 0.1.2-12
- Add Grub Requires for efi booting

* Tue Aug 29 2017 Jeremiah Summers <Jeremiah.Summers@unity-linux.org> 0.1.2-11
- Add pulseaudio

* Tue Aug 29 2017 Jeremiah Summers <Jeremiah.Summers@unity-linux.org> 0.1.2-10
- Fix home perms

* Tue Aug 29 2017 Jeremiah Summers <Jeremiah.Summers@unity-linux.org> 0.1.2-9
- Add vboxadditions-kernel-unity-desktop-latest

* Tue Aug 29 2017 Jeremiah Summers <Jeremiah.Summers@unity-linux.org> 0.1.2-8
- Copy from xdg

* Tue Aug 29 2017 Jeremiah Summers <Jeremiah.Summers@unity-linux.org> 0.1.2-7
- Require qupzilla

* Tue Aug 29 2017 Jeremiah Summers <Jeremiah.Summers@unity-linux.org> 0.1.2-6
- Copy lxqt config file to openbox config inorder to bypass start message

* Mon Aug 28 2017 Jeremiah Summers <Jeremiah.Summers@unity-linux.org> 0.1.2-5
- Symlink lxqt config file to openbox config inorder to bypass start message

* Mon Aug 28 2017 Jeremiah Summers <Jeremiah.Summers@unity-linux.org> 0.1.2-4
- Add vboxadditions-kernel-desktop-latest instead of dkms install on boot

* Mon Aug 21 2017 Jeremiah Summers <Jeremiah.Summers@unity-linux.org> 0.1.2-3
- Fix travis file add live user 

* Mon Aug 21 2017 Jeremiah Summers <Jeremiah.Summers@unity-linux.org> 0.1.2-2
- Edit tito (Jeremiah.Summers@io.com)

* Thu Aug 17 2017 JMiahMan <jmiahman@unity-linux.org> 0.1.2-1
- Implamented Tito
