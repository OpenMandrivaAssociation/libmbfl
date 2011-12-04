%define	fver 1.0.1

%define	major 1
%define libname %mklibname mbfl %{major}
%define develname %mklibname mbfl -d

Summary:	Streamable kanji code filter and converter
Name:		libmbfl
Version:	1.1.0
Release:	7
License:	LGPL
Group:		System/Libraries
URL:		http://sourceforge.jp/projects/php-i18n/
Source0:	http://osdn.dl.sourceforge.jp/php-i18n/18570/%{name}-%{fver}.tar.bz2
# ftp://ftp.unicode.org/Public/MAPPINGS/
Source1:	unicode_mappings.tar.gz
Patch0:		libmbfl-php539RC1.diff
BuildRequires:	autoconf automake libtool

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
%patch0 -p1

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

%check
make check

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
