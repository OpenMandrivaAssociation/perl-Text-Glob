%define upstream_name	 Text-Glob
%define upstream_version 0.09

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Match globbing patterns against text
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Text::Glob implements glob(3) style matching that can be used to match against
text, rather than fetching names from a filesystem. If you want to do full file
globbing use the File::Glob module instead.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.90.0-4mdv2012.0
+ Revision: 765758
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.90.0-3
+ Revision: 764263
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 0.90.0-2
+ Revision: 676641
- rebuild

* Thu Mar 10 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.90.0-1
+ Revision: 643497
- update to new version 0.09

* Tue Jul 28 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.80.0-1mdv2010.0
+ Revision: 402537
- rebuild using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.08-3mdv2009.0
+ Revision: 268785
- rebuild early 2009.0 package (before pixel changes)

* Sat May 24 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-2mdv2009.0
+ Revision: 210961
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri May 04 2007 Olivier Thauvin <nanardon@mandriva.org> 0.08-1mdv2008.0
+ Revision: 22144
- 0.08


* Mon Jul 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-1mdv2007.0
- New version 0.07

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.06-5mdk
- Fix SPEC according to Perl Policy
	- Source URL
- use mkrel

* Tue Jun 07 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-4mdk 
- better url
- spec cleanup
- make test in %%check
- don't ship useless empty directories

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.06-3mdk
- fix buildrequires in a backward compatible way

* Fri Jul 23 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.06-2mdk 
- rpmbuildupdate aware
- fix summary capitalization

* Tue Mar 30 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.06-1mdk
- first mdk release

