*This activity has been created as part of the 42 curriculum by aspthiba.*

## Description
This project is a recreation of the `printf()` command in the stdio.h library. It intends to implement the function following the same rules as the printf() function, for the following conversions: cspdiuxX%, without implementing the buffer management of the original function.

## Instructions
This project contains a Makefile with the rules: all, clean, fclean, and re. the project can be compiled with the 'make' command. it can be cleaned by the 'make fclean' command, and it can be recompiled by the 'make re' command.

Compiling this project creates a libftprintf.a file which can be used in other projects.

This program handles the following format characters, which must be preceded by a '%'.
- c -> Char
- s -> String
- p -> Void * as hexadecimal (Base 16)
- d -> Decimal (Base 10) integer
- i -> Integer (Base 10) (same as d)
- u -> Unsigned integer (Base 10)
- x -> Hexadecimal (Base 16), lowercase
- X -> Hexadecimal (Base 16), uppercase
- % -> A '%' character

## Resources
[https://documentation.help/C-Cpp-Reference/printf.html]

No AI was used in this project.

## Details
This Printf project reads through the given string searching for the character '%', and, upon finding it, reads the character following it. this new character is passed to the function `check_percent()` which reads the character to determine the proper print format (ex. d -> decimal, h -> lowercase hex). Upon finding a proper character, the program uses `va_arg` to read the next input of the proper type and pass it to the function determined by the format character, where that input is handled in various ways to enable printing each format. During the reading of the original string and the handling of other variables, the `count` variable is incremented for each printed character so as to be returned at the end of the program, so as to return the total length of the printed string.