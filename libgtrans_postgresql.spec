Summary:	Database Access Library
Name:		libgtrans_postgresql_6_5_3
Version:	0.2.0
Release:	1
License:	GPL
Group:		Applications/Databases
Group(pl):	Aplikacje/Bazy danych
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Source0:	libgtrans_postgresql_6_5_3-%{ver}.tar.gz

%define		_sysconfdir	/etc

%description
libgtrans_postgresql_6_5_3 is a plugin for GNOME Transcript that
provides postgresql access.

%prep
%setup -q

%build
LDFLAGS="-s"; export LDFLAGS
%configure
make

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
