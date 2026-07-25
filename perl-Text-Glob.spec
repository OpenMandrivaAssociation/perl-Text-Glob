%define modname	Text-Glob
%define modver	0.11

Summary:	Match globbing patterns against text
Name:		perl-%{modname}
Version:	%{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Text-Glob
Source0:	https://cpan.metacpan.org/authors/id/R/RC/RCLAMP/Text-Glob-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:  perl(Test::More)

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

