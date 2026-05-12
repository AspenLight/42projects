# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aspthiba <aspthiba@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/25 17:21:59 by aspthiba          #+#    #+#              #
#    Updated: 2026/05/12 18:56:58 by aspthiba         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

CC = gcc
AR = ar rc

FLAGS = -Wall -Wextra -Werror

NAME = libftprintf.a

SRCS = ft_printf.c \
		ft_print_uid.c \
		ft_print_cs.c \
		ft_print_pxX.c \

OBJS = $(SRCS:.c=.o)

all: $(NAME)

$(NAME): $(OBJS)
		$(AR) $(NAME) $(OBJS)

%.o: %.c ft_printf.h
		$(CC) $(FLAGS) -c $< -o $@

clean:
		rm -f $(OBJS)

fclean: clean
		rm -f $(NAME)

re: fclean all

.PHONY: all clean fclean re
