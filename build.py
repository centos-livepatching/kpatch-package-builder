import string

if __name__ == '__main__':
    values = {
        'patch_file': 'example.patch',
    }

    with open('kpatch-patch.spec') as f:
        spec_template = string.Template(f.read())

    print(spec_template.substitute(values))
