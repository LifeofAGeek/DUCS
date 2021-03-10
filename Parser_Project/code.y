%{
   #include <stdio.h>
   #include <stdlib.h>
   #include <stdbool.h>

   void yyerror(const char* s); 
   int yylex();

   bool is_iden = false;
   

%}

%token KEY
%token SEMICOLON
%token IDEN
%token NUMBER
%token LEFT
%token RIGHT
%token LEFT_SHIFT
%token RIGHT_SHIFT
%token INCREMENT
%token NEWLINE

%left LEFT_SHIFT RIGHT_SHIFT
%left INCREMENT

%start statement

%%

statement: expr SEMICOLON NEWLINE {
                printf("\nValid statement!\n");
                return 0;
            }
         ;

expr: expr LEFT_SHIFT expr { is_iden = false; }
    | expr RIGHT_SHIFT expr { is_iden = false; }

    | INCREMENT expr { 
        if(is_iden) 
            is_iden = false;
        else
            yyerror("lvalue required as pre-increment operand!");
        }

    | expr INCREMENT {
        if(is_iden) 
            is_iden = false;
        else
            yyerror("lvalue required as post-increment operand!");
        }

    | NUMBER { is_iden = false; }
    | IDEN { is_iden = true; }
    | '(' expr ')'
    ;


%%

void yyerror(const char* s) {
	printf("Invalid Statement!! \n");
    printf("Error Type: %s\n", s);
    exit(0);
}


int main() {
    printf("Enter the expression to check the validity of :-\n");
    printf("1.) C++ Right Shift\n");
    printf("2.) C++ Left Shift\n");
    printf("3.) C++ Pre-increment and Post Increment\n");
    yyparse();

    return 0;
}
