#!/usr/bin/python
from cffi import FFI

ffibuilder = FFI()

ffibuilder.set_source(
    "bluemonday",
    """ //passed to the real C compiler
        #include "bluemonday.h"
    """,
    extra_objects=["bluemonday.so"],
)

ffibuilder.cdef(
    """
    extern long unsigned int NewUGCPolicy();

    extern void DestroyPolicy(long unsigned int p0);

    extern void CallPolicyFunction(long unsigned int p0, char* p1);

    extern void CallPolicyFunctionWithString(long unsigned int p0, char* p1, char* p2);

    extern void CallPolicyFunctionWithBool(long unsigned int p0, char* p1, unsigned int p2);

    extern char* SanitizeWithPolicy(long unsigned int p0, char* p1);
    """
)

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)