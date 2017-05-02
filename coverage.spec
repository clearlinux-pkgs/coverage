#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : coverage
Version  : 4.3.4
Release  : 32
URL      : http://pypi.debian.net/coverage/coverage-4.3.4.tar.gz
Source0  : http://pypi.debian.net/coverage/coverage-4.3.4.tar.gz
Summary  : Code coverage measurement for Python
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: coverage-bin
Requires: coverage-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
.. Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
.. For details: https://bitbucket.org/ned/coveragepy/src/default/NOTICE.txt

%package bin
Summary: bin components for the coverage package.
Group: Binaries

%description bin
bin components for the coverage package.


%package python
Summary: python components for the coverage package.
Group: Default

%description python
python components for the coverage package.


%prep
%setup -q -n coverage-4.3.4

%build
export LANG=C
export SOURCE_DATE_EPOCH=1489025705
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1489025705
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/coverage
/usr/bin/coverage-2.7
/usr/bin/coverage-3.6
/usr/bin/coverage2
/usr/bin/coverage3

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
