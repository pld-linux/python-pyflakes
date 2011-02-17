%define 	module	pyflakes
Summary:	Passive checker of Python programs
Summary(pl.UTF-8):	Pasywny program do sprawdzania programów w Pythonie
Name:		python-%{module}
Version:	0.4.0
Release:	2
License:	MIT
Group:		Development/Tools
Source0:	http://pypi.python.org/packages/source/p/pyflakes/%{module}-%{version}.tar.gz
# Source0-md5:	630a72510aae8758f48cf60e4fa17176
URL:		http://www.divmod.org/projects/pyflakes
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
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

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

rm -rf $RPM_BUILD_ROOT%{py_sitescriptdir}/pyflakes/test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pyflakes
%{py_sitescriptdir}/pyflakes
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/pyflakes-%{version}-*.egg-info
%endif
