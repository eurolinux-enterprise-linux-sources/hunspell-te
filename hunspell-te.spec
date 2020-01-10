%define lang te
%define langrelease 2
%define langversion 0.01

Name: hunspell-te
Summary: Telugu hunspell dictionaries
%define upstreamid 20050929
Version: 0.%{upstreamid}
Release: 11%{?dist}
Group:          Applications/Text
##Upstream is unresponsive so unable to verify license version
License:        GPL+
URL:            http://aspell.net/
Source0:        ftp://ftp.gnu.org/gnu/aspell/dict/%{lang}/aspell6-%{lang}-%{langversion}-%{langrelease}.tar.bz2
BuildArch:      noarch
BuildRequires:  aspell >= 12:0.60
BuildRequires:  hunspell-devel
Requires:       hunspell

%description
Telugu hunspell dictionaries.This package
contains the efforts of aspell-te that converted by
wordlist2hunspell.

%prep
%setup -q -n aspell6-%{lang}-%{langversion}-%{langrelease}
prezip-bin -d < te.cwl > te.txt

%build
export LANG=te_IN.utf8
wordlist2hunspell te.txt te_IN

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%files 
%doc COPYING Copyright
%{_datadir}/myspell/*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.20050929-11
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20050929-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20050929-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Parag <pnemade AT redhat DOT com> - 0.20050929-8
- spec cleanup

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20050929-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20050929-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Mar 08 2010 Parag <pnemade AT redhat.com> - 0.20050929-5
- Resolves:rh#568227-[te_IN]Fix %description and license tag                                                

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20050929-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 17 2009 Parag <pnemade@redhat.com> - 0.20050929-3
- Use aspell source instead to pull source as BR:aspell-te
- Resolves:rh#511262 buildrequires aspell-te

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20050929-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Sep 12 2008 Caolan McNamara <caolanm@redhat.com> - 0.20050929-1
- initial version


