*This activity has been created as part of the 42 curriculum by aspthiba.*

## Description
This project is a program that reads a line from a given file descriptor. Calling the function `char *get_next_line(int fd)` returns a string containing the first line of the location pointed by the file descriptor `fd`, the first time the function is called. Calling the function again provides the second line of the file, and so on.

## Instructions
This project does not contain a Makefile. It can be compiled with `cc -Wall -Wextra -Werror -D BUFFER_SIZE=n get_next_line.c get_next_line_utils.c get_next_line.h` where n is the buffer size value for `read()`.

## Resources
This README by jdecorte contains information on static buffers and a step by step guide on how to write your own GNL, with more detailed and specific resources at the end of the document.
[https://github.com/jdecorte-be/get-next-line/blob/master/README.md]

No AI was used in this project.

## Details
This GNL program uses a static buffer to read and hold chunks of the file pointed to by `fd` of size `BUFFER_SIZE`. Following the buffer reading the file, the string `line` is filled with the first line of `buffer` until the end of file or a newline, using the function `ft_line()`. the buffer then uses `ft_next()` to erase the line that has already been read and allocated to `line` from the buffer (using `ft_free()`), leaving the beginning of the buffer as the next line to read once `get_next_line()` is called again. This logic makes it so every time `get_next_line()` is called, a new line from the file pointed to by `fd` is returned.

