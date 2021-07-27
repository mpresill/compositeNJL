# This file was automatically created by FeynRules 2.3.29
# Mathematica version: 11.1.1 for Mac OS X x86 (64-bit) (April 27, 2017)
# Date: Tue 2 Jan 2018 13:09:03



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

f3u = Parameter(name = 'f3u',
                nature = 'external',
                type = 'real',
                value = 1.,
                texname = '\\text{f3u}',
                lhablock = 'FRBlock',
                lhacode = [ 1 ])

f3d = Parameter(name = 'f3d',
                nature = 'external',
                type = 'real',
                value = 1.,
                texname = '\\text{f3d}',
                lhablock = 'FRBlock',
                lhacode = [ 2 ])

f3e = Parameter(name = 'f3e',
                nature = 'external',
                type = 'real',
                value = 1.,
                texname = '\\text{f3e}',
                lhablock = 'FRBlock',
                lhacode = [ 3 ])

lc = Parameter(name = 'lc',
               nature = 'external',
               type = 'real',
               value = 5000.,
               texname = '\\text{lc}',
               lhablock = 'FRBlock',
               lhacode = [ 4 ])

MUU = Parameter(name = 'MUU',
                nature = 'external',
                type = 'real',
                value = 5000.,
                texname = '\\text{MUU}',
                lhablock = 'FRBlock',
                lhacode = [ 5 ])

ML = Parameter(name = 'ML',
               nature = 'external',
               type = 'real',
               value = 50.,
               texname = '\\text{ML}',
               lhablock = 'FRBlock',
               lhacode = [ 6 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

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
               value = 125,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

MUs = Parameter(name = 'MUs',
                nature = 'external',
                type = 'real',
                value = 1000,
                texname = '\\text{MUs}',
                lhablock = 'MASS',
                lhacode = [ 4000002 ])

MCs = Parameter(name = 'MCs',
                nature = 'external',
                type = 'real',
                value = 1000,
                texname = '\\text{MCs}',
                lhablock = 'MASS',
                lhacode = [ 4000004 ])

MTs = Parameter(name = 'MTs',
                nature = 'external',
                type = 'real',
                value = 1000,
                texname = '\\text{MTs}',
                lhablock = 'MASS',
                lhacode = [ 4000006 ])

MDs = Parameter(name = 'MDs',
                nature = 'external',
                type = 'real',
                value = 1000,
                texname = '\\text{MDs}',
                lhablock = 'MASS',
                lhacode = [ 4000008 ])

MSs = Parameter(name = 'MSs',
                nature = 'external',
                type = 'real',
                value = 1000,
                texname = '\\text{MSs}',
                lhablock = 'MASS',
                lhacode = [ 4000010 ])

MBs = Parameter(name = 'MBs',
                nature = 'external',
                type = 'real',
                value = 1000,
                texname = '\\text{MBs}',
                lhablock = 'MASS',
                lhacode = [ 4000011 ])

MEs = Parameter(name = 'MEs',
                nature = 'external',
                type = 'real',
                value = 1000,
                texname = '\\text{MEs}',
                lhablock = 'MASS',
                lhacode = [ 4000018 ])

MMus = Parameter(name = 'MMus',
                 nature = 'external',
                 type = 'real',
                 value = 1000,
                 texname = '\\text{MMus}',
                 lhablock = 'MASS',
                 lhacode = [ 4000020 ])

MTaus = Parameter(name = 'MTaus',
                  nature = 'external',
                  type = 'real',
                  value = 1000,
                  texname = '\\text{MTaus}',
                  lhablock = 'MASS',
                  lhacode = [ 4000022 ])

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
               value = 0.00407,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

WUs = Parameter(name = 'WUs',
                nature = 'external',
                type = 'real',
                value = 30,
                texname = '\\text{WUs}',
                lhablock = 'DECAY',
                lhacode = [ 4000002 ])

WCs = Parameter(name = 'WCs',
                nature = 'external',
                type = 'real',
                value = 30,
                texname = '\\text{WCs}',
                lhablock = 'DECAY',
                lhacode = [ 4000004 ])

WTs = Parameter(name = 'WTs',
                nature = 'external',
                type = 'real',
                value = 30,
                texname = '\\text{WTs}',
                lhablock = 'DECAY',
                lhacode = [ 4000006 ])

WDs = Parameter(name = 'WDs',
                nature = 'external',
                type = 'real',
                value = 30,
                texname = '\\text{WDs}',
                lhablock = 'DECAY',
                lhacode = [ 4000008 ])

WSs = Parameter(name = 'WSs',
                nature = 'external',
                type = 'real',
                value = 30,
                texname = '\\text{WSs}',
                lhablock = 'DECAY',
                lhacode = [ 4000010 ])

WBs = Parameter(name = 'WBs',
                nature = 'external',
                type = 'real',
                value = 30,
                texname = '\\text{WBs}',
                lhablock = 'DECAY',
                lhacode = [ 4000011 ])

WN1Es = Parameter(name = 'WN1Es',
                  nature = 'external',
                  type = 'real',
                  value = 30,
                  texname = '\\text{WN1Es}',
                  lhablock = 'DECAY',
                  lhacode = [ 4000012 ])

WN1Mus = Parameter(name = 'WN1Mus',
                   nature = 'external',
                   type = 'real',
                   value = 30,
                   texname = '\\text{WN1Mus}',
                   lhablock = 'DECAY',
                   lhacode = [ 4000014 ])

WN1Taus = Parameter(name = 'WN1Taus',
                    nature = 'external',
                    type = 'real',
                    value = 30,
                    texname = '\\text{WN1Taus}',
                    lhablock = 'DECAY',
                    lhacode = [ 4000016 ])

WN2Es = Parameter(name = 'WN2Es',
                  nature = 'external',
                  type = 'real',
                  value = 30,
                  texname = '\\text{WN2Es}',
                  lhablock = 'DECAY',
                  lhacode = [ 4000013 ])

WN2Mus = Parameter(name = 'WN2Mus',
                   nature = 'external',
                   type = 'real',
                   value = 30,
                   texname = '\\text{WN2Mus}',
                   lhablock = 'DECAY',
                   lhacode = [ 4000015 ])

WN2Taus = Parameter(name = 'WN2Taus',
                    nature = 'external',
                    type = 'real',
                    value = 30,
                    texname = '\\text{WN2Taus}',
                    lhablock = 'DECAY',
                    lhacode = [ 4000017 ])

WEs = Parameter(name = 'WEs',
                nature = 'external',
                type = 'real',
                value = 30,
                texname = '\\text{WEs}',
                lhablock = 'DECAY',
                lhacode = [ 4000018 ])

WMus = Parameter(name = 'WMus',
                 nature = 'external',
                 type = 'real',
                 value = 30,
                 texname = '\\text{WMus}',
                 lhablock = 'DECAY',
                 lhacode = [ 4000020 ])

WTaus = Parameter(name = 'WTaus',
                  nature = 'external',
                  type = 'real',
                  value = 30,
                  texname = '\\text{WTaus}',
                  lhablock = 'DECAY',
                  lhacode = [ 4000022 ])

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

M1s = Parameter(name = 'M1s',
                nature = 'internal',
                type = 'real',
                value = 'abs(ML/2. - cmath.sqrt(ML**2 + 4*MUU**2)/2.)',
                texname = '\\text{M1s}')

M2s = Parameter(name = 'M2s',
                nature = 'internal',
                type = 'real',
                value = 'abs(ML/2. + cmath.sqrt(ML**2 + 4*MUU**2)/2.)',
                texname = '\\text{M2s}')

Maux = Parameter(name = 'Maux',
                 nature = 'internal',
                 type = 'real',
                 value = 'lc',
                 texname = '\\text{Maux}')

Mauxo = Parameter(name = 'Mauxo',
                  nature = 'internal',
                  type = 'real',
                  value = 'lc',
                  texname = '\\text{Mauxo}')

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

THETA = Parameter(name = 'THETA',
                  nature = 'internal',
                  type = 'real',
                  value = '-cmath.atan((2*MUU)/ML)/2.',
                  texname = '\\Theta')

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

