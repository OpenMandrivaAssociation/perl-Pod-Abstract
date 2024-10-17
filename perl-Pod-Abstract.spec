%define upstream_name    Pod-Abstract
%define upstream_version 0.20

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    5

License:    GPL+ or Artistic
Group:      Development/Perl
Summary:    Basic multipart section numbering

Source0:    http://www.cpan.org/modules/by-module/Pod/%{upstream_name}-%{upstream_version}.tar.gz
Url:        https://search.cpan.org/dist/%{upstream_name}

BuildRequires: perl-devel
BuildRequires: perl(IO::String)
BuildArch: noarch

%description
POD::Abstract provides a means to load a POD (or POD compatible) document
without direct reference to it's syntax, and perform manipulations on the
abstract syntax tree.

This can be used to support additional features for POD, to format output,
to compile into alternative formats, etc.

WHY?
    If you've ever asked yourself "What does Pod do for me?", this module
    is intended to answer that question.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%clean

%files
%doc Changes README
%{_mandir}/man1/*
%{_mandir}/man3/*
%perl_vendorlib/*
/usr/bin/paf



%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.200.0-2mdv2011.0
+ Revision: 654280
- rebuild for updated spec-helper

* Sun Jan 03 2010 Jérôme Quelin <jquelin@mandriva.org> 0.200.0-1mdv2011.0
+ Revision: 485806
- update to 0.20

* Sun Jul 12 2009 Jérôme Quelin <jquelin@mandriva.org> 0.190.0-1mdv2010.0
+ Revision: 395170
- update to 0.19

* Wed May 27 2009 Jérôme Quelin <jquelin@mandriva.org> 0.170.0-1mdv2010.0
+ Revision: 380217
- fixed rpm version
- update to 0.17
- now using %%perl_convert_version
- fixed wrong file in %%doc

* Wed May 13 2009 Jérôme Quelin <jquelin@mandriva.org> 0.16-1mdv2010.0
+ Revision: 375445
- change in packaged files
- adding missing buildrequires
- import perl-Pod-Abstract


* Wed May 13 2009 cpan2dist 0.16-1mdv
- initial mdv release, generated with cpan2dist

