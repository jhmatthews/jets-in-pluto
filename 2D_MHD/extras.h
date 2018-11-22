/* ///////////////////////////////////////////////////////////////////// */
/*! 
  \file  
  \brief extra definitions used to modelling jets with pluto.

  \author J. Matthews (james.matthews@physics.ox.ac.uk)
  \date   May 15, 2017
*/
/* ///////////////////////////////////////////////////////////////////// */

/* routines for jet and ambient medium */
double GetJetParams(double *var_array, double eta);
double GetAmbientDensity(double x1, double x2, double x3, double beta, double r_c, double rho0);