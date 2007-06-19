Summary:	GPE PIM Interchange library
Summary(pl.UTF-8):	Biblioteka wymiany danych GPE PIM
Name:		libgpevtype
Version:	0.17
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://gpe.linuxtogo.org/download/source/%{name}-%{version}.tar.bz2
# Source0-md5:	c9c031ee32bcdb3c8bf0d31083330d63
URL:		http://gpe.linuxtogo.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.0
BuildRequires:	libeventdb-devel >= 0.29
BuildRequires:	libmimedir-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GPE PIM Interchange library.

%description -l pl.UTF-8
Biblioteka wymiany danych GPE PIM.

%package devel
Summary:	Header files for libgpevtype
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libgpevtype
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.0
Requires:	libeventdb-devel >= 0.29
Requires:	libmimedir-devel

%description devel
Header files for libgpevtype.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libgpevtype.

%package static
Summary:	Static libgpevtype library
Summary(pl.UTF-8):	Statyczna biblioteka libgpevtype
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgpevtype library.

%description static -l pl.UTF-8
Statyczna biblioteka libgpevtype.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgpevtype.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgpevtype.so
%{_libdir}/libgpevtype.la
%{_includedir}/gpe/*.h
%{_pkgconfigdir}/libgpevtype.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgpevtype.a
