%include	/usr/lib/rpm/macros.perl
%define	pdir	Log
%define	pnam	Topics
Summary:	Log::Topics perl module
Summary(pl):	Modu³ perla Log::Topics
Name:		perl-Log-Topics
Version:	0.02
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	116ad36f1df4a04afeb65321c229d2b6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Log::Topics controls flow of logging messages.

%description -l pl
Log::Topics kontroluje przep³yw logów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Log/Topics.pm
%{_mandir}/man3/*
