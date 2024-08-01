Summary:	Modern Quake 1 engine based on FitzQuake
Name:		quakespasm
Version:	0.96.3
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/quakespasm/%{name}-%{version}.tar.gz
# Source0-md5:	7f345895b5739763abd4a35c2037cf86
URL:		http://quakespasm.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL2-devel
BuildRequires:	flac-devel
BuildRequires:	libmikmod-devel
BuildRequires:	libmpg123-devel
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
BuildRequires:	opusfile-devel
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Modern Quake 1 engine based on FitzQuake.

%prep
%setup -q

%build
cd Quake
%{__make} \
	CC="%{__cc}" \
	CPUFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}" \
	STRIP=/bin/true \
	DO_USERDIRS=1 \
	MP3LIB=mpg123 \
	USE_CODEC_FLAC=1 \
	USE_CODEC_OPUS=1 \
	USE_CODEC_MIKMOD=1 \
	USE_SDL2=1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p Quake/quakespasm $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Quakespasm.txt Quakespasm-Music.txt
%attr(755,root,root) %{_bindir}/quakespasm
