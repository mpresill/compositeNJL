# This file was automatically created by FeynRules 2.3.48
# Mathematica version: 12.3.1 for Mac OS X ARM (64-bit) (July 8, 2021)
# Date: Tue 5 Jul 2022 18:11:28


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.g, P.g, P.g ],
             color = [ 'f(1,2,3)' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_17})

V_2 = Vertex(name = 'V_2',
             particles = [ P.g, P.g, P.g, P.g ],
             color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
             lorentz = [ L.VVVV1, L.VVVV3, L.VVVV4 ],
             couplings = {(1,1):C.GC_23,(0,0):C.GC_23,(2,2):C.GC_23})

V_3 = Vertex(name = 'V_3',
             particles = [ P.a, P.W__minus__, P.W__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_6})

V_4 = Vertex(name = 'V_4',
             particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VVVV2 ],
             couplings = {(0,0):C.GC_10})

V_5 = Vertex(name = 'V_5',
             particles = [ P.W__minus__, P.W__plus__, P.Z ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_39})

V_6 = Vertex(name = 'V_6',
             particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VVVV2 ],
             couplings = {(0,0):C.GC_27})

V_7 = Vertex(name = 'V_7',
             particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
             color = [ '1' ],
             lorentz = [ L.VVVV5 ],
             couplings = {(0,0):C.GC_44})

V_8 = Vertex(name = 'V_8',
             particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
             color = [ '1' ],
             lorentz = [ L.VVVV2 ],
             couplings = {(0,0):C.GC_28})

V_9 = Vertex(name = 'V_9',
             particles = [ P.e__plus__, P.e__minus__, P.a ],
             color = [ '1' ],
             lorentz = [ L.FFV1 ],
             couplings = {(0,0):C.GC_5})

V_10 = Vertex(name = 'V_10',
              particles = [ P.mu__plus__, P.mu__minus__, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_5})

V_11 = Vertex(name = 'V_11',
              particles = [ P.ta__plus__, P.ta__minus__, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_5})

V_12 = Vertex(name = 'V_12',
              particles = [ P.c__tilde__, P.c, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_4})

V_13 = Vertex(name = 'V_13',
              particles = [ P.t__tilde__, P.t, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_4})

V_14 = Vertex(name = 'V_14',
              particles = [ P.u__tilde__, P.u, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_4})

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
              couplings = {(0,0):C.GC_19})

V_19 = Vertex(name = 'V_19',
              particles = [ P.t__tilde__, P.t, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_19})

V_20 = Vertex(name = 'V_20',
              particles = [ P.u__tilde__, P.u, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_19})

V_21 = Vertex(name = 'V_21',
              particles = [ P.b__tilde__, P.b, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_19})

V_22 = Vertex(name = 'V_22',
              particles = [ P.d__tilde__, P.d, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_19})

V_23 = Vertex(name = 'V_23',
              particles = [ P.s__tilde__, P.s, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_19})

V_24 = Vertex(name = 'V_24',
              particles = [ P.d__tilde__, P.c, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_35})

V_25 = Vertex(name = 'V_25',
              particles = [ P.s__tilde__, P.c, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_36})

V_26 = Vertex(name = 'V_26',
              particles = [ P.b__tilde__, P.t, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_32})

V_27 = Vertex(name = 'V_27',
              particles = [ P.d__tilde__, P.u, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_33})

V_28 = Vertex(name = 'V_28',
              particles = [ P.s__tilde__, P.u, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_34})

V_29 = Vertex(name = 'V_29',
              particles = [ P.t__tilde__, P.b, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_32})

V_30 = Vertex(name = 'V_30',
              particles = [ P.c__tilde__, P.d, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_86})

V_31 = Vertex(name = 'V_31',
              particles = [ P.u__tilde__, P.d, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_84})

V_32 = Vertex(name = 'V_32',
              particles = [ P.c__tilde__, P.s, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_87})

V_33 = Vertex(name = 'V_33',
              particles = [ P.u__tilde__, P.s, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_85})

V_34 = Vertex(name = 'V_34',
              particles = [ P.e__plus__, P.ve, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_32})

V_35 = Vertex(name = 'V_35',
              particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_32})

V_36 = Vertex(name = 'V_36',
              particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_32})

V_37 = Vertex(name = 'V_37',
              particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_32})

V_38 = Vertex(name = 'V_38',
              particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_32})

V_39 = Vertex(name = 'V_39',
              particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_32})

V_40 = Vertex(name = 'V_40',
              particles = [ P.c__tilde__, P.c, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV5 ],
              couplings = {(0,0):C.GC_38,(0,1):C.GC_46})

V_41 = Vertex(name = 'V_41',
              particles = [ P.t__tilde__, P.t, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV5 ],
              couplings = {(0,0):C.GC_38,(0,1):C.GC_46})

V_42 = Vertex(name = 'V_42',
              particles = [ P.u__tilde__, P.u, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV5 ],
              couplings = {(0,0):C.GC_38,(0,1):C.GC_46})

V_43 = Vertex(name = 'V_43',
              particles = [ P.b__tilde__, P.b, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_37,(0,1):C.GC_46})

V_44 = Vertex(name = 'V_44',
              particles = [ P.d__tilde__, P.d, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_37,(0,1):C.GC_46})

V_45 = Vertex(name = 'V_45',
              particles = [ P.s__tilde__, P.s, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_37,(0,1):C.GC_46})

V_46 = Vertex(name = 'V_46',
              particles = [ P.ve__tilde__, P.ve, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_51})

V_47 = Vertex(name = 'V_47',
              particles = [ P.vm__tilde__, P.vm, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_51})

V_48 = Vertex(name = 'V_48',
              particles = [ P.vt__tilde__, P.vt, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_51})

V_49 = Vertex(name = 'V_49',
              particles = [ P.e__plus__, P.e__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2, L.FFV4 ],
              couplings = {(0,0):C.GC_37,(0,1):C.GC_47})

V_50 = Vertex(name = 'V_50',
              particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2, L.FFV4 ],
              couplings = {(0,0):C.GC_37,(0,1):C.GC_47})

V_51 = Vertex(name = 'V_51',
              particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2, L.FFV4 ],
              couplings = {(0,0):C.GC_37,(0,1):C.GC_47})

V_52 = Vertex(name = 'V_52',
              particles = [ P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_24})

V_53 = Vertex(name = 'V_53',
              particles = [ P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_78})

V_54 = Vertex(name = 'V_54',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_26})

V_55 = Vertex(name = 'V_55',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS4 ],
              couplings = {(0,0):C.GC_79})

V_56 = Vertex(name = 'V_56',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_66})

V_57 = Vertex(name = 'V_57',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS4 ],
              couplings = {(0,0):C.GC_80})

V_58 = Vertex(name = 'V_58',
              particles = [ P.ta__plus__, P.ta__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS4 ],
              couplings = {(0,0):C.GC_83})

V_59 = Vertex(name = 'V_59',
              particles = [ P.t__tilde__, P.t, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS4 ],
              couplings = {(0,0):C.GC_82})

V_60 = Vertex(name = 'V_60',
              particles = [ P.ghG, P.ghG__tilde__, P.g ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_17})

V_61 = Vertex(name = 'V_61',
              particles = [ P.a, P.a, P.Pic1__tilde__, P.Pic1__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_11})

V_62 = Vertex(name = 'V_62',
              particles = [ P.a, P.Pic1__tilde__, P.Pic1__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_5})

V_63 = Vertex(name = 'V_63',
              particles = [ P.a, P.a, P.Pi0d ],
              color = [ '1' ],
              lorentz = [ L.VVS3 ],
              couplings = {(0,0):C.GC_69})

V_64 = Vertex(name = 'V_64',
              particles = [ P.a, P.a, P.Pi0u ],
              color = [ '1' ],
              lorentz = [ L.VVS3 ],
              couplings = {(0,0):C.GC_70})

V_65 = Vertex(name = 'V_65',
              particles = [ P.a, P.W__minus__, P.Pic1__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_72})

V_66 = Vertex(name = 'V_66',
              particles = [ P.a, P.W__plus__, P.Pic1__tilde__ ],
              color = [ '1' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_72})

V_67 = Vertex(name = 'V_67',
              particles = [ P.W__minus__, P.W__plus__, P.Pi0d ],
              color = [ '1' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_71})

V_68 = Vertex(name = 'V_68',
              particles = [ P.W__minus__, P.W__plus__, P.Pi0u ],
              color = [ '1' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_71})

V_69 = Vertex(name = 'V_69',
              particles = [ P.W__minus__, P.Z, P.Pic1__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_73})

V_70 = Vertex(name = 'V_70',
              particles = [ P.W__plus__, P.Z, P.Pic1__tilde__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_73})

V_71 = Vertex(name = 'V_71',
              particles = [ P.a, P.Z, P.Pi0d ],
              color = [ '1' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_76})

V_72 = Vertex(name = 'V_72',
              particles = [ P.a, P.Z, P.Pi0u ],
              color = [ '1' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_77})

V_73 = Vertex(name = 'V_73',
              particles = [ P.Z, P.Z, P.Pi0d ],
              color = [ '1' ],
              lorentz = [ L.VVS3 ],
              couplings = {(0,0):C.GC_74})

V_74 = Vertex(name = 'V_74',
              particles = [ P.Z, P.Z, P.Pi0u ],
              color = [ '1' ],
              lorentz = [ L.VVS3 ],
              couplings = {(0,0):C.GC_75})

V_75 = Vertex(name = 'V_75',
              particles = [ P.a, P.Pi13due__tilde__, P.Pi13due ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_2})

V_76 = Vertex(name = 'V_76',
              particles = [ P.a, P.a, P.Pi13due__tilde__, P.Pi13due ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_8})

V_77 = Vertex(name = 'V_77',
              particles = [ P.a, P.Pi13tre__tilde__, P.Pi13tre ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_2})

V_78 = Vertex(name = 'V_78',
              particles = [ P.a, P.a, P.Pi13tre__tilde__, P.Pi13tre ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_8})

V_79 = Vertex(name = 'V_79',
              particles = [ P.a, P.Pi13uno__tilde__, P.Pi13uno ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_2})

V_80 = Vertex(name = 'V_80',
              particles = [ P.a, P.a, P.Pi13uno__tilde__, P.Pi13uno ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_8})

V_81 = Vertex(name = 'V_81',
              particles = [ P.a, P.Pi53due__tilde__, P.Pi53due ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_7})

V_82 = Vertex(name = 'V_82',
              particles = [ P.a, P.a, P.Pi53due__tilde__, P.Pi53due ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_12})

V_83 = Vertex(name = 'V_83',
              particles = [ P.a, P.Pi53tre__tilde__, P.Pi53tre ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_7})

V_84 = Vertex(name = 'V_84',
              particles = [ P.a, P.a, P.Pi53tre__tilde__, P.Pi53tre ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_12})

V_85 = Vertex(name = 'V_85',
              particles = [ P.a, P.Pi53uno__tilde__, P.Pi53uno ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_7})

V_86 = Vertex(name = 'V_86',
              particles = [ P.a, P.a, P.Pi53uno__tilde__, P.Pi53uno ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_12})

V_87 = Vertex(name = 'V_87',
              particles = [ P.a, P.Pid23due__tilde__, P.Pid23due ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_3})

V_88 = Vertex(name = 'V_88',
              particles = [ P.a, P.a, P.Pid23due__tilde__, P.Pid23due ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_9})

V_89 = Vertex(name = 'V_89',
              particles = [ P.a, P.Pid23tre__tilde__, P.Pid23tre ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_3})

V_90 = Vertex(name = 'V_90',
              particles = [ P.a, P.a, P.Pid23tre__tilde__, P.Pid23tre ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_9})

V_91 = Vertex(name = 'V_91',
              particles = [ P.a, P.Pid23uno__tilde__, P.Pid23uno ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_3})

V_92 = Vertex(name = 'V_92',
              particles = [ P.a, P.a, P.Pid23uno__tilde__, P.Pid23uno ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_9})

V_93 = Vertex(name = 'V_93',
              particles = [ P.a, P.Piu23due__tilde__, P.Piu23due ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_3})

V_94 = Vertex(name = 'V_94',
              particles = [ P.a, P.a, P.Piu23due__tilde__, P.Piu23due ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_9})

V_95 = Vertex(name = 'V_95',
              particles = [ P.a, P.Piu23tre__tilde__, P.Piu23tre ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_3})

V_96 = Vertex(name = 'V_96',
              particles = [ P.a, P.a, P.Piu23tre__tilde__, P.Piu23tre ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_9})

V_97 = Vertex(name = 'V_97',
              particles = [ P.a, P.Piu23uno__tilde__, P.Piu23uno ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_3})

V_98 = Vertex(name = 'V_98',
              particles = [ P.a, P.a, P.Piu23uno__tilde__, P.Piu23uno ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_9})

V_99 = Vertex(name = 'V_99',
              particles = [ P.d__tilde__, P.d, P.Pi0d ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_81})

V_100 = Vertex(name = 'V_100',
               particles = [ P.s__tilde__, P.s, P.Pi0d ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_81})

V_101 = Vertex(name = 'V_101',
               particles = [ P.b__tilde__, P.b, P.Pi0d ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_81})

V_102 = Vertex(name = 'V_102',
               particles = [ P.E0__tilde__, P.e__minus__, P.Pic1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_81})

V_103 = Vertex(name = 'V_103',
               particles = [ P.Mu0__tilde__, P.mu__minus__, P.Pic1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_81})

V_104 = Vertex(name = 'V_104',
               particles = [ P.Tau0__tilde__, P.ta__minus__, P.Pic1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_81})

V_105 = Vertex(name = 'V_105',
               particles = [ P.e__plus__, P.Ec, P.Pi0d ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_81})

V_106 = Vertex(name = 'V_106',
               particles = [ P.mu__plus__, P.Muc, P.Pi0d ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_81})

V_107 = Vertex(name = 'V_107',
               particles = [ P.ta__plus__, P.Tauc, P.Pi0d ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_81})

V_108 = Vertex(name = 'V_108',
               particles = [ P.ve__tilde__, P.N01, P.Pi0u ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_81})

V_109 = Vertex(name = 'V_109',
               particles = [ P.vm__tilde__, P.N02, P.Pi0u ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_81})

V_110 = Vertex(name = 'V_110',
               particles = [ P.vt__tilde__, P.N03, P.Pi0u ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_81})

V_111 = Vertex(name = 'V_111',
               particles = [ P.ve__tilde__, P.Nc1, P.Pic1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_81})

V_112 = Vertex(name = 'V_112',
               particles = [ P.vm__tilde__, P.Nc2, P.Pic1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_81})

V_113 = Vertex(name = 'V_113',
               particles = [ P.vt__tilde__, P.Nc3, P.Pic1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_81})

V_114 = Vertex(name = 'V_114',
               particles = [ P.d__tilde__, P.u, P.Pic1__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_81})

V_115 = Vertex(name = 'V_115',
               particles = [ P.u__tilde__, P.u, P.Pi0u ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_81})

V_116 = Vertex(name = 'V_116',
               particles = [ P.s__tilde__, P.c, P.Pic1__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_81})

V_117 = Vertex(name = 'V_117',
               particles = [ P.c__tilde__, P.c, P.Pi0u ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_81})

V_118 = Vertex(name = 'V_118',
               particles = [ P.b__tilde__, P.t, P.Pic1__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_81})

V_119 = Vertex(name = 'V_119',
               particles = [ P.t__tilde__, P.t, P.Pi0u ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_81})

V_120 = Vertex(name = 'V_120',
               particles = [ P.vm__tilde__, P.s, P.Pi13due__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_81})

V_121 = Vertex(name = 'V_121',
               particles = [ P.vt__tilde__, P.b, P.Pi13tre__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_81})

V_122 = Vertex(name = 'V_122',
               particles = [ P.ve__tilde__, P.d, P.Pi13uno__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_81})

V_123 = Vertex(name = 'V_123',
               particles = [ P.mu__plus__, P.c, P.Pi53due__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_81})

V_124 = Vertex(name = 'V_124',
               particles = [ P.ta__plus__, P.t, P.Pi53tre__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_81})

V_125 = Vertex(name = 'V_125',
               particles = [ P.e__plus__, P.u, P.Pi53uno__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_81})

V_126 = Vertex(name = 'V_126',
               particles = [ P.mu__plus__, P.s, P.Pid23due__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_81})

V_127 = Vertex(name = 'V_127',
               particles = [ P.ta__plus__, P.b, P.Pid23tre__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_81})

V_128 = Vertex(name = 'V_128',
               particles = [ P.e__plus__, P.d, P.Pid23uno__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_81})

V_129 = Vertex(name = 'V_129',
               particles = [ P.vm__tilde__, P.c, P.Piu23due__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_81})

V_130 = Vertex(name = 'V_130',
               particles = [ P.vt__tilde__, P.t, P.Piu23tre__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_81})

V_131 = Vertex(name = 'V_131',
               particles = [ P.ve__tilde__, P.u, P.Piu23uno__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_81})

V_132 = Vertex(name = 'V_132',
               particles = [ P.u__tilde__, P.d, P.Pic1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_81})

V_133 = Vertex(name = 'V_133',
               particles = [ P.c__tilde__, P.s, P.Pic1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_81})

V_134 = Vertex(name = 'V_134',
               particles = [ P.t__tilde__, P.b, P.Pic1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_81})

V_135 = Vertex(name = 'V_135',
               particles = [ P.e__plus__, P.E0, P.Pic1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_81})

V_136 = Vertex(name = 'V_136',
               particles = [ P.u__tilde__, P.d, P.e__plus__, P.E0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF1 ],
               couplings = {(0,0):C.GC_25})

V_137 = Vertex(name = 'V_137',
               particles = [ P.mu__plus__, P.Mu0, P.Pic1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_81})

V_138 = Vertex(name = 'V_138',
               particles = [ P.c__tilde__, P.s, P.mu__plus__, P.Mu0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF1 ],
               couplings = {(0,0):C.GC_25})

V_139 = Vertex(name = 'V_139',
               particles = [ P.ta__plus__, P.Tau0, P.Pic1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_81})

V_140 = Vertex(name = 'V_140',
               particles = [ P.t__tilde__, P.b, P.ta__plus__, P.Tau0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF1 ],
               couplings = {(0,0):C.GC_25})

V_141 = Vertex(name = 'V_141',
               particles = [ P.Ec__tilde__, P.e__minus__, P.Pi0d ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_81})

V_142 = Vertex(name = 'V_142',
               particles = [ P.Muc__tilde__, P.mu__minus__, P.Pi0d ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_81})

V_143 = Vertex(name = 'V_143',
               particles = [ P.Tauc__tilde__, P.ta__minus__, P.Pi0d ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_81})

V_144 = Vertex(name = 'V_144',
               particles = [ P.Ec__tilde__, P.e__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1 ],
               couplings = {(0,0):C.GC_25})

V_145 = Vertex(name = 'V_145',
               particles = [ P.Muc__tilde__, P.mu__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1 ],
               couplings = {(0,0):C.GC_25})

V_146 = Vertex(name = 'V_146',
               particles = [ P.Tauc__tilde__, P.ta__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1 ],
               couplings = {(0,0):C.GC_25})

V_147 = Vertex(name = 'V_147',
               particles = [ P.d__tilde__, P.d, P.e__plus__, P.Ec ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF1 ],
               couplings = {(0,0):C.GC_25})

V_148 = Vertex(name = 'V_148',
               particles = [ P.s__tilde__, P.s, P.mu__plus__, P.Muc ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF1 ],
               couplings = {(0,0):C.GC_25})

V_149 = Vertex(name = 'V_149',
               particles = [ P.b__tilde__, P.b, P.ta__plus__, P.Tauc ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF1 ],
               couplings = {(0,0):C.GC_25})

V_150 = Vertex(name = 'V_150',
               particles = [ P.u__tilde__, P.u, P.ve__tilde__, P.N01 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF1 ],
               couplings = {(0,0):C.GC_25})

V_151 = Vertex(name = 'V_151',
               particles = [ P.c__tilde__, P.c, P.vm__tilde__, P.N02 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF1 ],
               couplings = {(0,0):C.GC_25})

V_152 = Vertex(name = 'V_152',
               particles = [ P.t__tilde__, P.t, P.vt__tilde__, P.N03 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF1 ],
               couplings = {(0,0):C.GC_25})

V_153 = Vertex(name = 'V_153',
               particles = [ P.E0__tilde__, P.e__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1 ],
               couplings = {(0,0):C.GC_25})

V_154 = Vertex(name = 'V_154',
               particles = [ P.ve__tilde__, P.Nc1, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1 ],
               couplings = {(0,0):C.GC_25})

V_155 = Vertex(name = 'V_155',
               particles = [ P.Mu0__tilde__, P.mu__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1 ],
               couplings = {(0,0):C.GC_25})

V_156 = Vertex(name = 'V_156',
               particles = [ P.vm__tilde__, P.Nc2, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1 ],
               couplings = {(0,0):C.GC_25})

V_157 = Vertex(name = 'V_157',
               particles = [ P.Tau0__tilde__, P.ta__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1 ],
               couplings = {(0,0):C.GC_25})

V_158 = Vertex(name = 'V_158',
               particles = [ P.vt__tilde__, P.Nc3, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1 ],
               couplings = {(0,0):C.GC_25})

V_159 = Vertex(name = 'V_159',
               particles = [ P.N01__tilde__, P.ve, P.Pi0u ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_81})

V_160 = Vertex(name = 'V_160',
               particles = [ P.Nc1__tilde__, P.ve, P.Pic1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_81})

V_161 = Vertex(name = 'V_161',
               particles = [ P.u__tilde__, P.d, P.Nc1__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF1 ],
               couplings = {(0,0):C.GC_25})

V_162 = Vertex(name = 'V_162',
               particles = [ P.N02__tilde__, P.vm, P.Pi0u ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_81})

V_163 = Vertex(name = 'V_163',
               particles = [ P.Nc2__tilde__, P.vm, P.Pic1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_81})

V_164 = Vertex(name = 'V_164',
               particles = [ P.c__tilde__, P.s, P.Nc2__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF1 ],
               couplings = {(0,0):C.GC_25})

V_165 = Vertex(name = 'V_165',
               particles = [ P.N03__tilde__, P.vt, P.Pi0u ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_81})

V_166 = Vertex(name = 'V_166',
               particles = [ P.Nc3__tilde__, P.vt, P.Pic1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_81})

V_167 = Vertex(name = 'V_167',
               particles = [ P.t__tilde__, P.b, P.Nc3__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF1 ],
               couplings = {(0,0):C.GC_25})

V_168 = Vertex(name = 'V_168',
               particles = [ P.N01__tilde__, P.ve, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1 ],
               couplings = {(0,0):C.GC_25})

V_169 = Vertex(name = 'V_169',
               particles = [ P.N02__tilde__, P.vm, P.c__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1 ],
               couplings = {(0,0):C.GC_25})

V_170 = Vertex(name = 'V_170',
               particles = [ P.N03__tilde__, P.vt, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1 ],
               couplings = {(0,0):C.GC_25})

V_171 = Vertex(name = 'V_171',
               particles = [ P.s__tilde__, P.vm, P.Pi13due ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_81})

V_172 = Vertex(name = 'V_172',
               particles = [ P.c__tilde__, P.mu__minus__, P.Pi53due ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_81})

V_173 = Vertex(name = 'V_173',
               particles = [ P.s__tilde__, P.mu__minus__, P.Pid23due ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_81})

V_174 = Vertex(name = 'V_174',
               particles = [ P.c__tilde__, P.vm, P.Piu23due ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_81})

V_175 = Vertex(name = 'V_175',
               particles = [ P.b__tilde__, P.vt, P.Pi13tre ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_81})

V_176 = Vertex(name = 'V_176',
               particles = [ P.t__tilde__, P.ta__minus__, P.Pi53tre ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_81})

V_177 = Vertex(name = 'V_177',
               particles = [ P.b__tilde__, P.ta__minus__, P.Pid23tre ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_81})

V_178 = Vertex(name = 'V_178',
               particles = [ P.t__tilde__, P.vt, P.Piu23tre ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_81})

V_179 = Vertex(name = 'V_179',
               particles = [ P.d__tilde__, P.ve, P.Pi13uno ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_81})

V_180 = Vertex(name = 'V_180',
               particles = [ P.u__tilde__, P.e__minus__, P.Pi53uno ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_81})

V_181 = Vertex(name = 'V_181',
               particles = [ P.d__tilde__, P.e__minus__, P.Pid23uno ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_81})

V_182 = Vertex(name = 'V_182',
               particles = [ P.u__tilde__, P.ve, P.Piu23uno ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_81})

V_183 = Vertex(name = 'V_183',
               particles = [ P.g, P.Pi53uno__tilde__, P.Pi53uno ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_18})

V_184 = Vertex(name = 'V_184',
               particles = [ P.a, P.g, P.Pi53uno__tilde__, P.Pi53uno ],
               color = [ 'T(2,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_22})

V_185 = Vertex(name = 'V_185',
               particles = [ P.g, P.Pid23uno__tilde__, P.Pid23uno ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_18})

V_186 = Vertex(name = 'V_186',
               particles = [ P.a, P.g, P.Pid23uno__tilde__, P.Pid23uno ],
               color = [ 'T(2,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_21})

V_187 = Vertex(name = 'V_187',
               particles = [ P.g, P.g, P.Pi53uno__tilde__, P.Pi53uno ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_23,(0,0):C.GC_23})

V_188 = Vertex(name = 'V_188',
               particles = [ P.g, P.g, P.Pid23uno__tilde__, P.Pid23uno ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_23,(0,0):C.GC_23})

V_189 = Vertex(name = 'V_189',
               particles = [ P.g, P.Pi13uno__tilde__, P.Pi13uno ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_18})

V_190 = Vertex(name = 'V_190',
               particles = [ P.a, P.g, P.Pi13uno__tilde__, P.Pi13uno ],
               color = [ 'T(2,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_20})

V_191 = Vertex(name = 'V_191',
               particles = [ P.g, P.Piu23uno__tilde__, P.Piu23uno ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_18})

V_192 = Vertex(name = 'V_192',
               particles = [ P.a, P.g, P.Piu23uno__tilde__, P.Piu23uno ],
               color = [ 'T(2,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_21})

V_193 = Vertex(name = 'V_193',
               particles = [ P.g, P.g, P.Pi13uno__tilde__, P.Pi13uno ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_23,(0,0):C.GC_23})

V_194 = Vertex(name = 'V_194',
               particles = [ P.g, P.g, P.Piu23uno__tilde__, P.Piu23uno ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_23,(0,0):C.GC_23})

V_195 = Vertex(name = 'V_195',
               particles = [ P.g, P.Pi53due__tilde__, P.Pi53due ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_18})

V_196 = Vertex(name = 'V_196',
               particles = [ P.a, P.g, P.Pi53due__tilde__, P.Pi53due ],
               color = [ 'T(2,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_22})

V_197 = Vertex(name = 'V_197',
               particles = [ P.g, P.Pid23due__tilde__, P.Pid23due ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_18})

V_198 = Vertex(name = 'V_198',
               particles = [ P.a, P.g, P.Pid23due__tilde__, P.Pid23due ],
               color = [ 'T(2,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_21})

V_199 = Vertex(name = 'V_199',
               particles = [ P.g, P.g, P.Pi53due__tilde__, P.Pi53due ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_23,(0,0):C.GC_23})

V_200 = Vertex(name = 'V_200',
               particles = [ P.g, P.g, P.Pid23due__tilde__, P.Pid23due ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_23,(0,0):C.GC_23})

V_201 = Vertex(name = 'V_201',
               particles = [ P.g, P.Pi13due__tilde__, P.Pi13due ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_18})

V_202 = Vertex(name = 'V_202',
               particles = [ P.a, P.g, P.Pi13due__tilde__, P.Pi13due ],
               color = [ 'T(2,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_20})

V_203 = Vertex(name = 'V_203',
               particles = [ P.g, P.Piu23due__tilde__, P.Piu23due ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_18})

V_204 = Vertex(name = 'V_204',
               particles = [ P.a, P.g, P.Piu23due__tilde__, P.Piu23due ],
               color = [ 'T(2,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_21})

V_205 = Vertex(name = 'V_205',
               particles = [ P.g, P.g, P.Pi13due__tilde__, P.Pi13due ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_23,(0,0):C.GC_23})

V_206 = Vertex(name = 'V_206',
               particles = [ P.g, P.g, P.Piu23due__tilde__, P.Piu23due ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_23,(0,0):C.GC_23})

V_207 = Vertex(name = 'V_207',
               particles = [ P.g, P.Pi53tre__tilde__, P.Pi53tre ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_18})

V_208 = Vertex(name = 'V_208',
               particles = [ P.a, P.g, P.Pi53tre__tilde__, P.Pi53tre ],
               color = [ 'T(2,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_22})

V_209 = Vertex(name = 'V_209',
               particles = [ P.g, P.Pid23tre__tilde__, P.Pid23tre ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_18})

V_210 = Vertex(name = 'V_210',
               particles = [ P.a, P.g, P.Pid23tre__tilde__, P.Pid23tre ],
               color = [ 'T(2,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_21})

V_211 = Vertex(name = 'V_211',
               particles = [ P.g, P.g, P.Pi53tre__tilde__, P.Pi53tre ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_23,(0,0):C.GC_23})

V_212 = Vertex(name = 'V_212',
               particles = [ P.g, P.g, P.Pid23tre__tilde__, P.Pid23tre ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_23,(0,0):C.GC_23})

V_213 = Vertex(name = 'V_213',
               particles = [ P.g, P.Pi13tre__tilde__, P.Pi13tre ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_18})

V_214 = Vertex(name = 'V_214',
               particles = [ P.a, P.g, P.Pi13tre__tilde__, P.Pi13tre ],
               color = [ 'T(2,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_20})

V_215 = Vertex(name = 'V_215',
               particles = [ P.g, P.Piu23tre__tilde__, P.Piu23tre ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_18})

V_216 = Vertex(name = 'V_216',
               particles = [ P.a, P.g, P.Piu23tre__tilde__, P.Piu23tre ],
               color = [ 'T(2,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_21})

V_217 = Vertex(name = 'V_217',
               particles = [ P.g, P.g, P.Pi13tre__tilde__, P.Pi13tre ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_23,(0,0):C.GC_23})

V_218 = Vertex(name = 'V_218',
               particles = [ P.g, P.g, P.Piu23tre__tilde__, P.Piu23tre ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_23,(0,0):C.GC_23})

V_219 = Vertex(name = 'V_219',
               particles = [ P.W__minus__, P.Pi53uno, P.Pid23uno__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_32})

V_220 = Vertex(name = 'V_220',
               particles = [ P.a, P.W__minus__, P.Pi53uno, P.Pid23uno__tilde__ ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_43})

V_221 = Vertex(name = 'V_221',
               particles = [ P.g, P.W__minus__, P.Pi53uno, P.Pid23uno__tilde__ ],
               color = [ 'T(1,3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_45})

V_222 = Vertex(name = 'V_222',
               particles = [ P.W__minus__, P.Pi13uno__tilde__, P.Piu23uno ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_31})

V_223 = Vertex(name = 'V_223',
               particles = [ P.a, P.W__minus__, P.Pi13uno__tilde__, P.Piu23uno ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_40})

V_224 = Vertex(name = 'V_224',
               particles = [ P.g, P.W__minus__, P.Pi13uno__tilde__, P.Piu23uno ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_45})

V_225 = Vertex(name = 'V_225',
               particles = [ P.a, P.W__minus__, P.Pi0d, P.Pic1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_42})

V_226 = Vertex(name = 'V_226',
               particles = [ P.W__minus__, P.Pi0d, P.Pic1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_29})

V_227 = Vertex(name = 'V_227',
               particles = [ P.a, P.W__minus__, P.Pi0u, P.Pic1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_41})

V_228 = Vertex(name = 'V_228',
               particles = [ P.W__minus__, P.Pi0u, P.Pic1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_30})

V_229 = Vertex(name = 'V_229',
               particles = [ P.W__minus__, P.Pi53due, P.Pid23due__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_32})

V_230 = Vertex(name = 'V_230',
               particles = [ P.a, P.W__minus__, P.Pi53due, P.Pid23due__tilde__ ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_43})

V_231 = Vertex(name = 'V_231',
               particles = [ P.g, P.W__minus__, P.Pi53due, P.Pid23due__tilde__ ],
               color = [ 'T(1,3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_45})

V_232 = Vertex(name = 'V_232',
               particles = [ P.W__minus__, P.Pi13due__tilde__, P.Piu23due ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_31})

V_233 = Vertex(name = 'V_233',
               particles = [ P.a, P.W__minus__, P.Pi13due__tilde__, P.Piu23due ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_40})

V_234 = Vertex(name = 'V_234',
               particles = [ P.g, P.W__minus__, P.Pi13due__tilde__, P.Piu23due ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_45})

V_235 = Vertex(name = 'V_235',
               particles = [ P.W__minus__, P.Pi53tre, P.Pid23tre__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_32})

V_236 = Vertex(name = 'V_236',
               particles = [ P.a, P.W__minus__, P.Pi53tre, P.Pid23tre__tilde__ ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_43})

V_237 = Vertex(name = 'V_237',
               particles = [ P.g, P.W__minus__, P.Pi53tre, P.Pid23tre__tilde__ ],
               color = [ 'T(1,3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_45})

V_238 = Vertex(name = 'V_238',
               particles = [ P.W__minus__, P.Pi13tre__tilde__, P.Piu23tre ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_31})

V_239 = Vertex(name = 'V_239',
               particles = [ P.a, P.W__minus__, P.Pi13tre__tilde__, P.Piu23tre ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_40})

V_240 = Vertex(name = 'V_240',
               particles = [ P.g, P.W__minus__, P.Pi13tre__tilde__, P.Piu23tre ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_45})

V_241 = Vertex(name = 'V_241',
               particles = [ P.W__plus__, P.Pi53uno__tilde__, P.Pid23uno ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_31})

V_242 = Vertex(name = 'V_242',
               particles = [ P.a, P.W__plus__, P.Pi53uno__tilde__, P.Pid23uno ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_43})

V_243 = Vertex(name = 'V_243',
               particles = [ P.g, P.W__plus__, P.Pi53uno__tilde__, P.Pid23uno ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_45})

V_244 = Vertex(name = 'V_244',
               particles = [ P.W__minus__, P.W__plus__, P.Pi53uno__tilde__, P.Pi53uno ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_26})

V_245 = Vertex(name = 'V_245',
               particles = [ P.W__minus__, P.W__plus__, P.Pid23uno__tilde__, P.Pid23uno ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_26})

V_246 = Vertex(name = 'V_246',
               particles = [ P.W__plus__, P.Pi13uno, P.Piu23uno__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_32})

V_247 = Vertex(name = 'V_247',
               particles = [ P.a, P.W__plus__, P.Pi13uno, P.Piu23uno__tilde__ ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_40})

V_248 = Vertex(name = 'V_248',
               particles = [ P.g, P.W__plus__, P.Pi13uno, P.Piu23uno__tilde__ ],
               color = [ 'T(1,3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_45})

V_249 = Vertex(name = 'V_249',
               particles = [ P.W__minus__, P.W__plus__, P.Pi13uno__tilde__, P.Pi13uno ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_26})

V_250 = Vertex(name = 'V_250',
               particles = [ P.W__minus__, P.W__plus__, P.Piu23uno__tilde__, P.Piu23uno ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_26})

V_251 = Vertex(name = 'V_251',
               particles = [ P.a, P.W__plus__, P.Pi0d, P.Pic1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_42})

V_252 = Vertex(name = 'V_252',
               particles = [ P.W__plus__, P.Pi0d, P.Pic1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_30})

V_253 = Vertex(name = 'V_253',
               particles = [ P.W__minus__, P.W__plus__, P.Pi0d, P.Pi0d ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_26})

V_254 = Vertex(name = 'V_254',
               particles = [ P.W__minus__, P.W__plus__, P.Pic1__tilde__, P.Pic1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_26})

V_255 = Vertex(name = 'V_255',
               particles = [ P.a, P.W__plus__, P.Pi0u, P.Pic1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_41})

V_256 = Vertex(name = 'V_256',
               particles = [ P.W__plus__, P.Pi0u, P.Pic1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_29})

V_257 = Vertex(name = 'V_257',
               particles = [ P.W__minus__, P.W__plus__, P.Pi0u, P.Pi0u ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_26})

V_258 = Vertex(name = 'V_258',
               particles = [ P.W__plus__, P.Pi53due__tilde__, P.Pid23due ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_31})

V_259 = Vertex(name = 'V_259',
               particles = [ P.a, P.W__plus__, P.Pi53due__tilde__, P.Pid23due ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_43})

V_260 = Vertex(name = 'V_260',
               particles = [ P.g, P.W__plus__, P.Pi53due__tilde__, P.Pid23due ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_45})

V_261 = Vertex(name = 'V_261',
               particles = [ P.W__minus__, P.W__plus__, P.Pi53due__tilde__, P.Pi53due ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_26})

V_262 = Vertex(name = 'V_262',
               particles = [ P.W__minus__, P.W__plus__, P.Pid23due__tilde__, P.Pid23due ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_26})

V_263 = Vertex(name = 'V_263',
               particles = [ P.W__plus__, P.Pi13due, P.Piu23due__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_32})

V_264 = Vertex(name = 'V_264',
               particles = [ P.a, P.W__plus__, P.Pi13due, P.Piu23due__tilde__ ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_40})

V_265 = Vertex(name = 'V_265',
               particles = [ P.g, P.W__plus__, P.Pi13due, P.Piu23due__tilde__ ],
               color = [ 'T(1,3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_45})

V_266 = Vertex(name = 'V_266',
               particles = [ P.W__minus__, P.W__plus__, P.Pi13due__tilde__, P.Pi13due ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_26})

V_267 = Vertex(name = 'V_267',
               particles = [ P.W__minus__, P.W__plus__, P.Piu23due__tilde__, P.Piu23due ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_26})

V_268 = Vertex(name = 'V_268',
               particles = [ P.W__plus__, P.Pi53tre__tilde__, P.Pid23tre ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_31})

V_269 = Vertex(name = 'V_269',
               particles = [ P.a, P.W__plus__, P.Pi53tre__tilde__, P.Pid23tre ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_43})

V_270 = Vertex(name = 'V_270',
               particles = [ P.g, P.W__plus__, P.Pi53tre__tilde__, P.Pid23tre ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_45})

V_271 = Vertex(name = 'V_271',
               particles = [ P.W__minus__, P.W__plus__, P.Pi53tre__tilde__, P.Pi53tre ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_26})

V_272 = Vertex(name = 'V_272',
               particles = [ P.W__minus__, P.W__plus__, P.Pid23tre__tilde__, P.Pid23tre ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_26})

V_273 = Vertex(name = 'V_273',
               particles = [ P.W__plus__, P.Pi13tre, P.Piu23tre__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_32})

V_274 = Vertex(name = 'V_274',
               particles = [ P.a, P.W__plus__, P.Pi13tre, P.Piu23tre__tilde__ ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_40})

V_275 = Vertex(name = 'V_275',
               particles = [ P.g, P.W__plus__, P.Pi13tre, P.Piu23tre__tilde__ ],
               color = [ 'T(1,3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_45})

V_276 = Vertex(name = 'V_276',
               particles = [ P.W__minus__, P.W__plus__, P.Pi13tre__tilde__, P.Pi13tre ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_26})

V_277 = Vertex(name = 'V_277',
               particles = [ P.W__minus__, P.W__plus__, P.Piu23tre__tilde__, P.Piu23tre ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_26})

V_278 = Vertex(name = 'V_278',
               particles = [ P.Z, P.Pi53uno__tilde__, P.Pi53uno ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_52})

V_279 = Vertex(name = 'V_279',
               particles = [ P.a, P.Z, P.Pi53uno__tilde__, P.Pi53uno ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_58})

V_280 = Vertex(name = 'V_280',
               particles = [ P.Z, P.Pid23uno__tilde__, P.Pid23uno ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_53})

V_281 = Vertex(name = 'V_281',
               particles = [ P.a, P.Z, P.Pid23uno__tilde__, P.Pid23uno ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_57})

V_282 = Vertex(name = 'V_282',
               particles = [ P.g, P.Z, P.Pi53uno__tilde__, P.Pi53uno ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_62})

V_283 = Vertex(name = 'V_283',
               particles = [ P.g, P.Z, P.Pid23uno__tilde__, P.Pid23uno ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_61})

V_284 = Vertex(name = 'V_284',
               particles = [ P.W__minus__, P.Z, P.Pi53uno, P.Pid23uno__tilde__ ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_16})

V_285 = Vertex(name = 'V_285',
               particles = [ P.W__plus__, P.Z, P.Pi53uno__tilde__, P.Pid23uno ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_16})

V_286 = Vertex(name = 'V_286',
               particles = [ P.Z, P.Z, P.Pi53uno__tilde__, P.Pi53uno ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_67})

V_287 = Vertex(name = 'V_287',
               particles = [ P.Z, P.Z, P.Pid23uno__tilde__, P.Pid23uno ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_68})

V_288 = Vertex(name = 'V_288',
               particles = [ P.Z, P.Pi13uno__tilde__, P.Pi13uno ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_49})

V_289 = Vertex(name = 'V_289',
               particles = [ P.a, P.Z, P.Pi13uno__tilde__, P.Pi13uno ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_54})

V_290 = Vertex(name = 'V_290',
               particles = [ P.Z, P.Piu23uno__tilde__, P.Piu23uno ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_48})

V_291 = Vertex(name = 'V_291',
               particles = [ P.a, P.Z, P.Piu23uno__tilde__, P.Piu23uno ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_55})

V_292 = Vertex(name = 'V_292',
               particles = [ P.g, P.Z, P.Pi13uno__tilde__, P.Pi13uno ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_59})

V_293 = Vertex(name = 'V_293',
               particles = [ P.g, P.Z, P.Piu23uno__tilde__, P.Piu23uno ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_60})

V_294 = Vertex(name = 'V_294',
               particles = [ P.W__minus__, P.Z, P.Pi13uno__tilde__, P.Piu23uno ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_13})

V_295 = Vertex(name = 'V_295',
               particles = [ P.W__plus__, P.Z, P.Pi13uno, P.Piu23uno__tilde__ ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_13})

V_296 = Vertex(name = 'V_296',
               particles = [ P.Z, P.Z, P.Pi13uno__tilde__, P.Pi13uno ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_64})

V_297 = Vertex(name = 'V_297',
               particles = [ P.Z, P.Z, P.Piu23uno__tilde__, P.Piu23uno ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_63})

V_298 = Vertex(name = 'V_298',
               particles = [ P.a, P.Z, P.Pic1__tilde__, P.Pic1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_56})

V_299 = Vertex(name = 'V_299',
               particles = [ P.Z, P.Pic1__tilde__, P.Pic1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_50})

V_300 = Vertex(name = 'V_300',
               particles = [ P.W__minus__, P.Z, P.Pi0d, P.Pic1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_14})

V_301 = Vertex(name = 'V_301',
               particles = [ P.W__plus__, P.Z, P.Pi0d, P.Pic1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_14})

V_302 = Vertex(name = 'V_302',
               particles = [ P.Z, P.Z, P.Pi0d, P.Pi0d ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_66})

V_303 = Vertex(name = 'V_303',
               particles = [ P.Z, P.Z, P.Pic1__tilde__, P.Pic1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_65})

V_304 = Vertex(name = 'V_304',
               particles = [ P.W__minus__, P.Z, P.Pi0u, P.Pic1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_15})

V_305 = Vertex(name = 'V_305',
               particles = [ P.W__plus__, P.Z, P.Pi0u, P.Pic1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_15})

V_306 = Vertex(name = 'V_306',
               particles = [ P.Z, P.Z, P.Pi0u, P.Pi0u ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_66})

V_307 = Vertex(name = 'V_307',
               particles = [ P.Z, P.Pi53due__tilde__, P.Pi53due ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_52})

V_308 = Vertex(name = 'V_308',
               particles = [ P.a, P.Z, P.Pi53due__tilde__, P.Pi53due ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_58})

V_309 = Vertex(name = 'V_309',
               particles = [ P.Z, P.Pid23due__tilde__, P.Pid23due ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_53})

V_310 = Vertex(name = 'V_310',
               particles = [ P.a, P.Z, P.Pid23due__tilde__, P.Pid23due ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_57})

V_311 = Vertex(name = 'V_311',
               particles = [ P.g, P.Z, P.Pi53due__tilde__, P.Pi53due ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_62})

V_312 = Vertex(name = 'V_312',
               particles = [ P.g, P.Z, P.Pid23due__tilde__, P.Pid23due ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_61})

V_313 = Vertex(name = 'V_313',
               particles = [ P.W__minus__, P.Z, P.Pi53due, P.Pid23due__tilde__ ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_16})

V_314 = Vertex(name = 'V_314',
               particles = [ P.W__plus__, P.Z, P.Pi53due__tilde__, P.Pid23due ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_16})

V_315 = Vertex(name = 'V_315',
               particles = [ P.Z, P.Z, P.Pi53due__tilde__, P.Pi53due ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_67})

V_316 = Vertex(name = 'V_316',
               particles = [ P.Z, P.Z, P.Pid23due__tilde__, P.Pid23due ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_68})

V_317 = Vertex(name = 'V_317',
               particles = [ P.Z, P.Pi13due__tilde__, P.Pi13due ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_49})

V_318 = Vertex(name = 'V_318',
               particles = [ P.a, P.Z, P.Pi13due__tilde__, P.Pi13due ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_54})

V_319 = Vertex(name = 'V_319',
               particles = [ P.Z, P.Piu23due__tilde__, P.Piu23due ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_48})

V_320 = Vertex(name = 'V_320',
               particles = [ P.a, P.Z, P.Piu23due__tilde__, P.Piu23due ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_55})

V_321 = Vertex(name = 'V_321',
               particles = [ P.g, P.Z, P.Pi13due__tilde__, P.Pi13due ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_59})

V_322 = Vertex(name = 'V_322',
               particles = [ P.g, P.Z, P.Piu23due__tilde__, P.Piu23due ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_60})

V_323 = Vertex(name = 'V_323',
               particles = [ P.W__minus__, P.Z, P.Pi13due__tilde__, P.Piu23due ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_13})

V_324 = Vertex(name = 'V_324',
               particles = [ P.W__plus__, P.Z, P.Pi13due, P.Piu23due__tilde__ ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_13})

V_325 = Vertex(name = 'V_325',
               particles = [ P.Z, P.Z, P.Pi13due__tilde__, P.Pi13due ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_64})

V_326 = Vertex(name = 'V_326',
               particles = [ P.Z, P.Z, P.Piu23due__tilde__, P.Piu23due ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_63})

V_327 = Vertex(name = 'V_327',
               particles = [ P.Z, P.Pi53tre__tilde__, P.Pi53tre ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_52})

V_328 = Vertex(name = 'V_328',
               particles = [ P.a, P.Z, P.Pi53tre__tilde__, P.Pi53tre ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_58})

V_329 = Vertex(name = 'V_329',
               particles = [ P.Z, P.Pid23tre__tilde__, P.Pid23tre ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_53})

V_330 = Vertex(name = 'V_330',
               particles = [ P.a, P.Z, P.Pid23tre__tilde__, P.Pid23tre ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_57})

V_331 = Vertex(name = 'V_331',
               particles = [ P.g, P.Z, P.Pi53tre__tilde__, P.Pi53tre ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_62})

V_332 = Vertex(name = 'V_332',
               particles = [ P.g, P.Z, P.Pid23tre__tilde__, P.Pid23tre ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_61})

V_333 = Vertex(name = 'V_333',
               particles = [ P.W__minus__, P.Z, P.Pi53tre, P.Pid23tre__tilde__ ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_16})

V_334 = Vertex(name = 'V_334',
               particles = [ P.W__plus__, P.Z, P.Pi53tre__tilde__, P.Pid23tre ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_16})

V_335 = Vertex(name = 'V_335',
               particles = [ P.Z, P.Z, P.Pi53tre__tilde__, P.Pi53tre ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_67})

V_336 = Vertex(name = 'V_336',
               particles = [ P.Z, P.Z, P.Pid23tre__tilde__, P.Pid23tre ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_68})

V_337 = Vertex(name = 'V_337',
               particles = [ P.Z, P.Pi13tre__tilde__, P.Pi13tre ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_49})

V_338 = Vertex(name = 'V_338',
               particles = [ P.a, P.Z, P.Pi13tre__tilde__, P.Pi13tre ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_54})

V_339 = Vertex(name = 'V_339',
               particles = [ P.Z, P.Piu23tre__tilde__, P.Piu23tre ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_48})

V_340 = Vertex(name = 'V_340',
               particles = [ P.a, P.Z, P.Piu23tre__tilde__, P.Piu23tre ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_55})

V_341 = Vertex(name = 'V_341',
               particles = [ P.g, P.Z, P.Pi13tre__tilde__, P.Pi13tre ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_59})

V_342 = Vertex(name = 'V_342',
               particles = [ P.g, P.Z, P.Piu23tre__tilde__, P.Piu23tre ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_60})

V_343 = Vertex(name = 'V_343',
               particles = [ P.W__minus__, P.Z, P.Pi13tre__tilde__, P.Piu23tre ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_13})

V_344 = Vertex(name = 'V_344',
               particles = [ P.W__plus__, P.Z, P.Pi13tre, P.Piu23tre__tilde__ ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_13})

V_345 = Vertex(name = 'V_345',
               particles = [ P.Z, P.Z, P.Pi13tre__tilde__, P.Pi13tre ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_64})

V_346 = Vertex(name = 'V_346',
               particles = [ P.Z, P.Z, P.Piu23tre__tilde__, P.Piu23tre ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_63})

