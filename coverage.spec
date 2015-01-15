#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : coverage
Version  : 3.7.1
Release  : 11
URL      : https://pypi.python.org/packages/source/c/coverage/coverage-3.7.1.tar.gz
Source0  : https://pypi.python.org/packages/source/c/coverage/coverage-3.7.1.tar.gz
Summary  : Code coverage measurement for Python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: coverage-bin
Requires: coverage-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Coverage.py: code coverage testing for Python
Coverage.py measures code coverage, typically during test execution.  It uses
the code analysis tools and tracing hooks provided in the Python standard
library to determine which lines are executable, and which have been executed.

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
%setup -q -n coverage-3.7.1

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
py.test-2.7 || :
%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}
python3 setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/coverage
/usr/bin/coverage-2.7
/usr/bin/coverage-3.4
/usr/bin/coverage2
/usr/bin/coverage3

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
