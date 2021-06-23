#!/usr/bin/env python
# encoding: utf-8

name = "seed"
shortDesc = ""
longDesc = """

"""
autoGenerated=True
entry(
    index = 0,
    label = "X + NH3 <=> NH3X",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.79731, n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Rebrov_Pt111
""",
)

entry(
    index = 1,
    label = "X + X + O2 <=> OX + OX",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.023519, n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Rebrov_Pt111
""",
)

entry(
    index = 2,
    label = "OX + NH3X <=> OHX + NH2_X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.85e+23,'cm^2/(mol*s)'), n=0, Ea=(157000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Rebrov_Pt111
""",
)

entry(
    index = 3,
    label = "OX + NH2_X <=> OHX + NH_X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.03e+21,'cm^2/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Rebrov_Pt111
""",
)

entry(
    index = 4,
    label = "OX + NH_X <=> NX + OHX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.03e+21,'cm^2/(mol*s)'), n=0, Ea=(58500,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Rebrov_Pt111
""",
)

entry(
    index = 5,
    label = "OX + NX <=> X + NOX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(8.46e+21,'cm^2/(mol*s)'), n=0, Ea=(131000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Rebrov_Pt111
""",
)

entry(
    index = 6,
    label = "OX + NH_X <=> X + NHO_X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.03e+21,'cm^2/(mol*s)'), n=0, Ea=(73000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Rebrov_Pt111
""",
)

entry(
    index = 7,
    label = "OX + NHO_X <=> NOX + OHX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(8.05e+23,'cm^2/(mol*s)'), n=0, Ea=(118000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Rebrov_Pt111
""",
)

entry(
    index = 8,
    label = "NX + NX <=> X + X + N2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(3.22e+21,'cm^2/(mol*s)'), n=0, Ea=(124000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Rebrov_Pt111
""",
)

entry(
    index = 9,
    label = "NX + NOX <=> X + X + N2O",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.01e+19,'cm^2/(mol*s)'), n=0, Ea=(98900,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Rebrov_Pt111
""",
)

entry(
    index = 10,
    label = "X + N2O <=> OX + N2",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.016034, n=0, Ea=(72200,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Rebrov_Pt111
""",
)

entry(
    index = 11,
    label = "NOX <=> X + NO",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.5e+13,'1/s'), n=0, Ea=(143000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Rebrov_Pt111
""",
)

entry(
    index = 12,
    label = "OHX + NH_X <=> NX + H2O_X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.03e+21,'cm^2/(mol*s)'), n=0, Ea=(46000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Rebrov_Pt111
""",
)

entry(
    index = 13,
    label = "OHX + OHX <=> X + OX + H2O",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.03e+21,'cm^2/(mol*s)'), n=0, Ea=(113000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Rebrov_Pt111
""",
)

entry(
    index = 14,
    label = "OX + H2O_X <=> OHX + OHX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.03e+19,'cm^2/(mol*s)'), n=0, Ea=(52700,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Rebrov_Pt111
""",
)

entry(
    index = 15,
    label = "H2O_X <=> X + H2O",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1e+13,'1/s'), n=0, Ea=(40300,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Rebrov_Pt111
""",
)

entry(
    index = 16,
    label = "NH_X + NH3X <=> NH2_X + NH2_X",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(4.94901e+15,'m^2/(mol*s)'), n=0.652756, Ea=(120.135,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template [AdsorbateVdW;Adsorbate1] for rate rule [N-R;*=NH]
    Euclidian distance = 3.1622776601683795
    Multiplied by reaction path degeneracy 3.0
    family: Surface_Abstraction_vdW"""),
    longDesc = 
"""
Estimated using template [AdsorbateVdW;Adsorbate1] for rate rule [N-R;*=NH]
Euclidian distance = 3.1622776601683795
Multiplied by reaction path degeneracy 3.0
family: Surface_Abstraction_vdW
""",
)

entry(
    index = 17,
    label = "NX + NH3X <=> NH_X + NH2_X",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(4.94901e+15,'m^2/(mol*s)'), n=0.652756, Ea=(120.135,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template [AdsorbateVdW;Adsorbate1] for rate rule [N-R;*#N]
    Euclidian distance = 2.23606797749979
    Multiplied by reaction path degeneracy 3.0
    family: Surface_Abstraction_vdW"""),
    longDesc = 
"""
Estimated using template [AdsorbateVdW;Adsorbate1] for rate rule [N-R;*#N]
Euclidian distance = 2.23606797749979
Multiplied by reaction path degeneracy 3.0
family: Surface_Abstraction_vdW
""",
)

entry(
    index = 18,
    label = "NHO_X + NH2_X <=> NOX + NH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1e+13,'m^2/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K'), comment="""Estimated using template [Donating;Abstracting] for rate rule [N-H;*NH2]
    Euclidian distance = 3.605551275463989
    family: Surface_Abstraction_Single_vdW
    Ea raised from -62.0 to 0.0 kJ/mol."""),
    longDesc = 
"""
Estimated using template [Donating;Abstracting] for rate rule [N-H;*NH2]
Euclidian distance = 3.605551275463989
family: Surface_Abstraction_Single_vdW
Ea raised from -62.0 to 0.0 kJ/mol.
""",
)

entry(
    index = 19,
    label = "OHX + NH3X <=> H2O_X + NH2_X",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(3e+13,'m^2/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K'), comment="""Estimated using template [Donating;Abstracting] for rate rule [NH3;*O-H]
    Euclidian distance = 3.605551275463989
    Multiplied by reaction path degeneracy 3.0
    family: Surface_Abstraction_Single_vdW
    Ea raised from -16.0 to 0.0 kJ/mol."""),
    longDesc = 
"""
Estimated using template [Donating;Abstracting] for rate rule [NH3;*O-H]
Euclidian distance = 3.605551275463989
Multiplied by reaction path degeneracy 3.0
family: Surface_Abstraction_Single_vdW
Ea raised from -16.0 to 0.0 kJ/mol.
""",
)

entry(
    index = 20,
    label = "NX + NH2_X <=> NH_X + NH_X",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(8.35926e+17,'m^2/(mol*s)'), n=-0.0183333, Ea=(30.05,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template [Abstracting;*R-H] for rate rule [:N#*;*-N-H]
    Euclidian distance = 3.605551275463989
    Multiplied by reaction path degeneracy 2.0
    family: Surface_Abstraction"""),
    longDesc = 
"""
Estimated using template [Abstracting;*R-H] for rate rule [:N#*;*-N-H]
Euclidian distance = 3.605551275463989
Multiplied by reaction path degeneracy 2.0
family: Surface_Abstraction
""",
)

entry(
    index = 21,
    label = "NH_X + NHO_X <=> NOX + NH2_X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.64967e+15,'m^2/(mol*s)'), n=0.652756, Ea=(120.135,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template [AdsorbateVdW;Adsorbate1] for rate rule [N-R;*=NH]
    Euclidian distance = 3.1622776601683795
    family: Surface_Abstraction_vdW"""),
    longDesc = 
"""
Estimated using template [AdsorbateVdW;Adsorbate1] for rate rule [N-R;*=NH]
Euclidian distance = 3.1622776601683795
family: Surface_Abstraction_vdW
""",
)

entry(
    index = 22,
    label = "NH_X + H2O_X <=> OHX + NH2_X",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(4.17313e+12,'m^2/(mol*s)'), n=1.13551, Ea=(145.878,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template [O-R;Adsorbate1] for rate rule [O-R;*=NH]
    Euclidian distance = 3.0
    Multiplied by reaction path degeneracy 2.0
    family: Surface_Abstraction_vdW"""),
    longDesc = 
"""
Estimated using template [O-R;Adsorbate1] for rate rule [O-R;*=NH]
Euclidian distance = 3.0
Multiplied by reaction path degeneracy 2.0
family: Surface_Abstraction_vdW
""",
)

entry(
    index = 23,
    label = "OX + HX <=> X + OHX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.28e+21,'cm^2/(mol*s)'), n=0, Ea=(11200,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/CPOX_Pt/Deutschmann2006
""",
)

entry(
    index = 24,
    label = "HX + OHX <=> X + H2O_X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.04e+21,'cm^2/(mol*s)'), n=0, Ea=(66220,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/CPOX_Pt/Deutschmann2006
""",
)

entry(
    index = 25,
    label = "X + NH2_X <=> HX + NH_X",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.718e+22,'cm^2/(mol*s)'), n=0, Ea=(75.74,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K'), comment="""Matched reaction 9 NH2_X + Ni_4 <=> NHX_1 + HX_5 in Surface_Dissociation/training
    This reaction matched rate rule [N-H2;VacantSite]
    family: Surface_Dissociation
    metal: None"""),
    longDesc = 
"""
Matched reaction 9 NH2_X + Ni_4 <=> NHX_1 + HX_5 in Surface_Dissociation/training
This reaction matched rate rule [N-H2;VacantSite]
family: Surface_Dissociation
metal: None
""",
)

entry(
    index = 26,
    label = "X + NH_X <=> NX + HX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.213e+19,'cm^2/(mol*s)'), n=0, Ea=(22.93,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K'), comment="""Matched reaction 11 NHX_2 + Ni_4 <=> NX + HX_5 in Surface_Dissociation/training
    This reaction matched rate rule [N-H;VacantSite]
    family: Surface_Dissociation
    metal: None"""),
    longDesc = 
"""
Matched reaction 11 NHX_2 + Ni_4 <=> NX + HX_5 in Surface_Dissociation/training
This reaction matched rate rule [N-H;VacantSite]
family: Surface_Dissociation
metal: None
""",
)

entry(
    index = 27,
    label = "X + NHO_X <=> NOX + HX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.90767e+22,'cm^2/(mol*s)'), n=0, Ea=(78.99,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K'), comment="""From training reaction 7 used for N-H;VacantSite
    Exact match found for rate rule [N-H;VacantSite]
    Euclidian distance = 0
    family: Surface_Dissociation_vdW"""),
    longDesc = 
"""
From training reaction 7 used for N-H;VacantSite
Exact match found for rate rule [N-H;VacantSite]
Euclidian distance = 0
family: Surface_Dissociation_vdW
""",
)

entry(
    index = 28,
    label = "X + X + H2O <=> HX + OHX",
    degeneracy = 2.0,
    kinetics = StickingCoefficient(A=0.032, n=0, Ea=(61.9349,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K'), comment="""Estimated using template [Adsorbate;VacantSite1;VacantSite2] for rate rule [H2O;VacantSite1;VacantSite2]
    Euclidian distance = 3.0
    Multiplied by reaction path degeneracy 2.0
    family: Surface_Adsorption_Dissociative
    Ea raised from 0.0 to 61.9 kJ/mol to match endothermicity of reaction."""),
    longDesc = 
"""
Estimated using template [Adsorbate;VacantSite1;VacantSite2] for rate rule [H2O;VacantSite1;VacantSite2]
Euclidian distance = 3.0
Multiplied by reaction path degeneracy 2.0
family: Surface_Adsorption_Dissociative
Ea raised from 0.0 to 61.9 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 29,
    label = "X + X + NH3 <=> HX + NH2_X",
    degeneracy = 3.0,
    kinetics = StickingCoefficient(A=0.048, n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K'), comment="""Estimated using template [Adsorbate;VacantSite1;VacantSite2] for rate rule [N;VacantSite1;VacantSite2]
    Euclidian distance = 1.0
    Multiplied by reaction path degeneracy 3.0
    family: Surface_Adsorption_Dissociative"""),
    longDesc = 
"""
Estimated using template [Adsorbate;VacantSite1;VacantSite2] for rate rule [N;VacantSite1;VacantSite2]
Euclidian distance = 1.0
Multiplied by reaction path degeneracy 3.0
family: Surface_Adsorption_Dissociative
""",
)

entry(
    index = 30,
    label = "X + NH3X <=> HX + NH2_X",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(5.723e+22,'cm^2/(mol*s)'), n=0, Ea=(78.99,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K'), comment="""Matched reaction 7 NH3_X + X_4 <=> NH2_X + H* in Surface_Dissociation_vdW/training
    This reaction matched rate rule [N-H;VacantSite]
    family: Surface_Dissociation_vdW
    metal: None"""),
    longDesc = 
"""
Matched reaction 7 NH3_X + X_4 <=> NH2_X + H* in Surface_Dissociation_vdW/training
This reaction matched rate rule [N-H;VacantSite]
family: Surface_Dissociation_vdW
metal: None
""",
)

entry(
    index = 31,
    label = "X + N2 <=> NN_ads",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.1, n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K'), comment="""From training reaction 5 used for Adsorbate;VacantSite
    Exact match found for rate rule [Adsorbate;VacantSite]
    Euclidian distance = 0
    family: Surface_Adsorption_vdW"""),
    longDesc = 
"""
From training reaction 5 used for Adsorbate;VacantSite
Exact match found for rate rule [Adsorbate;VacantSite]
Euclidian distance = 0
family: Surface_Adsorption_vdW
""",
)

entry(
    index = 32,
    label = "X + N2O <=> N2O-2",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.1, n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K'), comment="""From training reaction 5 used for Adsorbate;VacantSite
    Exact match found for rate rule [Adsorbate;VacantSite]
    Euclidian distance = 0
    family: Surface_Adsorption_vdW"""),
    longDesc = 
"""
From training reaction 5 used for Adsorbate;VacantSite
Exact match found for rate rule [Adsorbate;VacantSite]
Euclidian distance = 0
family: Surface_Adsorption_vdW
""",
)

