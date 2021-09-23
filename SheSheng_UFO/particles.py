# This file was automatically created by FeynRules 2.3.48
# Mathematica version: 12.3.1 for Mac OS X ARM (64-bit) (July 8, 2021)
# Date: Wed 22 Sep 2021 11:32:10


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
               width = Param.ZERO,
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
                width = Param.ZERO,
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
                width = Param.ZERO,
                texname = 'ghWm',
                antitexname = 'ghWm~',
                charge = -1,
                GhostNumber = 1,
                LeptonNumber = 0,
                Y = 0)

ghWm__tilde__ = ghWm.anti()

ghG = Particle(pdg_code = 9000005,
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
                       mass = Param.MM,
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
              width = Param.ZERO,
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
                     width = Param.ZERO,
                     texname = 'G+',
                     antitexname = 'G-',
                     goldstone = True,
                     charge = 1,
                     GhostNumber = 0,
                     LeptonNumber = 0,
                     Y = 0)

G__minus__ = G__plus__.anti()

E0 = Particle(pdg_code = 4000002,
              name = 'E0',
              antiname = 'E0~',
              spin = 2,
              color = 1,
              mass = Param.MUU,
              width = Param.WEs,
              texname = 'E0',
              antitexname = 'E0~',
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 1,
              Y = 0)

E0__tilde__ = E0.anti()

Mu0 = Particle(pdg_code = 4000004,
               name = 'Mu0',
               antiname = 'Mu0~',
               spin = 2,
               color = 1,
               mass = Param.MUU,
               width = Param.WMus,
               texname = 'Mu0',
               antitexname = 'Mu0~',
               charge = 0,
               GhostNumber = 0,
               LeptonNumber = 1,
               Y = 0)

Mu0__tilde__ = Mu0.anti()

Tau0 = Particle(pdg_code = 4000006,
                name = 'Tau0',
                antiname = 'Tau0~',
                spin = 2,
                color = 1,
                mass = Param.MUU,
                width = Param.WTaus,
                texname = 'Tau0',
                antitexname = 'Tau0~',
                charge = 0,
                GhostNumber = 0,
                LeptonNumber = 1,
                Y = 0)

Tau0__tilde__ = Tau0.anti()

Nc1 = Particle(pdg_code = 4000008,
               name = 'Nc1',
               antiname = 'Nc1~',
               spin = 2,
               color = 1,
               mass = Param.MUU,
               width = Param.WNc1,
               texname = 'Nc1',
               antitexname = 'Nc1~',
               charge = -1,
               GhostNumber = 0,
               LeptonNumber = 1,
               Y = 0)

Nc1__tilde__ = Nc1.anti()

Nc2 = Particle(pdg_code = 4000010,
               name = 'Nc2',
               antiname = 'Nc2~',
               spin = 2,
               color = 1,
               mass = Param.MUU,
               width = Param.WNc2,
               texname = 'Nc2',
               antitexname = 'Nc2~',
               charge = -1,
               GhostNumber = 0,
               LeptonNumber = 1,
               Y = 0)

Nc2__tilde__ = Nc2.anti()

Nc3 = Particle(pdg_code = 4000012,
               name = 'Nc3',
               antiname = 'Nc3~',
               spin = 2,
               color = 1,
               mass = Param.MUU,
               width = Param.WNc3,
               texname = 'Nc3',
               antitexname = 'Nc3~',
               charge = -1,
               GhostNumber = 0,
               LeptonNumber = 1,
               Y = 0)

Nc3__tilde__ = Nc3.anti()

Ec = Particle(pdg_code = 4000014,
              name = 'Ec',
              antiname = 'Ec~',
              spin = 2,
              color = 1,
              mass = Param.MUU,
              width = Param.WEc,
              texname = 'Ec',
              antitexname = 'Ec~',
              charge = -1,
              GhostNumber = 0,
              LeptonNumber = 1,
              Y = 0)

Ec__tilde__ = Ec.anti()

Muc = Particle(pdg_code = 4000016,
               name = 'Muc',
               antiname = 'Muc~',
               spin = 2,
               color = 1,
               mass = Param.MUU,
               width = Param.WMuc,
               texname = 'Muc',
               antitexname = 'Muc~',
               charge = -1,
               GhostNumber = 0,
               LeptonNumber = 1,
               Y = 0)

Muc__tilde__ = Muc.anti()

Tauc = Particle(pdg_code = 4000018,
                name = 'Tauc',
                antiname = 'Tauc~',
                spin = 2,
                color = 1,
                mass = Param.MUU,
                width = Param.WTauc,
                texname = 'Tauc',
                antitexname = 'Tauc~',
                charge = -1,
                GhostNumber = 0,
                LeptonNumber = 1,
                Y = 0)

Tauc__tilde__ = Tauc.anti()

N01 = Particle(pdg_code = 4000020,
               name = 'N01',
               antiname = 'N01~',
               spin = 2,
               color = 1,
               mass = Param.MUU,
               width = Param.WN01,
               texname = 'N01',
               antitexname = 'N01~',
               charge = 0,
               GhostNumber = 0,
               LeptonNumber = 1,
               Y = 0)

N01__tilde__ = N01.anti()

N02 = Particle(pdg_code = 4000022,
               name = 'N02',
               antiname = 'N02~',
               spin = 2,
               color = 1,
               mass = Param.MUU,
               width = Param.WN02,
               texname = 'N02',
               antitexname = 'N02~',
               charge = 0,
               GhostNumber = 0,
               LeptonNumber = 1,
               Y = 0)

N02__tilde__ = N02.anti()

N03 = Particle(pdg_code = 4000024,
               name = 'N03',
               antiname = 'N03~',
               spin = 2,
               color = 1,
               mass = Param.MUU,
               width = Param.WN03,
               texname = 'N03',
               antitexname = 'N03~',
               charge = 0,
               GhostNumber = 0,
               LeptonNumber = 1,
               Y = 0)

N03__tilde__ = N03.anti()

AL01__plus__ = Particle(pdg_code = 9000006,
                        name = 'AL01+',
                        antiname = 'AL01~',
                        spin = 1,
                        color = 1,
                        mass = Param.lc,
                        width = Param.ZERO,
                        texname = 'AL01+',
                        antitexname = 'AL01~',
                        charge = 1,
                        GhostNumber = 0,
                        LeptonNumber = 0,
                        Y = 0)

AL01__tilde__ = AL01__plus__.anti()

AL02__plus__ = Particle(pdg_code = 9000007,
                        name = 'AL02+',
                        antiname = 'AL02~',
                        spin = 1,
                        color = 1,
                        mass = Param.lc,
                        width = Param.ZERO,
                        texname = 'AL02+',
                        antitexname = 'AL02~',
                        charge = 1,
                        GhostNumber = 0,
                        LeptonNumber = 0,
                        Y = 0)

AL02__tilde__ = AL02__plus__.anti()

AL03__plus__ = Particle(pdg_code = 9000008,
                        name = 'AL03+',
                        antiname = 'AL03~',
                        spin = 1,
                        color = 1,
                        mass = Param.lc,
                        width = Param.ZERO,
                        texname = 'AL03+',
                        antitexname = 'AL03~',
                        charge = 1,
                        GhostNumber = 0,
                        LeptonNumber = 0,
                        Y = 0)

AL03__tilde__ = AL03__plus__.anti()

ANc1__plus__ = Particle(pdg_code = 9000009,
                        name = 'ANc1+',
                        antiname = 'ANc1~',
                        spin = 1,
                        color = 1,
                        mass = Param.lc,
                        width = Param.ZERO,
                        texname = 'ANc1+',
                        antitexname = 'ANc1~',
                        charge = 1,
                        GhostNumber = 0,
                        LeptonNumber = 0,
                        Y = 0)

ANc1__tilde__ = ANc1__plus__.anti()

ANc2__plus__ = Particle(pdg_code = 9000010,
                        name = 'ANc2+',
                        antiname = 'ANc2~',
                        spin = 1,
                        color = 1,
                        mass = Param.lc,
                        width = Param.ZERO,
                        texname = 'ANc2+',
                        antitexname = 'ANc2~',
                        charge = 1,
                        GhostNumber = 0,
                        LeptonNumber = 0,
                        Y = 0)

ANc2__tilde__ = ANc2__plus__.anti()

ANc3__plus__ = Particle(pdg_code = 9000011,
                        name = 'ANc3+',
                        antiname = 'ANc3~',
                        spin = 1,
                        color = 1,
                        mass = Param.lc,
                        width = Param.ZERO,
                        texname = 'ANc3+',
                        antitexname = 'ANc3~',
                        charge = 1,
                        GhostNumber = 0,
                        LeptonNumber = 0,
                        Y = 0)

ANc3__tilde__ = ANc3__plus__.anti()

ALc1 = Particle(pdg_code = 9000012,
                name = 'ALc1',
                antiname = 'ALc1',
                spin = 1,
                color = 1,
                mass = Param.lc,
                width = Param.ZERO,
                texname = 'ALc1',
                antitexname = 'ALc1',
                charge = 0,
                GhostNumber = 0,
                LeptonNumber = 0,
                Y = 0)

ALc2 = Particle(pdg_code = 9000013,
                name = 'ALc2',
                antiname = 'ALc2',
                spin = 1,
                color = 1,
                mass = Param.lc,
                width = Param.ZERO,
                texname = 'ALc2',
                antitexname = 'ALc2',
                charge = 0,
                GhostNumber = 0,
                LeptonNumber = 0,
                Y = 0)

ALc3 = Particle(pdg_code = 9000014,
                name = 'ALc3',
                antiname = 'ALc3',
                spin = 1,
                color = 1,
                mass = Param.lc,
                width = Param.ZERO,
                texname = 'ALc3',
                antitexname = 'ALc3',
                charge = 0,
                GhostNumber = 0,
                LeptonNumber = 0,
                Y = 0)

AN01 = Particle(pdg_code = 9000015,
                name = 'AN01',
                antiname = 'AN01',
                spin = 1,
                color = 1,
                mass = Param.lc,
                width = Param.ZERO,
                texname = 'AN01',
                antitexname = 'AN01',
                charge = 0,
                GhostNumber = 0,
                LeptonNumber = 0,
                Y = 0)

AN02 = Particle(pdg_code = 9000016,
                name = 'AN02',
                antiname = 'AN02',
                spin = 1,
                color = 1,
                mass = Param.lc,
                width = Param.ZERO,
                texname = 'AN02',
                antitexname = 'AN02',
                charge = 0,
                GhostNumber = 0,
                LeptonNumber = 0,
                Y = 0)

AN03 = Particle(pdg_code = 9000017,
                name = 'AN03',
                antiname = 'AN03',
                spin = 1,
                color = 1,
                mass = Param.lc,
                width = Param.ZERO,
                texname = 'AN03',
                antitexname = 'AN03',
                charge = 0,
                GhostNumber = 0,
                LeptonNumber = 0,
                Y = 0)

Pic1__plus__ = Particle(pdg_code = 9000018,
                        name = 'Pic1+',
                        antiname = 'Pic1~',
                        spin = 1,
                        color = 1,
                        mass = Param.MPi,
                        width = Param.WPic1,
                        texname = 'Pic1+',
                        antitexname = 'Pic1~',
                        charge = 1,
                        GhostNumber = 0,
                        LeptonNumber = 0,
                        Y = 0)

Pic1__tilde__ = Pic1__plus__.anti()

Pi0u = Particle(pdg_code = 9000019,
                name = 'Pi0u',
                antiname = 'Pi0u',
                spin = 1,
                color = 1,
                mass = Param.MPi,
                width = Param.WPi0u,
                texname = 'Pi0u',
                antitexname = 'Pi0u',
                charge = 0,
                GhostNumber = 0,
                LeptonNumber = 0,
                Y = 0)

Pi0d = Particle(pdg_code = 9000020,
                name = 'Pi0d',
                antiname = 'Pi0d',
                spin = 1,
                color = 1,
                mass = Param.MPi,
                width = Param.WPi0d,
                texname = 'Pi0d',
                antitexname = 'Pi0d',
                charge = 0,
                GhostNumber = 0,
                LeptonNumber = 0,
                Y = 0)

