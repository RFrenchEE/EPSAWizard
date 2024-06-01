from utilities._program_consts import EPSA_DEBUG

# Debug print
def dprint(s):
    if EPSA_DEBUG:
        print(s)

def pprint_function_called(funcname):
    print(f"Function called: {funcname}()")

def pprint_method_called(classname, methodname):
    print(f"Method Called: {classname}.{methodname}()")