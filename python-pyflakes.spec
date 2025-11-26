#
# Conditional build:
%bcond_without	tests	# test target

%define 	module	pyflakes
Summary:	Passive checker of Python programs
Summary(pl.UTF-8):	Pasywny program do sprawdzania programów w Pythonie
Name:		python-%{module}
# keep < 2.5 here for python2 support
# and < 2.4 to support flake8 3.9.x, which was the last with python2 support
# (there were no flake8 releases supporting pyflakes 2.4.x and python2)
Version:	2.3.1
Release:	6
License:	MIT
Group:		Development/Tools
#Source0Download: https://pypi.org/simple/pyflakes/
Source0:	https://files.pythonhosted.org/packages/source/p/pyflakes/%{module}-%{version}.tar.gz
# Source0-md5:	0b60a307a6b293ee505fe0134e9d46e9
URL:		https://github.com/PyCQA/pyflakes
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
Provides:	pyflakes = %{version}-%{release}
Obsoletes:	pyflakes < 0.4.0-2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pyflakes is a simple program which checks Python source files for
errors. It is similar to PyChecker in scope, but differs in that it
does not execute the modules to check them. This is both safer and
faster, although it does not perform as many checks. Unlike PyLint,
Pyflakes checks only for logical errors in programs; it does not
perform any checks on style.

%description -l pl.UTF-8
Pyflakes to prosty program sprawdzający pliki źródłowe Pythona pod
kątem błędów. Jest podobny do PyCheckera jeśli chodzi o zakres
działania, ale różni się tym, że nie wykonuje modułów przy sprawdzaniu
ich. Jest to zarówno bardziej bezpieczne, jak i szybze, choć nie
sprawdza tak wielu rzeczy. W przeciwieństwie do PyLinta Pyflakes szuka
tylko błędów logicznych w programach; nie sprawdza stylu.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%if %{with tests}
%{__python} -m unittest discover -s pyflakes/test
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/pyflakes{,-2}

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/pyflakes/test
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE NEWS.rst README.rst
%attr(755,root,root) %{_bindir}/pyflakes-2
%{py_sitescriptdir}/pyflakes
%{py_sitescriptdir}/pyflakes-%{version}-py*.egg-info
