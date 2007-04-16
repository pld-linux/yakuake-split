Summary:	Very powerful Quake style Konsole
Summary(de.UTF-8):	Ein Quake ähnlicher Konsole Emulator
Summary(pl.UTF-8):	Rozbudowany emulator terminala w stylu Quake
Name:		yakuake-split
Version:	2.8.1.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://kde-apps.org/CONTENT/content-files/56234-yakuake-%{version}.tar.gz
# Source0-md5:	c7fe650a593bba1808034102ab07f38e
Patch0:		kde-ac260.patch
Patch1:		kde-ac260-lt.patch
Patch2:		kde-am.patch
Patch3:		yakuake-desktop.patch
URL:		http://www.kde-apps.org/content/show.php/yakuake-split?content=56234
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
Obsoletes:	yakuake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A KDE konsole which looks like those found in Quake.

%description -l de.UTF-8
Eine KDE Konsole die der aus Quake ähnelt.

%description -l pl.UTF-8
Konsola KDE wyglądem przypominająca konsolę komend z gry Quake.

%prep
%setup -q -n yakuake-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs
%configure \
%if "%{_lib}" == "lib64"
        --enable-libsuffix=64 \
%endif
        --%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
        --with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT%{_desktopdir}

install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT{%{_datadir}/applnk/Utilities,%{_desktopdir}}/yakuake.desktop

#%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS 
%attr(755,root,root) %{_bindir}/yakuake
%{_desktopdir}/*.desktop
%dir %{_datadir}/apps/yakuake
%dir %{_datadir}/apps/yakuake/default
%{_datadir}/apps/yakuake/default/tabs.skin
%dir %{_datadir}/apps/yakuake/default/tabs
%{_datadir}/apps/yakuake/default/tabs/*.png
%{_datadir}/apps/yakuake/default/title.skin
%dir %{_datadir}/apps/yakuake/default/title
%{_datadir}/apps/yakuake/default/title/*.png
%{_datadir}/apps/yakuake/default/install.sh
%{_datadir}/apps/yakuake/default/manual.readme
%{_iconsdir}/hicolor/*x*/apps/yakuake.png
