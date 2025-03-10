#
# Conditional build:
%bcond_without	tests	# test target
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	pyflakes
Summary:	Passive checker of Python programs
Summary(pl.UTF-8):	Pasywny program do sprawdzania programów w Pythonie
Name:		python-%{module}
# NOTE: before upgrading to >=2.4.0 check for python2-compatible flake8 release supporting new pyflakes
Version:	2.3.1
Release:	4
License:	MIT
Group:		Development/Tools
#Source0Download: https://pypi.org/simple/pyflakes/
Source0:	https://files.pythonhosted.org/packages/source/p/pyflakes/%{module}-%{version}.tar.gz
# Source0-md5:	0b60a307a6b293ee505fe0134e9d46e9
URL:		https://github.com/PyCQA/pyflakes
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.4
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%endif
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

%package -n python3-%{module}
Summary:	Passive checker of Python programs
Summary(pl.UTF-8):	Pasywny program do sprawdzania programów w Pythonie
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4
# default binary moved
Conflicts:	python-pyflakes < 2.1.1-4

%description -n python3-%{module}
Pyflakes is a simple program which checks Python source files for
errors. It is similar to PyChecker in scope, but differs in that it
does not execute the modules to check them. This is both safer and
faster, although it does not perform as many checks. Unlike PyLint,
Pyflakes checks only for logical errors in programs; it does not
perform any checks on style.

%description -n python3-%{module} -l pl.UTF-8
Pyflakes to prosty program sprawdzający pliki źródłowe Pythona pod
kątem błędów. Jest podobny do PyCheckera jeśli chodzi o zakres
działania, ale różni się tym, że nie wykonuje modułów przy sprawdzaniu
ich. Jest to zarówno bardziej bezpieczne, jak i szybze, choć nie
sprawdza tak wielu rzeczy. W przeciwieństwie do PyLinta Pyflakes szuka
tylko błędów logicznych w programach; nie sprawdza stylu.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m unittest discover -s pyflakes/test
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m unittest discover -s pyflakes/test
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/pyflakes{,-2}

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/pyflakes/test
%py_postclean
%endif

%if %{with python3}
%py3_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/pyflakes{,-3}
ln -sf pyflakes-3 $RPM_BUILD_ROOT%{_bindir}/pyflakes

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/pyflakes/test
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE NEWS.rst README.rst
%attr(755,root,root) %{_bindir}/pyflakes-2
%{py_sitescriptdir}/pyflakes
%{py_sitescriptdir}/pyflakes-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc AUTHORS LICENSE NEWS.rst README.rst
%attr(755,root,root) %{_bindir}/pyflakes
%attr(755,root,root) %{_bindir}/pyflakes-3
%{py3_sitescriptdir}/pyflakes
%{py3_sitescriptdir}/pyflakes-%{version}-py*.egg-info
%endif
