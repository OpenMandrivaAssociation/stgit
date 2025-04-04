Summary: 	Stacked GIT
Name:		stgit
Version: 	0.17.1
Release: 	1
Url: 		https://www.procode.org/stgit/
Source0: 	http://download.gna.org/stgit/%{name}-%{version}.tar.gz

License: 	GPL
Group: 		Development/Other
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
%make

%install
%make install DESTDIR=%{buildroot} prefix=%{_prefix}

%files
%{_bindir}/*
%{_datadir}/%{name}
%{py2_puresitedir}/%{name}
%{py2_puresitedir}/%{name}-*.egg-info
%doc README AUTHORS INSTALL COPYING

