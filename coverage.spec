#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : coverage
Version  : 6.0
Release  : 98
URL      : https://files.pythonhosted.org/packages/14/2d/0bfa3483ad8bd4a14e72a1923ebb5b0de14842a7730a4a05c6d47b4d944d/coverage-6.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/14/2d/0bfa3483ad8bd4a14e72a1923ebb5b0de14842a7730a4a05c6d47b4d944d/coverage-6.0.tar.gz
Summary  : Code coverage measurement for Python
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: coverage-bin = %{version}-%{release}
Requires: coverage-license = %{version}-%{release}
Requires: coverage-python = %{version}-%{release}
Requires: coverage-python3 = %{version}-%{release}
Requires: tomli
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tomli
BuildRequires : tox
BuildRequires : virtualenv

%description
.. Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
.. For details: https://github.com/nedbat/coveragepy/blob/master/NOTICE.txt

%package bin
Summary: bin components for the coverage package.
Group: Binaries
Requires: coverage-license = %{version}-%{release}

%description bin
bin components for the coverage package.


%package license
Summary: license components for the coverage package.
Group: Default

%description license
license components for the coverage package.


%package python
Summary: python components for the coverage package.
Group: Default
Requires: coverage-python3 = %{version}-%{release}

%description python
python components for the coverage package.


%package python3
Summary: python3 components for the coverage package.
Group: Default
Requires: python3-core
Provides: pypi(coverage)

%description python3
python3 components for the coverage package.


%prep
%setup -q -n coverage-6.0
cd %{_builddir}/coverage-6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1633357401
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/coverage
cp %{_builddir}/coverage-6.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/coverage/598f87f072f66e2269dd6919292b2934dbb20492
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/coverage
/usr/bin/coverage-3.9
/usr/bin/coverage3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/coverage/598f87f072f66e2269dd6919292b2934dbb20492

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
