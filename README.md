kpatch-package-builder
======================

Build RPM packages to install and manage kernel livepatch modules.

Dependencies
------------

kpatch-package-builder depends on PyYaml and Jinja2. To install on Fedora,
CentOS and other Red Hat systems:

    $ sudo yum install python-yaml python-jinja2


Manifest files
--------------

Manifest files describe a set of packages, with each package containing one or
more patches built for particular kernel versions.

Here is a minimalistic example, which describes a single package,
`livepatch-test`. This package contains a single kernel patch, which is built
for a single kernel version (`3.10.0-229.el7`):

```yaml
packages:
  - name: livepatch-test
    version: 1
    patches:
      - filename: livepatch-test.patch
        kernels:
          - 3.10.0-229.el7
```

Help
----

    $ kpatch-package-builder -h
    usage: kpatch-package-builder [-h] [-v] (-p PATCH | --manifest FILE)
                                  [-o FILE | -b] [-k VERSION] [-a ARCH]
                                  [--set-release NUM] [--set-version NUM] [-d]

    Build an RPM package or an RPM spec file to install and manage a kpatch
    livepatch module.

    optional arguments:
      -h, --help            show this help message and exit
      -v, --version         show program's version number and exit
      -p PATCH, --patch PATCH
                            patch file from which to build the livepatch module
      --manifest FILE       manifest file describing a mapping between packages,
                            patches and kernel versions
      -o FILE, --output FILE
                            name of output spec file
      -b, --build-rpm       build an RPM package
      -k VERSION, --kernel VERSION
                            target kernel version to build the livepatch module
                            against. Defaults to the currently running version
      -a ARCH, --arch ARCH  architecture to compile the patch against
      --set-release NUM     package release version
      --set-version NUM     package version number
      -d, --debug           print debug information

    Usage examples:

    Build an RPM package for a given patch:

        $ kpatch-package-builder --build-rpm module.patch

    Generate a spec file to later build into an RPM:

        $ kpatch-package-builder --output module.spec module.patch

