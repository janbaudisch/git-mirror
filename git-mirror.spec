Name: git-mirror
Version: 0.1.0
Release: 1%{?dist}
Summary: A tool for mirroring a remote git repository to another one
License: GPL-3.0
URL: https://git.sr.ht/~janbaudisch/git-mirror
Source0: https://git.sr.ht/~janbaudisch/git-mirror/archive/%{version}.tar.gz
Requires: git

%description
git-mirror is a tool for mirroring a remote git repository to another one.

%define debug_package %{nil}

%prep
%autosetup

%install
install -Dpm 755 git-mirror %{buildroot}%{_bindir}/git-mirror
install -Dpm 644 git-mirror.1 %{_mandir}/man1/git-mirror.1
gzip %{_mandir}/man1/git-mirror.1

%files
%license LICENSE
%{_bindir}/git-mirror
%{_mandir}/man1/git-mirror.1.gz