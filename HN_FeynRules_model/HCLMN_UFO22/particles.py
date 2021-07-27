# This file was automatically created by FeynRules 2.3.29
# Mathematica version: 11.1.1 for Mac OS X x86 (64-bit) (April 27, 2017)
# Date: Fri 22 Dec 2017 10:59:29


from __future__ import division
from object_library import all_particles, Particle
import parameters as Param

import propagators as Prop

a = Particle(pdg_code = 22,
             name = 'a',
             antiname = 'a',
             spin = 3,
             color = 1,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'a',
             antitexname = 'a',
             charge = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

Z = Particle(pdg_code = 23,
             name = 'Z',
             antiname = 'Z',
             spin = 3,
             color = 1,
             mass = Param.MZ,
             width = Param.WZ,
             texname = 'Z',
             antitexname = 'Z',
             charge = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

W__plus__ = Particle(pdg_code = 24,
                     name = 'W+',
                     antiname = 'W-',
                     spin = 3,
                     color = 1,
                     mass = Param.MW,
                     width = Param.WW,
                     texname = 'W+',
                     antitexname = 'W-',
                     charge = 1,
                     GhostNumber = 0,
                     LeptonNumber = 0,
                     Y = 0)

W__minus__ = W__plus__.anti()

g = Particle(pdg_code = 21,
             name = 'g',
             antiname = 'g',
             spin = 3,
             color = 8,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'g',
             antitexname = 'g',
             charge = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

ghA = Particle(pdg_code = 9000001,
               name = 'ghA',
               antiname = 'ghA~',
               spin = -1,
               color = 1,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'ghA',
               antitexname = 'ghA~',
               charge = 0,
               GhostNumber = 1,
               LeptonNumber = 0,
               Y = 0)

ghA__tilde__ = ghA.anti()

ghZ = Particle(pdg_code = 9000002,
               name = 'ghZ',
               antiname = 'ghZ~',
               spin = -1,
               color = 1,
               mass = Param.MZ,
               width = Param.WZ,
               texname = 'ghZ',
               antitexname = 'ghZ~',
               charge = 0,
               GhostNumber = 1,
               LeptonNumber = 0,
               Y = 0)

ghZ__tilde__ = ghZ.anti()

ghWp = Particle(pdg_code = 9000003,
                name = 'ghWp',
                antiname = 'ghWp~',
                spin = -1,
                color = 1,
                mass = Param.MW,
                width = Param.WW,
                texname = 'ghWp',
                antitexname = 'ghWp~',
                charge = 1,
                GhostNumber = 1,
                LeptonNumber = 0,
                Y = 0)

ghWp__tilde__ = ghWp.anti()

ghWm = Particle(pdg_code = 9000004,
                name = 'ghWm',
                antiname = 'ghWm~',
                spin = -1,
                color = 1,
                mass = Param.MW,
                width = Param.WW,
                texname = 'ghWm',
                antitexname = 'ghWm~',
                charge = -1,
                GhostNumber = 1,
                LeptonNumber = 0,
                Y = 0)

ghWm__tilde__ = ghWm.anti()

ghG = Particle(pdg_code = 82,
               name = 'ghG',
               antiname = 'ghG~',
               spin = -1,
               color = 8,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'ghG',
               antitexname = 'ghG~',
               charge = 0,
               GhostNumber = 1,
               LeptonNumber = 0,
               Y = 0)

ghG__tilde__ = ghG.anti()

ve = Particle(pdg_code = 12,
              name = 've',
              antiname = 've~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 've',
              antitexname = 've~',
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 1,
              Y = 0)

ve__tilde__ = ve.anti()

vm = Particle(pdg_code = 14,
              name = 'vm',
              antiname = 'vm~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 'vm',
              antitexname = 'vm~',
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 1,
              Y = 0)

vm__tilde__ = vm.anti()

vt = Particle(pdg_code = 16,
              name = 'vt',
              antiname = 'vt~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 'vt',
              antitexname = 'vt~',
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 1,
              Y = 0)

vt__tilde__ = vt.anti()

e__minus__ = Particle(pdg_code = 11,
                      name = 'e-',
                      antiname = 'e+',
                      spin = 2,
                      color = 1,
                      mass = Param.ZERO,
                      width = Param.ZERO,
                      texname = 'e-',
                      antitexname = 'e+',
                      charge = -1,
                      GhostNumber = 0,
                      LeptonNumber = 1,
                      Y = 0)

e__plus__ = e__minus__.anti()

mu__minus__ = Particle(pdg_code = 13,
                       name = 'mu-',
                       antiname = 'mu+',
                       spin = 2,
                       color = 1,
                       mass = Param.ZERO,
                       width = Param.ZERO,
                       texname = 'mu-',
                       antitexname = 'mu+',
                       charge = -1,
                       GhostNumber = 0,
                       LeptonNumber = 1,
                       Y = 0)

mu__plus__ = mu__minus__.anti()

ta__minus__ = Particle(pdg_code = 15,
                       name = 'ta-',
                       antiname = 'ta+',
                       spin = 2,
                       color = 1,
                       mass = Param.MTA,
                       width = Param.ZERO,
                       texname = 'ta-',
                       antitexname = 'ta+',
                       charge = -1,
                       GhostNumber = 0,
                       LeptonNumber = 1,
                       Y = 0)

ta__plus__ = ta__minus__.anti()

u = Particle(pdg_code = 2,
             name = 'u',
             antiname = 'u~',
             spin = 2,
             color = 3,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'u',
             antitexname = 'u~',
             charge = 2/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

u__tilde__ = u.anti()

c = Particle(pdg_code = 4,
             name = 'c',
             antiname = 'c~',
             spin = 2,
             color = 3,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'c',
             antitexname = 'c~',
             charge = 2/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

c__tilde__ = c.anti()

t = Particle(pdg_code = 6,
             name = 't',
             antiname = 't~',
             spin = 2,
             color = 3,
             mass = Param.MT,
             width = Param.WT,
             texname = 't',
             antitexname = 't~',
             charge = 2/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

t__tilde__ = t.anti()

d = Particle(pdg_code = 1,
             name = 'd',
             antiname = 'd~',
             spin = 2,
             color = 3,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'd',
             antitexname = 'd~',
             charge = -1/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

d__tilde__ = d.anti()

s = Particle(pdg_code = 3,
             name = 's',
             antiname = 's~',
             spin = 2,
             color = 3,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 's',
             antitexname = 's~',
             charge = -1/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

s__tilde__ = s.anti()

b = Particle(pdg_code = 5,
             name = 'b',
             antiname = 'b~',
             spin = 2,
             color = 3,
             mass = Param.MB,
             width = Param.ZERO,
             texname = 'b',
             antitexname = 'b~',
             charge = -1/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

b__tilde__ = b.anti()

H = Particle(pdg_code = 25,
             name = 'H',
             antiname = 'H',
             spin = 1,
             color = 1,
             mass = Param.MH,
             width = Param.WH,
             texname = 'H',
             antitexname = 'H',
             charge = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

G0 = Particle(pdg_code = 250,
              name = 'G0',
              antiname = 'G0',
              spin = 1,
              color = 1,
              mass = Param.MZ,
              width = Param.WZ,
              texname = 'G0',
              antitexname = 'G0',
              goldstone = True,
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 0,
              Y = 0)

G__plus__ = Particle(pdg_code = 251,
                     name = 'G+',
                     antiname = 'G-',
                     spin = 1,
                     color = 1,
                     mass = Param.MW,
                     width = Param.WW,
                     texname = 'G+',
                     antitexname = 'G-',
                     goldstone = True,
                     charge = 1,
                     GhostNumber = 0,
                     LeptonNumber = 0,
                     Y = 0)

G__minus__ = G__plus__.anti()

Us = Particle(pdg_code = 4000002,
              name = 'Us',
              antiname = 'Us~',
              spin = 2,
              color = 3,
              mass = Param.MUs,
              width = Param.WUs,
              texname = 'Us',
              antitexname = 'Us~',
              charge = 5/3,
              GhostNumber = 0,
              LeptonNumber = 0,
              Y = 0)

Us__tilde__ = Us.anti()

Cs = Particle(pdg_code = 4000004,
              name = 'Cs',
              antiname = 'Cs~',
              spin = 2,
              color = 3,
              mass = Param.MCs,
              width = Param.WCs,
              texname = 'Cs',
              antitexname = 'Cs~',
              charge = 5/3,
              GhostNumber = 0,
              LeptonNumber = 0,
              Y = 0)

Cs__tilde__ = Cs.anti()

Ts = Particle(pdg_code = 4000006,
              name = 'Ts',
              antiname = 'Ts~',
              spin = 2,
              color = 3,
              mass = Param.MTs,
              width = Param.WTs,
              texname = 'Ts',
              antitexname = 'Ts~',
              charge = 5/3,
              GhostNumber = 0,
              LeptonNumber = 0,
              Y = 0)

Ts__tilde__ = Ts.anti()

Ds = Particle(pdg_code = 4000008,
              name = 'Ds',
              antiname = 'Ds~',
              spin = 2,
              color = 3,
              mass = Param.MDs,
              width = Param.WDs,
              texname = 'Ds',
              antitexname = 'Ds~',
              charge = -4/3,
              GhostNumber = 0,
              LeptonNumber = 0,
              Y = 0)

Ds__tilde__ = Ds.anti()

Ss = Particle(pdg_code = 4000010,
              name = 'Ss',
              antiname = 'Ss~',
              spin = 2,
              color = 3,
              mass = Param.MSs,
              width = Param.WSs,
              texname = 'Ss',
              antitexname = 'Ss~',
              charge = -4/3,
              GhostNumber = 0,
              LeptonNumber = 0,
              Y = 0)

Ss__tilde__ = Ss.anti()

Bs = Particle(pdg_code = 4000011,
              name = 'Bs',
              antiname = 'Bs~',
              spin = 2,
              color = 3,
              mass = Param.MBs,
              width = Param.WBs,
              texname = 'Bs',
              antitexname = 'Bs~',
              charge = -4/3,
              GhostNumber = 0,
              LeptonNumber = 0,
              Y = 0)

Bs__tilde__ = Bs.anti()

N1Es = Particle(pdg_code = 4000012,
                name = 'N1Es',
                antiname = 'N1Es',
                spin = 2,
                color = 1,
                mass = Param.M1s,
                width = Param.WN1Es,
                texname = 'N1Es',
                antitexname = 'N1Es',
                charge = 0,
                GhostNumber = 0,
                LeptonNumber = 0,
                Y = 0)

N1Mus = Particle(pdg_code = 4000014,
                 name = 'N1Mus',
                 antiname = 'N1Mus',
                 spin = 2,
                 color = 1,
                 mass = Param.M1s,
                 width = Param.WN1Mus,
                 texname = 'N1Mus',
                 antitexname = 'N1Mus',
                 charge = 0,
                 GhostNumber = 0,
                 LeptonNumber = 0,
                 Y = 0)

N1Taus = Particle(pdg_code = 4000016,
                  name = 'N1Taus',
                  antiname = 'N1Taus',
                  spin = 2,
                  color = 1,
                  mass = Param.M1s,
                  width = Param.WN1Taus,
                  texname = 'N1Taus',
                  antitexname = 'N1Taus',
                  charge = 0,
                  GhostNumber = 0,
                  LeptonNumber = 0,
                  Y = 0)

N2Es = Particle(pdg_code = 4000013,
                name = 'N2Es',
                antiname = 'N2Es',
                spin = 2,
                color = 1,
                mass = Param.M2s,
                width = Param.WN2Es,
                texname = 'N2Es',
                antitexname = 'N2Es',
                charge = 0,
                GhostNumber = 0,
                LeptonNumber = 0,
                Y = 0)

N2Mus = Particle(pdg_code = 4000015,
                 name = 'N2Mus',
                 antiname = 'N2Mus',
                 spin = 2,
                 color = 1,
                 mass = Param.M2s,
                 width = Param.WN2Mus,
                 texname = 'N2Mus',
                 antitexname = 'N2Mus',
                 charge = 0,
                 GhostNumber = 0,
                 LeptonNumber = 0,
                 Y = 0)

N2Taus = Particle(pdg_code = 4000017,
                  name = 'N2Taus',
                  antiname = 'N2Taus',
                  spin = 2,
                  color = 1,
                  mass = Param.M2s,
                  width = Param.WN2Taus,
                  texname = 'N2Taus',
                  antitexname = 'N2Taus',
                  charge = 0,
                  GhostNumber = 0,
                  LeptonNumber = 0,
                  Y = 0)

Es = Particle(pdg_code = 4000018,
              name = 'Es',
              antiname = 'Es~',
              spin = 2,
              color = 1,
              mass = Param.MEs,
              width = Param.WEs,
              texname = 'Es',
              antitexname = 'Es~',
              charge = -2,
              GhostNumber = 0,
              LeptonNumber = 1,
              Y = 0)

Es__tilde__ = Es.anti()

Mus = Particle(pdg_code = 4000020,
               name = 'Mus',
               antiname = 'Mus~',
               spin = 2,
               color = 1,
               mass = Param.MMus,
               width = Param.WMus,
               texname = 'Mus',
               antitexname = 'Mus~',
               charge = -2,
               GhostNumber = 0,
               LeptonNumber = 1,
               Y = 0)

Mus__tilde__ = Mus.anti()

Taus = Particle(pdg_code = 4000022,
                name = 'Taus',
                antiname = 'Taus~',
                spin = 2,
                color = 1,
                mass = Param.MTaus,
                width = Param.WTaus,
                texname = 'Taus',
                antitexname = 'Taus~',
                charge = -2,
                GhostNumber = 0,
                LeptonNumber = 1,
                Y = 0)

Taus__tilde__ = Taus.anti()

Aux__plus__ = Particle(pdg_code = 9000005,
                       name = 'Aux+',
                       antiname = 'Aux-',
                       spin = 3,
                       color = 1,
                       mass = Param.Maux,
                       width = Param.ZERO,         
                	   propagator = Prop.V0,
                       texname = 'Aux+',
                       antitexname = 'Aux-',
                       charge = 1,
                       GhostNumber = 0,
                       LeptonNumber = 0,
                       Y = 0)

Aux__minus__ = Aux__plus__.anti()

Auxo = Particle(pdg_code = 9000006,
                name = 'Auxo',
                antiname = 'Auxo',
                spin = 3,
                color = 1,
                mass = Param.Mauxo,
                width = Param.ZERO,
                propagator = Prop.V0,
                texname = 'Auxo',
                antitexname = 'Auxo',
                charge = 0,
                GhostNumber = 0,
                LeptonNumber = 0,
                Y = 0)

