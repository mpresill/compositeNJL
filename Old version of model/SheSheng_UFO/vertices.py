# This file was automatically created by FeynRules 2.3.48
# Mathematica version: 12.3.1 for Mac OS X ARM (64-bit) (July 8, 2021)
# Date: Tue 11 Jan 2022 11:16:58


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.g, P.g, P.g ],
             color = [ 'f(1,2,3)' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_6})

V_2 = Vertex(name = 'V_2',
             particles = [ P.g, P.g, P.g, P.g ],
             color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
             lorentz = [ L.VVVV1, L.VVVV3, L.VVVV4 ],
             couplings = {(1,1):C.GC_8,(0,0):C.GC_8,(2,2):C.GC_8})

V_3 = Vertex(name = 'V_3',
             particles = [ P.a, P.W__minus__, P.W__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_4})

V_4 = Vertex(name = 'V_4',
             particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VVVV2 ],
             couplings = {(0,0):C.GC_5})

V_5 = Vertex(name = 'V_5',
             particles = [ P.W__minus__, P.W__plus__, P.Z ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_27})

V_6 = Vertex(name = 'V_6',
             particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VVVV2 ],
             couplings = {(0,0):C.GC_18})

V_7 = Vertex(name = 'V_7',
             particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
             color = [ '1' ],
             lorentz = [ L.VVVV5 ],
             couplings = {(0,0):C.GC_28})

V_8 = Vertex(name = 'V_8',
             particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
             color = [ '1' ],
             lorentz = [ L.VVVV2 ],
             couplings = {(0,0):C.GC_19})

V_9 = Vertex(name = 'V_9',
             particles = [ P.e__plus__, P.e__minus__, P.a ],
             color = [ '1' ],
             lorentz = [ L.FFV1 ],
             couplings = {(0,0):C.GC_3})

V_10 = Vertex(name = 'V_10',
              particles = [ P.mu__plus__, P.mu__minus__, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_3})

V_11 = Vertex(name = 'V_11',
              particles = [ P.ta__plus__, P.ta__minus__, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_3})

V_12 = Vertex(name = 'V_12',
              particles = [ P.c__tilde__, P.c, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_2})

V_13 = Vertex(name = 'V_13',
              particles = [ P.t__tilde__, P.t, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_2})

V_14 = Vertex(name = 'V_14',
              particles = [ P.u__tilde__, P.u, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_2})

V_15 = Vertex(name = 'V_15',
              particles = [ P.b__tilde__, P.b, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_1})

V_16 = Vertex(name = 'V_16',
              particles = [ P.d__tilde__, P.d, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_1})

V_17 = Vertex(name = 'V_17',
              particles = [ P.s__tilde__, P.s, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_1})

V_18 = Vertex(name = 'V_18',
              particles = [ P.c__tilde__, P.c, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_7})

V_19 = Vertex(name = 'V_19',
              particles = [ P.t__tilde__, P.t, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_7})

V_20 = Vertex(name = 'V_20',
              particles = [ P.u__tilde__, P.u, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_7})

V_21 = Vertex(name = 'V_21',
              particles = [ P.b__tilde__, P.b, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_7})

V_22 = Vertex(name = 'V_22',
              particles = [ P.d__tilde__, P.d, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_7})

V_23 = Vertex(name = 'V_23',
              particles = [ P.s__tilde__, P.s, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_7})

V_24 = Vertex(name = 'V_24',
              particles = [ P.d__tilde__, P.c, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_24})

V_25 = Vertex(name = 'V_25',
              particles = [ P.s__tilde__, P.c, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_25})

V_26 = Vertex(name = 'V_26',
              particles = [ P.b__tilde__, P.t, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_21})

V_27 = Vertex(name = 'V_27',
              particles = [ P.d__tilde__, P.u, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_22})

V_28 = Vertex(name = 'V_28',
              particles = [ P.s__tilde__, P.u, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_23})

V_29 = Vertex(name = 'V_29',
              particles = [ P.t__tilde__, P.b, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_21})

V_30 = Vertex(name = 'V_30',
              particles = [ P.c__tilde__, P.d, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_47})

V_31 = Vertex(name = 'V_31',
              particles = [ P.u__tilde__, P.d, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_45})

V_32 = Vertex(name = 'V_32',
              particles = [ P.c__tilde__, P.s, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_48})

V_33 = Vertex(name = 'V_33',
              particles = [ P.u__tilde__, P.s, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_46})

V_34 = Vertex(name = 'V_34',
              particles = [ P.e__plus__, P.ve, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_21})

V_35 = Vertex(name = 'V_35',
              particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_21})

V_36 = Vertex(name = 'V_36',
              particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_21})

V_37 = Vertex(name = 'V_37',
              particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_21})

V_38 = Vertex(name = 'V_38',
              particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_21})

V_39 = Vertex(name = 'V_39',
              particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_21})

V_40 = Vertex(name = 'V_40',
              particles = [ P.c__tilde__, P.c, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_34,(0,1):C.GC_32})

V_41 = Vertex(name = 'V_41',
              particles = [ P.t__tilde__, P.t, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_34,(0,1):C.GC_32})

V_42 = Vertex(name = 'V_42',
              particles = [ P.u__tilde__, P.u, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_34,(0,1):C.GC_32})

V_43 = Vertex(name = 'V_43',
              particles = [ P.b__tilde__, P.b, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_33,(0,1):C.GC_30})

V_44 = Vertex(name = 'V_44',
              particles = [ P.d__tilde__, P.d, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_33,(0,1):C.GC_30})

V_45 = Vertex(name = 'V_45',
              particles = [ P.s__tilde__, P.s, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_33,(0,1):C.GC_30})

V_46 = Vertex(name = 'V_46',
              particles = [ P.ve__tilde__, P.ve, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_35})

V_47 = Vertex(name = 'V_47',
              particles = [ P.vm__tilde__, P.vm, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_35})

V_48 = Vertex(name = 'V_48',
              particles = [ P.vt__tilde__, P.vt, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_35})

V_49 = Vertex(name = 'V_49',
              particles = [ P.e__plus__, P.e__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2, L.FFV4 ],
              couplings = {(0,0):C.GC_26,(0,1):C.GC_31})

V_50 = Vertex(name = 'V_50',
              particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2, L.FFV4 ],
              couplings = {(0,0):C.GC_26,(0,1):C.GC_31})

V_51 = Vertex(name = 'V_51',
              particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2, L.FFV4 ],
              couplings = {(0,0):C.GC_26,(0,1):C.GC_31})

V_52 = Vertex(name = 'V_52',
              particles = [ P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_9})

V_53 = Vertex(name = 'V_53',
              particles = [ P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_39})

V_54 = Vertex(name = 'V_54',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_17})

V_55 = Vertex(name = 'V_55',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS4 ],
              couplings = {(0,0):C.GC_40})

V_56 = Vertex(name = 'V_56',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_38})

V_57 = Vertex(name = 'V_57',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS4 ],
              couplings = {(0,0):C.GC_41})

V_58 = Vertex(name = 'V_58',
              particles = [ P.b__tilde__, P.b, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS4 ],
              couplings = {(0,0):C.GC_42})

V_59 = Vertex(name = 'V_59',
              particles = [ P.ta__plus__, P.ta__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS4 ],
              couplings = {(0,0):C.GC_44})

V_60 = Vertex(name = 'V_60',
              particles = [ P.t__tilde__, P.t, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS4 ],
              couplings = {(0,0):C.GC_43})

V_61 = Vertex(name = 'V_61',
              particles = [ P.ghG, P.ghG__tilde__, P.g ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_6})

V_62 = Vertex(name = 'V_62',
              particles = [ P.a, P.a, P.Pi0d ],
              color = [ '1' ],
              lorentz = [ L.VVS3 ],
              couplings = {(0,0):C.GC_12})

V_63 = Vertex(name = 'V_63',
              particles = [ P.a, P.a, P.Pi0u ],
              color = [ '1' ],
              lorentz = [ L.VVS3 ],
              couplings = {(0,0):C.GC_13})

V_64 = Vertex(name = 'V_64',
              particles = [ P.a, P.W__minus__, P.Pic1__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_29})

V_65 = Vertex(name = 'V_65',
              particles = [ P.a, P.W__plus__, P.Pic1__tilde__ ],
              color = [ '1' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_29})

V_66 = Vertex(name = 'V_66',
              particles = [ P.W__minus__, P.W__plus__, P.Pi0d ],
              color = [ '1' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_20})

V_67 = Vertex(name = 'V_67',
              particles = [ P.W__minus__, P.W__plus__, P.Pi0u ],
              color = [ '1' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_20})

V_68 = Vertex(name = 'V_68',
              particles = [ P.W__minus__, P.Z, P.Pic1__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_14})

V_69 = Vertex(name = 'V_69',
              particles = [ P.W__plus__, P.Z, P.Pic1__tilde__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_14})

V_70 = Vertex(name = 'V_70',
              particles = [ P.a, P.Z, P.Pi0d ],
              color = [ '1' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_36})

V_71 = Vertex(name = 'V_71',
              particles = [ P.a, P.Z, P.Pi0u ],
              color = [ '1' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_37})

V_72 = Vertex(name = 'V_72',
              particles = [ P.Z, P.Z, P.Pi0d ],
              color = [ '1' ],
              lorentz = [ L.VVS3 ],
              couplings = {(0,0):C.GC_15})

V_73 = Vertex(name = 'V_73',
              particles = [ P.Z, P.Z, P.Pi0u ],
              color = [ '1' ],
              lorentz = [ L.VVS3 ],
              couplings = {(0,0):C.GC_16})

V_74 = Vertex(name = 'V_74',
              particles = [ P.d__tilde__, P.d, P.Pi0d ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_10})

V_75 = Vertex(name = 'V_75',
              particles = [ P.E0__tilde__, P.e__minus__, P.Pic1__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_10})

V_76 = Vertex(name = 'V_76',
              particles = [ P.e__plus__, P.Ec, P.Pi0d ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_10})

V_77 = Vertex(name = 'V_77',
              particles = [ P.ve__tilde__, P.N01, P.Pi0u ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_10})

V_78 = Vertex(name = 'V_78',
              particles = [ P.ve__tilde__, P.Nc1, P.Pic1__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_10})

V_79 = Vertex(name = 'V_79',
              particles = [ P.d__tilde__, P.u, P.Pic1__tilde__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_10})

V_80 = Vertex(name = 'V_80',
              particles = [ P.u__tilde__, P.u, P.Pi0u ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_10})

V_81 = Vertex(name = 'V_81',
              particles = [ P.ve__tilde__, P.d, P.Pi13__tilde__ ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_10})

V_82 = Vertex(name = 'V_82',
              particles = [ P.e__plus__, P.u, P.Pi53__tilde__ ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_10})

V_83 = Vertex(name = 'V_83',
              particles = [ P.e__plus__, P.d, P.Pid23__tilde__ ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_10})

V_84 = Vertex(name = 'V_84',
              particles = [ P.ve__tilde__, P.u, P.Piu23__tilde__ ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_10})

V_85 = Vertex(name = 'V_85',
              particles = [ P.u__tilde__, P.d, P.Pic1__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_10})

V_86 = Vertex(name = 'V_86',
              particles = [ P.e__plus__, P.E0, P.Pic1__tilde__ ],
              color = [ '1' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_10})

V_87 = Vertex(name = 'V_87',
              particles = [ P.u__tilde__, P.d, P.e__plus__, P.E0 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF1 ],
              couplings = {(0,0):C.GC_11})

V_88 = Vertex(name = 'V_88',
              particles = [ P.c__tilde__, P.s, P.mu__plus__, P.Mu0 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF1 ],
              couplings = {(0,0):C.GC_11})

V_89 = Vertex(name = 'V_89',
              particles = [ P.t__tilde__, P.b, P.ta__plus__, P.Tau0 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF1 ],
              couplings = {(0,0):C.GC_11})

V_90 = Vertex(name = 'V_90',
              particles = [ P.Ec__tilde__, P.e__minus__, P.Pi0d ],
              color = [ '1' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_10})

V_91 = Vertex(name = 'V_91',
              particles = [ P.Ec__tilde__, P.e__minus__, P.d__tilde__, P.d ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1 ],
              couplings = {(0,0):C.GC_11})

V_92 = Vertex(name = 'V_92',
              particles = [ P.Muc__tilde__, P.mu__minus__, P.s__tilde__, P.s ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1 ],
              couplings = {(0,0):C.GC_11})

V_93 = Vertex(name = 'V_93',
              particles = [ P.Tauc__tilde__, P.ta__minus__, P.b__tilde__, P.b ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1 ],
              couplings = {(0,0):C.GC_11})

V_94 = Vertex(name = 'V_94',
              particles = [ P.d__tilde__, P.d, P.e__plus__, P.Ec ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF1 ],
              couplings = {(0,0):C.GC_11})

V_95 = Vertex(name = 'V_95',
              particles = [ P.s__tilde__, P.s, P.mu__plus__, P.Muc ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF1 ],
              couplings = {(0,0):C.GC_11})

V_96 = Vertex(name = 'V_96',
              particles = [ P.b__tilde__, P.b, P.ta__plus__, P.Tauc ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF1 ],
              couplings = {(0,0):C.GC_11})

V_97 = Vertex(name = 'V_97',
              particles = [ P.u__tilde__, P.u, P.ve__tilde__, P.N01 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF1 ],
              couplings = {(0,0):C.GC_11})

V_98 = Vertex(name = 'V_98',
              particles = [ P.c__tilde__, P.c, P.vm__tilde__, P.N02 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF1 ],
              couplings = {(0,0):C.GC_11})

V_99 = Vertex(name = 'V_99',
              particles = [ P.t__tilde__, P.t, P.vt__tilde__, P.N03 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF1 ],
              couplings = {(0,0):C.GC_11})

V_100 = Vertex(name = 'V_100',
               particles = [ P.E0__tilde__, P.e__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1 ],
               couplings = {(0,0):C.GC_11})

V_101 = Vertex(name = 'V_101',
               particles = [ P.ve__tilde__, P.Nc1, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1 ],
               couplings = {(0,0):C.GC_11})

V_102 = Vertex(name = 'V_102',
               particles = [ P.Mu0__tilde__, P.mu__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1 ],
               couplings = {(0,0):C.GC_11})

V_103 = Vertex(name = 'V_103',
               particles = [ P.vm__tilde__, P.Nc2, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1 ],
               couplings = {(0,0):C.GC_11})

V_104 = Vertex(name = 'V_104',
               particles = [ P.Tau0__tilde__, P.ta__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1 ],
               couplings = {(0,0):C.GC_11})

V_105 = Vertex(name = 'V_105',
               particles = [ P.vt__tilde__, P.Nc3, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1 ],
               couplings = {(0,0):C.GC_11})

V_106 = Vertex(name = 'V_106',
               particles = [ P.N01__tilde__, P.ve, P.Pi0u ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_10})

V_107 = Vertex(name = 'V_107',
               particles = [ P.Nc1__tilde__, P.ve, P.Pic1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_10})

V_108 = Vertex(name = 'V_108',
               particles = [ P.u__tilde__, P.d, P.Nc1__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF1 ],
               couplings = {(0,0):C.GC_11})

V_109 = Vertex(name = 'V_109',
               particles = [ P.c__tilde__, P.s, P.Nc2__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF1 ],
               couplings = {(0,0):C.GC_11})

V_110 = Vertex(name = 'V_110',
               particles = [ P.t__tilde__, P.b, P.Nc3__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF1 ],
               couplings = {(0,0):C.GC_11})

V_111 = Vertex(name = 'V_111',
               particles = [ P.N01__tilde__, P.ve, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1 ],
               couplings = {(0,0):C.GC_11})

V_112 = Vertex(name = 'V_112',
               particles = [ P.N02__tilde__, P.vm, P.c__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1 ],
               couplings = {(0,0):C.GC_11})

V_113 = Vertex(name = 'V_113',
               particles = [ P.N03__tilde__, P.vt, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1 ],
               couplings = {(0,0):C.GC_11})

V_114 = Vertex(name = 'V_114',
               particles = [ P.d__tilde__, P.ve, P.Pi13 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_10})

V_115 = Vertex(name = 'V_115',
               particles = [ P.u__tilde__, P.e__minus__, P.Pi53 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_10})

V_116 = Vertex(name = 'V_116',
               particles = [ P.d__tilde__, P.e__minus__, P.Pid23 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_10})

V_117 = Vertex(name = 'V_117',
               particles = [ P.u__tilde__, P.ve, P.Piu23 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_10})

