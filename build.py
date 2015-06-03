import argparse
import os
import string


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

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate RPM spec file to '
                                                 'build a kpatch package')
    parser.add_argument('patch', metavar='PATCH',
                        help='patch file from which to build the livepatch '
                             'module')

    args = parser.parse_args()

    with open('kpatch-patch.spec') as f:
        template = f.read()

    print(generate_rpm_spec(template, args.patch))
