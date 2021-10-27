# compositeNJL

This repository is meant to collect the FeynRules and CalcHEP/UFO models for the model implemented in EPJC (220)80:309 by R. Leonardi et Al.

''HN_FeynRules_model'' contains the implementation of a dim-6 contact interaction in FeynRules for both CalcHEP and Madgraph (https://arxiv.org/pdf/1811.00374.pdf) to be used as a guideline for this new model with NJL interactions.

# Changes to be made in the UFO files after creating UFO from feynrules
1) After evaluating the notebook you will get UFO files but to implement these files into Madgraph you need to change somethings otherwise you will get below mentioned errors.
2) To resolve the error regarding External parameters you need to comment the lines 164-186 in parameters.py file.
3) To resolve the error regarding couplings you need to edit the coupling in couplings.py
from
GC_13 = Coupling(name = 'GC_13',
                 value = '(FPi**2*complex(0,1))/lc**2',
                 order = {'1':1})
to GC_13 = Coupling(name = 'GC_13',
value = '(FPi**2*complex(0,1))/lc**2',
order = {'NP':1})

4) Next thing is to add the auxiliary propagators for contact interactions. add the following lines to propagators.py file
#AUX
# AUX
S0 = Propagator(name = "S0",
                numerator = "complex(0,1)",
                denominator =  "Mass(id) * Mass(id)"
               )

               
5)  Lastly, you need to add this propagator to all the auxiliary particles present in the particles.py file.
add it like this 
AL01__plus__ = Particle(pdg_code = 9000006,
                        name = 'AL01+',
                        antiname = 'AL01~',
                        spin = 1,
                        color = 1,
                        mass = Param.lc,
                        width = Param.ZERO,
                        propagator = Prop.S0,
                        texname = 'AL01+',
                        antitexname = 'AL01~',
                        charge = 1,
                        GhostNumber = 0,
                        LeptonNumber = 0,
                        Y = 0)
6) Lastly, implement the UFO files in Madgraph.
