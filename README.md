kpatch-package-builder
======================

Generate RPM spec file to package and build a kpatch livepatch module.


    $ ./kpatch-package-builder --help
    usage: kpatch-package-builder [-h] [-o FILE | -b] [-k VERSION] [-a ARCH] PATCH

    Build an RPM package or an RPM spec file to install and manage a kpatch
    livepatch module.

    positional arguments:
      PATCH                 patch file from which to build the livepatch module

    optional arguments:
      -h, --help            show this help message and exit
      -o FILE, --output FILE
                            name of output spec file
      -b, --build-rpm       build an RPM package
      -k VERSION, --kernel VERSION
                            target kernel version to build the livepatch module
                            against
      -a ARCH, --arch ARCH  architecture to compile the patch against

    Usage examples:

    Build an RPM package for a given patch:

        $ kpatch-package-builder --build-rpm module.patch

    Generate a spec file to later build into an RPM:

        $ kpatch-package-builder --output module.spec module.patch
