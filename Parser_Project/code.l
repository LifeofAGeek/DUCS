%{
    #include <string.h>
    #include "y.tab.h"
    int digit, ls, rs, id, key;
%}


%%
[-+]?[0-9]+ {
    printf("Number:\n",yytext);
    return NUMBER;
}

"<<"    {
    printf("Operator Left Shift\n");
    return LEFT_SHIFT;
}

">>"    {
     printf("Operator Right Shift\n");
    return RIGHT_SHIFT;
}

"++"    {
    printf("INCREAMENT\n");
    return INCREMENT;
}

int|char|bool|float|void|for|do|while|if|else|return|void|#include|<iostream>|using|namespace|std|main|cout|cin  {
    // printf("Keyword: %s\n", yytext);
    return KEY;
}

[a-zA-Z_][a-zA-Z0-9_]*   {
		printf("Identifier: %s\n", yytext);	
		return IDEN;
}

[ \t] ;

; return SEMICOLON;

. return yytext[0];

\n return NEWLINE;

%%

int yywrap() {
    return 1;
}
