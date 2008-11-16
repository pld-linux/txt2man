#
Summary:	Txt2man converts flat ASCII text to man page format
Summary(pl.UTF-8):	Txt2man konwertuje plik tekstowy do formatu man
Name:		txt2man
Version:	1.5.5
Release:	0.1
License:	GPL v2+
Group:		Applications
Source0:	http://mvertes.free.fr/%{name}/txt2man
# Source0-md5:	7b0198c61552a96a4c8cacbbf377a925
Source1:	http://mvertes.free.fr/%{name}/src2man
# Source1-md5:	577a923d05a5c7e0a15a8d2542a3bb93
Source2:	http://mvertes.free.fr/%{name}/bookman
# Source2-md5:	5555539739c0dd1f982e33184c120403
Source3:	http://mvertes.free.fr/%{name}/Makefile
# Source3-md5:	cf16c0d44a77599fe433a7882680f6b1
URL:		http://mvertes.free.fr/txt2man
Requires:	awk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Txt2man converts flat ASCII text to man page format. It is a shell
script using gnu awk, that should run on any Unix like system.

%description -l pl.UTF-8
Txt2man konwertuje pliki tekstowe do formatu man. Txt2man jest
skryptem shellowym wykorzystującym awk, który powinien działać na
dowolnym systemie Unikso-podobnym.

%prep
%{__rm} -rf $RPM_BUILD_DIR/%{name}-%{version}
%{__mkdir} $RPM_BUILD_DIR/%{name}-%{version}
cd $RPM_BUILD_DIR/%{name}-%{version}
install -m0755 %SOURCE0 $RPM_BUILD_DIR/%{name}-%{version}
install -m0755 %SOURCE1 $RPM_BUILD_DIR/%{name}-%{version}
install -m0755 %SOURCE2 $RPM_BUILD_DIR/%{name}-%{version}
install        %SOURCE3 $RPM_BUILD_DIR/%{name}-%{version}

%build
cd $RPM_BUILD_DIR/%{name}-%{version}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

cd $RPM_BUILD_DIR/%{name}-%{version}

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install txt2man $RPM_BUILD_ROOT%{_bindir}/txt2man
install src2man $RPM_BUILD_ROOT%{_bindir}/src2man
install bookman $RPM_BUILD_ROOT%{_bindir}/bookman

install txt2man.1 $RPM_BUILD_ROOT%{_mandir}/man1/txt2man.1
install src2man.1 $RPM_BUILD_ROOT%{_mandir}/man1/src2man.1
install bookman.1 $RPM_BUILD_ROOT%{_mandir}/man1/bookman.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/txt2man
%attr(755,root,root) %{_bindir}/src2man
%attr(755,root,root) %{_bindir}/bookman
%{_mandir}/man1/txt2man.1*
%{_mandir}/man1/src2man.1*
%{_mandir}/man1/bookman.1*