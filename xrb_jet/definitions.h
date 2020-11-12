#define  PHYSICS                        RHD
#define  DIMENSIONS                     2
#define  COMPONENTS                     2
#define  GEOMETRY                       CYLINDRICAL
#define  BODY_FORCE                     NO
#define  FORCED_TURB                    NO
#define  COOLING                        NO
#define  RECONSTRUCTION                 LINEAR
#define  TIME_STEPPING                  RK2
#define  DIMENSIONAL_SPLITTING          NO
#define  NTRACER                        1
#define  USER_DEF_PARAMETERS            5

/* -- physics dependent declarations -- */

#define  EOS                            TAUB
#define  ENTROPY_SWITCH                 NO

/* -- user-defined parameters (labels) -- */

#define  ETA                            0
#define  JET_WIDTH                      1
#define  LORENTZ                        2
#define  OUTBURST_TIME                  3
#define  CS_A                           4

/* [Beg] user-defined constants (do not change this line) */

#define  WARNING_MESSAGES               NO
#define  INTERNAL_BOUNDARY              NO
#define  INITIAL_SMOOTHING              NO
#define  SHOCK_FLATTENING               MULTID
#define  LIMITER                        MINMOD_LIM
#define  UNIT_DENSITY                   (1.672661e-24)
#define  UNIT_LENGTH                    (100.0 * CONST_c)
#define  UNIT_VELOCITY                  (CONST_c)
#define  UNIT_TIME                      (UNIT_LENGTH/UNIT_VELOCITY)
#define  EPS_PSHOCK_FLATTEN             10

/* [End] user-defined constants (do not change this line) */
