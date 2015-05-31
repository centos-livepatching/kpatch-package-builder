%define kernel %(uname -r)
%define patch module-add-livepatch
%define installdir /var/lib/kpatch

Name:		kpatch-%{patch}
Version:	1
Release:	1%{?dist}
Summary:	kpatch livepatch module - Add livepatch to version

Group:		System Environment/Kernel
License:	GPLv2

Source0:	%{patch}.patch

%description 
Livepatch kernel module. Appends '-livepatch' to /proc/version.

%prep cp %SOURCE0 %{buildroot}

%build
kpatch-build -t vmlinux %SOURCE0

%install
mkdir -p %{buildroot}/%{installdir}/%{kernel}
cp -f "kpatch-%{patch}.ko" "%{buildroot}/%{installdir}/%{kernel}"

%files
%{installdir}/%{kernel}/kpatch-%{patch}.ko
