# compositeNJL

This repository is meant to collect the FeynRules and CalcHEP/UFO models for the model implemented in EPJC (220)80:309 by R. Leonardi et Al.

''HN_FeynRules_model'' contains the implementation of a dim-6 contact interaction in FeynRules for both CalcHEP and Madgraph (https://arxiv.org/pdf/1811.00374.pdf) to be used as a guideline for this new model with NJL interactions.

 "Old version of model" contains initial implementation of the model, further updates are mentioned below.
 
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

# January 2022 version
Folder= Old version of the model
Files name (SM.fr, SheSheng.fr, SheSheng_UFO, NJL-LQ-CI.nb, Massless.rst, Cabibbo.rst)
Model contains 
1) Contact interaction (so now auxiliary propagator is not needed)
2) Leptoquark interactions (with first generation)
3) Gauge interactions with composite bosons (charged and neutral)
In order to run the UFO files you just need to import the model in the Madgraph and you are good to go.. 



# Feb2022 update 
Folder= NJL-Model_version_3.1
New update contains the g g -> LQ LQ interactions, where LQ are the composite bosons Leptoquarks. 
Import the UFO files in Madgraph you are all set to go.. 


# April2022 update
Folder= NJL-Model_version_3.2
This version contains the following updates
1) All the Gauge interactions of the composite bosons and composite bosons LQ and the interactions are implemented via Kinetic terms.
2) Leptoquark interactions with all the generations, also we took care of the fact that LQ decay into one channel only, so that we can have BR=1.  
Import the UFO files in Madgraph you are all set to go.. 

# July2022 update
Folder= NJL-Model_version_3.3
In this update we implemented the mass of the b quark equals to zero because we are using PDF sets which have 5F scheme so to be coherent with that it is needed. 
Import the UFO files in Madgraph you are all set to go.. 

# For further information visit https://www.overleaf.com/project/6225f42f7d8f6ce5abbe33ab

