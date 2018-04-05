#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : coverage
Version  : 4.5.1
Release  : 45
URL      : http://pypi.debian.net/coverage/coverage-4.5.1.tar.gz
Source0  : http://pypi.debian.net/coverage/coverage-4.5.1.tar.gz
Summary  : Code coverage measurement for Python
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: coverage-bin
Requires: coverage-legacypython
Requires: coverage-python3
Requires: coverage-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : setuptools-legacypython
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


%package extras
Summary: extras components for the coverage package.
Group: Default

%description extras
extras components for the coverage package.


%package legacypython
Summary: legacypython components for the coverage package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the coverage package.


%package python
Summary: python components for the coverage package.
Group: Default
Requires: coverage-python3

%description python
python components for the coverage package.


%package python3
Summary: python3 components for the coverage package.
Group: Default
Requires: python3-core

%description python3
python3 components for the coverage package.


%prep
%setup -q -n coverage-4.5.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521136249
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1521136249
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/coverage-2.7
%exclude /usr/bin/coverage2
/usr/bin/coverage
/usr/bin/coverage-3.6
/usr/bin/coverage3

%files extras
%defattr(-,root,root,-)
/usr/bin/coverage-2.7
/usr/bin/coverage2

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
