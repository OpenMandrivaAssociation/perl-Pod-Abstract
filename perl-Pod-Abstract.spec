
%define realname   Pod-Abstract
%define version    0.16
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Basic multipart section numbering
Source:     http://www.cpan.org/modules/by-module/Pod/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
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
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes ._README README
%{_mandir}/man3/*
%perl_vendorlib/*
/usr/bin/paf
/usr/share/man/man1/paf.1

