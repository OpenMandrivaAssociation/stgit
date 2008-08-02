
Summary: 	Stacked GIT
Name:		stgit
Version: 	0.14.1
Release: 	%mkrel 4
Url: 		http://www.procode.org/stgit/
Source0: 	http://homepage.ntlworld.com/cmarinas/stgit/%{name}-%{version}.tar.gz

License: 	GPL
Group: 		Development/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: 	noarch
Requires: 	python
Requires: 	git-core
BuildRequires:	python-devel
BuildRequires:  git-core

%description
StGIT is a Python application providing similar functionality to Quilt (i.e.
pushing/popping patches to/from a stack) on top of GIT. These operations are
performed using GIT commands and the patches are stored as GIT commit objects,
allowing easy merging of the StGIT patches into other repositories using
standard GIT functionality.

Note that StGIT is not an SCM interface on top of GIT and it expects a
previously initialised GIT repository. For standard SCM operations, either use
plain GIT commands or the Cogito tool.


%prep
%setup

%build
python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT --prefix=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/%name
%{py_puresitedir}/%name
%{py_puresitedir}/%{name}-*.egg-info
%doc README AUTHORS INSTALL COPYING



