# This file was automatically created by FeynRules 2.3.48
# Mathematica version: 12.3.1 for Mac OS X ARM (64-bit) (July 8, 2021)
# Date: Tue 11 Jan 2022 11:16:58


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '-0.3333333333333333*(ee*complex(0,1))',
                order = {'QED':1})

GC_2 = Coupling(name = 'GC_2',
                value = '(2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_3 = Coupling(name = 'GC_3',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_4 = Coupling(name = 'GC_4',
                value = 'ee*complex(0,1)',
                order = {'QED':1})

GC_5 = Coupling(name = 'GC_5',
                value = 'ee**2*complex(0,1)',
                order = {'QED':2})

GC_6 = Coupling(name = 'GC_6',
                value = '-G',
                order = {'QCD':1})

GC_7 = Coupling(name = 'GC_7',
                value = 'complex(0,1)*G',
                order = {'QCD':1})

GC_8 = Coupling(name = 'GC_8',
                value = 'complex(0,1)*G**2',
                order = {'QCD':2})

GC_9 = Coupling(name = 'GC_9',
                value = '-6*complex(0,1)*lam',
                order = {'QED':2})

GC_10 = Coupling(name = 'GC_10',
                 value = '(FPi**2*complex(0,1))/lc**2',
                 order = {'NP':1})

GC_11 = Coupling(name = 'GC_11',
                 value = '(complex(0,1)*gstar**2)/lc**2',
                 order = {'NP':2})

GC_12 = Coupling(name = 'GC_12',
                 value = '(aEW*complex(0,1))/(6.*FPi*cmath.pi)',
                 order = {'QED':2})

GC_13 = Coupling(name = 'GC_13',
                 value = '(2*aEW*complex(0,1))/(3.*FPi*cmath.pi)',
                 order = {'QED':2})

GC_14 = Coupling(name = 'GC_14',
                 value = '(-5*aEW*complex(0,1))/(12.*FPi*cmath.pi*cmath.sqrt(2)) + (aEW*complex(0,1))/(8.*FPi*cmath.pi*sw**2*cmath.sqrt(2))',
                 order = {'QED':2})

GC_15 = Coupling(name = 'GC_15',
                 value = '(aEW*complex(0,1))/(8.*cw**2*FPi*cmath.pi) - (3*aEW*complex(0,1))/(16.*cw**2*FPi*cmath.pi*sw**2)',
                 order = {'QED':2})

GC_16 = Coupling(name = 'GC_16',
                 value = '-0.25*(aEW*complex(0,1))/(cw**2*FPi*cmath.pi) + (3*aEW*complex(0,1))/(16.*cw**2*FPi*cmath.pi*sw**2)',
                 order = {'QED':2})

GC_17 = Coupling(name = 'GC_17',
                 value = '(ee**2*complex(0,1))/(2.*sw**2)',
                 order = {'QED':2})

GC_18 = Coupling(name = 'GC_18',
                 value = '-((ee**2*complex(0,1))/sw**2)',
                 order = {'QED':2})

GC_19 = Coupling(name = 'GC_19',
                 value = '(cw**2*ee**2*complex(0,1))/sw**2',
                 order = {'QED':2})

GC_20 = Coupling(name = 'GC_20',
                 value = '(-3*aEW*complex(0,1))/(16.*FPi*cmath.pi*sw**2)',
                 order = {'QED':2})

GC_21 = Coupling(name = 'GC_21',
                 value = '(ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_22 = Coupling(name = 'GC_22',
                 value = '(CKM1x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_23 = Coupling(name = 'GC_23',
                 value = '(CKM1x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_24 = Coupling(name = 'GC_24',
                 value = '(CKM2x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_25 = Coupling(name = 'GC_25',
                 value = '(CKM2x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_26 = Coupling(name = 'GC_26',
                 value = '-0.5*(cw*ee*complex(0,1))/sw',
                 order = {'QED':1})

GC_27 = Coupling(name = 'GC_27',
                 value = '(cw*ee*complex(0,1))/sw',
                 order = {'QED':1})

GC_28 = Coupling(name = 'GC_28',
                 value = '(-2*cw*ee**2*complex(0,1))/sw',
                 order = {'QED':2})

GC_29 = Coupling(name = 'GC_29',
                 value = '(-3*aEW*complex(0,1))/(2.*FPi*cmath.pi*sw*cmath.sqrt(2))',
                 order = {'QED':2})

GC_30 = Coupling(name = 'GC_30',
                 value = '(ee*complex(0,1)*sw)/(3.*cw)',
                 order = {'QED':1})

GC_31 = Coupling(name = 'GC_31',
                 value = '(ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_32 = Coupling(name = 'GC_32',
                 value = '(-2*ee*complex(0,1)*sw)/(3.*cw)',
                 order = {'QED':1})

GC_33 = Coupling(name = 'GC_33',
                 value = '-0.5*(cw*ee*complex(0,1))/sw - (ee*complex(0,1)*sw)/(6.*cw)',
                 order = {'QED':1})

GC_34 = Coupling(name = 'GC_34',
                 value = '(cw*ee*complex(0,1))/(2.*sw) - (ee*complex(0,1)*sw)/(6.*cw)',
                 order = {'QED':1})

GC_35 = Coupling(name = 'GC_35',
                 value = '(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_36 = Coupling(name = 'GC_36',
                 value = '-0.125*(aEW*complex(0,1))/(cw*FPi*cmath.pi*sw) + (aEW*complex(0,1)*sw)/(12.*cw*FPi*cmath.pi)',
                 order = {'QED':2})

GC_37 = Coupling(name = 'GC_37',
                 value = '-0.25*(aEW*complex(0,1))/(cw*FPi*cmath.pi*sw) + (aEW*complex(0,1)*sw)/(3.*cw*FPi*cmath.pi)',
                 order = {'QED':2})

GC_38 = Coupling(name = 'GC_38',
                 value = 'ee**2*complex(0,1) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_39 = Coupling(name = 'GC_39',
                 value = '-6*complex(0,1)*lam*vev',
                 order = {'QED':1})

GC_40 = Coupling(name = 'GC_40',
                 value = '(ee**2*complex(0,1)*vev)/(2.*sw**2)',
                 order = {'QED':1})

GC_41 = Coupling(name = 'GC_41',
                 value = 'ee**2*complex(0,1)*vev + (cw**2*ee**2*complex(0,1)*vev)/(2.*sw**2) + (ee**2*complex(0,1)*sw**2*vev)/(2.*cw**2)',
                 order = {'QED':1})

GC_42 = Coupling(name = 'GC_42',
                 value = '-((complex(0,1)*yb)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_43 = Coupling(name = 'GC_43',
                 value = '-((complex(0,1)*yt)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_44 = Coupling(name = 'GC_44',
                 value = '-((complex(0,1)*ytau)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_45 = Coupling(name = 'GC_45',
                 value = '(ee*complex(0,1)*complexconjugate(CKM1x1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_46 = Coupling(name = 'GC_46',
                 value = '(ee*complex(0,1)*complexconjugate(CKM1x2))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_47 = Coupling(name = 'GC_47',
                 value = '(ee*complex(0,1)*complexconjugate(CKM2x1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_48 = Coupling(name = 'GC_48',
                 value = '(ee*complex(0,1)*complexconjugate(CKM2x2))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

