# This file was automatically created by FeynRules 2.3.48
# Mathematica version: 12.3.1 for Mac OS X ARM (64-bit) (July 8, 2021)
# Date: Tue 11 Jan 2022 11:16:58



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
cabi = Parameter(name = 'cabi',
                 nature = 'external',
                 type = 'real',
                 value = 0.227736,
                 texname = '\\theta _c',
                 lhablock = 'CKMBLOCK',
                 lhacode = [ 1 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

lc = Parameter(name = 'lc',
               nature = 'external',
               type = 'real',
               value = 5400.,
               texname = '\\text{lc}',
               lhablock = 'FRBlock',
               lhacode = [ 1 ])

muu = Parameter(name = 'muu',
                nature = 'external',
                type = 'real',
                value = 5400.,
                texname = '\\text{muu}',
                lhablock = 'FRBlock',
                lhacode = [ 2 ])

mpi = Parameter(name = 'mpi',
                nature = 'external',
                type = 'real',
                value = 1000.,
                texname = '\\text{mpi}',
                lhablock = 'FRBlock',
                lhacode = [ 3 ])

FPi = Parameter(name = 'FPi',
                nature = 'external',
                type = 'real',
                value = 5000.,
                texname = '\\text{FPi}',
                lhablock = 'FRBlock',
                lhacode = [ 4 ])

cabi2 = Parameter(name = 'cabi2',
                  nature = 'external',
                  type = 'real',
                  value = 0.227736,
                  texname = '\\text{cabi2}',
                  lhablock = 'FRBlock',
                  lhacode = [ 5 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MM = Parameter(name = 'MM',
               nature = 'external',
               type = 'real',
               value = 0.10566,
               texname = '\\text{MM}',
               lhablock = 'MASS',
               lhacode = [ 13 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 120,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

MPic1 = Parameter(name = 'MPic1',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{MPic1}',
                  lhablock = 'MASS',
                  lhacode = [ 9000006 ])

MPi0u = Parameter(name = 'MPi0u',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{MPi0u}',
                  lhablock = 'MASS',
                  lhacode = [ 9000007 ])

MPi0d = Parameter(name = 'MPi0d',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{MPi0d}',
                  lhablock = 'MASS',
                  lhacode = [ 9000008 ])

MPi53 = Parameter(name = 'MPi53',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{MPi53}',
                  lhablock = 'MASS',
                  lhacode = [ 9000009 ])

MPi13 = Parameter(name = 'MPi13',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{MPi13}',
                  lhablock = 'MASS',
                  lhacode = [ 9000010 ])

MPiu23 = Parameter(name = 'MPiu23',
                   nature = 'external',
                   type = 'real',
                   value = 1,
                   texname = '\\text{MPiu23}',
                   lhablock = 'MASS',
                   lhacode = [ 9000011 ])

MPid23 = Parameter(name = 'MPid23',
                   nature = 'external',
                   type = 'real',
                   value = 1,
                   texname = '\\text{MPid23}',
                   lhablock = 'MASS',
                   lhacode = [ 9000012 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00575308848,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

WEs = Parameter(name = 'WEs',
                nature = 'external',
                type = 'real',
                value = 30,
                texname = '\\text{WEs}',
                lhablock = 'DECAY',
                lhacode = [ 4000002 ])

WMus = Parameter(name = 'WMus',
                 nature = 'external',
                 type = 'real',
                 value = 30,
                 texname = '\\text{WMus}',
                 lhablock = 'DECAY',
                 lhacode = [ 4000004 ])

WTaus = Parameter(name = 'WTaus',
                  nature = 'external',
                  type = 'real',
                  value = 30,
                  texname = '\\text{WTaus}',
                  lhablock = 'DECAY',
                  lhacode = [ 4000006 ])

WNc1 = Parameter(name = 'WNc1',
                 nature = 'external',
                 type = 'real',
                 value = 30,
                 texname = '\\text{WNc1}',
                 lhablock = 'DECAY',
                 lhacode = [ 4000008 ])

WNc2 = Parameter(name = 'WNc2',
                 nature = 'external',
                 type = 'real',
                 value = 30,
                 texname = '\\text{WNc2}',
                 lhablock = 'DECAY',
                 lhacode = [ 4000010 ])

WNc3 = Parameter(name = 'WNc3',
                 nature = 'external',
                 type = 'real',
                 value = 30,
                 texname = '\\text{WNc3}',
                 lhablock = 'DECAY',
                 lhacode = [ 4000012 ])

WEc = Parameter(name = 'WEc',
                nature = 'external',
                type = 'real',
                value = 30,
                texname = '\\text{WEc}',
                lhablock = 'DECAY',
                lhacode = [ 4000014 ])

WMuc = Parameter(name = 'WMuc',
                 nature = 'external',
                 type = 'real',
                 value = 30,
                 texname = '\\text{WMuc}',
                 lhablock = 'DECAY',
                 lhacode = [ 4000016 ])

WTauc = Parameter(name = 'WTauc',
                  nature = 'external',
                  type = 'real',
                  value = 30,
                  texname = '\\text{WTauc}',
                  lhablock = 'DECAY',
                  lhacode = [ 4000018 ])

WN01 = Parameter(name = 'WN01',
                 nature = 'external',
                 type = 'real',
                 value = 30,
                 texname = '\\text{WN01}',
                 lhablock = 'DECAY',
                 lhacode = [ 4000020 ])

WN02 = Parameter(name = 'WN02',
                 nature = 'external',
                 type = 'real',
                 value = 30,
                 texname = '\\text{WN02}',
                 lhablock = 'DECAY',
                 lhacode = [ 4000022 ])

WN03 = Parameter(name = 'WN03',
                 nature = 'external',
                 type = 'real',
                 value = 30,
                 texname = '\\text{WN03}',
                 lhablock = 'DECAY',
                 lhacode = [ 4000024 ])

WPic1 = Parameter(name = 'WPic1',
                  nature = 'external',
                  type = 'real',
                  value = 30,
                  texname = '\\text{WPic1}',
                  lhablock = 'DECAY',
                  lhacode = [ 9000006 ])

WPi0u = Parameter(name = 'WPi0u',
                  nature = 'external',
                  type = 'real',
                  value = 30,
                  texname = '\\text{WPi0u}',
                  lhablock = 'DECAY',
                  lhacode = [ 9000007 ])

WPi0d = Parameter(name = 'WPi0d',
                  nature = 'external',
                  type = 'real',
                  value = 30,
                  texname = '\\text{WPi0d}',
                  lhablock = 'DECAY',
                  lhacode = [ 9000008 ])

WPi53 = Parameter(name = 'WPi53',
                  nature = 'external',
                  type = 'real',
                  value = 30,
                  texname = '\\text{WPi53}',
                  lhablock = 'DECAY',
                  lhacode = [ 9000009 ])

WPi13 = Parameter(name = 'WPi13',
                  nature = 'external',
                  type = 'real',
                  value = 30,
                  texname = '\\text{WPi13}',
                  lhablock = 'DECAY',
                  lhacode = [ 9000010 ])

WPiu23 = Parameter(name = 'WPiu23',
                   nature = 'external',
                   type = 'real',
                   value = 30,
                   texname = '\\text{WPiu23}',
                   lhablock = 'DECAY',
                   lhacode = [ 9000011 ])

WPid23 = Parameter(name = 'WPid23',
                   nature = 'external',
                   type = 'real',
                   value = 30,
                   texname = '\\text{WPid23}',
                   lhablock = 'DECAY',
                   lhacode = [ 9000012 ])

CKM1x1 = Parameter(name = 'CKM1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM1x1}')

CKM1x2 = Parameter(name = 'CKM1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.sin(cabi)',
                   texname = '\\text{CKM1x2}')

CKM2x1 = Parameter(name = 'CKM2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '-cmath.sin(cabi)',
                   texname = '\\text{CKM2x1}')

CKM2x2 = Parameter(name = 'CKM2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM2x2}')

MPi = Parameter(name = 'MPi',
                nature = 'internal',
                type = 'real',
                value = 'mpi',
                texname = '\\text{MPi}')

MUU = Parameter(name = 'MUU',
                nature = 'internal',
                type = 'real',
                value = 'muu',
                texname = '\\text{MUU}')

ONE1x1 = Parameter(name = 'ONE1x1',
                   nature = 'internal',
                   type = 'real',
                   value = '1',
                   texname = '\\text{ONE1x1}')

ONE1x2 = Parameter(name = 'ONE1x2',
                   nature = 'internal',
                   type = 'real',
                   value = '1',
                   texname = '\\text{ONE1x2}')

ONE1x3 = Parameter(name = 'ONE1x3',
                   nature = 'internal',
                   type = 'real',
                   value = '1',
                   texname = '\\text{ONE1x3}')

ONE2x1 = Parameter(name = 'ONE2x1',
                   nature = 'internal',
                   type = 'real',
                   value = '1',
                   texname = '\\text{ONE2x1}')

ONE2x2 = Parameter(name = 'ONE2x2',
                   nature = 'internal',
                   type = 'real',
                   value = '1',
                   texname = '\\text{ONE2x2}')

ONE2x3 = Parameter(name = 'ONE2x3',
                   nature = 'internal',
                   type = 'real',
                   value = '1',
                   texname = '\\text{ONE2x3}')

ONE3x1 = Parameter(name = 'ONE3x1',
                   nature = 'internal',
                   type = 'real',
                   value = '1',
                   texname = '\\text{ONE3x1}')

ONE3x2 = Parameter(name = 'ONE3x2',
                   nature = 'internal',
                   type = 'real',
                   value = '1',
                   texname = '\\text{ONE3x2}')

ONE3x3 = Parameter(name = 'ONE3x3',
                   nature = 'internal',
                   type = 'real',
                   value = '1',
                   texname = '\\text{ONE3x3}')

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

gstar = Parameter(name = 'gstar',
                  nature = 'internal',
                  type = 'real',
                  value = '2*cmath.sqrt(cmath.pi)',
                  texname = '\\text{gstar}')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*vev**2)',
                texname = '\\text{lam}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vev',
               texname = '\\text{yb}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')

