%define modname	Text-Glob
%define modver	0.09

Summary:	Match globbing patterns against text
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	15
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
Text::Glob implements glob(3) style matching that can be used to match against
text, rather than fetching names from a filesystem. If you want to do full file
globbing use the File::Glob module instead.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%check
make test

%files
%doc Changes
%{perl_vendorlib}/Text
%{_mandir}/man3/*

