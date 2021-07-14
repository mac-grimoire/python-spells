%{!?_version: %define _version 0.0.1 }

%global srcname carcano_foolist

Name:           python-%{srcname}
Version:        %{_version} 
Release:        1%{?dist}
Summary:        Python Based Ansible Dynamic Inventory Script
License:        LGPLv3+
Source0:        %{pypi_source} 

BuildArch:      noarch
BuildRequires:  python3-devel python3-setuptools
Requires:       python3 python3-pyyaml

%global _description %{expand:Python Based Ansible Dynamic Inventory Script.}

%description
%_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%_description

%package -n python3-%{srcname}-common
Summary:        %{summary}
BuildRequires:  python3-devel
%{?python_provide:%python_provide python3-%{srcname}-common}

%description -n python3-%{srcname}-common
Python 3 packages used by %_description

%prep
%autosetup -n %{srcname}-%{_version}

%build
%py3_build

%install
%py3_install
mkdir %{buildroot}/%{_sysconfdir}
mkdir %{buildroot}/%{_sysconfdir}/fooapp
mkdir %{buildroot}/%{_sysconfdir}/rsyslog.d
cp %{buildroot}/usr/bin/logging.conf %{buildroot}/%{_sysconfdir}/fooapp/logging.conf
mv %{buildroot}/usr/share/doc/fooapp/rsyslog/fooapp.conf %{buildroot}/%{_sysconfdir}/rsyslog.d/fooapp.conf

%check
%{__python3} setup.py test
rm -f %{buildroot}/usr/bin/logging.conf

%files -n python3-%{srcname}
%config  %{_sysconfdir}/fooapp/logging.conf
%config  %{_sysconfdir}/rsyslog.d/fooapp.conf
%{_bindir}/fooapp.py

%files -n python3-%{srcname}-common
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/carcano/foolist/

%post -n python3-%{srcname}
systemctl restart rsyslog

%postun -n python3-%{srcname}
systemctl restart rsyslog

%changelog
* Mon Jun 14 2021 Marco Antonio Carcano <mc@carcano.ch>
First release
