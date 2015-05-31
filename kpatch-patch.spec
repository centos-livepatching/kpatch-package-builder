%define kernel %(uname -r)
%define installdir /var/lib/kpatch

Name:		$name
Version:	1
Release:	1%{?dist}
Summary:	kpatch livepatch module

Group:		System Environment/Kernel
License:	GPLv2

Source0:	$patch_file

%description 
$description

%prep cp %SOURCE0 %{buildroot}

%build
kpatch-build -t vmlinux %SOURCE0

%install
mkdir -p %{buildroot}/%{installdir}/%{kernel}
cp -f "$kmod_filename" "%{buildroot}/%{installdir}/%{kernel}"

%files
%{installdir}/%{kernel}/$kmod_filename
