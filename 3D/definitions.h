#define  PHYSICS                 RHD
#define  DIMENSIONS              3
#define  COMPONENTS              3
#define  GEOMETRY                CARTESIAN
#define  BODY_FORCE              VECTOR
#define  COOLING                 NO
#define  RECONSTRUCTION          LINEAR
#define  TIME_STEPPING           RK2
#define  DIMENSIONAL_SPLITTING   NO
#define  NTRACER                 1
#define  USER_DEF_PARAMETERS     8

/* -- physics dependent declarations -- */

#define  EOS                     TAUB
#define  ENTROPY_SWITCH          NO

/* -- user-defined parameters (labels) -- */

#define  ETA                     0
#define  V_OVER_C                1
#define  JET_WIDTH               2
#define  JET_MACH_NUMBER         3
#define  CS_A                    4
#define  CORE_RADIUS             5
#define  BETA                    6
#define  JET_LOCATION            7

/* [Beg] user-defined constants (do not change this line) */

#define  UNIT_DENSITY            (6e-27)
#define  UNIT_LENGTH             (CONST_pc*1e3)
#define  UNIT_VELOCITY           (CONST_c)
#define  EPS_PSHOCK_FLATTEN      10

/* [End] user-defined constants (do not change this line) */

/* -- supplementary constants (user editable) -- */ 

#define  INITIAL_SMOOTHING   NO
#define  WARNING_MESSAGES    NO
#define  PRINT_TO_FILE       YES
#define  INTERNAL_BOUNDARY   YES
#define  SHOCK_FLATTENING    MULTID
#define  CHAR_LIMITING       YES
#define  LIMITER             MC_LIM
