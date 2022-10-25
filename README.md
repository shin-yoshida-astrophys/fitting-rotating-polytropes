# fitting-rotating-polytropes
Fitting rotating polytropic stellar models with simple analytic
formulae.

Individual fitting formulae for N=1, 1.5, 3.0 are submitted to RNAAS.


[Data files]

 omegadat.d: 1st column=polytropic index; 2nd column=normalized oblateness; 3rd column=normalized rotational frequency squared
  
  - normalizations
    * the oblateness is normalized by that of the mass-shedding model with the same polytropic index N
    * rotational frequency is normalized by $\sqrt{GM/R_e^3}$, where $M$ is the mass and $R_e$ is the equatorial radius.

 foblMS.d: 1st column=polytropic index; 2nd column=oblateness at the mass-shedding limit

[python script]
 
 fitting-Maclaurin.py: To check the residual of the Pade fitting of the rotational frequency of Maclaurin spheroids.
                       The residual in percent is plotted. Due to the "arcsin(e)"(where e stands for the ellipticity)
                       term, the residual looks wavy. This is also seen in the polytropic cases. 
                       See Chandrasekar ("Ellipsoidal figures of equilibrium", Dover, New York) for the analytic
                       formula of Maclaurin spheroid.
