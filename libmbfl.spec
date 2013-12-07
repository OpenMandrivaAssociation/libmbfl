%define	major	1
%define libname	%mklibname mbfl %{major}
%define devname	%mklibname mbfl -d

Summary:	Streamable kanji code filter and converter
Name:		libmbfl
Version:	1.2.0
Release:	4
License:	LGPLv2
Group:		System/Libraries
Url:		http://sourceforge.jp/projects/php-i18n/
Source0:	http://osdn.dl.sourceforge.jp/php-i18n/18570/%{name}-%{version}.tar.gz
# ftp://ftp.unicode.org/Public/MAPPINGS/
Source1:	unicode_mappings.tar.gz
Patch0:		libmbfl-automake-1.13.patch
BuildRequires:	dejagnu
BuildRequires:	libtool

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

%package -n	%{devname}
Summary:	Development library and header files for development with mbfl
Group:		Development/C
Requires:	%{libname} >= %{version}-%{release}
Provides:	mbfl-devel = %{version}-%{release}

%description -n	%{devname}
This package is only needed if you plan to develop or compile applications
which requires the mbfl library.

%prep
%setup -q -a1
%apply_patches

# fix strange perms
find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

chmod 644 AUTHORS DISCLAIMER LICENSE README
rm -f configure
touch NEWS ChangeLog COPYING
autoreconf -fi

%build
%configure2_5x \
	--disable-static

%make

#%%check
#make check

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libmbfl.so.%{major}*

%files -n %{devname}
%doc AUTHORS DISCLAIMER LICENSE README
%dir %{_includedir}/mbfl
%{_includedir}/mbfl/*.h
%{_libdir}/*.so

