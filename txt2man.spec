Summary:	Txt2man - convert flat ASCII text to man page format
Summary(pl.UTF-8):	Txt2man - konwersja plików tekstowych do formatu man
Name:		txt2man
Version:	1.7.1
Release:	1
License:	GPL v2+
Group:		Applications/Text
#Source0Download: https://github.com/mvertes/txt2man/releases
Source0:	https://github.com/mvertes/txt2man/archive/txt2man-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	0c587fda9780ade673ccbfc6d5b98fc9
URL:		https://github.com/mvertes/txt2man
Requires:	coreutils
Requires:	gawk
# for bookman
Suggests:	groff
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Txt2man converts flat ASCII text to man page format. It is a shell
script using awk, that should run on any Unix like system.

%description -l pl.UTF-8
Txt2man konwertuje pliki tekstowe do formatu man. Txt2man jest
skryptem powłoki wykorzystującym awk, który powinien działać na
dowolnym systemie uniksopodobnym.

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install txt2man $RPM_BUILD_ROOT%{_bindir}/txt2man
install src2man $RPM_BUILD_ROOT%{_bindir}/src2man
install bookman $RPM_BUILD_ROOT%{_bindir}/bookman

cp -p txt2man.1 $RPM_BUILD_ROOT%{_mandir}/man1/txt2man.1
cp -p src2man.1 $RPM_BUILD_ROOT%{_mandir}/man1/src2man.1
cp -p bookman.1 $RPM_BUILD_ROOT%{_mandir}/man1/bookman.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README
%attr(755,root,root) %{_bindir}/txt2man
%attr(755,root,root) %{_bindir}/src2man
%attr(755,root,root) %{_bindir}/bookman
%{_mandir}/man1/txt2man.1*
%{_mandir}/man1/src2man.1*
%{_mandir}/man1/bookman.1*
