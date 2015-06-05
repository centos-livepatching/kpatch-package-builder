kpatch-package-builder
======================

Generate RPM spec file to package and build a kpatch livepatch module.


    $ kpatch-package-builder --help
    usage: kpatch-package-builder [-h] [-o FILE | -b] [-k VERSION] [-a ARCH] PATCH

    Generate RPM spec file to build a kpatch package

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
