#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	pyflakes
Summary:	Passive checker of Python programs
Summary(pl.UTF-8):	Pasywny program do sprawdzania programów w Pythonie
Name:		python-%{module}
Version:	0.8.1
Release:	4
License:	MIT
Group:		Development/Tools
Source0:	http://pypi.python.org/packages/source/p/pyflakes/%{module}-%{version}.tar.gz
# Source0-md5:	905fe91ad14b912807e8fdc2ac2e2c23
URL:		http://www.divmod.org/projects/pyflakes
%if %{with python2}
BuildRequires:	python-devel
Requires:	python-modules
%endif

%{?with_tests:BuildRequires:	rpm-pythonprov}
BuildRequires:	rpmbuild(macros) >= 1.219
%if %{with python3}
BuildRequires:	python3-devel
BuildRequires:	python3-modules
%endif
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
Requires:	python3-modules

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
CC="%{__cc}" \
CFLAGS="%{rpmcppflags} %{rpmcflags}" \
%{__python} setup.py build --build-base build-2 %{?with_tests:test}
%endif

%if %{with python3}
CC="%{__cc}" \
CFLAGS="%{rpmcppflags} %{rpmcflags}" \
%{__python3} setup.py build --build-base build-3 %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%{__python} setup.py \
		build --build-base build-2 \
		install --skip-build \
		--optimize=2 \
		--root=$RPM_BUILD_ROOT

%py_postclean
%endif

%if %{with python3}
%{__python3} setup.py \
		build --build-base build-3 \
		install --skip-build \
		--optimize=2 \
		--root=$RPM_BUILD_ROOT
%endif

rm -rf $RPM_BUILD_ROOT%{py_sitescriptdir}/pyflakes/test

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pyflakes
%{py_sitescriptdir}/pyflakes
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/pyflakes-%{version}-*.egg-info
%endif
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
