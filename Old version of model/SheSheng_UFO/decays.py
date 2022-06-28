# This file was automatically created by FeynRules 2.3.48
# Mathematica version: 12.3.1 for Mac OS X ARM (64-bit) (July 8, 2021)
# Date: Tue 11 Jan 2022 11:16:58


from object_library import all_decays, Decay
import particles as P


Decay_b = Decay(name = 'Decay_b',
                particle = P.b,
                partial_widths = {(P.W__minus__,P.t):'(((3*ee**2*MB**2)/(2.*sw**2) + (3*ee**2*MT**2)/(2.*sw**2) + (3*ee**2*MB**4)/(2.*MW**2*sw**2) - (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) + (3*ee**2*MT**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MB)**3)'})

Decay_E0 = Decay(name = 'Decay_E0',
                 particle = P.E0,
                 partial_widths = {(P.Pic1__plus__,P.e__minus__):'((-MPi**2 + MUU**2)*(-((FPi**4*MPi**2)/lc**4) + (FPi**4*MUU**2)/lc**4))/(32.*cmath.pi*abs(MUU)**3)'})

Decay_Ec = Decay(name = 'Decay_Ec',
                 particle = P.Ec,
                 partial_widths = {(P.Pi0d,P.e__minus__):'((-MPi**2 + MUU**2)*(-((FPi**4*MPi**2)/lc**4) + (FPi**4*MUU**2)/lc**4))/(32.*cmath.pi*abs(MUU)**3)'})

Decay_H = Decay(name = 'Decay_H',
                particle = P.H,
                partial_widths = {(P.b,P.b__tilde__):'((-12*MB**2*yb**2 + 3*MH**2*yb**2)*cmath.sqrt(-4*MB**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.t,P.t__tilde__):'((3*MH**2*yt**2 - 12*MT**2*yt**2)*cmath.sqrt(MH**4 - 4*MH**2*MT**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((MH**2*ytau**2 - 4*MTA**2*ytau**2)*cmath.sqrt(MH**4 - 4*MH**2*MTA**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.W__minus__,P.W__plus__):'(((3*ee**4*vev**2)/(4.*sw**4) + (ee**4*MH**4*vev**2)/(16.*MW**4*sw**4) - (ee**4*MH**2*vev**2)/(4.*MW**2*sw**4))*cmath.sqrt(MH**4 - 4*MH**2*MW**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.Z,P.Z):'(((9*ee**4*vev**2)/2. + (3*ee**4*MH**4*vev**2)/(8.*MZ**4) - (3*ee**4*MH**2*vev**2)/(2.*MZ**2) + (3*cw**4*ee**4*vev**2)/(4.*sw**4) + (cw**4*ee**4*MH**4*vev**2)/(16.*MZ**4*sw**4) - (cw**4*ee**4*MH**2*vev**2)/(4.*MZ**2*sw**4) + (3*cw**2*ee**4*vev**2)/sw**2 + (cw**2*ee**4*MH**4*vev**2)/(4.*MZ**4*sw**2) - (cw**2*ee**4*MH**2*vev**2)/(MZ**2*sw**2) + (3*ee**4*sw**2*vev**2)/cw**2 + (ee**4*MH**4*sw**2*vev**2)/(4.*cw**2*MZ**4) - (ee**4*MH**2*sw**2*vev**2)/(cw**2*MZ**2) + (3*ee**4*sw**4*vev**2)/(4.*cw**4) + (ee**4*MH**4*sw**4*vev**2)/(16.*cw**4*MZ**4) - (ee**4*MH**2*sw**4*vev**2)/(4.*cw**4*MZ**2))*cmath.sqrt(MH**4 - 4*MH**2*MZ**2))/(32.*cmath.pi*abs(MH)**3)'})

Decay_mu__minus__ = Decay(name = 'Decay_mu__minus__',
                          particle = P.mu__minus__,
                          partial_widths = {(P.W__minus__,P.vm):'((MM**2 - MW**2)*((ee**2*MM**2)/(2.*sw**2) + (ee**2*MM**4)/(2.*MW**2*sw**2) - (ee**2*MW**2)/sw**2))/(32.*cmath.pi*abs(MM)**3)'})

Decay_N01 = Decay(name = 'Decay_N01',
                  particle = P.N01,
                  partial_widths = {(P.Pi0u,P.ve):'((-MPi**2 + MUU**2)*(-((FPi**4*MPi**2)/lc**4) + (FPi**4*MUU**2)/lc**4))/(32.*cmath.pi*abs(MUU)**3)'})

Decay_Nc1 = Decay(name = 'Decay_Nc1',
                  particle = P.Nc1,
                  partial_widths = {(P.Pic1__tilde__,P.ve):'((-MPi**2 + MUU**2)*(-((FPi**4*MPi**2)/lc**4) + (FPi**4*MUU**2)/lc**4))/(32.*cmath.pi*abs(MUU)**3)'})

Decay_Pi0d = Decay(name = 'Decay_Pi0d',
                   particle = P.Pi0d,
                   partial_widths = {(P.a,P.a):'(aEW**2*MPi**6)/(576.*FPi**2*cmath.pi**3*abs(MPi)**3)',
                                     (P.a,P.Z):'((MPi**2 - MZ**2)*(-0.010416666666666666*(aEW**2*MPi**4)/(cw**2*FPi**2*cmath.pi**2) + (aEW**2*MPi**2*MZ**2)/(48.*cw**2*FPi**2*cmath.pi**2) - (aEW**2*MZ**4)/(96.*cw**2*FPi**2*cmath.pi**2) + (aEW**2*MPi**4)/(128.*cw**2*FPi**2*cmath.pi**2*sw**2) - (aEW**2*MPi**2*MZ**2)/(64.*cw**2*FPi**2*cmath.pi**2*sw**2) + (aEW**2*MZ**4)/(128.*cw**2*FPi**2*cmath.pi**2*sw**2) + (aEW**2*MPi**4*sw**2)/(288.*cw**2*FPi**2*cmath.pi**2) - (aEW**2*MPi**2*MZ**2*sw**2)/(144.*cw**2*FPi**2*cmath.pi**2) + (aEW**2*MZ**4*sw**2)/(288.*cw**2*FPi**2*cmath.pi**2)))/(16.*cmath.pi*abs(MPi)**3)',
                                     (P.d,P.d__tilde__):'(3*FPi**4*MPi**4)/(8.*cmath.pi*lc**4*abs(MPi)**3)',
                                     (P.e__minus__,P.Ec__tilde__):'((MPi**2 - MUU**2)*((FPi**4*MPi**2)/lc**4 - (FPi**4*MUU**2)/lc**4))/(16.*cmath.pi*abs(MPi)**3)',
                                     (P.Ec,P.e__plus__):'((MPi**2 - MUU**2)*((FPi**4*MPi**2)/lc**4 - (FPi**4*MUU**2)/lc**4))/(16.*cmath.pi*abs(MPi)**3)',
                                     (P.W__minus__,P.W__plus__):'(((9*aEW**2*MPi**4)/(512.*FPi**2*cmath.pi**2*sw**4) - (9*aEW**2*MPi**2*MW**2)/(128.*FPi**2*cmath.pi**2*sw**4))*cmath.sqrt(MPi**4 - 4*MPi**2*MW**2))/(16.*cmath.pi*abs(MPi)**3)',
                                     (P.Z,P.Z):'(((aEW**2*MPi**4)/(32.*cw**4*FPi**2*cmath.pi**2) - (aEW**2*MPi**2*MZ**2)/(8.*cw**4*FPi**2*cmath.pi**2) + (9*aEW**2*MPi**4)/(128.*cw**4*FPi**2*cmath.pi**2*sw**4) - (9*aEW**2*MPi**2*MZ**2)/(32.*cw**4*FPi**2*cmath.pi**2*sw**4) - (3*aEW**2*MPi**4)/(32.*cw**4*FPi**2*cmath.pi**2*sw**2) + (3*aEW**2*MPi**2*MZ**2)/(8.*cw**4*FPi**2*cmath.pi**2*sw**2))*cmath.sqrt(MPi**4 - 4*MPi**2*MZ**2))/(32.*cmath.pi*abs(MPi)**3)'})

Decay_Pi0u = Decay(name = 'Decay_Pi0u',
                   particle = P.Pi0u,
                   partial_widths = {(P.a,P.a):'(aEW**2*MPi**6)/(36.*FPi**2*cmath.pi**3*abs(MPi)**3)',
                                     (P.a,P.Z):'((MPi**2 - MZ**2)*(-0.08333333333333333*(aEW**2*MPi**4)/(cw**2*FPi**2*cmath.pi**2) + (aEW**2*MPi**2*MZ**2)/(6.*cw**2*FPi**2*cmath.pi**2) - (aEW**2*MZ**4)/(12.*cw**2*FPi**2*cmath.pi**2) + (aEW**2*MPi**4)/(32.*cw**2*FPi**2*cmath.pi**2*sw**2) - (aEW**2*MPi**2*MZ**2)/(16.*cw**2*FPi**2*cmath.pi**2*sw**2) + (aEW**2*MZ**4)/(32.*cw**2*FPi**2*cmath.pi**2*sw**2) + (aEW**2*MPi**4*sw**2)/(18.*cw**2*FPi**2*cmath.pi**2) - (aEW**2*MPi**2*MZ**2*sw**2)/(9.*cw**2*FPi**2*cmath.pi**2) + (aEW**2*MZ**4*sw**2)/(18.*cw**2*FPi**2*cmath.pi**2)))/(16.*cmath.pi*abs(MPi)**3)',
                                     (P.N01,P.ve__tilde__):'((MPi**2 - MUU**2)*((FPi**4*MPi**2)/lc**4 - (FPi**4*MUU**2)/lc**4))/(16.*cmath.pi*abs(MPi)**3)',
                                     (P.u,P.u__tilde__):'(3*FPi**4*MPi**4)/(8.*cmath.pi*lc**4*abs(MPi)**3)',
                                     (P.ve,P.N01__tilde__):'((MPi**2 - MUU**2)*((FPi**4*MPi**2)/lc**4 - (FPi**4*MUU**2)/lc**4))/(16.*cmath.pi*abs(MPi)**3)',
                                     (P.W__minus__,P.W__plus__):'(((9*aEW**2*MPi**4)/(512.*FPi**2*cmath.pi**2*sw**4) - (9*aEW**2*MPi**2*MW**2)/(128.*FPi**2*cmath.pi**2*sw**4))*cmath.sqrt(MPi**4 - 4*MPi**2*MW**2))/(16.*cmath.pi*abs(MPi)**3)',
                                     (P.Z,P.Z):'(((aEW**2*MPi**4)/(8.*cw**4*FPi**2*cmath.pi**2) - (aEW**2*MPi**2*MZ**2)/(2.*cw**4*FPi**2*cmath.pi**2) + (9*aEW**2*MPi**4)/(128.*cw**4*FPi**2*cmath.pi**2*sw**4) - (9*aEW**2*MPi**2*MZ**2)/(32.*cw**4*FPi**2*cmath.pi**2*sw**4) - (3*aEW**2*MPi**4)/(16.*cw**4*FPi**2*cmath.pi**2*sw**2) + (3*aEW**2*MPi**2*MZ**2)/(4.*cw**4*FPi**2*cmath.pi**2*sw**2))*cmath.sqrt(MPi**4 - 4*MPi**2*MZ**2))/(32.*cmath.pi*abs(MPi)**3)'})

Decay_Pi13 = Decay(name = 'Decay_Pi13',
                   particle = P.Pi13,
                   partial_widths = {(P.d,P.ve__tilde__):'(FPi**4*MPi**4)/(16.*cmath.pi*lc**4*abs(MPi)**3)'})

Decay_Pi53 = Decay(name = 'Decay_Pi53',
                   particle = P.Pi53,
                   partial_widths = {(P.u,P.e__plus__):'(FPi**4*MPi**4)/(16.*cmath.pi*lc**4*abs(MPi)**3)'})

Decay_Pic1__plus__ = Decay(name = 'Decay_Pic1__plus__',
                           particle = P.Pic1__plus__,
                           partial_widths = {(P.a,P.W__plus__):'((MPi**2 - MW**2)*((9*aEW**2*MPi**4)/(16.*FPi**2*cmath.pi**2*sw**2) - (9*aEW**2*MPi**2*MW**2)/(8.*FPi**2*cmath.pi**2*sw**2) + (9*aEW**2*MW**4)/(16.*FPi**2*cmath.pi**2*sw**2)))/(16.*cmath.pi*abs(MPi)**3)',
                                             (P.E0,P.e__plus__):'((MPi**2 - MUU**2)*((FPi**4*MPi**2)/lc**4 - (FPi**4*MUU**2)/lc**4))/(16.*cmath.pi*abs(MPi)**3)',
                                             (P.u,P.d__tilde__):'(3*FPi**4*MPi**4)/(16.*cmath.pi*lc**4*abs(MPi)**3)',
                                             (P.ve,P.Nc1__tilde__):'((MPi**2 - MUU**2)*((FPi**4*MPi**2)/lc**4 - (FPi**4*MUU**2)/lc**4))/(16.*cmath.pi*abs(MPi)**3)',
                                             (P.W__plus__,P.Z):'(((25*aEW**2*MPi**4)/(576.*FPi**2*cmath.pi**2) - (25*aEW**2*MPi**2*MW**2)/(288.*FPi**2*cmath.pi**2) + (25*aEW**2*MW**4)/(576.*FPi**2*cmath.pi**2) - (25*aEW**2*MPi**2*MZ**2)/(288.*FPi**2*cmath.pi**2) - (25*aEW**2*MW**2*MZ**2)/(288.*FPi**2*cmath.pi**2) + (25*aEW**2*MZ**4)/(576.*FPi**2*cmath.pi**2) + (aEW**2*MPi**4)/(256.*FPi**2*cmath.pi**2*sw**4) - (aEW**2*MPi**2*MW**2)/(128.*FPi**2*cmath.pi**2*sw**4) + (aEW**2*MW**4)/(256.*FPi**2*cmath.pi**2*sw**4) - (aEW**2*MPi**2*MZ**2)/(128.*FPi**2*cmath.pi**2*sw**4) - (aEW**2*MW**2*MZ**2)/(128.*FPi**2*cmath.pi**2*sw**4) + (aEW**2*MZ**4)/(256.*FPi**2*cmath.pi**2*sw**4) - (5*aEW**2*MPi**4)/(192.*FPi**2*cmath.pi**2*sw**2) + (5*aEW**2*MPi**2*MW**2)/(96.*FPi**2*cmath.pi**2*sw**2) - (5*aEW**2*MW**4)/(192.*FPi**2*cmath.pi**2*sw**2) + (5*aEW**2*MPi**2*MZ**2)/(96.*FPi**2*cmath.pi**2*sw**2) + (5*aEW**2*MW**2*MZ**2)/(96.*FPi**2*cmath.pi**2*sw**2) - (5*aEW**2*MZ**4)/(192.*FPi**2*cmath.pi**2*sw**2))*cmath.sqrt(MPi**4 - 2*MPi**2*MW**2 + MW**4 - 2*MPi**2*MZ**2 - 2*MW**2*MZ**2 + MZ**4))/(16.*cmath.pi*abs(MPi)**3)'})

Decay_Pid23 = Decay(name = 'Decay_Pid23',
                    particle = P.Pid23,
                    partial_widths = {(P.d,P.e__plus__):'(FPi**4*MPi**4)/(16.*cmath.pi*lc**4*abs(MPi)**3)'})

Decay_Piu23 = Decay(name = 'Decay_Piu23',
                    particle = P.Piu23,
                    partial_widths = {(P.u,P.ve__tilde__):'(FPi**4*MPi**4)/(16.*cmath.pi*lc**4*abs(MPi)**3)'})

Decay_t = Decay(name = 'Decay_t',
                particle = P.t,
                partial_widths = {(P.W__plus__,P.b):'(((3*ee**2*MB**2)/(2.*sw**2) + (3*ee**2*MT**2)/(2.*sw**2) + (3*ee**2*MB**4)/(2.*MW**2*sw**2) - (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) + (3*ee**2*MT**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MT)**3)'})

Decay_ta__minus__ = Decay(name = 'Decay_ta__minus__',
                          particle = P.ta__minus__,
                          partial_widths = {(P.W__minus__,P.vt):'((MTA**2 - MW**2)*((ee**2*MTA**2)/(2.*sw**2) + (ee**2*MTA**4)/(2.*MW**2*sw**2) - (ee**2*MW**2)/sw**2))/(32.*cmath.pi*abs(MTA)**3)'})

Decay_W__plus__ = Decay(name = 'Decay_W__plus__',
                        particle = P.W__plus__,
                        partial_widths = {(P.a,P.Pic1__plus__):'((-MPi**2 + MW**2)*((9*aEW**2*MPi**4)/(16.*FPi**2*cmath.pi**2*sw**2) - (9*aEW**2*MPi**2*MW**2)/(8.*FPi**2*cmath.pi**2*sw**2) + (9*aEW**2*MW**4)/(16.*FPi**2*cmath.pi**2*sw**2)))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.c,P.d__tilde__):'(CKM2x1*ee**2*MW**4*complexconjugate(CKM2x1))/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.c,P.s__tilde__):'(CKM2x2*ee**2*MW**4*complexconjugate(CKM2x2))/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.Pic1__plus__,P.Z):'(((25*aEW**2*MPi**4)/(576.*FPi**2*cmath.pi**2) - (25*aEW**2*MPi**2*MW**2)/(288.*FPi**2*cmath.pi**2) + (25*aEW**2*MW**4)/(576.*FPi**2*cmath.pi**2) - (25*aEW**2*MPi**2*MZ**2)/(288.*FPi**2*cmath.pi**2) - (25*aEW**2*MW**2*MZ**2)/(288.*FPi**2*cmath.pi**2) + (25*aEW**2*MZ**4)/(576.*FPi**2*cmath.pi**2) + (aEW**2*MPi**4)/(256.*FPi**2*cmath.pi**2*sw**4) - (aEW**2*MPi**2*MW**2)/(128.*FPi**2*cmath.pi**2*sw**4) + (aEW**2*MW**4)/(256.*FPi**2*cmath.pi**2*sw**4) - (aEW**2*MPi**2*MZ**2)/(128.*FPi**2*cmath.pi**2*sw**4) - (aEW**2*MW**2*MZ**2)/(128.*FPi**2*cmath.pi**2*sw**4) + (aEW**2*MZ**4)/(256.*FPi**2*cmath.pi**2*sw**4) - (5*aEW**2*MPi**4)/(192.*FPi**2*cmath.pi**2*sw**2) + (5*aEW**2*MPi**2*MW**2)/(96.*FPi**2*cmath.pi**2*sw**2) - (5*aEW**2*MW**4)/(192.*FPi**2*cmath.pi**2*sw**2) + (5*aEW**2*MPi**2*MZ**2)/(96.*FPi**2*cmath.pi**2*sw**2) + (5*aEW**2*MW**2*MZ**2)/(96.*FPi**2*cmath.pi**2*sw**2) - (5*aEW**2*MZ**4)/(192.*FPi**2*cmath.pi**2*sw**2))*cmath.sqrt(MPi**4 - 2*MPi**2*MW**2 + MW**4 - 2*MPi**2*MZ**2 - 2*MW**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.t,P.b__tilde__):'(((-3*ee**2*MB**2)/(2.*sw**2) - (3*ee**2*MT**2)/(2.*sw**2) - (3*ee**2*MB**4)/(2.*MW**2*sw**2) + (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) - (3*ee**2*MT**4)/(2.*MW**2*sw**2) + (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.u,P.d__tilde__):'(CKM1x1*ee**2*MW**4*complexconjugate(CKM1x1))/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.u,P.s__tilde__):'(CKM1x2*ee**2*MW**4*complexconjugate(CKM1x2))/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.ve,P.e__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.vm,P.mu__plus__):'((-MM**2 + MW**2)*(-0.5*(ee**2*MM**2)/sw**2 - (ee**2*MM**4)/(2.*MW**2*sw**2) + (ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.vt,P.ta__plus__):'((-MTA**2 + MW**2)*(-0.5*(ee**2*MTA**2)/sw**2 - (ee**2*MTA**4)/(2.*MW**2*sw**2) + (ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)'})

Decay_Z = Decay(name = 'Decay_Z',
                particle = P.Z,
                partial_widths = {(P.a,P.Pi0d):'((-MPi**2 + MZ**2)*(-0.010416666666666666*(aEW**2*MPi**4)/(cw**2*FPi**2*cmath.pi**2) + (aEW**2*MPi**2*MZ**2)/(48.*cw**2*FPi**2*cmath.pi**2) - (aEW**2*MZ**4)/(96.*cw**2*FPi**2*cmath.pi**2) + (aEW**2*MPi**4)/(128.*cw**2*FPi**2*cmath.pi**2*sw**2) - (aEW**2*MPi**2*MZ**2)/(64.*cw**2*FPi**2*cmath.pi**2*sw**2) + (aEW**2*MZ**4)/(128.*cw**2*FPi**2*cmath.pi**2*sw**2) + (aEW**2*MPi**4*sw**2)/(288.*cw**2*FPi**2*cmath.pi**2) - (aEW**2*MPi**2*MZ**2*sw**2)/(144.*cw**2*FPi**2*cmath.pi**2) + (aEW**2*MZ**4*sw**2)/(288.*cw**2*FPi**2*cmath.pi**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.a,P.Pi0u):'((-MPi**2 + MZ**2)*(-0.08333333333333333*(aEW**2*MPi**4)/(cw**2*FPi**2*cmath.pi**2) + (aEW**2*MPi**2*MZ**2)/(6.*cw**2*FPi**2*cmath.pi**2) - (aEW**2*MZ**4)/(12.*cw**2*FPi**2*cmath.pi**2) + (aEW**2*MPi**4)/(32.*cw**2*FPi**2*cmath.pi**2*sw**2) - (aEW**2*MPi**2*MZ**2)/(16.*cw**2*FPi**2*cmath.pi**2*sw**2) + (aEW**2*MZ**4)/(32.*cw**2*FPi**2*cmath.pi**2*sw**2) + (aEW**2*MPi**4*sw**2)/(18.*cw**2*FPi**2*cmath.pi**2) - (aEW**2*MPi**2*MZ**2*sw**2)/(9.*cw**2*FPi**2*cmath.pi**2) + (aEW**2*MZ**4*sw**2)/(18.*cw**2*FPi**2*cmath.pi**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.b,P.b__tilde__):'((-7*ee**2*MB**2 + ee**2*MZ**2 - (3*cw**2*ee**2*MB**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) - (17*ee**2*MB**2*sw**2)/(6.*cw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MB**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.c,P.c__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.d,P.d__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.e__minus__,P.e__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.mu__minus__,P.mu__plus__):'((-5*ee**2*MM**2 - ee**2*MZ**2 - (cw**2*ee**2*MM**2)/(2.*sw**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MM**2*sw**2)/(2.*cw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2))*cmath.sqrt(-4*MM**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.Pic1__plus__,P.W__minus__):'(((25*aEW**2*MPi**4)/(576.*FPi**2*cmath.pi**2) - (25*aEW**2*MPi**2*MW**2)/(288.*FPi**2*cmath.pi**2) + (25*aEW**2*MW**4)/(576.*FPi**2*cmath.pi**2) - (25*aEW**2*MPi**2*MZ**2)/(288.*FPi**2*cmath.pi**2) - (25*aEW**2*MW**2*MZ**2)/(288.*FPi**2*cmath.pi**2) + (25*aEW**2*MZ**4)/(576.*FPi**2*cmath.pi**2) + (aEW**2*MPi**4)/(256.*FPi**2*cmath.pi**2*sw**4) - (aEW**2*MPi**2*MW**2)/(128.*FPi**2*cmath.pi**2*sw**4) + (aEW**2*MW**4)/(256.*FPi**2*cmath.pi**2*sw**4) - (aEW**2*MPi**2*MZ**2)/(128.*FPi**2*cmath.pi**2*sw**4) - (aEW**2*MW**2*MZ**2)/(128.*FPi**2*cmath.pi**2*sw**4) + (aEW**2*MZ**4)/(256.*FPi**2*cmath.pi**2*sw**4) - (5*aEW**2*MPi**4)/(192.*FPi**2*cmath.pi**2*sw**2) + (5*aEW**2*MPi**2*MW**2)/(96.*FPi**2*cmath.pi**2*sw**2) - (5*aEW**2*MW**4)/(192.*FPi**2*cmath.pi**2*sw**2) + (5*aEW**2*MPi**2*MZ**2)/(96.*FPi**2*cmath.pi**2*sw**2) + (5*aEW**2*MW**2*MZ**2)/(96.*FPi**2*cmath.pi**2*sw**2) - (5*aEW**2*MZ**4)/(192.*FPi**2*cmath.pi**2*sw**2))*cmath.sqrt(MPi**4 - 2*MPi**2*MW**2 + MW**4 - 2*MPi**2*MZ**2 - 2*MW**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.Pic1__tilde__,P.W__plus__):'(((25*aEW**2*MPi**4)/(576.*FPi**2*cmath.pi**2) - (25*aEW**2*MPi**2*MW**2)/(288.*FPi**2*cmath.pi**2) + (25*aEW**2*MW**4)/(576.*FPi**2*cmath.pi**2) - (25*aEW**2*MPi**2*MZ**2)/(288.*FPi**2*cmath.pi**2) - (25*aEW**2*MW**2*MZ**2)/(288.*FPi**2*cmath.pi**2) + (25*aEW**2*MZ**4)/(576.*FPi**2*cmath.pi**2) + (aEW**2*MPi**4)/(256.*FPi**2*cmath.pi**2*sw**4) - (aEW**2*MPi**2*MW**2)/(128.*FPi**2*cmath.pi**2*sw**4) + (aEW**2*MW**4)/(256.*FPi**2*cmath.pi**2*sw**4) - (aEW**2*MPi**2*MZ**2)/(128.*FPi**2*cmath.pi**2*sw**4) - (aEW**2*MW**2*MZ**2)/(128.*FPi**2*cmath.pi**2*sw**4) + (aEW**2*MZ**4)/(256.*FPi**2*cmath.pi**2*sw**4) - (5*aEW**2*MPi**4)/(192.*FPi**2*cmath.pi**2*sw**2) + (5*aEW**2*MPi**2*MW**2)/(96.*FPi**2*cmath.pi**2*sw**2) - (5*aEW**2*MW**4)/(192.*FPi**2*cmath.pi**2*sw**2) + (5*aEW**2*MPi**2*MZ**2)/(96.*FPi**2*cmath.pi**2*sw**2) + (5*aEW**2*MW**2*MZ**2)/(96.*FPi**2*cmath.pi**2*sw**2) - (5*aEW**2*MZ**4)/(192.*FPi**2*cmath.pi**2*sw**2))*cmath.sqrt(MPi**4 - 2*MPi**2*MW**2 + MW**4 - 2*MPi**2*MZ**2 - 2*MW**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.s,P.s__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.t,P.t__tilde__):'((-11*ee**2*MT**2 - ee**2*MZ**2 - (3*cw**2*ee**2*MT**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MT**2*sw**2)/(6.*cw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MT**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((-5*ee**2*MTA**2 - ee**2*MZ**2 - (cw**2*ee**2*MTA**2)/(2.*sw**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MTA**2*sw**2)/(2.*cw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2))*cmath.sqrt(-4*MTA**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.u,P.u__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ve,P.ve__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vm,P.vm__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vt,P.vt__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.W__minus__,P.W__plus__):'(((-12*cw**2*ee**2*MW**2)/sw**2 - (17*cw**2*ee**2*MZ**2)/sw**2 + (4*cw**2*ee**2*MZ**4)/(MW**2*sw**2) + (cw**2*ee**2*MZ**6)/(4.*MW**4*sw**2))*cmath.sqrt(-4*MW**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)'})

