# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aspthiba <aspthiba@learner.42.tech>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/22 16:19:17 by aspthiba          #+#    #+#              #
#    Updated: 2026/03/22 19:15:43 by julhuang         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

CC = cc

FLAGS = -Wall -Wextra -Werror

NAME = rush-02

SRCS = main.c \
       file_parsing.c \
       file_parsing_utils.c \
       file_parsing_write.c\
       write_number.c \
       prep_number.c \
       sort.c \
       sort_utils.c

all: $(NAME)

$(NAME):
	$(CC) $(FLAGS) $(SRCS) -o $(NAME)

%.o: %.c
	$(CC) $(FLAGS) -c rush_header.h $< -o $@

fclean: clean
	rm -f $(NAME) .index.dict .sort.dict

re: fclean all

.PHONY: all clean fclean re
