%define	major 1
%define libname %mklibname mbfl %{major}
%define develname %mklibname mbfl -d

Summary:	Streamable kanji code filter and converter
Name:		libmbfl
Version:	1.0.1
Release:	%mkrel 3
License:	LGPL
Group:		System/Libraries
URL:		http://sourceforge.jp/projects/php-i18n/
Source0:	http://osdn.dl.sourceforge.jp/php-i18n/18570/%{name}-%{version}.tar.bz2
Patch0:		libmbfl-php525.diff
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
Requires:	%{libname} = %{version}
Provides:	mbfl-devel = %{version}-%{release}
Obsoletes:	mbfl-devel

%description -n	%{develname}
This is Libmbfl, a streamable multibyte character code filter and converter
library.

This package is only needed if you plan to develop or compile applications
which requires the mbfl library.

%prep

%setup -q -n %{name}-%{version}
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

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS DISCLAIMER LICENSE README
%attr(0755,root,root) %{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%attr(0755,root,root) %dir %{_includedir}/mbfl
%attr(0644,root,root) %{_includedir}/mbfl/*.h
%attr(0644,root,root) %{_libdir}/*.so
%attr(0644,root,root) %{_libdir}/*.a
%attr(0644,root,root) %{_libdir}/*.la
