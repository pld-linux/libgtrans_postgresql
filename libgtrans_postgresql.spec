Summary:	Database Access Library for PostgreSQL
Summary(pl):	Biblioteka dostêpu do baz danych PostgreSQL
Name:		libgtrans_postgresql_6_5_3
Version:	0.2.0
Release:	1
License:	GPL
Group:		Applications/Databases
Group(de):	Applikationen/Dateibanken
Group(pl):	Aplikacje/Bazy danych
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/gtranscript/%{name}-%{version}.tar.gz
URL:		http://gtranscript.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc

%description
libgtrans_postgresql_6_5_3 is a plugin for GNOME Transcript that
provides postgresql access.

%description -l pl
libgtrans_postgresql_6_5_3 jest wtyczk± do GNOME Transcript dodaj±c±
obs³ugê baz danych postgresql 6.5.3.

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
