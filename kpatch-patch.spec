%define kernel $target_kernel.$target_arch
%define installdir /var/lib/kpatch

Name:		$name
Version:	1
Release:	1%{?dist}
Summary:	kpatch livepatch module

Group:		System Environment/Kernel
License:	GPLv2

Source0:	$patch_file

ExclusiveArch: $target_arch

%description 
$description

%prep cp %SOURCE0 %{buildroot}
yumdownloader --source "kernel-$target_kernel"

%build
kpatch-build -t vmlinux --sourcerpm "kernel-$target_kernel.src.rpm" %SOURCE0

%install
mkdir -p %{buildroot}/%{installdir}/%{kernel}
cp -f "$kmod_filename" "%{buildroot}/%{installdir}/%{kernel}"

%files
%{installdir}/%{kernel}/$kmod_filename
