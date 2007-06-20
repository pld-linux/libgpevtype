Summary:	GPE PIM Interchange library
Summary(pl.UTF-8):	Biblioteka wymiany danych GPE PIM
Name:		libgpevtype
Version:	0.50
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://gpe.linuxtogo.org/download/source/%{name}-%{version}.tar.bz2
# Source0-md5:	4d7a20b215c53b73786690e895f05750
URL:		http://gpe.linuxtogo.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.0
BuildRequires:	libeventdb-devel >= 0.90
BuildRequires:	libmimedir-devel >= 0.3.1
BuildRequires:	libtododb-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.98
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
Requires:	libeventdb-devel >= 0.90
Requires:	libmimedir-devel >= 0.3.1
Requires:	libtododb-devel

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

%package apidocs
Summary:	libgpevtype API documentation
Summary(pl.UTF-8):	Dokumentacja API libgpevtype
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libgpevtype API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API libgpevtype.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-html-dir=%{_gtkdocdir}
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

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libgpevtype
