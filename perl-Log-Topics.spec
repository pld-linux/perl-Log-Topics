%include	/usr/lib/rpm/macros.perl
Summary:	Log-Topics perl module
Summary(pl):	Modu� perla Log-Topics
Name:		perl-Log-Topics
Version:	0.02
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Log/Log-Topics-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Log-Topics controls flow of logging messages.

%description -l pl
Log-Topics kontroluje przep�yw log�w.

%prep
%setup -q -n Log-Topics-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Log/Topics.pm
%{_mandir}/man3/*
