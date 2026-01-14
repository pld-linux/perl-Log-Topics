%define		pdir	Log
%define		pnam	Topics
Summary:	Log::Topics perl module
Summary(pl.UTF-8):	Moduł perla Log::Topics
Name:		perl-Log-Topics
Version:	0.02
Release:	12
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	116ad36f1df4a04afeb65321c229d2b6
URL:		http://search.cpan.org/dist/Log-Topics/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Log::Topics controls flow of logging messages.

%description -l pl.UTF-8
Log::Topics kontroluje przepływ logów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Log/Topics.pm
%{_mandir}/man3/*
