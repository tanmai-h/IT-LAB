/* A Bison parser, made by GNU Bison 3.0.4.  */

/* Bison implementation for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015 Free Software Foundation, Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* C LALR(1) parser skeleton written by Richard Stallman, by
   simplifying the original so-called "semantic" parser.  */

/* All symbols defined below should begin with yy or YY, to avoid
   infringing on user name space.  This should be done even for local
   variables, as they might otherwise be expanded by user macros.
   There are some unavoidable exceptions within include files to
   define necessary library symbols; they are noted "INFRINGES ON
   USER NAME SPACE" below.  */

/* Identify Bison output.  */
#define YYBISON 1

/* Bison version.  */
#define YYBISON_VERSION "3.0.4"

/* Skeleton name.  */
#define YYSKELETON_NAME "yacc.c"

/* Pure parsers.  */
#define YYPURE 0

/* Push parsers.  */
#define YYPUSH 0

/* Pull parsers.  */
#define YYPULL 1




/* Copy the first part of user declarations.  */
#line 1 "subc-compiler.y" /* yacc.c:339  */

#include <stdio.h>
#include <stdlib.h>

extern FILE *fp;
FILE * f1;


#line 75 "y.tab.c" /* yacc.c:339  */

# ifndef YY_NULLPTR
#  if defined __cplusplus && 201103L <= __cplusplus
#   define YY_NULLPTR nullptr
#  else
#   define YY_NULLPTR 0
#  endif
# endif

/* Enabling verbose error messages.  */
#ifdef YYERROR_VERBOSE
# undef YYERROR_VERBOSE
# define YYERROR_VERBOSE 1
#else
# define YYERROR_VERBOSE 0
#endif


/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token type.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    INT = 258,
    VOID = 259,
    UINT = 260,
    WHILE = 261,
    START = 262,
    END = 263,
    IF = 264,
    ELSE = 265,
    SWITCH = 266,
    CASE = 267,
    BREAK = 268,
    DEFAULT = 269,
    NUM = 270,
    ID = 271,
    INCLUDE = 272,
    ASGN = 273,
    LOR = 274,
    LAND = 275,
    BOR = 276,
    BXOR = 277,
    BAND = 278,
    EQ = 279,
    NE = 280,
    LE = 281,
    GE = 282,
    LT = 283,
    GT = 284,
    IFX = 285,
    IFX1 = 286
  };
#endif
/* Tokens.  */
#define INT 258
#define VOID 259
#define UINT 260
#define WHILE 261
#define START 262
#define END 263
#define IF 264
#define ELSE 265
#define SWITCH 266
#define CASE 267
#define BREAK 268
#define DEFAULT 269
#define NUM 270
#define ID 271
#define INCLUDE 272
#define ASGN 273
#define LOR 274
#define LAND 275
#define BOR 276
#define BXOR 277
#define BAND 278
#define EQ 279
#define NE 280
#define LE 281
#define GE 282
#define LT 283
#define GT 284
#define IFX 285
#define IFX1 286

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;

int yyparse (void);



/* Copy the second part of user declarations.  */

#line 185 "y.tab.c" /* yacc.c:358  */

#ifdef short
# undef short
#endif

#ifdef YYTYPE_UINT8
typedef YYTYPE_UINT8 yytype_uint8;
#else
typedef unsigned char yytype_uint8;
#endif

#ifdef YYTYPE_INT8
typedef YYTYPE_INT8 yytype_int8;
#else
typedef signed char yytype_int8;
#endif

#ifdef YYTYPE_UINT16
typedef YYTYPE_UINT16 yytype_uint16;
#else
typedef unsigned short int yytype_uint16;
#endif

#ifdef YYTYPE_INT16
typedef YYTYPE_INT16 yytype_int16;
#else
typedef short int yytype_int16;
#endif

#ifndef YYSIZE_T
# ifdef __SIZE_TYPE__
#  define YYSIZE_T __SIZE_TYPE__
# elif defined size_t
#  define YYSIZE_T size_t
# elif ! defined YYSIZE_T
#  include <stddef.h> /* INFRINGES ON USER NAME SPACE */
#  define YYSIZE_T size_t
# else
#  define YYSIZE_T unsigned int
# endif
#endif

#define YYSIZE_MAXIMUM ((YYSIZE_T) -1)

#ifndef YY_
# if defined YYENABLE_NLS && YYENABLE_NLS
#  if ENABLE_NLS
#   include <libintl.h> /* INFRINGES ON USER NAME SPACE */
#   define YY_(Msgid) dgettext ("bison-runtime", Msgid)
#  endif
# endif
# ifndef YY_
#  define YY_(Msgid) Msgid
# endif
#endif

#ifndef YY_ATTRIBUTE
# if (defined __GNUC__                                               \
      && (2 < __GNUC__ || (__GNUC__ == 2 && 96 <= __GNUC_MINOR__)))  \
     || defined __SUNPRO_C && 0x5110 <= __SUNPRO_C
#  define YY_ATTRIBUTE(Spec) __attribute__(Spec)
# else
#  define YY_ATTRIBUTE(Spec) /* empty */
# endif
#endif

#ifndef YY_ATTRIBUTE_PURE
# define YY_ATTRIBUTE_PURE   YY_ATTRIBUTE ((__pure__))
#endif

#ifndef YY_ATTRIBUTE_UNUSED
# define YY_ATTRIBUTE_UNUSED YY_ATTRIBUTE ((__unused__))
#endif

#if !defined _Noreturn \
     && (!defined __STDC_VERSION__ || __STDC_VERSION__ < 201112)
# if defined _MSC_VER && 1200 <= _MSC_VER
#  define _Noreturn __declspec (noreturn)
# else
#  define _Noreturn YY_ATTRIBUTE ((__noreturn__))
# endif
#endif

/* Suppress unused-variable warnings by "using" E.  */
#if ! defined lint || defined __GNUC__
# define YYUSE(E) ((void) (E))
#else
# define YYUSE(E) /* empty */
#endif

#if defined __GNUC__ && 407 <= __GNUC__ * 100 + __GNUC_MINOR__
/* Suppress an incorrect diagnostic about yylval being uninitialized.  */
# define YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN \
    _Pragma ("GCC diagnostic push") \
    _Pragma ("GCC diagnostic ignored \"-Wuninitialized\"")\
    _Pragma ("GCC diagnostic ignored \"-Wmaybe-uninitialized\"")
# define YY_IGNORE_MAYBE_UNINITIALIZED_END \
    _Pragma ("GCC diagnostic pop")
#else
# define YY_INITIAL_VALUE(Value) Value
#endif
#ifndef YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
# define YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
# define YY_IGNORE_MAYBE_UNINITIALIZED_END
#endif
#ifndef YY_INITIAL_VALUE
# define YY_INITIAL_VALUE(Value) /* Nothing. */
#endif


#if ! defined yyoverflow || YYERROR_VERBOSE

/* The parser invokes alloca or malloc; define the necessary symbols.  */

# ifdef YYSTACK_USE_ALLOCA
#  if YYSTACK_USE_ALLOCA
#   ifdef __GNUC__
#    define YYSTACK_ALLOC __builtin_alloca
#   elif defined __BUILTIN_VA_ARG_INCR
#    include <alloca.h> /* INFRINGES ON USER NAME SPACE */
#   elif defined _AIX
#    define YYSTACK_ALLOC __alloca
#   elif defined _MSC_VER
#    include <malloc.h> /* INFRINGES ON USER NAME SPACE */
#    define alloca _alloca
#   else
#    define YYSTACK_ALLOC alloca
#    if ! defined _ALLOCA_H && ! defined EXIT_SUCCESS
#     include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
      /* Use EXIT_SUCCESS as a witness for stdlib.h.  */
#     ifndef EXIT_SUCCESS
#      define EXIT_SUCCESS 0
#     endif
#    endif
#   endif
#  endif
# endif

# ifdef YYSTACK_ALLOC
   /* Pacify GCC's 'empty if-body' warning.  */
#  define YYSTACK_FREE(Ptr) do { /* empty */; } while (0)
#  ifndef YYSTACK_ALLOC_MAXIMUM
    /* The OS might guarantee only one guard page at the bottom of the stack,
       and a page size can be as small as 4096 bytes.  So we cannot safely
       invoke alloca (N) if N exceeds 4096.  Use a slightly smaller number
       to allow for a few compiler-allocated temporary stack slots.  */
#   define YYSTACK_ALLOC_MAXIMUM 4032 /* reasonable circa 2006 */
#  endif
# else
#  define YYSTACK_ALLOC YYMALLOC
#  define YYSTACK_FREE YYFREE
#  ifndef YYSTACK_ALLOC_MAXIMUM
#   define YYSTACK_ALLOC_MAXIMUM YYSIZE_MAXIMUM
#  endif
#  if (defined __cplusplus && ! defined EXIT_SUCCESS \
       && ! ((defined YYMALLOC || defined malloc) \
             && (defined YYFREE || defined free)))
#   include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
#   ifndef EXIT_SUCCESS
#    define EXIT_SUCCESS 0
#   endif
#  endif
#  ifndef YYMALLOC
#   define YYMALLOC malloc
#   if ! defined malloc && ! defined EXIT_SUCCESS
void *malloc (YYSIZE_T); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
#  ifndef YYFREE
#   define YYFREE free
#   if ! defined free && ! defined EXIT_SUCCESS
void free (void *); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
# endif
#endif /* ! defined yyoverflow || YYERROR_VERBOSE */


#if (! defined yyoverflow \
     && (! defined __cplusplus \
         || (defined YYSTYPE_IS_TRIVIAL && YYSTYPE_IS_TRIVIAL)))

/* A type that is properly aligned for any stack member.  */
union yyalloc
{
  yytype_int16 yyss_alloc;
  YYSTYPE yyvs_alloc;
};

/* The size of the maximum gap between one aligned stack and the next.  */
# define YYSTACK_GAP_MAXIMUM (sizeof (union yyalloc) - 1)

/* The size of an array large to enough to hold all stacks, each with
   N elements.  */
# define YYSTACK_BYTES(N) \
     ((N) * (sizeof (yytype_int16) + sizeof (YYSTYPE)) \
      + YYSTACK_GAP_MAXIMUM)

# define YYCOPY_NEEDED 1

/* Relocate STACK from its old location to the new one.  The
   local variables YYSIZE and YYSTACKSIZE give the old and new number of
   elements in the stack, and YYPTR gives the new location of the
   stack.  Advance YYPTR to a properly aligned location for the next
   stack.  */
# define YYSTACK_RELOCATE(Stack_alloc, Stack)                           \
    do                                                                  \
      {                                                                 \
        YYSIZE_T yynewbytes;                                            \
        YYCOPY (&yyptr->Stack_alloc, Stack, yysize);                    \
        Stack = &yyptr->Stack_alloc;                                    \
        yynewbytes = yystacksize * sizeof (*Stack) + YYSTACK_GAP_MAXIMUM; \
        yyptr += yynewbytes / sizeof (*yyptr);                          \
      }                                                                 \
    while (0)

#endif

#if defined YYCOPY_NEEDED && YYCOPY_NEEDED
/* Copy COUNT objects from SRC to DST.  The source and destination do
   not overlap.  */
# ifndef YYCOPY
#  if defined __GNUC__ && 1 < __GNUC__
#   define YYCOPY(Dst, Src, Count) \
      __builtin_memcpy (Dst, Src, (Count) * sizeof (*(Src)))
#  else
#   define YYCOPY(Dst, Src, Count)              \
      do                                        \
        {                                       \
          YYSIZE_T yyi;                         \
          for (yyi = 0; yyi < (Count); yyi++)   \
            (Dst)[yyi] = (Src)[yyi];            \
        }                                       \
      while (0)
#  endif
# endif
#endif /* !YYCOPY_NEEDED */

/* YYFINAL -- State number of the termination state.  */
#define YYFINAL  6
/* YYLAST -- Last index in YYTABLE.  */
#define YYLAST   263

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  45
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  52
/* YYNRULES -- Number of rules.  */
#define YYNRULES  86
/* YYNSTATES -- Number of states.  */
#define YYNSTATES  143

/* YYTRANSLATE[YYX] -- Symbol number corresponding to YYX as returned
   by yylex, with out-of-bounds checking.  */
#define YYUNDEFTOK  2
#define YYMAXUTOK   286

#define YYTRANSLATE(YYX)                                                \
  ((unsigned int) (YYX) <= YYMAXUTOK ? yytranslate[YYX] : YYUNDEFTOK)

/* YYTRANSLATE[TOKEN-NUM] -- Symbol number corresponding to TOKEN-NUM
   as returned by yylex, without out-of-bounds checking.  */
static const yytype_uint8 yytranslate[] =
{
       0,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
      38,    39,    32,    30,    44,    31,     2,    33,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,    43,    42,
       2,     2,     2,     2,    34,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,    40,     2,    41,    35,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     1,     2,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    14,
      15,    16,    17,    18,    19,    20,    21,    22,    23,    24,
      25,    26,    27,    28,    29,    36,    37
};

#if YYDEBUG
  /* YYRLINE[YYN] -- Source line where rule number YYN was defined.  */
static const yytype_uint8 yyrline[] =
{
       0,    32,    32,    35,    36,    38,    39,    42,    43,    44,
      45,    46,    47,    52,    52,    53,    53,    54,    54,    55,
      55,    56,    56,    57,    57,    58,    58,    59,    59,    60,
      60,    61,    61,    62,    62,    63,    63,    64,    64,    65,
      65,    66,    66,    67,    68,    69,    73,    73,    75,    75,
      76,    79,    79,    81,    82,    85,    85,    86,    88,    88,
      89,    89,    92,    92,    95,    95,    96,   100,   101,   104,
     104,   104,   107,   108,   111,   111,   111,   115,   116,   116,
     120,   120,   120,   120,   124,   125,   126
};
#endif

#if YYDEBUG || YYERROR_VERBOSE || 0
/* YYTNAME[SYMBOL-NUM] -- String name of the symbol SYMBOL-NUM.
   First, the terminals, then, starting at YYNTOKENS, nonterminals.  */
static const char *const yytname[] =
{
  "$end", "error", "$undefined", "INT", "VOID", "UINT", "WHILE", "START",
  "END", "IF", "ELSE", "SWITCH", "CASE", "BREAK", "DEFAULT", "NUM", "ID",
  "INCLUDE", "ASGN", "LOR", "LAND", "BOR", "BXOR", "BAND", "EQ", "NE",
  "LE", "GE", "LT", "GT", "'+'", "'-'", "'*'", "'/'", "'@'", "'~'", "IFX",
  "IFX1", "'('", "')'", "'{'", "'}'", "';'", "':'", "','", "$accept",
  "pgmstart", "STMTS", "STMT1", "STMT", "EXP", "$@1", "$@2", "$@3", "$@4",
  "$@5", "$@6", "$@7", "$@8", "$@9", "$@10", "$@11", "$@12", "$@13",
  "$@14", "$@15", "STMT_IF", "$@16", "ELSESTMT", "$@17", "STMT_SWITCH",
  "$@18", "SWITCHBODY", "CASES", "$@19", "BREAKSTMT", "$@20", "$@21",
  "DEFAULTSTMT", "$@22", "DE", "$@23", "SWITCHEXP", "STMT_WHILE", "$@24",
  "$@25", "WHILEBODY", "STMT_DECLARE", "$@26", "$@27", "IDS", "$@28",
  "STMT_ASSGN", "$@29", "$@30", "$@31", "TYPE", YY_NULLPTR
};
#endif

# ifdef YYPRINT
/* YYTOKNUM[NUM] -- (External) token number corresponding to the
   (internal) symbol number NUM (which must be that of a token).  */
static const yytype_uint16 yytoknum[] =
{
       0,   256,   257,   258,   259,   260,   261,   262,   263,   264,
     265,   266,   267,   268,   269,   270,   271,   272,   273,   274,
     275,   276,   277,   278,   279,   280,   281,   282,   283,   284,
      43,    45,    42,    47,    64,   126,   285,   286,    40,    41,
     123,   125,    59,    58,    44
};
# endif

#define YYPACT_NINF -128

#define yypact_value_is_default(Yystate) \
  (!!((Yystate) == (-128)))

#define YYTABLE_NINF -83

#define yytable_value_is_error(Yytable_value) \
  0

  /* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
     STATE-NUM.  */
static const yytype_int16 yypact[] =
{
      28,  -128,  -128,  -128,     8,     4,  -128,   -16,   -15,    -5,
      56,    56,  -128,    -2,    -1,  -128,  -128,    21,    56,  -128,
    -128,  -128,    42,  -128,  -128,  -128,    16,   -12,   -12,    37,
    -128,  -128,    20,    47,  -128,  -128,  -128,   -12,    89,   109,
    -128,   -12,  -128,   129,  -128,  -128,  -128,  -128,  -128,  -128,
    -128,  -128,  -128,  -128,  -128,    45,    77,    78,    79,    80,
    -128,   -12,   149,   -33,  -128,   -12,   -12,   -12,   -12,   -12,
     -12,   -12,   -12,   -12,   -12,    -5,   -12,   -12,   -12,   -12,
     -12,    60,    53,  -128,  -128,    86,  -128,    61,    61,    38,
      38,    38,    38,   -17,   -17,  -128,  -128,    94,   230,   215,
     200,   185,   170,    93,    64,    14,  -128,  -128,  -128,    92,
      82,   110,  -128,  -128,  -128,  -128,   -33,    -5,  -128,  -128,
    -128,  -128,  -128,  -128,    83,    84,    14,    14,  -128,  -128,
     112,   130,  -128,  -128,    93,  -128,  -128,   102,  -128,   103,
      93,  -128,  -128
};

  /* YYDEFACT[STATE-NUM] -- Default reduction number in state STATE-NUM.
     Performed when YYTABLE does not specify something else to do.  Zero
     means the default is an error.  */
static const yytype_uint8 yydefact[] =
{
       0,    84,    85,    86,     0,     0,     1,     0,     0,     0,
       6,     6,     2,     0,     0,    80,    12,     0,     6,     9,
      11,    10,     0,     7,     8,    74,     0,     0,     0,     0,
       4,     5,     0,     0,     3,    45,    44,     0,    33,    33,
      81,     0,    75,    33,    23,    21,    15,    19,    13,    17,
      25,    27,    29,    31,    46,     0,     0,     0,     0,     0,
      51,     0,    33,     0,    43,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    33,    70,    77,     0,    76,    24,    22,    16,
      20,    14,    18,    26,    28,    30,    32,    50,    34,    36,
      38,    40,    42,    57,     0,    69,    78,    48,    47,     0,
       0,    53,    83,    72,    73,    71,     0,     0,    55,    52,
      62,    54,    79,    49,     0,     0,    69,    69,    67,    68,
      60,    66,    58,    56,    57,    64,    63,     0,    61,     0,
      57,    65,    59
};

  /* YYPGOTO[NTERM-NUM].  */
static const yytype_int16 yypgoto[] =
{
    -128,  -128,    -9,    -6,   -99,   -27,  -128,  -128,  -128,  -128,
    -128,  -128,  -128,  -128,  -128,  -128,  -128,  -128,  -128,  -128,
    -128,  -128,  -128,  -128,  -128,  -128,  -128,  -128,  -127,  -128,
    -128,  -128,  -128,  -128,  -128,  -128,  -128,    19,  -128,  -128,
    -128,  -128,  -128,  -128,  -128,    31,  -128,  -128,  -128,  -128,
    -128,   163
};

  /* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int16 yydefgoto[] =
{
      -1,     4,   128,    17,    18,    38,    69,    67,    70,    68,
      66,    65,    71,    72,    73,    74,    55,    56,    57,    58,
      59,    19,    75,   108,   117,    20,    81,   110,   111,   124,
     133,   137,   134,   121,   125,   136,   139,   130,    21,    22,
     105,   115,    23,    33,    63,    86,   116,    24,    29,    61,
     104,    25
};

  /* YYTABLE[YYPACT[STATE-NUM]] -- What to do in state STATE-NUM.  If
     positive, shift that token.  If negative, reduce the rule whose
     number is the opposite.  If YYTABLE_NINF, syntax error.  */
static const yytype_int16 yytable[] =
{
      12,    39,    10,    35,    36,    26,   114,   138,     6,    84,
      43,    85,    31,   142,    62,    52,    53,     1,     2,     3,
       7,    10,     8,    13,     9,    14,    37,   129,   129,    30,
      15,     1,     2,     3,    82,    11,    27,    28,    87,    88,
      89,    90,    91,    92,    93,    94,    95,    96,    32,    98,
      99,   100,   101,   102,    11,    40,    16,    34,    41,     1,
       2,     3,   -69,    42,    76,    13,    97,    14,    50,    51,
      52,    53,    15,   -35,   -37,   -39,   -41,    44,    45,    46,
      47,    48,    49,    50,    51,    52,    53,    46,    47,    48,
      49,    50,    51,    52,    53,   -82,   113,    77,    16,    78,
     103,    79,   106,    80,   107,   109,   112,   118,   123,   -35,
     -37,   -39,   -41,    44,    45,    46,    47,    48,    49,    50,
      51,    52,    53,   119,   120,   132,   126,   127,    54,   -35,
     -37,   -39,   -41,    44,    45,    46,    47,    48,    49,    50,
      51,    52,    53,   135,   140,   141,   131,   122,    60,   -35,
     -37,   -39,   -41,    44,    45,    46,    47,    48,    49,    50,
      51,    52,    53,     5,     0,     0,     0,     0,    64,   -35,
     -37,   -39,   -41,    44,    45,    46,    47,    48,    49,    50,
      51,    52,    53,     0,     0,     0,     0,     0,    83,   -33,
     -35,   -37,   -39,   -41,    44,    45,    46,    47,    48,    49,
      50,    51,    52,    53,   -33,   -35,   -37,   -39,     0,    44,
      45,    46,    47,    48,    49,    50,    51,    52,    53,   -33,
     -35,   -37,     0,     0,    44,    45,    46,    47,    48,    49,
      50,    51,    52,    53,   -33,   -35,     0,     0,     0,    44,
      45,    46,    47,    48,    49,    50,    51,    52,    53,   -33,
       0,     0,     0,     0,    44,    45,    46,    47,    48,    49,
      50,    51,    52,    53
};

static const yytype_int16 yycheck[] =
{
       9,    28,     7,    15,    16,    11,   105,   134,     0,    42,
      37,    44,    18,   140,    41,    32,    33,     3,     4,     5,
      16,     7,    38,     9,    39,    11,    38,   126,   127,     8,
      16,     3,     4,     5,    61,    40,    38,    38,    65,    66,
      67,    68,    69,    70,    71,    72,    73,    74,     6,    76,
      77,    78,    79,    80,    40,    18,    42,    41,    38,     3,
       4,     5,     6,    16,    19,     9,    75,    11,    30,    31,
      32,    33,    16,    20,    21,    22,    23,    24,    25,    26,
      27,    28,    29,    30,    31,    32,    33,    26,    27,    28,
      29,    30,    31,    32,    33,    42,   105,    20,    42,    21,
      40,    22,    16,    23,    10,    12,    42,    15,   117,    20,
      21,    22,    23,    24,    25,    26,    27,    28,    29,    30,
      31,    32,    33,    41,    14,    13,    43,    43,    39,    20,
      21,    22,    23,    24,    25,    26,    27,    28,    29,    30,
      31,    32,    33,    13,    42,    42,   127,   116,    39,    20,
      21,    22,    23,    24,    25,    26,    27,    28,    29,    30,
      31,    32,    33,     0,    -1,    -1,    -1,    -1,    39,    20,
      21,    22,    23,    24,    25,    26,    27,    28,    29,    30,
      31,    32,    33,    -1,    -1,    -1,    -1,    -1,    39,    19,
      20,    21,    22,    23,    24,    25,    26,    27,    28,    29,
      30,    31,    32,    33,    19,    20,    21,    22,    -1,    24,
      25,    26,    27,    28,    29,    30,    31,    32,    33,    19,
      20,    21,    -1,    -1,    24,    25,    26,    27,    28,    29,
      30,    31,    32,    33,    19,    20,    -1,    -1,    -1,    24,
      25,    26,    27,    28,    29,    30,    31,    32,    33,    19,
      -1,    -1,    -1,    -1,    24,    25,    26,    27,    28,    29,
      30,    31,    32,    33
};

  /* YYSTOS[STATE-NUM] -- The (internal number of the) accessing
     symbol of state STATE-NUM.  */
static const yytype_uint8 yystos[] =
{
       0,     3,     4,     5,    46,    96,     0,    16,    38,    39,
       7,    40,    47,     9,    11,    16,    42,    48,    49,    66,
      70,    83,    84,    87,    92,    96,    48,    38,    38,    93,
       8,    48,     6,    88,    41,    15,    16,    38,    50,    50,
      18,    38,    16,    50,    24,    25,    26,    27,    28,    29,
      30,    31,    32,    33,    39,    61,    62,    63,    64,    65,
      39,    94,    50,    89,    39,    56,    55,    52,    54,    51,
      53,    57,    58,    59,    60,    67,    19,    20,    21,    22,
      23,    71,    50,    39,    42,    44,    90,    50,    50,    50,
      50,    50,    50,    50,    50,    50,    50,    47,    50,    50,
      50,    50,    50,    40,    95,    85,    16,    10,    68,    12,
      72,    73,    42,    47,    49,    86,    91,    69,    15,    41,
      14,    78,    90,    47,    74,    79,    43,    43,    47,    49,
      82,    82,    13,    75,    77,    13,    80,    76,    73,    81,
      42,    42,    73
};

  /* YYR1[YYN] -- Symbol number of symbol that rule YYN derives.  */
static const yytype_uint8 yyr1[] =
{
       0,    45,    46,    47,    47,    48,    48,    49,    49,    49,
      49,    49,    49,    51,    50,    52,    50,    53,    50,    54,
      50,    55,    50,    56,    50,    57,    50,    58,    50,    59,
      50,    60,    50,    61,    50,    62,    50,    63,    50,    64,
      50,    65,    50,    50,    50,    50,    67,    66,    69,    68,
      68,    71,    70,    72,    72,    74,    73,    73,    76,    75,
      77,    75,    79,    78,    81,    80,    80,    82,    82,    84,
      85,    83,    86,    86,    88,    89,    87,    90,    91,    90,
      93,    94,    95,    92,    96,    96,    96
};

  /* YYR2[YYN] -- Number of symbols on the right hand side of rule YYN.  */
static const yytype_uint8 yyr2[] =
{
       0,     2,     5,     3,     3,     2,     0,     1,     1,     1,
       1,     1,     1,     0,     4,     0,     4,     0,     4,     0,
       4,     0,     4,     0,     4,     0,     4,     0,     4,     0,
       4,     0,     4,     0,     4,     0,     4,     0,     4,     0,
       4,     0,     4,     3,     1,     1,     0,     7,     0,     3,
       0,     0,     8,     1,     2,     0,     6,     0,     0,     4,
       0,     2,     0,     5,     0,     3,     0,     1,     1,     0,
       0,     7,     1,     1,     0,     0,     5,     1,     0,     4,
       0,     0,     0,     7,     1,     1,     1
};


#define yyerrok         (yyerrstatus = 0)
#define yyclearin       (yychar = YYEMPTY)
#define YYEMPTY         (-2)
#define YYEOF           0

#define YYACCEPT        goto yyacceptlab
#define YYABORT         goto yyabortlab
#define YYERROR         goto yyerrorlab


#define YYRECOVERING()  (!!yyerrstatus)

#define YYBACKUP(Token, Value)                                  \
do                                                              \
  if (yychar == YYEMPTY)                                        \
    {                                                           \
      yychar = (Token);                                         \
      yylval = (Value);                                         \
      YYPOPSTACK (yylen);                                       \
      yystate = *yyssp;                                         \
      goto yybackup;                                            \
    }                                                           \
  else                                                          \
    {                                                           \
      yyerror (YY_("syntax error: cannot back up")); \
      YYERROR;                                                  \
    }                                                           \
while (0)

/* Error token number */
#define YYTERROR        1
#define YYERRCODE       256



/* Enable debugging if requested.  */
#if YYDEBUG

# ifndef YYFPRINTF
#  include <stdio.h> /* INFRINGES ON USER NAME SPACE */
#  define YYFPRINTF fprintf
# endif

# define YYDPRINTF(Args)                        \
do {                                            \
  if (yydebug)                                  \
    YYFPRINTF Args;                             \
} while (0)

/* This macro is provided for backward compatibility. */
#ifndef YY_LOCATION_PRINT
# define YY_LOCATION_PRINT(File, Loc) ((void) 0)
#endif


# define YY_SYMBOL_PRINT(Title, Type, Value, Location)                    \
do {                                                                      \
  if (yydebug)                                                            \
    {                                                                     \
      YYFPRINTF (stderr, "%s ", Title);                                   \
      yy_symbol_print (stderr,                                            \
                  Type, Value); \
      YYFPRINTF (stderr, "\n");                                           \
    }                                                                     \
} while (0)


/*----------------------------------------.
| Print this symbol's value on YYOUTPUT.  |
`----------------------------------------*/

static void
yy_symbol_value_print (FILE *yyoutput, int yytype, YYSTYPE const * const yyvaluep)
{
  FILE *yyo = yyoutput;
  YYUSE (yyo);
  if (!yyvaluep)
    return;
# ifdef YYPRINT
  if (yytype < YYNTOKENS)
    YYPRINT (yyoutput, yytoknum[yytype], *yyvaluep);
# endif
  YYUSE (yytype);
}


/*--------------------------------.
| Print this symbol on YYOUTPUT.  |
`--------------------------------*/

static void
yy_symbol_print (FILE *yyoutput, int yytype, YYSTYPE const * const yyvaluep)
{
  YYFPRINTF (yyoutput, "%s %s (",
             yytype < YYNTOKENS ? "token" : "nterm", yytname[yytype]);

  yy_symbol_value_print (yyoutput, yytype, yyvaluep);
  YYFPRINTF (yyoutput, ")");
}

/*------------------------------------------------------------------.
| yy_stack_print -- Print the state stack from its BOTTOM up to its |
| TOP (included).                                                   |
`------------------------------------------------------------------*/

static void
yy_stack_print (yytype_int16 *yybottom, yytype_int16 *yytop)
{
  YYFPRINTF (stderr, "Stack now");
  for (; yybottom <= yytop; yybottom++)
    {
      int yybot = *yybottom;
      YYFPRINTF (stderr, " %d", yybot);
    }
  YYFPRINTF (stderr, "\n");
}

# define YY_STACK_PRINT(Bottom, Top)                            \
do {                                                            \
  if (yydebug)                                                  \
    yy_stack_print ((Bottom), (Top));                           \
} while (0)


/*------------------------------------------------.
| Report that the YYRULE is going to be reduced.  |
`------------------------------------------------*/

static void
yy_reduce_print (yytype_int16 *yyssp, YYSTYPE *yyvsp, int yyrule)
{
  unsigned long int yylno = yyrline[yyrule];
  int yynrhs = yyr2[yyrule];
  int yyi;
  YYFPRINTF (stderr, "Reducing stack by rule %d (line %lu):\n",
             yyrule - 1, yylno);
  /* The symbols being reduced.  */
  for (yyi = 0; yyi < yynrhs; yyi++)
    {
      YYFPRINTF (stderr, "   $%d = ", yyi + 1);
      yy_symbol_print (stderr,
                       yystos[yyssp[yyi + 1 - yynrhs]],
                       &(yyvsp[(yyi + 1) - (yynrhs)])
                                              );
      YYFPRINTF (stderr, "\n");
    }
}

# define YY_REDUCE_PRINT(Rule)          \
do {                                    \
  if (yydebug)                          \
    yy_reduce_print (yyssp, yyvsp, Rule); \
} while (0)

/* Nonzero means print parse trace.  It is left uninitialized so that
   multiple parsers can coexist.  */
int yydebug;
#else /* !YYDEBUG */
# define YYDPRINTF(Args)
# define YY_SYMBOL_PRINT(Title, Type, Value, Location)
# define YY_STACK_PRINT(Bottom, Top)
# define YY_REDUCE_PRINT(Rule)
#endif /* !YYDEBUG */


/* YYINITDEPTH -- initial size of the parser's stacks.  */
#ifndef YYINITDEPTH
# define YYINITDEPTH 200
#endif

/* YYMAXDEPTH -- maximum size the stacks can grow to (effective only
   if the built-in stack extension method is used).

   Do not make this value too large; the results are undefined if
   YYSTACK_ALLOC_MAXIMUM < YYSTACK_BYTES (YYMAXDEPTH)
   evaluated with infinite-precision integer arithmetic.  */

#ifndef YYMAXDEPTH
# define YYMAXDEPTH 10000
#endif


#if YYERROR_VERBOSE

# ifndef yystrlen
#  if defined __GLIBC__ && defined _STRING_H
#   define yystrlen strlen
#  else
/* Return the length of YYSTR.  */
static YYSIZE_T
yystrlen (const char *yystr)
{
  YYSIZE_T yylen;
  for (yylen = 0; yystr[yylen]; yylen++)
    continue;
  return yylen;
}
#  endif
# endif

# ifndef yystpcpy
#  if defined __GLIBC__ && defined _STRING_H && defined _GNU_SOURCE
#   define yystpcpy stpcpy
#  else
/* Copy YYSRC to YYDEST, returning the address of the terminating '\0' in
   YYDEST.  */
static char *
yystpcpy (char *yydest, const char *yysrc)
{
  char *yyd = yydest;
  const char *yys = yysrc;

  while ((*yyd++ = *yys++) != '\0')
    continue;

  return yyd - 1;
}
#  endif
# endif

# ifndef yytnamerr
/* Copy to YYRES the contents of YYSTR after stripping away unnecessary
   quotes and backslashes, so that it's suitable for yyerror.  The
   heuristic is that double-quoting is unnecessary unless the string
   contains an apostrophe, a comma, or backslash (other than
   backslash-backslash).  YYSTR is taken from yytname.  If YYRES is
   null, do not copy; instead, return the length of what the result
   would have been.  */
static YYSIZE_T
yytnamerr (char *yyres, const char *yystr)
{
  if (*yystr == '"')
    {
      YYSIZE_T yyn = 0;
      char const *yyp = yystr;

      for (;;)
        switch (*++yyp)
          {
          case '\'':
          case ',':
            goto do_not_strip_quotes;

          case '\\':
            if (*++yyp != '\\')
              goto do_not_strip_quotes;
            /* Fall through.  */
          default:
            if (yyres)
              yyres[yyn] = *yyp;
            yyn++;
            break;

          case '"':
            if (yyres)
              yyres[yyn] = '\0';
            return yyn;
          }
    do_not_strip_quotes: ;
    }

  if (! yyres)
    return yystrlen (yystr);

  return yystpcpy (yyres, yystr) - yyres;
}
# endif

/* Copy into *YYMSG, which is of size *YYMSG_ALLOC, an error message
   about the unexpected token YYTOKEN for the state stack whose top is
   YYSSP.

   Return 0 if *YYMSG was successfully written.  Return 1 if *YYMSG is
   not large enough to hold the message.  In that case, also set
   *YYMSG_ALLOC to the required number of bytes.  Return 2 if the
   required number of bytes is too large to store.  */
static int
yysyntax_error (YYSIZE_T *yymsg_alloc, char **yymsg,
                yytype_int16 *yyssp, int yytoken)
{
  YYSIZE_T yysize0 = yytnamerr (YY_NULLPTR, yytname[yytoken]);
  YYSIZE_T yysize = yysize0;
  enum { YYERROR_VERBOSE_ARGS_MAXIMUM = 5 };
  /* Internationalized format string. */
  const char *yyformat = YY_NULLPTR;
  /* Arguments of yyformat. */
  char const *yyarg[YYERROR_VERBOSE_ARGS_MAXIMUM];
  /* Number of reported tokens (one for the "unexpected", one per
     "expected"). */
  int yycount = 0;

  /* There are many possibilities here to consider:
     - If this state is a consistent state with a default action, then
       the only way this function was invoked is if the default action
       is an error action.  In that case, don't check for expected
       tokens because there are none.
     - The only way there can be no lookahead present (in yychar) is if
       this state is a consistent state with a default action.  Thus,
       detecting the absence of a lookahead is sufficient to determine
       that there is no unexpected or expected token to report.  In that
       case, just report a simple "syntax error".
     - Don't assume there isn't a lookahead just because this state is a
       consistent state with a default action.  There might have been a
       previous inconsistent state, consistent state with a non-default
       action, or user semantic action that manipulated yychar.
     - Of course, the expected token list depends on states to have
       correct lookahead information, and it depends on the parser not
       to perform extra reductions after fetching a lookahead from the
       scanner and before detecting a syntax error.  Thus, state merging
       (from LALR or IELR) and default reductions corrupt the expected
       token list.  However, the list is correct for canonical LR with
       one exception: it will still contain any token that will not be
       accepted due to an error action in a later state.
  */
  if (yytoken != YYEMPTY)
    {
      int yyn = yypact[*yyssp];
      yyarg[yycount++] = yytname[yytoken];
      if (!yypact_value_is_default (yyn))
        {
          /* Start YYX at -YYN if negative to avoid negative indexes in
             YYCHECK.  In other words, skip the first -YYN actions for
             this state because they are default actions.  */
          int yyxbegin = yyn < 0 ? -yyn : 0;
          /* Stay within bounds of both yycheck and yytname.  */
          int yychecklim = YYLAST - yyn + 1;
          int yyxend = yychecklim < YYNTOKENS ? yychecklim : YYNTOKENS;
          int yyx;

          for (yyx = yyxbegin; yyx < yyxend; ++yyx)
            if (yycheck[yyx + yyn] == yyx && yyx != YYTERROR
                && !yytable_value_is_error (yytable[yyx + yyn]))
              {
                if (yycount == YYERROR_VERBOSE_ARGS_MAXIMUM)
                  {
                    yycount = 1;
                    yysize = yysize0;
                    break;
                  }
                yyarg[yycount++] = yytname[yyx];
                {
                  YYSIZE_T yysize1 = yysize + yytnamerr (YY_NULLPTR, yytname[yyx]);
                  if (! (yysize <= yysize1
                         && yysize1 <= YYSTACK_ALLOC_MAXIMUM))
                    return 2;
                  yysize = yysize1;
                }
              }
        }
    }

  switch (yycount)
    {
# define YYCASE_(N, S)                      \
      case N:                               \
        yyformat = S;                       \
      break
      YYCASE_(0, YY_("syntax error"));
      YYCASE_(1, YY_("syntax error, unexpected %s"));
      YYCASE_(2, YY_("syntax error, unexpected %s, expecting %s"));
      YYCASE_(3, YY_("syntax error, unexpected %s, expecting %s or %s"));
      YYCASE_(4, YY_("syntax error, unexpected %s, expecting %s or %s or %s"));
      YYCASE_(5, YY_("syntax error, unexpected %s, expecting %s or %s or %s or %s"));
# undef YYCASE_
    }

  {
    YYSIZE_T yysize1 = yysize + yystrlen (yyformat);
    if (! (yysize <= yysize1 && yysize1 <= YYSTACK_ALLOC_MAXIMUM))
      return 2;
    yysize = yysize1;
  }

  if (*yymsg_alloc < yysize)
    {
      *yymsg_alloc = 2 * yysize;
      if (! (yysize <= *yymsg_alloc
             && *yymsg_alloc <= YYSTACK_ALLOC_MAXIMUM))
        *yymsg_alloc = YYSTACK_ALLOC_MAXIMUM;
      return 1;
    }

  /* Avoid sprintf, as that infringes on the user's name space.
     Don't have undefined behavior even if the translation
     produced a string with the wrong number of "%s"s.  */
  {
    char *yyp = *yymsg;
    int yyi = 0;
    while ((*yyp = *yyformat) != '\0')
      if (*yyp == '%' && yyformat[1] == 's' && yyi < yycount)
        {
          yyp += yytnamerr (yyp, yyarg[yyi++]);
          yyformat += 2;
        }
      else
        {
          yyp++;
          yyformat++;
        }
  }
  return 0;
}
#endif /* YYERROR_VERBOSE */

/*-----------------------------------------------.
| Release the memory associated to this symbol.  |
`-----------------------------------------------*/

static void
yydestruct (const char *yymsg, int yytype, YYSTYPE *yyvaluep)
{
  YYUSE (yyvaluep);
  if (!yymsg)
    yymsg = "Deleting";
  YY_SYMBOL_PRINT (yymsg, yytype, yyvaluep, yylocationp);

  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  YYUSE (yytype);
  YY_IGNORE_MAYBE_UNINITIALIZED_END
}




/* The lookahead symbol.  */
int yychar;

/* The semantic value of the lookahead symbol.  */
YYSTYPE yylval;
/* Number of syntax errors so far.  */
int yynerrs;


/*----------.
| yyparse.  |
`----------*/

int
yyparse (void)
{
    int yystate;
    /* Number of tokens to shift before error messages enabled.  */
    int yyerrstatus;

    /* The stacks and their tools:
       'yyss': related to states.
       'yyvs': related to semantic values.

       Refer to the stacks through separate pointers, to allow yyoverflow
       to reallocate them elsewhere.  */

    /* The state stack.  */
    yytype_int16 yyssa[YYINITDEPTH];
    yytype_int16 *yyss;
    yytype_int16 *yyssp;

    /* The semantic value stack.  */
    YYSTYPE yyvsa[YYINITDEPTH];
    YYSTYPE *yyvs;
    YYSTYPE *yyvsp;

    YYSIZE_T yystacksize;

  int yyn;
  int yyresult;
  /* Lookahead token as an internal (translated) token number.  */
  int yytoken = 0;
  /* The variables used to return semantic value and location from the
     action routines.  */
  YYSTYPE yyval;

#if YYERROR_VERBOSE
  /* Buffer for error messages, and its allocated size.  */
  char yymsgbuf[128];
  char *yymsg = yymsgbuf;
  YYSIZE_T yymsg_alloc = sizeof yymsgbuf;
#endif

#define YYPOPSTACK(N)   (yyvsp -= (N), yyssp -= (N))

  /* The number of symbols on the RHS of the reduced rule.
     Keep to zero when no symbol should be popped.  */
  int yylen = 0;

  yyssp = yyss = yyssa;
  yyvsp = yyvs = yyvsa;
  yystacksize = YYINITDEPTH;

  YYDPRINTF ((stderr, "Starting parse\n"));

  yystate = 0;
  yyerrstatus = 0;
  yynerrs = 0;
  yychar = YYEMPTY; /* Cause a token to be read.  */
  goto yysetstate;

/*------------------------------------------------------------.
| yynewstate -- Push a new state, which is found in yystate.  |
`------------------------------------------------------------*/
 yynewstate:
  /* In all cases, when you get here, the value and location stacks
     have just been pushed.  So pushing a state here evens the stacks.  */
  yyssp++;

 yysetstate:
  *yyssp = yystate;

  if (yyss + yystacksize - 1 <= yyssp)
    {
      /* Get the current used size of the three stacks, in elements.  */
      YYSIZE_T yysize = yyssp - yyss + 1;

#ifdef yyoverflow
      {
        /* Give user a chance to reallocate the stack.  Use copies of
           these so that the &'s don't force the real ones into
           memory.  */
        YYSTYPE *yyvs1 = yyvs;
        yytype_int16 *yyss1 = yyss;

        /* Each stack pointer address is followed by the size of the
           data in use in that stack, in bytes.  This used to be a
           conditional around just the two extra args, but that might
           be undefined if yyoverflow is a macro.  */
        yyoverflow (YY_("memory exhausted"),
                    &yyss1, yysize * sizeof (*yyssp),
                    &yyvs1, yysize * sizeof (*yyvsp),
                    &yystacksize);

        yyss = yyss1;
        yyvs = yyvs1;
      }
#else /* no yyoverflow */
# ifndef YYSTACK_RELOCATE
      goto yyexhaustedlab;
# else
      /* Extend the stack our own way.  */
      if (YYMAXDEPTH <= yystacksize)
        goto yyexhaustedlab;
      yystacksize *= 2;
      if (YYMAXDEPTH < yystacksize)
        yystacksize = YYMAXDEPTH;

      {
        yytype_int16 *yyss1 = yyss;
        union yyalloc *yyptr =
          (union yyalloc *) YYSTACK_ALLOC (YYSTACK_BYTES (yystacksize));
        if (! yyptr)
          goto yyexhaustedlab;
        YYSTACK_RELOCATE (yyss_alloc, yyss);
        YYSTACK_RELOCATE (yyvs_alloc, yyvs);
#  undef YYSTACK_RELOCATE
        if (yyss1 != yyssa)
          YYSTACK_FREE (yyss1);
      }
# endif
#endif /* no yyoverflow */

      yyssp = yyss + yysize - 1;
      yyvsp = yyvs + yysize - 1;

      YYDPRINTF ((stderr, "Stack size increased to %lu\n",
                  (unsigned long int) yystacksize));

      if (yyss + yystacksize - 1 <= yyssp)
        YYABORT;
    }

  YYDPRINTF ((stderr, "Entering state %d\n", yystate));

  if (yystate == YYFINAL)
    YYACCEPT;

  goto yybackup;

/*-----------.
| yybackup.  |
`-----------*/
yybackup:

  /* Do appropriate processing given the current state.  Read a
     lookahead token if we need one and don't already have one.  */

  /* First try to decide what to do without reference to lookahead token.  */
  yyn = yypact[yystate];
  if (yypact_value_is_default (yyn))
    goto yydefault;

  /* Not known => get a lookahead token if don't already have one.  */

  /* YYCHAR is either YYEMPTY or YYEOF or a valid lookahead symbol.  */
  if (yychar == YYEMPTY)
    {
      YYDPRINTF ((stderr, "Reading a token: "));
      yychar = yylex ();
    }

  if (yychar <= YYEOF)
    {
      yychar = yytoken = YYEOF;
      YYDPRINTF ((stderr, "Now at end of input.\n"));
    }
  else
    {
      yytoken = YYTRANSLATE (yychar);
      YY_SYMBOL_PRINT ("Next token is", yytoken, &yylval, &yylloc);
    }

  /* If the proper action on seeing token YYTOKEN is to reduce or to
     detect an error, take that action.  */
  yyn += yytoken;
  if (yyn < 0 || YYLAST < yyn || yycheck[yyn] != yytoken)
    goto yydefault;
  yyn = yytable[yyn];
  if (yyn <= 0)
    {
      if (yytable_value_is_error (yyn))
        goto yyerrlab;
      yyn = -yyn;
      goto yyreduce;
    }

  /* Count tokens shifted since error; after three, turn off error
     status.  */
  if (yyerrstatus)
    yyerrstatus--;

  /* Shift the lookahead token.  */
  YY_SYMBOL_PRINT ("Shifting", yytoken, &yylval, &yylloc);

  /* Discard the shifted token.  */
  yychar = YYEMPTY;

  yystate = yyn;
  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  *++yyvsp = yylval;
  YY_IGNORE_MAYBE_UNINITIALIZED_END

  goto yynewstate;


/*-----------------------------------------------------------.
| yydefault -- do the default action for the current state.  |
`-----------------------------------------------------------*/
yydefault:
  yyn = yydefact[yystate];
  if (yyn == 0)
    goto yyerrlab;
  goto yyreduce;


/*-----------------------------.
| yyreduce -- Do a reduction.  |
`-----------------------------*/
yyreduce:
  /* yyn is the number of a rule to reduce with.  */
  yylen = yyr2[yyn];

  /* If YYLEN is nonzero, implement the default value of the action:
     '$$ = $1'.

     Otherwise, the following line sets YYVAL to garbage.
     This behavior is undocumented and Bison
     users should not rely upon it.  Assigning to YYVAL
     unconditionally makes the parser a bit smaller, and it avoids a
     GCC warning that YYVAL may be used uninitialized.  */
  yyval = yyvsp[1-yylen];


  YY_REDUCE_PRINT (yyn);
  switch (yyn)
    {
        case 13:
#line 52 "subc-compiler.y" /* yacc.c:1646  */
    {push();}
#line 1395 "y.tab.c" /* yacc.c:1646  */
    break;

  case 14:
#line 52 "subc-compiler.y" /* yacc.c:1646  */
    {codegen_logical();}
#line 1401 "y.tab.c" /* yacc.c:1646  */
    break;

  case 15:
#line 53 "subc-compiler.y" /* yacc.c:1646  */
    {push();}
#line 1407 "y.tab.c" /* yacc.c:1646  */
    break;

  case 16:
#line 53 "subc-compiler.y" /* yacc.c:1646  */
    {codegen_logical();}
#line 1413 "y.tab.c" /* yacc.c:1646  */
    break;

  case 17:
#line 54 "subc-compiler.y" /* yacc.c:1646  */
    {push();}
#line 1419 "y.tab.c" /* yacc.c:1646  */
    break;

  case 18:
#line 54 "subc-compiler.y" /* yacc.c:1646  */
    {codegen_logical();}
#line 1425 "y.tab.c" /* yacc.c:1646  */
    break;

  case 19:
#line 55 "subc-compiler.y" /* yacc.c:1646  */
    {push();}
#line 1431 "y.tab.c" /* yacc.c:1646  */
    break;

  case 20:
#line 55 "subc-compiler.y" /* yacc.c:1646  */
    {codegen_logical();}
#line 1437 "y.tab.c" /* yacc.c:1646  */
    break;

  case 21:
#line 56 "subc-compiler.y" /* yacc.c:1646  */
    {push();}
#line 1443 "y.tab.c" /* yacc.c:1646  */
    break;

  case 22:
#line 56 "subc-compiler.y" /* yacc.c:1646  */
    {codegen_logical();}
#line 1449 "y.tab.c" /* yacc.c:1646  */
    break;

  case 23:
#line 57 "subc-compiler.y" /* yacc.c:1646  */
    {push();}
#line 1455 "y.tab.c" /* yacc.c:1646  */
    break;

  case 24:
#line 57 "subc-compiler.y" /* yacc.c:1646  */
    {codegen_logical();}
#line 1461 "y.tab.c" /* yacc.c:1646  */
    break;

  case 25:
#line 58 "subc-compiler.y" /* yacc.c:1646  */
    {push();}
#line 1467 "y.tab.c" /* yacc.c:1646  */
    break;

  case 26:
#line 58 "subc-compiler.y" /* yacc.c:1646  */
    {codegen_algebric();}
#line 1473 "y.tab.c" /* yacc.c:1646  */
    break;

  case 27:
#line 59 "subc-compiler.y" /* yacc.c:1646  */
    {push();}
#line 1479 "y.tab.c" /* yacc.c:1646  */
    break;

  case 28:
#line 59 "subc-compiler.y" /* yacc.c:1646  */
    {codegen_algebric();}
#line 1485 "y.tab.c" /* yacc.c:1646  */
    break;

  case 29:
#line 60 "subc-compiler.y" /* yacc.c:1646  */
    {push();}
#line 1491 "y.tab.c" /* yacc.c:1646  */
    break;

  case 30:
#line 60 "subc-compiler.y" /* yacc.c:1646  */
    {codegen_algebric();}
#line 1497 "y.tab.c" /* yacc.c:1646  */
    break;

  case 31:
#line 61 "subc-compiler.y" /* yacc.c:1646  */
    {push();}
#line 1503 "y.tab.c" /* yacc.c:1646  */
    break;

  case 32:
#line 61 "subc-compiler.y" /* yacc.c:1646  */
    {codegen_algebric();}
#line 1509 "y.tab.c" /* yacc.c:1646  */
    break;

  case 33:
#line 62 "subc-compiler.y" /* yacc.c:1646  */
    {push();}
#line 1515 "y.tab.c" /* yacc.c:1646  */
    break;

  case 34:
#line 62 "subc-compiler.y" /* yacc.c:1646  */
    {codegen_logical();}
#line 1521 "y.tab.c" /* yacc.c:1646  */
    break;

  case 35:
#line 63 "subc-compiler.y" /* yacc.c:1646  */
    {push();}
#line 1527 "y.tab.c" /* yacc.c:1646  */
    break;

  case 36:
#line 63 "subc-compiler.y" /* yacc.c:1646  */
    {codegen_logical();}
#line 1533 "y.tab.c" /* yacc.c:1646  */
    break;

  case 37:
#line 64 "subc-compiler.y" /* yacc.c:1646  */
    {push();}
#line 1539 "y.tab.c" /* yacc.c:1646  */
    break;

  case 38:
#line 64 "subc-compiler.y" /* yacc.c:1646  */
    {codegen_logical();}
#line 1545 "y.tab.c" /* yacc.c:1646  */
    break;

  case 39:
#line 65 "subc-compiler.y" /* yacc.c:1646  */
    {push();}
#line 1551 "y.tab.c" /* yacc.c:1646  */
    break;

  case 40:
#line 65 "subc-compiler.y" /* yacc.c:1646  */
    {codegen_logical();}
#line 1557 "y.tab.c" /* yacc.c:1646  */
    break;

  case 41:
#line 66 "subc-compiler.y" /* yacc.c:1646  */
    {push();}
#line 1563 "y.tab.c" /* yacc.c:1646  */
    break;

  case 42:
#line 66 "subc-compiler.y" /* yacc.c:1646  */
    {codegen_logical();}
#line 1569 "y.tab.c" /* yacc.c:1646  */
    break;

  case 44:
#line 68 "subc-compiler.y" /* yacc.c:1646  */
    {check();push();}
#line 1575 "y.tab.c" /* yacc.c:1646  */
    break;

  case 45:
#line 69 "subc-compiler.y" /* yacc.c:1646  */
    {push();}
#line 1581 "y.tab.c" /* yacc.c:1646  */
    break;

  case 46:
#line 73 "subc-compiler.y" /* yacc.c:1646  */
    {if_label1();}
#line 1587 "y.tab.c" /* yacc.c:1646  */
    break;

  case 48:
#line 75 "subc-compiler.y" /* yacc.c:1646  */
    {if_label2();}
#line 1593 "y.tab.c" /* yacc.c:1646  */
    break;

  case 49:
#line 75 "subc-compiler.y" /* yacc.c:1646  */
    {if_label3();}
#line 1599 "y.tab.c" /* yacc.c:1646  */
    break;

  case 50:
#line 76 "subc-compiler.y" /* yacc.c:1646  */
    {if_label3();}
#line 1605 "y.tab.c" /* yacc.c:1646  */
    break;

  case 51:
#line 79 "subc-compiler.y" /* yacc.c:1646  */
    {switch_start();}
#line 1611 "y.tab.c" /* yacc.c:1646  */
    break;

  case 53:
#line 81 "subc-compiler.y" /* yacc.c:1646  */
    {switch_end();}
#line 1617 "y.tab.c" /* yacc.c:1646  */
    break;

  case 54:
#line 82 "subc-compiler.y" /* yacc.c:1646  */
    {switch_end();}
#line 1623 "y.tab.c" /* yacc.c:1646  */
    break;

  case 55:
#line 85 "subc-compiler.y" /* yacc.c:1646  */
    {switch_case();}
#line 1629 "y.tab.c" /* yacc.c:1646  */
    break;

  case 58:
#line 88 "subc-compiler.y" /* yacc.c:1646  */
    {switch_break();}
#line 1635 "y.tab.c" /* yacc.c:1646  */
    break;

  case 60:
#line 89 "subc-compiler.y" /* yacc.c:1646  */
    {switch_nobreak();}
#line 1641 "y.tab.c" /* yacc.c:1646  */
    break;

  case 62:
#line 92 "subc-compiler.y" /* yacc.c:1646  */
    {switch_default();}
#line 1647 "y.tab.c" /* yacc.c:1646  */
    break;

  case 64:
#line 95 "subc-compiler.y" /* yacc.c:1646  */
    {switch_break();}
#line 1653 "y.tab.c" /* yacc.c:1646  */
    break;

  case 69:
#line 104 "subc-compiler.y" /* yacc.c:1646  */
    {while_start();}
#line 1659 "y.tab.c" /* yacc.c:1646  */
    break;

  case 70:
#line 104 "subc-compiler.y" /* yacc.c:1646  */
    {while_rep();}
#line 1665 "y.tab.c" /* yacc.c:1646  */
    break;

  case 72:
#line 107 "subc-compiler.y" /* yacc.c:1646  */
    {while_end();}
#line 1671 "y.tab.c" /* yacc.c:1646  */
    break;

  case 73:
#line 108 "subc-compiler.y" /* yacc.c:1646  */
    {while_end();}
#line 1677 "y.tab.c" /* yacc.c:1646  */
    break;

  case 74:
#line 111 "subc-compiler.y" /* yacc.c:1646  */
    {setType();}
#line 1683 "y.tab.c" /* yacc.c:1646  */
    break;

  case 75:
#line 111 "subc-compiler.y" /* yacc.c:1646  */
    {STMT_DECLARE();}
#line 1689 "y.tab.c" /* yacc.c:1646  */
    break;

  case 78:
#line 116 "subc-compiler.y" /* yacc.c:1646  */
    {STMT_DECLARE();}
#line 1695 "y.tab.c" /* yacc.c:1646  */
    break;

  case 80:
#line 120 "subc-compiler.y" /* yacc.c:1646  */
    {push();}
#line 1701 "y.tab.c" /* yacc.c:1646  */
    break;

  case 81:
#line 120 "subc-compiler.y" /* yacc.c:1646  */
    {push();}
#line 1707 "y.tab.c" /* yacc.c:1646  */
    break;

  case 82:
#line 120 "subc-compiler.y" /* yacc.c:1646  */
    {codegen_assign();}
#line 1713 "y.tab.c" /* yacc.c:1646  */
    break;


#line 1717 "y.tab.c" /* yacc.c:1646  */
      default: break;
    }
  /* User semantic actions sometimes alter yychar, and that requires
     that yytoken be updated with the new translation.  We take the
     approach of translating immediately before every use of yytoken.
     One alternative is translating here after every semantic action,
     but that translation would be missed if the semantic action invokes
     YYABORT, YYACCEPT, or YYERROR immediately after altering yychar or
     if it invokes YYBACKUP.  In the case of YYABORT or YYACCEPT, an
     incorrect destructor might then be invoked immediately.  In the
     case of YYERROR or YYBACKUP, subsequent parser actions might lead
     to an incorrect destructor call or verbose syntax error message
     before the lookahead is translated.  */
  YY_SYMBOL_PRINT ("-> $$ =", yyr1[yyn], &yyval, &yyloc);

  YYPOPSTACK (yylen);
  yylen = 0;
  YY_STACK_PRINT (yyss, yyssp);

  *++yyvsp = yyval;

  /* Now 'shift' the result of the reduction.  Determine what state
     that goes to, based on the state we popped back to and the rule
     number reduced by.  */

  yyn = yyr1[yyn];

  yystate = yypgoto[yyn - YYNTOKENS] + *yyssp;
  if (0 <= yystate && yystate <= YYLAST && yycheck[yystate] == *yyssp)
    yystate = yytable[yystate];
  else
    yystate = yydefgoto[yyn - YYNTOKENS];

  goto yynewstate;


/*--------------------------------------.
| yyerrlab -- here on detecting error.  |
`--------------------------------------*/
yyerrlab:
  /* Make sure we have latest lookahead translation.  See comments at
     user semantic actions for why this is necessary.  */
  yytoken = yychar == YYEMPTY ? YYEMPTY : YYTRANSLATE (yychar);

  /* If not already recovering from an error, report this error.  */
  if (!yyerrstatus)
    {
      ++yynerrs;
#if ! YYERROR_VERBOSE
      yyerror (YY_("syntax error"));
#else
# define YYSYNTAX_ERROR yysyntax_error (&yymsg_alloc, &yymsg, \
                                        yyssp, yytoken)
      {
        char const *yymsgp = YY_("syntax error");
        int yysyntax_error_status;
        yysyntax_error_status = YYSYNTAX_ERROR;
        if (yysyntax_error_status == 0)
          yymsgp = yymsg;
        else if (yysyntax_error_status == 1)
          {
            if (yymsg != yymsgbuf)
              YYSTACK_FREE (yymsg);
            yymsg = (char *) YYSTACK_ALLOC (yymsg_alloc);
            if (!yymsg)
              {
                yymsg = yymsgbuf;
                yymsg_alloc = sizeof yymsgbuf;
                yysyntax_error_status = 2;
              }
            else
              {
                yysyntax_error_status = YYSYNTAX_ERROR;
                yymsgp = yymsg;
              }
          }
        yyerror (yymsgp);
        if (yysyntax_error_status == 2)
          goto yyexhaustedlab;
      }
# undef YYSYNTAX_ERROR
#endif
    }



  if (yyerrstatus == 3)
    {
      /* If just tried and failed to reuse lookahead token after an
         error, discard it.  */

      if (yychar <= YYEOF)
        {
          /* Return failure if at end of input.  */
          if (yychar == YYEOF)
            YYABORT;
        }
      else
        {
          yydestruct ("Error: discarding",
                      yytoken, &yylval);
          yychar = YYEMPTY;
        }
    }

  /* Else will try to reuse lookahead token after shifting the error
     token.  */
  goto yyerrlab1;


/*---------------------------------------------------.
| yyerrorlab -- error raised explicitly by YYERROR.  |
`---------------------------------------------------*/
yyerrorlab:

  /* Pacify compilers like GCC when the user code never invokes
     YYERROR and the label yyerrorlab therefore never appears in user
     code.  */
  if (/*CONSTCOND*/ 0)
     goto yyerrorlab;

  /* Do not reclaim the symbols of the rule whose action triggered
     this YYERROR.  */
  YYPOPSTACK (yylen);
  yylen = 0;
  YY_STACK_PRINT (yyss, yyssp);
  yystate = *yyssp;
  goto yyerrlab1;


/*-------------------------------------------------------------.
| yyerrlab1 -- common code for both syntax error and YYERROR.  |
`-------------------------------------------------------------*/
yyerrlab1:
  yyerrstatus = 3;      /* Each real token shifted decrements this.  */

  for (;;)
    {
      yyn = yypact[yystate];
      if (!yypact_value_is_default (yyn))
        {
          yyn += YYTERROR;
          if (0 <= yyn && yyn <= YYLAST && yycheck[yyn] == YYTERROR)
            {
              yyn = yytable[yyn];
              if (0 < yyn)
                break;
            }
        }

      /* Pop the current state because it cannot handle the error token.  */
      if (yyssp == yyss)
        YYABORT;


      yydestruct ("Error: popping",
                  yystos[yystate], yyvsp);
      YYPOPSTACK (1);
      yystate = *yyssp;
      YY_STACK_PRINT (yyss, yyssp);
    }

  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  *++yyvsp = yylval;
  YY_IGNORE_MAYBE_UNINITIALIZED_END


  /* Shift the error token.  */
  YY_SYMBOL_PRINT ("Shifting", yystos[yyn], yyvsp, yylsp);

  yystate = yyn;
  goto yynewstate;


/*-------------------------------------.
| yyacceptlab -- YYACCEPT comes here.  |
`-------------------------------------*/
yyacceptlab:
  yyresult = 0;
  goto yyreturn;

/*-----------------------------------.
| yyabortlab -- YYABORT comes here.  |
`-----------------------------------*/
yyabortlab:
  yyresult = 1;
  goto yyreturn;

#if !defined yyoverflow || YYERROR_VERBOSE
/*-------------------------------------------------.
| yyexhaustedlab -- memory exhaustion comes here.  |
`-------------------------------------------------*/
yyexhaustedlab:
  yyerror (YY_("memory exhausted"));
  yyresult = 2;
  /* Fall through.  */
#endif

yyreturn:
  if (yychar != YYEMPTY)
    {
      /* Make sure we have latest lookahead translation.  See comments at
         user semantic actions for why this is necessary.  */
      yytoken = YYTRANSLATE (yychar);
      yydestruct ("Cleanup: discarding lookahead",
                  yytoken, &yylval);
    }
  /* Do not reclaim the symbols of the rule whose action triggered
     this YYABORT or YYACCEPT.  */
  YYPOPSTACK (yylen);
  YY_STACK_PRINT (yyss, yyssp);
  while (yyssp != yyss)
    {
      yydestruct ("Cleanup: popping",
                  yystos[*yyssp], yyvsp);
      YYPOPSTACK (1);
    }
#ifndef yyoverflow
  if (yyss != yyssa)
    YYSTACK_FREE (yyss);
#endif
#if YYERROR_VERBOSE
  if (yymsg != yymsgbuf)
    YYSTACK_FREE (yymsg);
#endif
  return yyresult;
}
#line 129 "subc-compiler.y" /* yacc.c:1906  */


#include <ctype.h>
#include"lex.yy.c"
int count=0;

char st[1000][10];
int top=0;
int i=0;
char temp[2]="t";

int label[200];
int lnum=0;
int ltop=0;
int switch_stack[1000];
int stop=0;
char type[10];
struct Table
{
	char id[20];
	char type[10];
}
table[10000];
int tableCount=0;

int main(int argc, char *argv[])
{
	yyin = fopen(argv[1], "r");
	f1=fopen("output","w");
	
   if(!yyparse())
		printf("\nParsing complete\n");
	else
	{
		printf("\nParsing failed\n");
		exit(0);
	}
	
	fclose(yyin);
	fclose(f1);
	intermediateCode();
    return 0;
}
         
yyerror(char *s) {
	printf("Syntex Error in line number : %d : %s %s\n", yylineno, s, yytext );
}
    
push()
{
  	strcpy(st[++top],yytext);
}

codegen_logical()
{
 	sprintf(temp,"$t%d",i);
  	fprintf(f1,"%s\t=\t%s\t%s\t%s\n",temp,st[top-2],st[top-1],st[top]);
  	top-=2;
 	strcpy(st[top],temp);
 	i++;
}

codegen_algebric()
{
 	sprintf(temp,"$t%d",i); // converts temp to reqd format
  	fprintf(f1,"%s\t=\t%s\t%s\t%s\n",temp,st[top-2],st[top-1],st[top]);
  	top-=2;
 	strcpy(st[top],temp);
 	i++;
}
codegen_assign()
{
 	fprintf(f1,"%s\t=\t%s\n",st[top-2],st[top]);
 	top-=3;
}
 
if_label1()
{
 	lnum++;
 	fprintf(f1,"\tif( not %s)",st[top]);
 	fprintf(f1,"\tgoto $L%d\n",lnum);
 	label[++ltop]=lnum;
}

if_label2()
{
	int x;
	lnum++;
	x=label[ltop--]; 
	fprintf(f1,"\t\tgoto $L%d\n",lnum);
	fprintf(f1,"$L%d: \n",x); 
	label[++ltop]=lnum;
}

if_label3()
{
	int y;
	y=label[ltop--];
	fprintf(f1,"$L%d: \n",y);
	top--;
}
while_start()
{
	lnum++;
	label[++ltop]=lnum;
	fprintf(f1,"$L%d:\n",lnum);
}
while_rep()
{
	lnum++;
 	fprintf(f1,"if( not %s)",st[top]);
 	fprintf(f1,"\tgoto $L%d\n",lnum);
 	label[++ltop]=lnum;
}
while_end()
{
	int x,y;
	y=label[ltop--];
	x=label[ltop--];
	fprintf(f1,"\t\tgoto $L%d\n",x);
	fprintf(f1,"$L%d: \n",y);
	top--;
}
switch_start()
{
	lnum++;
	label[++ltop]=lnum;
	lnum++;
	label[++ltop]=lnum;
	switch_stack[++stop]=1;
}
switch_case()
{
	int x,y,z;
	z=switch_stack[stop--];
	if(z==1)
	{
		x=label[ltop--];
	}
	else if(z==2)
	{
		y=label[ltop--];
		x=label[ltop--];
	}
	fprintf(f1,"$L%d:\n",x);
	lnum++;
	label[++ltop]=lnum;
 	fprintf(f1,"if(%s != %s)",st[top],yytext);
 	fprintf(f1,"\tgoto $L%d\n",label[ltop]);
 	if(z==2)
 	{
 		fprintf(f1,"$L%d:\n",y);
 	}
}
switch_default()
{
	int x=label[ltop--];
	fprintf(f1,"$L%d:\n",x);
	lnum++;
	label[++ltop]=lnum;
}
switch_break()
{
	switch_stack[++stop]=1;
	fprintf(f1,"\t\tgoto $L%d\n",label[ltop-1]);
}
switch_nobreak()
{
	switch_stack[++stop]=2;
	lnum++;
	label[++ltop]=lnum;
	fprintf(f1,"\t\tgoto $L%d\n",label[ltop]);
}
switch_end()
{
	int x=label[ltop--];
	fprintf(f1,"$L%d:\n",x);
	x=label[ltop--];
	fprintf(f1,"$L%d:\n",x);
	top--;
	stop--;
}


/* for symbol table*/

check()
{

	char temp[20];
	strcpy(temp,yytext);
	int flag=0;
	for(i=0;i<tableCount;i++)
	{
		if(!strcmp(table[i].id,temp))
		{
			flag=1;
			break;
		}
	}
	if(!flag)
	{
		yyerror("Variable not declard");
		exit(0);
	}
}

setType()
{
	strcpy(type,yytext);
}


STMT_DECLARE()
{
	char temp[20];
	int i,flag;
	flag=0;
	strcpy(temp,yytext);
	for(i=0;i<tableCount;i++)
	{
		if(!strcmp(table[i].id,temp))
			{
			flag=1;
			break;
				}
	}
	if(flag)
	{
		yyerror("reSTMT_DECLARE of ");
		exit(0);
	}
	else
	{
		strcpy(table[tableCount].id,temp);
		strcpy(table[tableCount].type,type);
		tableCount++;
		}
}

intermediateCode()
{
	int Labels[100000];
	char buf[100];
	f1=fopen("output","r");
	int flag=0,lineno=1;
	memset(Labels,0,sizeof(Labels));
	while(fgets(buf,sizeof(buf),f1)!=NULL)
	{
		//printf("%s",buf);
		if(buf[0]=='$'&&buf[1]=='$'&&buf[2]=='L')
		{
			int k=atoi(&buf[3]);
			//printf("hi %d\n",k);
			Labels[k]=lineno;
		}
		else
		{
			lineno++;
		}
	}
	fclose(f1);
	f1=fopen("output","r");
	lineno=0;

	printf("\n\n\n*********************InterMediate Code***************************\n\n");
	while(fgets(buf,sizeof(buf),f1)!=NULL)
	{
		//printf("%s",buf);
		if(buf[0]=='$'&&buf[1]=='$'&&buf[2]=='L')
		{
			;
		}
		else
		{
			flag=0;
			lineno++;
			printf("%3d:\t",lineno);
			int len=strlen(buf),i,flag1=0;
			for(i=len-3;i>=0;i--)
			{
				if(buf[i]=='$'&&buf[i+1]=='$'&&buf[i+2]=='L')
				{
					flag1=1;
					break;
				}
			}
			if(flag1)
			{
				buf[i]=='\0';
				int k=atoi(&buf[i+3]),j;
				//printf("%s",buf);
				for(j=0;j<i;j++)
					printf("%c",buf[j]);
				printf(" %d\n",Labels[k]);
			}
			else printf("%s",buf);
		}
	}
	printf("%3d:\tend\n",++lineno);
	fclose(f1);
}
