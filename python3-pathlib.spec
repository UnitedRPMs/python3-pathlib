Name:           python3-pathlib
Version:        2.3.3
Release:        1%{?dist}
Summary:        Object-oriented filesystem paths
License:        MIT
Group:          Development/Languages
URL:            https://pypi.python.org/pypi/pathlib2/
Source:         https://files.pythonhosted.org/packages/source/p/pathlib2/pathlib2-%{version}.tar.gz
BuildRequires:  python3-devel
BuildRequires:  python3-mock
BuildRequires:  python3-scandir
BuildRequires:  python3-six

Requires:       python3-six
Requires:       python3-scandir

BuildArch:      noarch

%description
The goal of pathlib2 is to provide a backport of
`standard pathlib <http://docs.python.org/dev/library/pathlib.html>`_
module which tracks the standard library module,
so all the newest features of the standard pathlib can be
used also on older Python versions.

%prep
%autosetup -n pathlib2-%{version}

%build
%py3_build

%install
%py3_install

%files 
%license LICENSE.rst
%doc CHANGELOG.rst README.rst
%{python3_sitelib}/*

%changelog

* Wed Mar 13 2019 - David Va <davidva AT tuta DOT io> 2.3.3-1
- Initial build
