from cffi import FFI

ffibuilder = FFI()

with open('./pymeos_cffi/builder/meos.h', 'r') as f:
    content = f.read()
ffibuilder.cdef(content)

ffibuilder.set_source('_meos_cffi',
                      '#include "meos_mod.h"   // the C header of the library',
                      include_dirs = ['/Users/zaynluo/Documents/temp_pymeos', '/usr/local/include'],
                      library_dirs = ['/usr/local/lib'],
                      libraries=['meos'], )  # library name, for the linker

if __name__ == "__main__":  # not when running with setuptools
    ffibuilder.compile(verbose=True)
