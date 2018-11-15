/* ///////////////////////////////////////////////////////////////////// */
/*! 
  \file  
  \brief Variable jet routines.

  Functions for creating a variable jet.

  \author J. Matthews (james.matthews@physics.ox.ac.uk)
  \date   May 18, 2017
*/
/* ///////////////////////////////////////////////////////////////////// */

#include "pluto.h"
#include "extras.h"

/* ///////////////////////////////////////////////////////////////////// */
double GetJetParams(double *var_array, double eta) 
/*! 
  Specify the properties inside the jet - could be used to set a variable jet.
*/
/* ///////////////////////////////////////////////////////////////////// */
{
  double v_j, rho;
  double mach_number = g_inputParam[JET_MACH_NUMBER];

  v_j = g_inputParam[V_OVER_C] * CONST_c / UNIT_VELOCITY;  
  rho = 1.0 / eta;

  /* copy to array */
  var_array[RHO] = rho;
  var_array[VX2] = v_j;

  /* set pressure by jet mach number */
  var_array[PRS] = v_j * v_j / mach_number / mach_number / (5.0/3.0) * rho;

  return v_j;
}

/* ///////////////////////////////////////////////////////////////////// */
double GetAmbientDensity(double x1, double x2, double x3, double beta, double r_c, double rho0) 
/*! 
  Get the ambient density at a location x1, x2 according to an isothermal
  King profile of the form
  \f[
      \rho(r) = \rho_0 \left[1 + \left(\frac{r}{r_c}\right)^2 \right]^{-3 \beta/2}
  \f]

  where \f$r_c\f$ is the core radius, \f$\rho_0\f$ is the base density 
  and \f$\beta\f$

  \author J. Matthews (james.matthews@physics.ox.ac.uk)
  \date   September 27, 2016
*/
/* ///////////////////////////////////////////////////////////////////// */
{
  double r, rho, exponent;
  if ((beta < 0) || (beta > 2)) {
      print ("!! Error: beta must be >0,<2.\n");
      exit(0);
  }
  #if GEOMETRY == CARTESIAN
    r = sqrt(x1*x1 + x2*x2 + x3*x3); /* spherical radius in cart. coords */
  #elif GEOMETRY == CYLINDRICAL
    r = sqrt(x1*x1 + x2*x2); /* spherical radius in cyl. coords */
  #elif GEOMETRY == SPHERICAL
    r = x1; /* spherical radius in sph. coords */
  #endif

  exponent = -3.0 * beta / 2.0;
  rho = 1.0 + pow(r/r_c, 2.0);
  rho = pow(rho, exponent);
  rho *= rho0;

  return rho;
}