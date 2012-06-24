%include	/usr/lib/rpm/macros.perl
%define	pdir	Log
%define	pnam	Topics
Summary:	Log::Topics perl module
Summary(pl):	Modu� perla Log::Topics
Name:		perl-Log-Topics
Version:	0.02
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Log::Topics controls flow of logging messages.

%description -l pl
Log::Topics kontroluje przep�yw log�w.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitelib}/Log/Topics.pm
%{_mandir}/man3/*
