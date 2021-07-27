# This file was automatically created by FeynRules 2.3.24
# Mathematica version: 10.4.1 for Linux x86 (64-bit) (April 11, 2016)
# Date: Fri 13 Jan 2017 15:25:06


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '-(ee*complex(0,1))/3.',
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
                value = 'complex(0,1)*gstar',
                order = {'NP':1})

GC_10 = Coupling(name = 'GC_10',
                 value = '2*complex(0,1)*gstar',
                 order = {'NP':1})

GC_11 = Coupling(name = 'GC_11',
                 value = '-6*complex(0,1)*lam',
                 order = {'QED':2})

GC_12 = Coupling(name = 'GC_12',
                 value = 'complex(0,1)*gstar*ONE1x1',
                 order = {'NP':1})

GC_13 = Coupling(name = 'GC_13',
                 value = 'complex(0,1)*gstar*ONE1x2',
                 order = {'NP':1})

GC_14 = Coupling(name = 'GC_14',
                 value = 'complex(0,1)*gstar*ONE1x3',
                 order = {'NP':1})

GC_15 = Coupling(name = 'GC_15',
                 value = 'complex(0,1)*gstar*ONE2x1',
                 order = {'NP':1})

GC_16 = Coupling(name = 'GC_16',
                 value = 'complex(0,1)*gstar*ONE2x2',
                 order = {'NP':1})

GC_17 = Coupling(name = 'GC_17',
                 value = 'complex(0,1)*gstar*ONE2x3',
                 order = {'NP':1})

GC_18 = Coupling(name = 'GC_18',
                 value = 'complex(0,1)*gstar*ONE3x1',
                 order = {'NP':1})

GC_19 = Coupling(name = 'GC_19',
                 value = 'complex(0,1)*gstar*ONE3x2',
                 order = {'NP':1})

GC_20 = Coupling(name = 'GC_20',
                 value = 'complex(0,1)*gstar*ONE3x3',
                 order = {'NP':1})

GC_21 = Coupling(name = 'GC_21',
                 value = '(ee**2*complex(0,1))/(2.*sw**2)',
                 order = {'QED':2})

GC_22 = Coupling(name = 'GC_22',
                 value = '-((ee**2*complex(0,1))/sw**2)',
                 order = {'QED':2})

GC_23 = Coupling(name = 'GC_23',
                 value = '(cw**2*ee**2*complex(0,1))/sw**2',
                 order = {'QED':2})

GC_24 = Coupling(name = 'GC_24',
                 value = '(ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_25 = Coupling(name = 'GC_25',
                 value = '(CKM1x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_26 = Coupling(name = 'GC_26',
                 value = '(CKM1x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_27 = Coupling(name = 'GC_27',
                 value = '(CKM2x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_28 = Coupling(name = 'GC_28',
                 value = '(CKM2x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_29 = Coupling(name = 'GC_29',
                 value = '-(cw*ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_30 = Coupling(name = 'GC_30',
                 value = '(cw*ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_31 = Coupling(name = 'GC_31',
                 value = '(cw*ee*complex(0,1))/sw',
                 order = {'QED':1})

GC_32 = Coupling(name = 'GC_32',
                 value = '(-2*cw*ee**2*complex(0,1))/sw',
                 order = {'QED':2})

GC_33 = Coupling(name = 'GC_33',
                 value = '-(ee*complex(0,1)*sw)/(6.*cw)',
                 order = {'QED':1})

GC_34 = Coupling(name = 'GC_34',
                 value = '(ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_35 = Coupling(name = 'GC_35',
                 value = '(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_36 = Coupling(name = 'GC_36',
                 value = 'ee**2*complex(0,1) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_37 = Coupling(name = 'GC_37',
                 value = '-6*complex(0,1)*lam*vev',
                 order = {'QED':1})

GC_38 = Coupling(name = 'GC_38',
                 value = '(ee**2*complex(0,1)*vev)/(2.*sw**2)',
                 order = {'QED':1})

GC_39 = Coupling(name = 'GC_39',
                 value = 'ee**2*complex(0,1)*vev + (cw**2*ee**2*complex(0,1)*vev)/(2.*sw**2) + (ee**2*complex(0,1)*sw**2*vev)/(2.*cw**2)',
                 order = {'QED':1})

GC_40 = Coupling(name = 'GC_40',
                 value = '-((complex(0,1)*yb)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_41 = Coupling(name = 'GC_41',
                 value = '-((complex(0,1)*yt)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_42 = Coupling(name = 'GC_42',
                 value = '-((complex(0,1)*ytau)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_43 = Coupling(name = 'GC_43',
                 value = '(ee*complex(0,1)*complexconjugate(CKM1x1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_44 = Coupling(name = 'GC_44',
                 value = '(ee*complex(0,1)*complexconjugate(CKM1x2))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_45 = Coupling(name = 'GC_45',
                 value = '(ee*complex(0,1)*complexconjugate(CKM2x1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_46 = Coupling(name = 'GC_46',
                 value = '(ee*complex(0,1)*complexconjugate(CKM2x2))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_47 = Coupling(name = 'GC_47',
                 value = '-(gstar*cmath.cos(THETA)*cmath.sqrt(2))',
                 order = {'NP':1})

GC_48 = Coupling(name = 'GC_48',
                 value = 'gstar*cmath.cos(THETA)*cmath.sqrt(2)',
                 order = {'NP':1})

GC_49 = Coupling(name = 'GC_49',
                 value = '-(ee*f3e*complex(0,1)*cmath.cos(THETA))/(4.*cw*lc)',
                 order = {'QED':2})

GC_50 = Coupling(name = 'GC_50',
                 value = '(ee*f3e*complex(0,1)*cmath.cos(THETA))/(4.*lc*sw)',
                 order = {'QED':2})

GC_51 = Coupling(name = 'GC_51',
                 value = '-(ee*f3e*complex(0,1)*cmath.cos(THETA))/(2.*lc*sw*cmath.sqrt(2))',
                 order = {'QED':2})

GC_52 = Coupling(name = 'GC_52',
                 value = 'complex(0,1)*gstar*cmath.sqrt(2)*cmath.sin(THETA)',
                 order = {'NP':1})

GC_53 = Coupling(name = 'GC_53',
                 value = '-(ee*f3e*cmath.sin(THETA))/(4.*cw*lc)',
                 order = {'QED':2})

GC_54 = Coupling(name = 'GC_54',
                 value = '(ee*f3e*cmath.sin(THETA))/(4.*cw*lc)',
                 order = {'QED':2})

GC_55 = Coupling(name = 'GC_55',
                 value = '-(ee*f3e*cmath.sin(THETA))/(4.*lc*sw)',
                 order = {'QED':2})

GC_56 = Coupling(name = 'GC_56',
                 value = '(ee*f3e*cmath.sin(THETA))/(4.*lc*sw)',
                 order = {'QED':2})

GC_57 = Coupling(name = 'GC_57',
                 value = '-(ee*f3e*cmath.sin(THETA))/(2.*lc*sw*cmath.sqrt(2))',
                 order = {'QED':2})

GC_58 = Coupling(name = 'GC_58',
                 value = '(ee*f3e*cmath.sin(THETA))/(2.*lc*sw*cmath.sqrt(2))',
                 order = {'QED':2})

