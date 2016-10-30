#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Test
%define		pnam	Without-Module
%include	/usr/lib/rpm/macros.perl
Summary:	Test::Without::Module - Test fallback behaviour in absence of modules
Name:		perl-Test-Without-Module
Version:	0.18
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	cd19ad26024e89fdfefb0ae0334ee500
URL:		http://search.cpan.org/dist/Test-Without-Module/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows you to deliberately hide modules from a program
even though they are installed. This is mostly useful for testing modules
that have a fallback when a certain dependency module is not installed.

None. All magic is done via use Test::Without::Module LIST and
no Test::Without::Module LIST.

This function returns a reference to a copy of the current hash of forbidden
modules or an empty hash if none are currently forbidden. This is convenient
if you are testing and/or debugging this module.

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
