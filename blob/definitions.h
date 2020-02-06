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
#define  USER_DEF_PARAMETERS            7

/* -- physics dependent declarations -- */

#define  EOS                            TAUB
#define  ENTROPY_SWITCH                 NO

/* -- user-defined parameters (labels) -- */

#define  ETA                            0
#define  V_OVER_C                       1
#define  JET_WIDTH                      2
#define  JET_MACH_NUMBER                3
#define  CS_A                           4
#define  CORE_RADIUS                    5
#define  BETA                           6

/* [Beg] user-defined constants (do not change this line) */

#define  WARNING_MESSAGES               NO
#define  INTERNAL_BOUNDARY              NO
#define  INITIAL_SMOOTHING				NO  
#define  SHOCK_FLATTENING               MULTID
#define  CHAR_LIMITING                  YES
#define  LIMITER                        MINMOD_LIM
#define  UNIT_DENSITY                   (6e-23)
#define  UNIT_LENGTH                    (CONST_pc)
#define  UNIT_VELOCITY                  (CONST_c)
#define  EPS_PSHOCK_FLATTEN             3

/* [End] user-defined constants (do not change this line) */
