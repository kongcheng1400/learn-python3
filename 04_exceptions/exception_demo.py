class SimplestError(Exception): pass
class SimplestErrorType1(SimplestError): pass
raise SimplestErrorType1('simplest error from %s at %d' % ('testdemo', 1))
'''
try:
    raise SimplestError('simplest error from %s at %d' % ('testdemo', 1))
finally:
    print('finally')

except SimplestError as se:
    print(se, se.args)
'''