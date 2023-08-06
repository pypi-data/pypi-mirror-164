"""
ALL RIGHTS RESERVED ABDUR_RAHMAAN JANHANGEER
_______________________________________________________________________________
COMMON COMPILER THEORY SYNTAX P1

- eof -> end of file character : tells the lexer that it has encountered the
    end of the file. Current methods just return a value telling it has reached
    the end
- grammar -> set of rules that describe a language
- context-free grammar -> rules that define a language independent of syntax
- Context-Free Grammar (CFG) in our case -> a set of rules that
    describe all possible strings in a given formal language
***
it is to be noted that source code are of type strings and as such the word
'string' is used
***

- production -> production rules specify replacement or substitutions. e.g.
    A → a means that A can be replaced by a. A → a is a production
- start symbol -> In the example below, S is the start symbol
    S → Av
    A → x

- terminal   -> does not appear on the left side of a production
- non-terminal -> that which can be broken down further
***
terminal symbol is one thing in grammar and another in syntax analysis.
see tokens below
***
- term       -> what you add or substract e.g. 1+2+3 i.e. 1 2 3
- factor     -> what you multiply or divide e.g. 3*4*5 i.e 3 4 5
- expression -> combination of term and expression etc
______________________________________________________________________
FORMAL GRAMMAR REPRESENTATIONS

-- Chomsky Normal Form (CNF)
basically has → and | where it means or
normally starts with S to denote Start symbol
Capital letters means replaceable characters

S -> a
#meaning only possible sentence is the token a

S -> aBa
B -> bb
#B can be replaced with bb

USE OF |

S -> aBa
B -> bb
B -> aa

can be represented by

S -> aBa
B -> bb | aa

(| means or thus meaning two choices)

the above define strings of fixed length. not useful for programming languages
to solve this we use recursion. see

S -> aBa
B -> bb | aaB

more or less complete description of a computer lang :

S -> EXPRESSION
EXPRESSION -> TERM | TERM + EXPRESSION | TERM - EXPRESSION
TERM -> FACTOR | FACTOR * EXPRESSION | FACTOR / EXPRESSION
FACTOR -> NUMBER | ( EXPRESSION )
NUMBER -> 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 |
          1 NUMBER | 2 NUMBER | 3 NUMBER | 4 NUMBER |
          5 NUMBER | 6 NUMBER | 7 NUMBER | 8 NUMBER |
          9 NUMBER | 0 NUMBER

-- Extended Backus Naur Form (EBNF)
Backus and Naur worked on a representation scheme and others extended on it

uses :== as separator
terminals in ''
[] 0 or 1 occurance of expansion
{} 1 or >1 occurance of expansion

S :== 'a' B 'a'
B :== 'bb'

grammar example
S :== EXPRESSION
EXPRESSION :== TERM | TERM { [+,-] TERM] }
TERM :== FACTOR | FACTOR { [*,/] FACTOR] }
FACTOR :== NUMBER | '(' EXPRESSION ')'
NUMBER :== '1' | '2' | '3' | '4' | '5' |
           '6' | '7' | '8' | '9' | '0' |
           '1' NUMBER | '2' NUMBER | '3' NUMBER |
           '4' NUMBER | '5' NUMBER | '6' NUMBER |
           '7' NUMBER | '8' NUMBER | '9' NUMBER | '0' NUMBER


______________________________________________________________________
GRAMMAR.TXT

in many languages you have a file defining the grammar in a file called
grammar.txt (which greenBerry's author has not yet included upto now).

1) C lang : see end of file

2)
Here is a more common example :

program = stmts eof "program1" ;

stmts = stmt "stmts1" (';' stmt "stmts2")* ;

stmt = "stmt1"
     | selection "stmt2"
     | iteration "stmt3"
     | assignment "stmt4" ;

selection = 'if' alts 'fi' "selection1" ;

iteration = 'do' alts 'od' "iteration1" ;

alts = alt "alts1" ('::' alt "alts2")* ;

alt = guard '?' stmts "alt1" ;

guard = expr "guard1" ;

assignment = vars ':=' exprs                  "assignment1"
           | vars ':=' subprogram ':=' exprs  "assignment2"
           |      ':=' subprogram ':=' exprs  "assignment3"
           | vars ':=' subprogram ':='        "assignment4"
           |      ':=' subprogram ':='        "assignment5" ;

vars = id "vars1" (',' id "vars2")* ;

exprs = expr "exprs1" (',' expr "exprs2")* ;

subprogram = id "subprogram1" ;

expr = disjunction "expr1" ;

disjunction = conjunction "disjunction1" ('|' conjunction "disjunction2")* ;

conjunction = negation "conjunction1" ('&' negation "conjunction2")* ;

negation = relation "negation1"
         | '~' relation "negation2" ;

relation = sum          "relation1"
         | sum '<'  sum "relation2"
         | sum '<=' sum "relation3"
         | sum '='  sum "relation4"
         | sum '~=' sum "relation5"
         | sum '>=' sum "relation6"
         | sum '>'  sum "relation7" ;

sum = (term "sum1" | '-' term "sum2") ('+' term "sum3" | '-' term "sum4")* ;

term = factor "term1"
      ('*' factor "term2" | '/' factor "term3" | '//' factor "term4")* ;

factor = 'true'       "factor1"
       | 'false'      "factor2"
       | integer      "factor3"
       | real         "factor4"
       | id           "factor5"
       | '(' expr ')' "factor6"
       | 'b2i' factor "factor7"
       | 'i2r' factor "factor8"
       | 'r2i' factor "factor9"
       | 'rand'       "factor10" ;

3)
another variety

program ::= func | e
func	::= DEFINE type id ( decls ) block program
block	::= BEGIN decls stmts END program
decls	::= decls decl | e
decl	::= type id;
type	::= type [ num ] | basic
stmts	::= stmts stmt | e
stmt	::= id = bool;
	 |  decls
	 |  IF ( bool ) stmt |  IF ( bool ) stmt ELSE stmt
	 |  WHILE ( bool ) stmt	 |  DO stmt WHILE ( bool );
	 |  BREAK;
	 |  PRINT lit;
	 |  READ id;
	 |  block
	 |  RETURN bool;
bool	::= bool OR join | join
join	::= join AND equality | equality
equality ::= equality == rel | equality != rel | rel
rel	::= expr < expr | expr <= expr | expr >= expr |
		expr > expr | expr
expr	::= expr + term | expr - term | term
term	::= term * unary | term / unary | unary
unary	::= NOT unary | - unary | factor
factor	::= ( bool ) | id | num | real | true | false


____________________________________________________________________________
COMMON COMPILER THEORY SYNTAX P2
- identifiers(id) -> must be declared before they are used
- litteral        -> fixed values : 11, 'w'
- constants       -> change-once values : once declared / set cannot be altered
- variables       -> multiple changes allowed

- CBC lexer -> CBC means Char/character by Char/character, a program that goes
    over the source text character by character

- keyword   -> word having a special meaning to the compiler

- lexeme    -> set of characters identified by the lexer
    e.g x = 5 + pencils
    lexemes : x,=,5,+,pencils

- pattern   -> set of rules that specifies when the sequence of characters from
    an input makes a token

- token     -> typically a mapping of value and type. common cases :
    1) identifiers
    2) keywords
    3) operators
    4) special symbols
    5) constant e.g. PI

    for more info see STEP 1 in analysis
    token and terminal symbol are in essence the same

- front-end : from high-level language to some intermediate language
- back-end : from some intermediary language to binary code
    in each steps below, front-end and back-end has been labelled in ()
__________ __ __
CASE :
x = 1 + y * 5

symbol table : contains symbol, type and scope (psst + - * don't have scope,
    referring to id)

_______________________________________________________________________________
ANALYSIS
_________
(front-end)
STEP 1 : Lexical Analysis -> output tokens
info : tool known as Lexer or Scanner

x     -> identifier (id)
=     -> assignment operator
1 + y -> expression
        1     -> litteral, type : number
        +     -> add operator
        y     -> identifier (id)
*     -> mult operator
5     -> litteral, type : number

transformed into tokens where
<id, 1> means first id
<=> for eqal sign as it is a litteral :
tokens :
<id, 1> <=> <num, 1> <+> <id, 2> <*> <num, 5>

starting here and in subsequent steps, symbol table :
    1. x
    2. y

Normally : Skips whitespace (new line, space, tabs ...),
ignore comments (single line, multiline)
_________
(front-end)
STEP 2 : Syntax analysis -> checks order of tokens
info : tool known as Parser

<id, 1> <=> <num, 1> (verified)
<id, 1> <=> <*> (unverified)

also generates parse trees
                        ASSIGN
                          |
               id         =          expression
                |                        |
                x         expression     +     expression
                              |                   |
                            number   expression   *   expression
                              1          |                |
                                     identifier         number
                                         y                5
 syntax tree as

                                  =
                    <id, 1>                +
                                <num, 1>           *
                                           <id, 2>    <num, 5>

trees are often generated in JSON format or XML format

JSON
{
        'some_id':
        {
                'type':....,
                'another_property':....,
                'etc':....,
        }
}

XML
<function>
    <keyword> func </keyword>
</function>

etc ... just a good enough to represent and handle format
_________
(front-end)
STEP 3 : Semantical Analysis (semantics means meaning)
generates extended syntax tree
handles type corecion for the parse tree above (given y was float)
                                  =
                    <id, 1>                +
                                <num, 1>           *
                                           <id, 2>    int_to_float
                                                      <num, 5>
_______________________________________________________________________________
SYNTHESIS

_________
(front-end)
STEP 1: intermediate code generation
the farthest nodes are reduced like
t1 = tofloat(5)
t2 = t1 * id_2
t3 = 1  + t2
id_1 = t3

_________
(front-end)
STEP 2: optimisation
t1 = 5.0 * id_2
id_1 = 1 + t1

high-level to high-level stops here

_________
(back-end)
STEP 3: code generation
the above in assembly or VM (Virtual Machine) code (psst worth a try)

_________
(back-end)
STEP 4: target specific optimisation

Bibliography :
    - wikipaedia.com
    - dragon book
    - tiger book
    - mdh.se lectures 07/04, compiler-intro
    - Compiler Basics, James Alan Farrell (1995)
    - Vipul97 on github
    - OrangeAaron on github
    - Elements of Computing Systems, MIT Press, Nisan & Schocken
    - Basics of Compiler Design, Torben Ægidius Mogensen
    - stackoverflow.com
    - tutorialspoint.com
    - dartmouth.edu, Bill McKeeman (2007)

useful demos :
    http://effbot.org/zone/simple-top-down-parsing.htm
"""

if __name__ == "__main__":
    print("see infile notes")

"""
Here is a grammar.txt for the C lanaguage, which reveals quite a few
tricks you might not know about

primary-expression
    identifier
    constant
    string-literal
    ( expression )

postfix-expression
    primary-expression
    postfix-expression [ expression ]
    postfix-expression ( )
    postfix-expression ( argument-expression-list )
    postfix-expression . identifier
    postfix-expression -> identifier
    postfix-expression ++
    postfix-expression --

argument-expression-list
    assignment-expression
    argument-expression-list , assignment-expression

unary-expression
    postfix-expression
    ++ unary-expression
    -- unary-expression
    unary-operator cast-expression
    sizeof unary-expression
    sizeof ( type-name )

unary-operator
    &
    *
    +
    -
    ~
    !

cast-expression
    unary-expression
    ( type-name ) cast-expression

multiplicative-expression
    cast-expression
    multiplicative-expression * cast-expression
    multiplicative-expression / cast-expression
    multiplicative-expression % cast-expression

additive-expression
    multiplicative-expression
    additive-expression + multiplicative-expression
    additive-expression - multiplicative-expression

shift-expression
    additive-expression
    shift-expression << additive-expression
    shift-expression >> additive-expression

relational-expression
    shift-expression
    relational-expression < shift-expression
    relational-expression > shift-expression
    relational-expression <= shift-expression
    relational-expression >= shift-expression

equality-expression
    relational-expression
    equality-expression == relational-expression
    equality-expression != relational-expression

AND-expression
    equality-expression
    AND-expression & equality-expression

exclusive-OR-expression
    AND-expression
    exclusive-OR-expression ^ AND-expression

inclusive-OR-expression
    exclusive-OR-expression
    inclusive-OR-expression | exclusive-OR-expression

logical-AND-expression
    inclusive-OR-expression
    logical-AND-expression && inclusive-OR-expression

logical-OR-expression
    logical-AND-expression
    logical-OR-expression || logical-AND-expression

conditional-expression
    logical-OR-expression
    logical-OR-expression ? expression : conditional-expression

assignment-expression
    conditional-expression
    unary-expression assignment-operator assignment-expression

assignment-operator
    =
    *=
    /=
    %=
    +=
    -=
    <<=
    >>=
    &=
    ^=
    |=

expression
    assignment-expression
    expression , assignment-expression

constant-expression
    conditional-expression

#
# C declaration rules
#

declaration
    declaration-specifiers ;
    declaration-specifiers init-declarator-list ;

declaration-specifiers
    storage-class-specifier
    type-specifier
    type-qualifier
    storage-class-specifier declaration-specifiers
    type-specifier          declaration-specifiers
    type-qualifier          declaration-specifiers

init-declarator-list
    init-declarator
    init-declarator-list , init-declarator

init-declarator
    declarator
    declarator = initializer

storage-class-specifier
    typedef
    extern
    static
    auto
    register

type-specifier
    void
    char
    short
    int
    long
    float
    double
    signed
    unsigned
    struct-or-union-specifier
    enum-specifier
    typedef-name

struct-or-union-specifier
    struct-or-union { struct-declaration-list }
    struct-or-union identifier { struct-declaration-list }
    struct-or-union identifier

struct-or-union
    struct
    union

struct-declaration-list
    struct-declaration
    struct-declaration-list struct-declaration

struct-declaration
    specifier-qualifier-list struct-declarator-list ;

specifier-qualifier-list
    type-specifier
    type-qualifier
    type-specifier specifier-qualifier-list
    type-qualifier specifier-qualifier-list

struct-declarator-list
    struct-declarator
    struct-declarator-list , struct-declarator

struct-declarator
    declarator
     constant-expression
    declarator  constant-expression

enum-specifier
    enum { enumerator-list }
    enum identifier { enumerator-list }
    enum identifier

enumerator-list
    enumerator
    enumerator-list , enumerator

enumerator
    enumeration-constant
    enumeration-constant = constant-expression

enumeration-constant
    identifier

type-qualifier
    const
    volatile

declarator
    direct-declarator
    pointer direct-declarator

direct-declarator
    identifier
    ( declarator )
    direct-declarator [ ]
    direct-declarator [ constant-expression ]
    direct-declarator ( )
    direct-declarator ( parameter-type-list )
    direct-declarator ( identifier-list )

pointer
     *
     * pointer
     * type-qualifier-list
     * type-qualifier-list pointer

type-qualifier-list
    type-qualifier
    type-qualifier-list type-qualifier

parameter-type-list
    parameter-list
    parameter-list , ...

parameter-list
    parameter-declaration
    parameter-list , parameter-declaration

parameter-declaration
    declaration-specifiers declarator
    declaration-specifiers
    declaration-specifiers abstract-declarator

identifier-list
    identifier
    identifier-list , identifier

type-name
    specifier-qualifier-list
    specifier-qualifier-list abstract-declarator

abstract-declarator
    pointer
    direct-abstract-declarator
    pointer direct-abstract-declarator

direct-abstract-declarator
    ( abstract-declarator )
    [ ]
    [ constant-expression ]
    ( )
    ( parameter-type-list )
    direct-abstract-declarator [ ]
    direct-abstract-declarator [ constant-expression ]
    direct-abstract-declarator ( )
    direct-abstract-declarator ( parameter-type-list )

typedef-name
    identifier

initializer
    assignment-expression
    { initializer-list }
    { initializer-list , }

initializer-list
    initializer
    initializer-list , initializer

#
# C statement rules
#

statement
    labeled-statement
    compound-statement
    expression-statement
    selection-statement
    iteration-statement
    jump-statement

labeled-statement
    identifier : statement
    case constant-expression : statement
    default : statement

compound-statement
    { }
    { declaration-list }
    { statement-list }
    { declaration-list statement-list }

declaration-list
    declaration
    declaration-list declaration

statement-list
    statement
    statement-list statement

expression-statement
    ;
    expression ;

selection-statement
    if ( expression ) statement
    if ( expression ) statement else statement
    switch ( expression ) statement

iteration-statement
    while ( expression ) statement
    do statement while ( expression ) ;
    for (            ;            ;            ) statement
    for (            ;            ; expression ) statement
    for (            ; expression ;            ) statement
    for (            ; expression ; expression ) statement
    for ( expression ;            ;            ) statement
    for ( expression ;            ; expression ) statement
    for ( expression ; expression ;            ) statement
    for ( expression ; expression ; expression ) statement

jump-statement
    goto identifier ;
    continue ;
    break ;
    return ;
    return expression ;

translation-unit
    external-declaration
    translation-unit external-declaration

external-declaration
    function-definition
    declaration

function-definition
                           declarator                  compound-statement
    declaration-specifiers declarator                  compound-statement
                           declarator declaration-list compound-statement
    declaration-specifiers declarator declaration-list compound-statement
"""
