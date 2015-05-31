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
    }

    return spec_template.substitute(values)

if __name__ == '__main__':

    with open('kpatch-patch.spec') as f:
        template = f.read()

    print(generate_rpm_spec(template, 'example.patch'))
