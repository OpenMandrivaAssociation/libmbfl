%define	fver 1.2.0

%define	major 1
%define libname %mklibname mbfl %{major}
%define develname %mklibname mbfl -d

Summary:	Streamable kanji code filter and converter
Name:		libmbfl
Version:	1.2.0
Release:	1
License:	LGPL
Group:		System/Libraries
URL:		http://sourceforge.jp/projects/php-i18n/
Source0:	http://osdn.dl.sourceforge.jp/php-i18n/18570/%{name}-%{fver}.tar.gz
# ftp://ftp.unicode.org/Public/MAPPINGS/
Source1:	unicode_mappings.tar.gz
Patch0:		libmbfl-automake-1.13.patch
BuildRequires:	autoconf automake libtool
BuildRequires:	dejagnu

%description
This is Libmbfl, a streamable multibyte character code filter and converter
library.

%package -n	%{libname}
Summary:	Streamable kanji code filter and converter library
Group:          System/Libraries

%description -n	%{libname}
This is Libmbfl, a streamable multibyte character code filter and converter
library.

This package provides the shared mbfl library.

%package -n	%{develname}
Summary:	Static library and header files for development with mbfl
Group:		Development/C
Requires:	%{libname} >= %{version}-%{release}
Provides:	mbfl-devel = %{version}-%{release}
Obsoletes:	mbfl-devel

%description -n	%{develname}
This is Libmbfl, a streamable multibyte character code filter and converter
library.

This package is only needed if you plan to develop or compile applications
which requires the mbfl library.

%prep

%setup -q -n %{name}-%{fver} -a1
%apply_patches

# fix strange perms
find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

chmod 644 AUTHORS DISCLAIMER LICENSE README

%build
rm -f configure
touch NEWS ChangeLog COPYING
libtoolize --copy --force; aclocal; autoheader; automake --add-missing --force-missing; autoconf

%configure2_5x

%make

#%%check
#make check

%install
rm -rf %{buildroot}

%makeinstall_std

# cleanup
rm -f %{buildroot}%{_libdir}/*.*a

%files -n %{libname}
%doc AUTHORS DISCLAIMER LICENSE README
%attr(0755,root,root) %{_libdir}/*.so.%{major}*

%files -n %{develname}
%attr(0755,root,root) %dir %{_includedir}/mbfl
%attr(0644,root,root) %{_includedir}/mbfl/*.h
%attr(0644,root,root) %{_libdir}/*.so


%changelog
* Sat Jan 14 2012 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-5.1
- sync with php-5.3.9RC1

* Fri Jun 17 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-5mdv2011.0
+ Revision: 685743
- sync with php-5.3.7RC1

* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-4
+ Revision: 660203
- sync with php-5.3.6 (CVE-2010-4156)
- P1: security fix for CVE-2010-4156 (the correct patch)
- P1: security fix for CVE-2010-4156

* Mon Jul 12 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-1mdv2011.0
+ Revision: 551233
- 1.1.0 (sync with php-5.3.3RC1)

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-8mdv2010.1
+ Revision: 519022
- rebuild

* Sun Sep 27 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-7mdv2010.0
+ Revision: 449751
- sync with php-5.3.1RC1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.2-6mdv2010.0
+ Revision: 425603
- rebuild

* Sat Feb 07 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-5mdv2009.1
+ Revision: 338371
- sync with php-5.3.0beta1

* Thu Dec 18 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-4mdv2009.1
+ Revision: 315575
- rebuild

* Fri Aug 22 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-3mdv2009.0
+ Revision: 275163
- rebuild

* Fri Aug 22 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-2mdv2009.0
+ Revision: 275077
- rebuild
- sync with upcoming php-5.3.0 (P0)
- added S1 to make it build
- fix build (P1)

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Apr 20 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-3mdv2009.0
+ Revision: 195934
- sync with php-5.2.5

* Fri Feb 29 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-2mdv2008.1
+ Revision: 176677
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 16 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-1mdv2008.0
+ Revision: 64237
- Import libmbfl



* Thu Aug 16 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-1mdv2008.0
- initial Mandriva package
