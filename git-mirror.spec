%define debug_package %{nil}

Name: git-mirror
Version: 0.3.2
Release: 1%{?dist}
Summary: A tool for mirroring a remote git repository to another one
License: GPL-3.0
URL: https://git.sr.ht/~janbaudisch/git-mirror
Source0: https://git.sr.ht/~janbaudisch/git-mirror/archive/%{version}.tar.gz
BuildRequires: systemd
Requires: git

%description
git-mirror is a tool for mirroring a remote git repository to another one.

%prep
%autosetup

%build
gzip git-mirror.1
gzip git-mirror-auto.1

%install
install -Dpm 755 git-mirror %{buildroot}%{_bindir}/git-mirror
install -Dpm 755 git-mirror-auto %{buildroot}%{_bindir}/git-mirror-auto
install -Dpm 644 git-mirror.1.gz %{buildroot}%{_mandir}/man1/git-mirror.1.gz
install -Dpm 644 git-mirror-auto.1.gz %{buildroot}%{_mandir}/man1/git-mirror-auto.1.gz
install -Dpm 644 git-mirror-auto.service %{buildroot}%{_unitdir}/git-mirror-auto.service
install -Dpm 644 git-mirror-auto.timer %{buildroot}%{_unitdir}/git-mirror-auto.timer
install -Dpm 644 git-mirror-auto.env %{buildroot}%{_sysconfdir}/git-mirror/git-mirror-auto.env

%files
%license LICENSE
%{_bindir}/git-mirror
%{_bindir}/git-mirror-auto
%{_mandir}/man1/git-mirror.1.gz
%{_mandir}/man1/git-mirror-auto.1.gz
%{_unitdir}/git-mirror-auto.service
%{_unitdir}/git-mirror-auto.timer
%config(noreplace) %{_sysconfdir}/git-mirror/git-mirror-auto.env
