Summary:	Passive checker of Python programs
Summary(pl.UTF-8):	Pasywny program do sprawdzania programów w Pythonie
Name:		pyflakes
Version:	0.2.1
Release:	0.1
License:	MIT
Group:		Development/Tools
Source0:	http://www.divmod.org/static/projects/pyflakes/%{name}-%{version}.tar.gz
# Source0-md5:	e65d9245d706350b3db811280d897f30
Patch0:		%{name}-IOError.patch
URL:		http://www.divmod.org/projects/pyflakes
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
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
sprawdza tak wielu rzeczy. W przeciwieństwie do PyLinta Pyflakes
szuka tylko błędów logicznych w programach; nie sprawdza stylu.

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT

python ./setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/pyflakes
