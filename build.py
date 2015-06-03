import argparse
import os
import string

SPEC_TEMPLATE = '''%define kernel $target_kernel.$target_arch
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
'''

def generate_rpm_spec(template, patch_file):
    spec_template = string.Template(template)

    base_name, _ = os.path.splitext(patch_file)

    values = {
        'name': 'kpatch-module-{}'.format(base_name),
        'patch_file': patch_file,
        'kmod_filename': 'kpatch-{}.ko'.format(base_name),
        'description': 'Package generated from {} by '
                       'kpatch-package-builder'.format(patch_file),
        'target_kernel': '3.10.0-229.el7',
        'target_arch': 'x86_64',
    }

    return spec_template.substitute(values)


def get_args():
    parser = argparse.ArgumentParser(description='Generate RPM spec file to '
                                                 'build a kpatch package')
    parser.add_argument('patch', metavar='PATCH',
                        help='patch file from which to build the livepatch '
                             'module')
    parser.add_argument('-o', '--output', metavar='FILE', default=None,
                        help='name of output spec file')

    return parser.parse_args()

if __name__ == '__main__':
    args = get_args()

    spec_content = generate_rpm_spec(SPEC_TEMPLATE, args.patch)

    with open(args.output, 'w') as f:
        f.write(spec_content)
