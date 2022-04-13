# This file was automatically created by FeynRules 2.3.48
# Mathematica version: 12.3.1 for Mac OS X ARM (64-bit) (July 8, 2021)
# Date: Wed 13 Apr 2022 12:32:18


from object_library import all_decays, Decay
import particles as P


Decay_b = Decay(name = 'Decay_b',
                particle = P.b,
                partial_widths = {(P.Pi13,P.vt):'((-MassB**2 + MB**2)*(-3*MassB**2*Ystar**2 + 3*MB**2*Ystar**2))/(96.*cmath.pi*abs(MB)**3)',
                                  (P.Pic1__tilde__,P.t):'((-3*MassB**2*Ystar**2 + 3*MB**2*Ystar**2 + 3*MT**2*Ystar**2)*cmath.sqrt(MassB**4 - 2*MassB**2*MB**2 + MB**4 - 2*MassB**2*MT**2 - 2*MB**2*MT**2 + MT**4))/(96.*cmath.pi*abs(MB)**3)',
                                  (P.Pid23,P.ta__minus__):'((-3*MassB**2*Ystar**2 + 3*MB**2*Ystar**2 + 3*MTA**2*Ystar**2)*cmath.sqrt(MassB**4 - 2*MassB**2*MB**2 + MB**4 - 2*MassB**2*MTA**2 - 2*MB**2*MTA**2 + MTA**4))/(96.*cmath.pi*abs(MB)**3)',
                                  (P.W__minus__,P.t):'(((3*ee**2*MB**2)/(2.*sw**2) + (3*ee**2*MT**2)/(2.*sw**2) + (3*ee**2*MB**4)/(2.*MW**2*sw**2) - (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) + (3*ee**2*MT**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MB)**3)'})

Decay_E0 = Decay(name = 'Decay_E0',
                 particle = P.E0,
                 partial_widths = {(P.Pic1__plus__,P.e__minus__):'((-MassB**2 + MassF**2)*(-(MassB**2*Ystar**2) + MassF**2*Ystar**2))/(32.*cmath.pi*abs(MassF)**3)'})

Decay_Ec = Decay(name = 'Decay_Ec',
                 particle = P.Ec,
                 partial_widths = {(P.Pi0d,P.e__minus__):'((-MassB**2 + MassF**2)*(-(MassB**2*Ystar**2) + MassF**2*Ystar**2))/(32.*cmath.pi*abs(MassF)**3)'})

Decay_H = Decay(name = 'Decay_H',
                particle = P.H,
                partial_widths = {(P.b,P.b__tilde__):'((-12*MB**2*yb**2 + 3*MH**2*yb**2)*cmath.sqrt(-4*MB**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.t,P.t__tilde__):'((3*MH**2*yt**2 - 12*MT**2*yt**2)*cmath.sqrt(MH**4 - 4*MH**2*MT**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((MH**2*ytau**2 - 4*MTA**2*ytau**2)*cmath.sqrt(MH**4 - 4*MH**2*MTA**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.W__minus__,P.W__plus__):'(((3*ee**4*vev**2)/(4.*sw**4) + (ee**4*MH**4*vev**2)/(16.*MW**4*sw**4) - (ee**4*MH**2*vev**2)/(4.*MW**2*sw**4))*cmath.sqrt(MH**4 - 4*MH**2*MW**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.Z,P.Z):'(((9*ee**4*vev**2)/2. + (3*ee**4*MH**4*vev**2)/(8.*MZ**4) - (3*ee**4*MH**2*vev**2)/(2.*MZ**2) + (3*cw**4*ee**4*vev**2)/(4.*sw**4) + (cw**4*ee**4*MH**4*vev**2)/(16.*MZ**4*sw**4) - (cw**4*ee**4*MH**2*vev**2)/(4.*MZ**2*sw**4) + (3*cw**2*ee**4*vev**2)/sw**2 + (cw**2*ee**4*MH**4*vev**2)/(4.*MZ**4*sw**2) - (cw**2*ee**4*MH**2*vev**2)/(MZ**2*sw**2) + (3*ee**4*sw**2*vev**2)/cw**2 + (ee**4*MH**4*sw**2*vev**2)/(4.*cw**2*MZ**4) - (ee**4*MH**2*sw**2*vev**2)/(cw**2*MZ**2) + (3*ee**4*sw**4*vev**2)/(4.*cw**4) + (ee**4*MH**4*sw**4*vev**2)/(16.*cw**4*MZ**4) - (ee**4*MH**2*sw**4*vev**2)/(4.*cw**4*MZ**2))*cmath.sqrt(MH**4 - 4*MH**2*MZ**2))/(32.*cmath.pi*abs(MH)**3)'})

Decay_mu__minus__ = Decay(name = 'Decay_mu__minus__',
                          particle = P.mu__minus__,
                          partial_widths = {(P.Pi0d,P.Muc):'((-(MassB**2*Ystar**2) + MassF**2*Ystar**2 + MM**2*Ystar**2)*cmath.sqrt(MassB**4 - 2*MassB**2*MassF**2 + MassF**4 - 2*MassB**2*MM**2 - 2*MassF**2*MM**2 + MM**4))/(32.*cmath.pi*abs(MM)**3)',
                                            (P.Pi53__tilde__,P.c):'((-MassB**2 + MM**2)*(-3*MassB**2*Ystar**2 + 3*MM**2*Ystar**2))/(32.*cmath.pi*abs(MM)**3)',
                                            (P.Pic1__tilde__,P.Mu0):'((-(MassB**2*Ystar**2) + MassF**2*Ystar**2 + MM**2*Ystar**2)*cmath.sqrt(MassB**4 - 2*MassB**2*MassF**2 + MassF**4 - 2*MassB**2*MM**2 - 2*MassF**2*MM**2 + MM**4))/(32.*cmath.pi*abs(MM)**3)',
                                            (P.Pid23__tilde__,P.s):'((-MassB**2 + MM**2)*(-3*MassB**2*Ystar**2 + 3*MM**2*Ystar**2))/(32.*cmath.pi*abs(MM)**3)',
                                            (P.W__minus__,P.vm):'((MM**2 - MW**2)*((ee**2*MM**2)/(2.*sw**2) + (ee**2*MM**4)/(2.*MW**2*sw**2) - (ee**2*MW**2)/sw**2))/(32.*cmath.pi*abs(MM)**3)'})

Decay_Mu0 = Decay(name = 'Decay_Mu0',
                  particle = P.Mu0,
                  partial_widths = {(P.Pic1__plus__,P.mu__minus__):'((-(MassB**2*Ystar**2) + MassF**2*Ystar**2 + MM**2*Ystar**2)*cmath.sqrt(MassB**4 - 2*MassB**2*MassF**2 + MassF**4 - 2*MassB**2*MM**2 - 2*MassF**2*MM**2 + MM**4))/(32.*cmath.pi*abs(MassF)**3)'})

Decay_Muc = Decay(name = 'Decay_Muc',
                  particle = P.Muc,
                  partial_widths = {(P.Pi0d,P.mu__minus__):'((-(MassB**2*Ystar**2) + MassF**2*Ystar**2 + MM**2*Ystar**2)*cmath.sqrt(MassB**4 - 2*MassB**2*MassF**2 + MassF**4 - 2*MassB**2*MM**2 - 2*MassF**2*MM**2 + MM**4))/(32.*cmath.pi*abs(MassF)**3)'})

Decay_N01 = Decay(name = 'Decay_N01',
                  particle = P.N01,
                  partial_widths = {(P.Pi0u,P.ve):'((-MassB**2 + MassF**2)*(-(MassB**2*Ystar**2) + MassF**2*Ystar**2))/(32.*cmath.pi*abs(MassF)**3)'})

Decay_N02 = Decay(name = 'Decay_N02',
                  particle = P.N02,
                  partial_widths = {(P.Pi0u,P.vm):'((-MassB**2 + MassF**2)*(-(MassB**2*Ystar**2) + MassF**2*Ystar**2))/(32.*cmath.pi*abs(MassF)**3)'})

Decay_N03 = Decay(name = 'Decay_N03',
                  particle = P.N03,
                  partial_widths = {(P.Pi0u,P.vt):'((-MassB**2 + MassF**2)*(-(MassB**2*Ystar**2) + MassF**2*Ystar**2))/(32.*cmath.pi*abs(MassF)**3)'})

Decay_Nc1 = Decay(name = 'Decay_Nc1',
                  particle = P.Nc1,
                  partial_widths = {(P.Pic1__tilde__,P.ve):'((-MassB**2 + MassF**2)*(-(MassB**2*Ystar**2) + MassF**2*Ystar**2))/(32.*cmath.pi*abs(MassF)**3)'})

Decay_Nc2 = Decay(name = 'Decay_Nc2',
                  particle = P.Nc2,
                  partial_widths = {(P.Pic1__tilde__,P.vm):'((-MassB**2 + MassF**2)*(-(MassB**2*Ystar**2) + MassF**2*Ystar**2))/(32.*cmath.pi*abs(MassF)**3)'})

Decay_Nc3 = Decay(name = 'Decay_Nc3',
                  particle = P.Nc3,
                  partial_widths = {(P.Pic1__tilde__,P.vt):'((-MassB**2 + MassF**2)*(-(MassB**2*Ystar**2) + MassF**2*Ystar**2))/(32.*cmath.pi*abs(MassF)**3)'})

Decay_Pi0d = Decay(name = 'Decay_Pi0d',
                   particle = P.Pi0d,
                   partial_widths = {(P.a,P.a):'(aEW**2*MassB**6*Ustar**2)/(144.*cmath.pi**3*abs(MassB)**3)',
                                     (P.a,P.Z):'((MassB**2 - MZ**2)*(-0.041666666666666664*(aEW**2*MassB**4*Ustar**2)/(cw**2*cmath.pi**2) + (aEW**2*MassB**2*MZ**2*Ustar**2)/(12.*cw**2*cmath.pi**2) - (aEW**2*MZ**4*Ustar**2)/(24.*cw**2*cmath.pi**2) + (aEW**2*MassB**4*Ustar**2)/(32.*cw**2*cmath.pi**2*sw**2) - (aEW**2*MassB**2*MZ**2*Ustar**2)/(16.*cw**2*cmath.pi**2*sw**2) + (aEW**2*MZ**4*Ustar**2)/(32.*cw**2*cmath.pi**2*sw**2) + (aEW**2*MassB**4*sw**2*Ustar**2)/(72.*cw**2*cmath.pi**2) - (aEW**2*MassB**2*MZ**2*sw**2*Ustar**2)/(36.*cw**2*cmath.pi**2) + (aEW**2*MZ**4*sw**2*Ustar**2)/(72.*cw**2*cmath.pi**2)))/(16.*cmath.pi*abs(MassB)**3)',
                                     (P.b,P.b__tilde__):'((6*MassB**2*Ystar**2 - 24*MB**2*Ystar**2)*cmath.sqrt(MassB**4 - 4*MassB**2*MB**2))/(16.*cmath.pi*abs(MassB)**3)',
                                     (P.d,P.d__tilde__):'(3*MassB**4*Ystar**2)/(8.*cmath.pi*abs(MassB)**3)',
                                     (P.e__minus__,P.Ec__tilde__):'((MassB**2 - MassF**2)*(MassB**2*Ystar**2 - MassF**2*Ystar**2))/(16.*cmath.pi*abs(MassB)**3)',
                                     (P.Ec,P.e__plus__):'((MassB**2 - MassF**2)*(MassB**2*Ystar**2 - MassF**2*Ystar**2))/(16.*cmath.pi*abs(MassB)**3)',
                                     (P.mu__minus__,P.Muc__tilde__):'((MassB**2*Ystar**2 - MassF**2*Ystar**2 - MM**2*Ystar**2)*cmath.sqrt(MassB**4 - 2*MassB**2*MassF**2 + MassF**4 - 2*MassB**2*MM**2 - 2*MassF**2*MM**2 + MM**4))/(16.*cmath.pi*abs(MassB)**3)',
                                     (P.Muc,P.mu__plus__):'((MassB**2*Ystar**2 - MassF**2*Ystar**2 - MM**2*Ystar**2)*cmath.sqrt(MassB**4 - 2*MassB**2*MassF**2 + MassF**4 - 2*MassB**2*MM**2 - 2*MassF**2*MM**2 + MM**4))/(16.*cmath.pi*abs(MassB)**3)',
                                     (P.s,P.s__tilde__):'(3*MassB**4*Ystar**2)/(8.*cmath.pi*abs(MassB)**3)',
                                     (P.ta__minus__,P.Tauc__tilde__):'((MassB**2*Ystar**2 - MassF**2*Ystar**2 - MTA**2*Ystar**2)*cmath.sqrt(MassB**4 - 2*MassB**2*MassF**2 + MassF**4 - 2*MassB**2*MTA**2 - 2*MassF**2*MTA**2 + MTA**4))/(16.*cmath.pi*abs(MassB)**3)',
                                     (P.Tauc,P.ta__plus__):'((MassB**2*Ystar**2 - MassF**2*Ystar**2 - MTA**2*Ystar**2)*cmath.sqrt(MassB**4 - 2*MassB**2*MassF**2 + MassF**4 - 2*MassB**2*MTA**2 - 2*MassF**2*MTA**2 + MTA**4))/(16.*cmath.pi*abs(MassB)**3)',
                                     (P.W__minus__,P.W__plus__):'(((9*aEW**2*MassB**4*Ustar**2)/(128.*cmath.pi**2*sw**4) - (9*aEW**2*MassB**2*MW**2*Ustar**2)/(32.*cmath.pi**2*sw**4))*cmath.sqrt(MassB**4 - 4*MassB**2*MW**2))/(16.*cmath.pi*abs(MassB)**3)',
                                     (P.Z,P.Z):'(((aEW**2*MassB**4*Ustar**2)/(8.*cw**4*cmath.pi**2) - (aEW**2*MassB**2*MZ**2*Ustar**2)/(2.*cw**4*cmath.pi**2) + (9*aEW**2*MassB**4*Ustar**2)/(32.*cw**4*cmath.pi**2*sw**4) - (9*aEW**2*MassB**2*MZ**2*Ustar**2)/(8.*cw**4*cmath.pi**2*sw**4) - (3*aEW**2*MassB**4*Ustar**2)/(8.*cw**4*cmath.pi**2*sw**2) + (3*aEW**2*MassB**2*MZ**2*Ustar**2)/(2.*cw**4*cmath.pi**2*sw**2))*cmath.sqrt(MassB**4 - 4*MassB**2*MZ**2))/(32.*cmath.pi*abs(MassB)**3)'})

Decay_Pi0u = Decay(name = 'Decay_Pi0u',
                   particle = P.Pi0u,
                   partial_widths = {(P.a,P.a):'(aEW**2*MassB**6*Ustar**2)/(9.*cmath.pi**3*abs(MassB)**3)',
                                     (P.a,P.Z):'((MassB**2 - MZ**2)*(-0.3333333333333333*(aEW**2*MassB**4*Ustar**2)/(cw**2*cmath.pi**2) + (2*aEW**2*MassB**2*MZ**2*Ustar**2)/(3.*cw**2*cmath.pi**2) - (aEW**2*MZ**4*Ustar**2)/(3.*cw**2*cmath.pi**2) + (aEW**2*MassB**4*Ustar**2)/(8.*cw**2*cmath.pi**2*sw**2) - (aEW**2*MassB**2*MZ**2*Ustar**2)/(4.*cw**2*cmath.pi**2*sw**2) + (aEW**2*MZ**4*Ustar**2)/(8.*cw**2*cmath.pi**2*sw**2) + (2*aEW**2*MassB**4*sw**2*Ustar**2)/(9.*cw**2*cmath.pi**2) - (4*aEW**2*MassB**2*MZ**2*sw**2*Ustar**2)/(9.*cw**2*cmath.pi**2) + (2*aEW**2*MZ**4*sw**2*Ustar**2)/(9.*cw**2*cmath.pi**2)))/(16.*cmath.pi*abs(MassB)**3)',
                                     (P.c,P.c__tilde__):'(3*MassB**4*Ystar**2)/(8.*cmath.pi*abs(MassB)**3)',
                                     (P.N01,P.ve__tilde__):'((MassB**2 - MassF**2)*(MassB**2*Ystar**2 - MassF**2*Ystar**2))/(16.*cmath.pi*abs(MassB)**3)',
                                     (P.N02,P.vm__tilde__):'((MassB**2 - MassF**2)*(MassB**2*Ystar**2 - MassF**2*Ystar**2))/(16.*cmath.pi*abs(MassB)**3)',
                                     (P.N03,P.vt__tilde__):'((MassB**2 - MassF**2)*(MassB**2*Ystar**2 - MassF**2*Ystar**2))/(16.*cmath.pi*abs(MassB)**3)',
                                     (P.t,P.t__tilde__):'((6*MassB**2*Ystar**2 - 24*MT**2*Ystar**2)*cmath.sqrt(MassB**4 - 4*MassB**2*MT**2))/(16.*cmath.pi*abs(MassB)**3)',
                                     (P.u,P.u__tilde__):'(3*MassB**4*Ystar**2)/(8.*cmath.pi*abs(MassB)**3)',
                                     (P.ve,P.N01__tilde__):'((MassB**2 - MassF**2)*(MassB**2*Ystar**2 - MassF**2*Ystar**2))/(16.*cmath.pi*abs(MassB)**3)',
                                     (P.vm,P.N02__tilde__):'((MassB**2 - MassF**2)*(MassB**2*Ystar**2 - MassF**2*Ystar**2))/(16.*cmath.pi*abs(MassB)**3)',
                                     (P.vt,P.N03__tilde__):'((MassB**2 - MassF**2)*(MassB**2*Ystar**2 - MassF**2*Ystar**2))/(16.*cmath.pi*abs(MassB)**3)',
                                     (P.W__minus__,P.W__plus__):'(((9*aEW**2*MassB**4*Ustar**2)/(128.*cmath.pi**2*sw**4) - (9*aEW**2*MassB**2*MW**2*Ustar**2)/(32.*cmath.pi**2*sw**4))*cmath.sqrt(MassB**4 - 4*MassB**2*MW**2))/(16.*cmath.pi*abs(MassB)**3)',
                                     (P.Z,P.Z):'(((aEW**2*MassB**4*Ustar**2)/(2.*cw**4*cmath.pi**2) - (2*aEW**2*MassB**2*MZ**2*Ustar**2)/(cw**4*cmath.pi**2) + (9*aEW**2*MassB**4*Ustar**2)/(32.*cw**4*cmath.pi**2*sw**4) - (9*aEW**2*MassB**2*MZ**2*Ustar**2)/(8.*cw**4*cmath.pi**2*sw**4) - (3*aEW**2*MassB**4*Ustar**2)/(4.*cw**4*cmath.pi**2*sw**2) + (3*aEW**2*MassB**2*MZ**2*Ustar**2)/(cw**4*cmath.pi**2*sw**2))*cmath.sqrt(MassB**4 - 4*MassB**2*MZ**2))/(32.*cmath.pi*abs(MassB)**3)'})

Decay_Pi13 = Decay(name = 'Decay_Pi13',
                   particle = P.Pi13,
                   partial_widths = {(P.b,P.vt__tilde__):'((MassB**2 - MB**2)*(3*MassB**2*Ystar**2 - 3*MB**2*Ystar**2))/(48.*cmath.pi*abs(MassB)**3)',
                                     (P.d,P.ve__tilde__):'(MassB**4*Ystar**2)/(16.*cmath.pi*abs(MassB)**3)',
                                     (P.s,P.vm__tilde__):'(MassB**4*Ystar**2)/(16.*cmath.pi*abs(MassB)**3)'})

Decay_Pi53 = Decay(name = 'Decay_Pi53',
                   particle = P.Pi53,
                   partial_widths = {(P.c,P.mu__plus__):'((MassB**2 - MM**2)*(3*MassB**2*Ystar**2 - 3*MM**2*Ystar**2))/(48.*cmath.pi*abs(MassB)**3)',
                                     (P.t,P.ta__plus__):'((3*MassB**2*Ystar**2 - 3*MT**2*Ystar**2 - 3*MTA**2*Ystar**2)*cmath.sqrt(MassB**4 - 2*MassB**2*MT**2 + MT**4 - 2*MassB**2*MTA**2 - 2*MT**2*MTA**2 + MTA**4))/(48.*cmath.pi*abs(MassB)**3)',
                                     (P.u,P.e__plus__):'(MassB**4*Ystar**2)/(16.*cmath.pi*abs(MassB)**3)'})

Decay_Pic1__plus__ = Decay(name = 'Decay_Pic1__plus__',
                           particle = P.Pic1__plus__,
                           partial_widths = {(P.a,P.W__plus__):'((MassB**2 - MW**2)*((9*aEW**2*MassB**4*Ustar**2)/(16.*cmath.pi**2*sw**2) - (9*aEW**2*MassB**2*MW**2*Ustar**2)/(8.*cmath.pi**2*sw**2) + (9*aEW**2*MW**4*Ustar**2)/(16.*cmath.pi**2*sw**2)))/(16.*cmath.pi*abs(MassB)**3)',
                                             (P.c,P.s__tilde__):'(3*MassB**4*Ystar**2)/(16.*cmath.pi*abs(MassB)**3)',
                                             (P.E0,P.e__plus__):'((MassB**2 - MassF**2)*(MassB**2*Ystar**2 - MassF**2*Ystar**2))/(16.*cmath.pi*abs(MassB)**3)',
                                             (P.Mu0,P.mu__plus__):'((MassB**2*Ystar**2 - MassF**2*Ystar**2 - MM**2*Ystar**2)*cmath.sqrt(MassB**4 - 2*MassB**2*MassF**2 + MassF**4 - 2*MassB**2*MM**2 - 2*MassF**2*MM**2 + MM**4))/(16.*cmath.pi*abs(MassB)**3)',
                                             (P.t,P.b__tilde__):'((3*MassB**2*Ystar**2 - 3*MB**2*Ystar**2 - 3*MT**2*Ystar**2)*cmath.sqrt(MassB**4 - 2*MassB**2*MB**2 + MB**4 - 2*MassB**2*MT**2 - 2*MB**2*MT**2 + MT**4))/(16.*cmath.pi*abs(MassB)**3)',
                                             (P.Tau0,P.ta__plus__):'((MassB**2*Ystar**2 - MassF**2*Ystar**2 - MTA**2*Ystar**2)*cmath.sqrt(MassB**4 - 2*MassB**2*MassF**2 + MassF**4 - 2*MassB**2*MTA**2 - 2*MassF**2*MTA**2 + MTA**4))/(16.*cmath.pi*abs(MassB)**3)',
                                             (P.u,P.d__tilde__):'(3*MassB**4*Ystar**2)/(16.*cmath.pi*abs(MassB)**3)',
                                             (P.ve,P.Nc1__tilde__):'((MassB**2 - MassF**2)*(MassB**2*Ystar**2 - MassF**2*Ystar**2))/(16.*cmath.pi*abs(MassB)**3)',
                                             (P.vm,P.Nc2__tilde__):'((MassB**2 - MassF**2)*(MassB**2*Ystar**2 - MassF**2*Ystar**2))/(16.*cmath.pi*abs(MassB)**3)',
                                             (P.vt,P.Nc3__tilde__):'((MassB**2 - MassF**2)*(MassB**2*Ystar**2 - MassF**2*Ystar**2))/(16.*cmath.pi*abs(MassB)**3)',
                                             (P.W__plus__,P.Z):'(((25*aEW**2*MassB**4*Ustar**2)/(576.*cmath.pi**2) - (25*aEW**2*MassB**2*MW**2*Ustar**2)/(288.*cmath.pi**2) + (25*aEW**2*MW**4*Ustar**2)/(576.*cmath.pi**2) - (25*aEW**2*MassB**2*MZ**2*Ustar**2)/(288.*cmath.pi**2) - (25*aEW**2*MW**2*MZ**2*Ustar**2)/(288.*cmath.pi**2) + (25*aEW**2*MZ**4*Ustar**2)/(576.*cmath.pi**2) + (aEW**2*MassB**4*Ustar**2)/(256.*cmath.pi**2*sw**4) - (aEW**2*MassB**2*MW**2*Ustar**2)/(128.*cmath.pi**2*sw**4) + (aEW**2*MW**4*Ustar**2)/(256.*cmath.pi**2*sw**4) - (aEW**2*MassB**2*MZ**2*Ustar**2)/(128.*cmath.pi**2*sw**4) - (aEW**2*MW**2*MZ**2*Ustar**2)/(128.*cmath.pi**2*sw**4) + (aEW**2*MZ**4*Ustar**2)/(256.*cmath.pi**2*sw**4) - (5*aEW**2*MassB**4*Ustar**2)/(192.*cmath.pi**2*sw**2) + (5*aEW**2*MassB**2*MW**2*Ustar**2)/(96.*cmath.pi**2*sw**2) - (5*aEW**2*MW**4*Ustar**2)/(192.*cmath.pi**2*sw**2) + (5*aEW**2*MassB**2*MZ**2*Ustar**2)/(96.*cmath.pi**2*sw**2) + (5*aEW**2*MW**2*MZ**2*Ustar**2)/(96.*cmath.pi**2*sw**2) - (5*aEW**2*MZ**4*Ustar**2)/(192.*cmath.pi**2*sw**2))*cmath.sqrt(MassB**4 - 2*MassB**2*MW**2 + MW**4 - 2*MassB**2*MZ**2 - 2*MW**2*MZ**2 + MZ**4))/(16.*cmath.pi*abs(MassB)**3)'})

Decay_Pid23 = Decay(name = 'Decay_Pid23',
                    particle = P.Pid23,
                    partial_widths = {(P.b,P.ta__plus__):'((3*MassB**2*Ystar**2 - 3*MB**2*Ystar**2 - 3*MTA**2*Ystar**2)*cmath.sqrt(MassB**4 - 2*MassB**2*MB**2 + MB**4 - 2*MassB**2*MTA**2 - 2*MB**2*MTA**2 + MTA**4))/(48.*cmath.pi*abs(MassB)**3)',
                                      (P.d,P.e__plus__):'(MassB**4*Ystar**2)/(16.*cmath.pi*abs(MassB)**3)',
                                      (P.s,P.mu__plus__):'((MassB**2 - MM**2)*(3*MassB**2*Ystar**2 - 3*MM**2*Ystar**2))/(48.*cmath.pi*abs(MassB)**3)'})

Decay_Piu23 = Decay(name = 'Decay_Piu23',
                    particle = P.Piu23,
                    partial_widths = {(P.c,P.vm__tilde__):'(MassB**4*Ystar**2)/(16.*cmath.pi*abs(MassB)**3)',
                                      (P.t,P.vt__tilde__):'((MassB**2 - MT**2)*(3*MassB**2*Ystar**2 - 3*MT**2*Ystar**2))/(48.*cmath.pi*abs(MassB)**3)',
                                      (P.u,P.ve__tilde__):'(MassB**4*Ystar**2)/(16.*cmath.pi*abs(MassB)**3)'})

Decay_t = Decay(name = 'Decay_t',
                particle = P.t,
                partial_widths = {(P.Pi53,P.ta__minus__):'((-3*MassB**2*Ystar**2 + 3*MT**2*Ystar**2 + 3*MTA**2*Ystar**2)*cmath.sqrt(MassB**4 - 2*MassB**2*MT**2 + MT**4 - 2*MassB**2*MTA**2 - 2*MT**2*MTA**2 + MTA**4))/(96.*cmath.pi*abs(MT)**3)',
                                  (P.Pic1__plus__,P.b):'((-3*MassB**2*Ystar**2 + 3*MB**2*Ystar**2 + 3*MT**2*Ystar**2)*cmath.sqrt(MassB**4 - 2*MassB**2*MB**2 + MB**4 - 2*MassB**2*MT**2 - 2*MB**2*MT**2 + MT**4))/(96.*cmath.pi*abs(MT)**3)',
                                  (P.Piu23,P.vt):'((-MassB**2 + MT**2)*(-3*MassB**2*Ystar**2 + 3*MT**2*Ystar**2))/(96.*cmath.pi*abs(MT)**3)',
                                  (P.W__plus__,P.b):'(((3*ee**2*MB**2)/(2.*sw**2) + (3*ee**2*MT**2)/(2.*sw**2) + (3*ee**2*MB**4)/(2.*MW**2*sw**2) - (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) + (3*ee**2*MT**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MT)**3)'})

Decay_ta__minus__ = Decay(name = 'Decay_ta__minus__',
                          particle = P.ta__minus__,
                          partial_widths = {(P.Pi0d,P.Tauc):'((-(MassB**2*Ystar**2) + MassF**2*Ystar**2 + MTA**2*Ystar**2)*cmath.sqrt(MassB**4 - 2*MassB**2*MassF**2 + MassF**4 - 2*MassB**2*MTA**2 - 2*MassF**2*MTA**2 + MTA**4))/(32.*cmath.pi*abs(MTA)**3)',
                                            (P.Pi53__tilde__,P.t):'((-3*MassB**2*Ystar**2 + 3*MT**2*Ystar**2 + 3*MTA**2*Ystar**2)*cmath.sqrt(MassB**4 - 2*MassB**2*MT**2 + MT**4 - 2*MassB**2*MTA**2 - 2*MT**2*MTA**2 + MTA**4))/(32.*cmath.pi*abs(MTA)**3)',
                                            (P.Pic1__tilde__,P.Tau0):'((-(MassB**2*Ystar**2) + MassF**2*Ystar**2 + MTA**2*Ystar**2)*cmath.sqrt(MassB**4 - 2*MassB**2*MassF**2 + MassF**4 - 2*MassB**2*MTA**2 - 2*MassF**2*MTA**2 + MTA**4))/(32.*cmath.pi*abs(MTA)**3)',
                                            (P.Pid23__tilde__,P.b):'((-3*MassB**2*Ystar**2 + 3*MB**2*Ystar**2 + 3*MTA**2*Ystar**2)*cmath.sqrt(MassB**4 - 2*MassB**2*MB**2 + MB**4 - 2*MassB**2*MTA**2 - 2*MB**2*MTA**2 + MTA**4))/(32.*cmath.pi*abs(MTA)**3)',
                                            (P.W__minus__,P.vt):'((MTA**2 - MW**2)*((ee**2*MTA**2)/(2.*sw**2) + (ee**2*MTA**4)/(2.*MW**2*sw**2) - (ee**2*MW**2)/sw**2))/(32.*cmath.pi*abs(MTA)**3)'})

Decay_Tau0 = Decay(name = 'Decay_Tau0',
                   particle = P.Tau0,
                   partial_widths = {(P.Pic1__plus__,P.ta__minus__):'((-(MassB**2*Ystar**2) + MassF**2*Ystar**2 + MTA**2*Ystar**2)*cmath.sqrt(MassB**4 - 2*MassB**2*MassF**2 + MassF**4 - 2*MassB**2*MTA**2 - 2*MassF**2*MTA**2 + MTA**4))/(32.*cmath.pi*abs(MassF)**3)'})

Decay_Tauc = Decay(name = 'Decay_Tauc',
                   particle = P.Tauc,
                   partial_widths = {(P.Pi0d,P.ta__minus__):'((-(MassB**2*Ystar**2) + MassF**2*Ystar**2 + MTA**2*Ystar**2)*cmath.sqrt(MassB**4 - 2*MassB**2*MassF**2 + MassF**4 - 2*MassB**2*MTA**2 - 2*MassF**2*MTA**2 + MTA**4))/(32.*cmath.pi*abs(MassF)**3)'})

Decay_W__plus__ = Decay(name = 'Decay_W__plus__',
                        particle = P.W__plus__,
                        partial_widths = {(P.a,P.Pic1__plus__):'((-MassB**2 + MW**2)*((9*aEW**2*MassB**4*Ustar**2)/(16.*cmath.pi**2*sw**2) - (9*aEW**2*MassB**2*MW**2*Ustar**2)/(8.*cmath.pi**2*sw**2) + (9*aEW**2*MW**4*Ustar**2)/(16.*cmath.pi**2*sw**2)))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.c,P.d__tilde__):'(CKM2x1*ee**2*MW**4*complexconjugate(CKM2x1))/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.c,P.s__tilde__):'(CKM2x2*ee**2*MW**4*complexconjugate(CKM2x2))/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.Pi0d,P.Pic1__plus__):'((-0.5*(ee**2*MassB**2)/sw**2 + (ee**2*MW**2)/(8.*sw**2))*cmath.sqrt(-4*MassB**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.Pi0u,P.Pic1__plus__):'((-0.5*(ee**2*MassB**2)/sw**2 + (ee**2*MW**2)/(8.*sw**2))*cmath.sqrt(-4*MassB**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.Pi13__tilde__,P.Piu23):'(((-6*ee**2*MassB**2)/sw**2 + (3*ee**2*MW**2)/(2.*sw**2))*cmath.sqrt(-4*MassB**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.Pi53,P.Pid23__tilde__):'(((-6*ee**2*MassB**2)/sw**2 + (3*ee**2*MW**2)/(2.*sw**2))*cmath.sqrt(-4*MassB**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.Pic1__plus__,P.Z):'(((25*aEW**2*MassB**4*Ustar**2)/(576.*cmath.pi**2) - (25*aEW**2*MassB**2*MW**2*Ustar**2)/(288.*cmath.pi**2) + (25*aEW**2*MW**4*Ustar**2)/(576.*cmath.pi**2) - (25*aEW**2*MassB**2*MZ**2*Ustar**2)/(288.*cmath.pi**2) - (25*aEW**2*MW**2*MZ**2*Ustar**2)/(288.*cmath.pi**2) + (25*aEW**2*MZ**4*Ustar**2)/(576.*cmath.pi**2) + (aEW**2*MassB**4*Ustar**2)/(256.*cmath.pi**2*sw**4) - (aEW**2*MassB**2*MW**2*Ustar**2)/(128.*cmath.pi**2*sw**4) + (aEW**2*MW**4*Ustar**2)/(256.*cmath.pi**2*sw**4) - (aEW**2*MassB**2*MZ**2*Ustar**2)/(128.*cmath.pi**2*sw**4) - (aEW**2*MW**2*MZ**2*Ustar**2)/(128.*cmath.pi**2*sw**4) + (aEW**2*MZ**4*Ustar**2)/(256.*cmath.pi**2*sw**4) - (5*aEW**2*MassB**4*Ustar**2)/(192.*cmath.pi**2*sw**2) + (5*aEW**2*MassB**2*MW**2*Ustar**2)/(96.*cmath.pi**2*sw**2) - (5*aEW**2*MW**4*Ustar**2)/(192.*cmath.pi**2*sw**2) + (5*aEW**2*MassB**2*MZ**2*Ustar**2)/(96.*cmath.pi**2*sw**2) + (5*aEW**2*MW**2*MZ**2*Ustar**2)/(96.*cmath.pi**2*sw**2) - (5*aEW**2*MZ**4*Ustar**2)/(192.*cmath.pi**2*sw**2))*cmath.sqrt(MassB**4 - 2*MassB**2*MW**2 + MW**4 - 2*MassB**2*MZ**2 - 2*MW**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.t,P.b__tilde__):'(((-3*ee**2*MB**2)/(2.*sw**2) - (3*ee**2*MT**2)/(2.*sw**2) - (3*ee**2*MB**4)/(2.*MW**2*sw**2) + (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) - (3*ee**2*MT**4)/(2.*MW**2*sw**2) + (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.u,P.d__tilde__):'(CKM1x1*ee**2*MW**4*complexconjugate(CKM1x1))/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.u,P.s__tilde__):'(CKM1x2*ee**2*MW**4*complexconjugate(CKM1x2))/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.ve,P.e__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.vm,P.mu__plus__):'((-MM**2 + MW**2)*(-0.5*(ee**2*MM**2)/sw**2 - (ee**2*MM**4)/(2.*MW**2*sw**2) + (ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.vt,P.ta__plus__):'((-MTA**2 + MW**2)*(-0.5*(ee**2*MTA**2)/sw**2 - (ee**2*MTA**4)/(2.*MW**2*sw**2) + (ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)'})

Decay_Z = Decay(name = 'Decay_Z',
                particle = P.Z,
                partial_widths = {(P.a,P.Pi0d):'((-MassB**2 + MZ**2)*(-0.041666666666666664*(aEW**2*MassB**4*Ustar**2)/(cw**2*cmath.pi**2) + (aEW**2*MassB**2*MZ**2*Ustar**2)/(12.*cw**2*cmath.pi**2) - (aEW**2*MZ**4*Ustar**2)/(24.*cw**2*cmath.pi**2) + (aEW**2*MassB**4*Ustar**2)/(32.*cw**2*cmath.pi**2*sw**2) - (aEW**2*MassB**2*MZ**2*Ustar**2)/(16.*cw**2*cmath.pi**2*sw**2) + (aEW**2*MZ**4*Ustar**2)/(32.*cw**2*cmath.pi**2*sw**2) + (aEW**2*MassB**4*sw**2*Ustar**2)/(72.*cw**2*cmath.pi**2) - (aEW**2*MassB**2*MZ**2*sw**2*Ustar**2)/(36.*cw**2*cmath.pi**2) + (aEW**2*MZ**4*sw**2*Ustar**2)/(72.*cw**2*cmath.pi**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.a,P.Pi0u):'((-MassB**2 + MZ**2)*(-0.3333333333333333*(aEW**2*MassB**4*Ustar**2)/(cw**2*cmath.pi**2) + (2*aEW**2*MassB**2*MZ**2*Ustar**2)/(3.*cw**2*cmath.pi**2) - (aEW**2*MZ**4*Ustar**2)/(3.*cw**2*cmath.pi**2) + (aEW**2*MassB**4*Ustar**2)/(8.*cw**2*cmath.pi**2*sw**2) - (aEW**2*MassB**2*MZ**2*Ustar**2)/(4.*cw**2*cmath.pi**2*sw**2) + (aEW**2*MZ**4*Ustar**2)/(8.*cw**2*cmath.pi**2*sw**2) + (2*aEW**2*MassB**4*sw**2*Ustar**2)/(9.*cw**2*cmath.pi**2) - (4*aEW**2*MassB**2*MZ**2*sw**2*Ustar**2)/(9.*cw**2*cmath.pi**2) + (2*aEW**2*MZ**4*sw**2*Ustar**2)/(9.*cw**2*cmath.pi**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.b,P.b__tilde__):'((-7*ee**2*MB**2 + ee**2*MZ**2 - (3*cw**2*ee**2*MB**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) - (17*ee**2*MB**2*sw**2)/(6.*cw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MB**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.c,P.c__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.d,P.d__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.e__minus__,P.e__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.mu__minus__,P.mu__plus__):'((-5*ee**2*MM**2 - ee**2*MZ**2 - (cw**2*ee**2*MM**2)/(2.*sw**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MM**2*sw**2)/(2.*cw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2))*cmath.sqrt(-4*MM**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.Pi13__tilde__,P.Pi13):'((-2*ee**2*MassB**2 + (ee**2*MZ**2)/2. - (3*cw**2*ee**2*MassB**2)/sw**2 + (3*cw**2*ee**2*MZ**2)/(4.*sw**2) - (ee**2*MassB**2*sw**2)/(3.*cw**2) + (ee**2*MZ**2*sw**2)/(12.*cw**2))*cmath.sqrt(-4*MassB**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.Pi53__tilde__,P.Pi53):'((14*ee**2*MassB**2 - (7*ee**2*MZ**2)/2. - (3*cw**2*ee**2*MassB**2)/sw**2 + (3*cw**2*ee**2*MZ**2)/(4.*sw**2) - (49*ee**2*MassB**2*sw**2)/(3.*cw**2) + (49*ee**2*MZ**2*sw**2)/(12.*cw**2))*cmath.sqrt(-4*MassB**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.Pic1__plus__,P.W__minus__):'(((25*aEW**2*MassB**4*Ustar**2)/(576.*cmath.pi**2) - (25*aEW**2*MassB**2*MW**2*Ustar**2)/(288.*cmath.pi**2) + (25*aEW**2*MW**4*Ustar**2)/(576.*cmath.pi**2) - (25*aEW**2*MassB**2*MZ**2*Ustar**2)/(288.*cmath.pi**2) - (25*aEW**2*MW**2*MZ**2*Ustar**2)/(288.*cmath.pi**2) + (25*aEW**2*MZ**4*Ustar**2)/(576.*cmath.pi**2) + (aEW**2*MassB**4*Ustar**2)/(256.*cmath.pi**2*sw**4) - (aEW**2*MassB**2*MW**2*Ustar**2)/(128.*cmath.pi**2*sw**4) + (aEW**2*MW**4*Ustar**2)/(256.*cmath.pi**2*sw**4) - (aEW**2*MassB**2*MZ**2*Ustar**2)/(128.*cmath.pi**2*sw**4) - (aEW**2*MW**2*MZ**2*Ustar**2)/(128.*cmath.pi**2*sw**4) + (aEW**2*MZ**4*Ustar**2)/(256.*cmath.pi**2*sw**4) - (5*aEW**2*MassB**4*Ustar**2)/(192.*cmath.pi**2*sw**2) + (5*aEW**2*MassB**2*MW**2*Ustar**2)/(96.*cmath.pi**2*sw**2) - (5*aEW**2*MW**4*Ustar**2)/(192.*cmath.pi**2*sw**2) + (5*aEW**2*MassB**2*MZ**2*Ustar**2)/(96.*cmath.pi**2*sw**2) + (5*aEW**2*MW**2*MZ**2*Ustar**2)/(96.*cmath.pi**2*sw**2) - (5*aEW**2*MZ**4*Ustar**2)/(192.*cmath.pi**2*sw**2))*cmath.sqrt(MassB**4 - 2*MassB**2*MW**2 + MW**4 - 2*MassB**2*MZ**2 - 2*MW**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.Pic1__tilde__,P.Pic1__plus__):'((2*ee**2*MassB**2 - (ee**2*MZ**2)/2. - (cw**2*ee**2*MassB**2)/sw**2 + (cw**2*ee**2*MZ**2)/(4.*sw**2) - (ee**2*MassB**2*sw**2)/cw**2 + (ee**2*MZ**2*sw**2)/(4.*cw**2))*cmath.sqrt(-4*MassB**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.Pic1__tilde__,P.W__plus__):'(((25*aEW**2*MassB**4*Ustar**2)/(576.*cmath.pi**2) - (25*aEW**2*MassB**2*MW**2*Ustar**2)/(288.*cmath.pi**2) + (25*aEW**2*MW**4*Ustar**2)/(576.*cmath.pi**2) - (25*aEW**2*MassB**2*MZ**2*Ustar**2)/(288.*cmath.pi**2) - (25*aEW**2*MW**2*MZ**2*Ustar**2)/(288.*cmath.pi**2) + (25*aEW**2*MZ**4*Ustar**2)/(576.*cmath.pi**2) + (aEW**2*MassB**4*Ustar**2)/(256.*cmath.pi**2*sw**4) - (aEW**2*MassB**2*MW**2*Ustar**2)/(128.*cmath.pi**2*sw**4) + (aEW**2*MW**4*Ustar**2)/(256.*cmath.pi**2*sw**4) - (aEW**2*MassB**2*MZ**2*Ustar**2)/(128.*cmath.pi**2*sw**4) - (aEW**2*MW**2*MZ**2*Ustar**2)/(128.*cmath.pi**2*sw**4) + (aEW**2*MZ**4*Ustar**2)/(256.*cmath.pi**2*sw**4) - (5*aEW**2*MassB**4*Ustar**2)/(192.*cmath.pi**2*sw**2) + (5*aEW**2*MassB**2*MW**2*Ustar**2)/(96.*cmath.pi**2*sw**2) - (5*aEW**2*MW**4*Ustar**2)/(192.*cmath.pi**2*sw**2) + (5*aEW**2*MassB**2*MZ**2*Ustar**2)/(96.*cmath.pi**2*sw**2) + (5*aEW**2*MW**2*MZ**2*Ustar**2)/(96.*cmath.pi**2*sw**2) - (5*aEW**2*MZ**4*Ustar**2)/(192.*cmath.pi**2*sw**2))*cmath.sqrt(MassB**4 - 2*MassB**2*MW**2 + MW**4 - 2*MassB**2*MZ**2 - 2*MW**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.Pid23__tilde__,P.Pid23):'((-14*ee**2*MassB**2 + (7*ee**2*MZ**2)/2. - (3*cw**2*ee**2*MassB**2)/sw**2 + (3*cw**2*ee**2*MZ**2)/(4.*sw**2) - (49*ee**2*MassB**2*sw**2)/(3.*cw**2) + (49*ee**2*MZ**2*sw**2)/(12.*cw**2))*cmath.sqrt(-4*MassB**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.Piu23__tilde__,P.Piu23):'((2*ee**2*MassB**2 - (ee**2*MZ**2)/2. - (3*cw**2*ee**2*MassB**2)/sw**2 + (3*cw**2*ee**2*MZ**2)/(4.*sw**2) - (ee**2*MassB**2*sw**2)/(3.*cw**2) + (ee**2*MZ**2*sw**2)/(12.*cw**2))*cmath.sqrt(-4*MassB**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.s,P.s__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.t,P.t__tilde__):'((-11*ee**2*MT**2 - ee**2*MZ**2 - (3*cw**2*ee**2*MT**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MT**2*sw**2)/(6.*cw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MT**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((-5*ee**2*MTA**2 - ee**2*MZ**2 - (cw**2*ee**2*MTA**2)/(2.*sw**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MTA**2*sw**2)/(2.*cw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2))*cmath.sqrt(-4*MTA**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.u,P.u__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ve,P.ve__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vm,P.vm__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vt,P.vt__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.W__minus__,P.W__plus__):'(((-12*cw**2*ee**2*MW**2)/sw**2 - (17*cw**2*ee**2*MZ**2)/sw**2 + (4*cw**2*ee**2*MZ**4)/(MW**2*sw**2) + (cw**2*ee**2*MZ**6)/(4.*MW**4*sw**2))*cmath.sqrt(-4*MW**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)'})

