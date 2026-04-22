*This activity has been created as part of the 42 curriculum by aspthiba.*

## Description
This project is a C Library full of programs created to emulate common and useful C functions, for the purpose of understanding how each function works, as well as use in future projects.

## Instructions
This project contains a Makefile with the rules: all, clean, fclean, and re. the project can be compiled with the 'make all' command. it can be cleaned by the 'make fclean' command, and it can be recompiled by the 'make re' command. Compiling this project creates a libft.a file which can be used as a C library in other projects.

## Resources
[link]https://www.tutorialspoint.com/c_standard_library/index.htm
See Libft Subject PDF for descriptions of functions not found within the C Standard Library.
For a description or a detailed syntax of a function, check the file 'libft.h' or the file matching the name of the function.
No AI was used in this project.

## Library
This library contains many useful or common C functions, rewritten by myself, following the Norme. All functions are named `ft_[function name]`. These functions are as follows:
* atoi
* bzero
* calloc
* isalnum
* isalpha
* isascii
* isdigit
* isprint
* itoa
* memchr
* memcmp
* memcpy
* memmove
* memset
* putchar_fd
* putendl_fd
* putnbr_fd
* putstr_fd
* split
* strchr
* strdup
* striteri
* strjoin
* strlcat
* strlcpy
* strlen
* strmapi
* strncmp
* strnstr
* strrchr
* strtrim
* substr
* tolower
* toupper

In addition to these functions, this library contains the data structure 't_list', which contains the data `void *content` (the data contained within a node) and `struct s_list *next` (the address of the next node, or NULL if the current node is the last). The functions utilizing this data structure are as follows:
* lstadd_back (Adds the node 'new' at the end of the provided list)
* lstadd_front (Adds the node 'new' at the beginning of the provided list)
* lstclear (Deletes and frees the given node and all its successors, sets the pointer to the list to NULL)
* lstdelone (Takes a node as parameter and frees its content)
* lstiter (Iterates through the provided list and applies the function 'f' to the content of each node)
* lstlast (Returns the last node of the provided list)
* lstmap (Iterates through the provided list and creates a new list containing the results of applying function 'f' to the content of each node in the provided list)
* lstnew (Allocates memory and returns a new node, 'content' initialized with the given parameter)
* lstsize (Counts the number of nodes in the provided list)