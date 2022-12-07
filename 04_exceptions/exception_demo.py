class SimplestError(Exception): pass
class SimplestErrorType1(SimplestError): pass
#raise SimplestErrorType1('simplest error from %s at %d' % ('testdemo', 1))

try:
    raise SimplestError('simplest error from %s at %d' % ('testdemo', 1))
except SimplestError as se:
    print('catch specific error:')
    print(se, se.args)
except Exception as err:
    print('\n\n\n not known error:')
    print(f"Unexpected {err=}, {type(err)=}")
finally:
    print('finally')