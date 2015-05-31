import os
import string

if __name__ == '__main__':
    patch_file = 'example.patch'
    base_name, _ = os.path.splitext(patch_file)

    values = {
        'name': 'kpatch-module-{}'.format(base_name),
        'patch_file': patch_file,
        'kmod_filename': 'kpatch-{}.ko'.format(base_name),
        'description': 'Package generated from {} by '
                       'kpatch-package-builder'.format(patch_file),
    }

    with open('kpatch-patch.spec') as f:
        spec_template = string.Template(f.read())

    print(spec_template.substitute(values))
