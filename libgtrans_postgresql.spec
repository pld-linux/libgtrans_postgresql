# TODO: fix %files
Summary:	Database Access Library for PostgreSQL
Summary(pl.UTF-8):	Biblioteka dostępu do baz danych PostgreSQL
Name:		libgtrans_postgresql_6_5_3
Version:	0.2.0
Release:	1
License:	GPL
Group:		Applications/Databases
Source0:	http://dl.sourceforge.net/gtranscript/%{name}-%{version}.tar.gz
# Source0-md5:	a7183fd71d6a4ea2495bc49e21d76fd5
URL:		http://gtranscript.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgtrans_postgresql_6_5_3 is a plugin for GNOME Transcript that
provides PostgreSQL access.

%description -l pl.UTF-8
libgtrans_postgresql_6_5_3 jest wtyczką do GNOME Transcript dodającą
obsługę baz danych PostgreSQL 6.5.3.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS
%{_prefix}/*
