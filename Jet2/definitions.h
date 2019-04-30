#define  PHYSICS                        RMHD
#define  DIMENSIONS                     2
#define  COMPONENTS                     3
#define  GEOMETRY                       CYLINDRICAL
#define  BODY_FORCE                     NO
#define  FORCED_TURB                    NO
#define  COOLING                        NO
#define  RECONSTRUCTION                 LINEAR
#define  TIME_STEPPING                  RK2
#define  DIMENSIONAL_SPLITTING          NO
#define  NTRACER                        1
#define  USER_DEF_PARAMETERS            6

/* -- physics dependent declarations -- */

#define  EOS                            TAUB
#define  ENTROPY_SWITCH                 NO
#define  DIVB_CONTROL                   DIV_CLEANING
#define  RESISTIVITY                    NO

/* -- user-defined parameters (labels) -- */

#define  MACH                           0
#define  LORENTZ                        1
#define  RHOJ                           2
#define  RHOA                           3
#define  SIGMA_POL                      4
#define  SIGMA_TOR                      5

/* [Beg] user-defined constants (do not change this line) */

#define  LIMITER                        VANLEER_LIM
#define  SHOCK_FLATTENING               MULTID
#define  ASSIGN_VECTOR_POTENTIAL        YES
#define  UNIT_DENSITY                   (6e-27)
#define  UNIT_LENGTH                    (CONST_pc*1e3)
#define  UNIT_VELOCITY                  (CONST_c)
#define  EPS_PSHOCK_FLATTEN             10

/* [End] user-defined constants (do not change this line) */
