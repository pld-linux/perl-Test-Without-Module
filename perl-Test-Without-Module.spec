#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Test
%define		pnam	Without-Module
%include	/usr/lib/rpm/macros.perl
Summary:	Test::Without::Module - Test fallback behaviour in absence of modules
Summary(pl.UTF-8):	Test::Without::Module - testowanie rozwiązań zapasowych w przypadku braku modułów
Name:		perl-Test-Without-Module
Version:	0.20
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	34684186b66929bbcd12d3ac8ae03f9d
URL:		https://metacpan.org/release/Test-Without-Module
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows you to deliberately hide modules from a program
even though they are installed. This is mostly useful for testing
modules that have a fallback when a certain dependency module is not
installed.

%description -l pl.UTF-8
Ten moduł pozwala celowo ukrywać moduły przed programem, nawet jeśli
są zainstalowane. Jest to przydatne głównie do testowania modułów,
które mają rozwiązania zapasowe w przypadku, kiedy jakiś wymagany
moduł nie jest zainstalowany.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Test/Without
%{perl_vendorlib}/Test/Without/Module.pm
%{_mandir}/man3/Test::Without::Module.3pm*
