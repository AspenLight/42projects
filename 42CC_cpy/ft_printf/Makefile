# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: asthibau <asthibau@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/08/27 20:20:03 by asthibau          #+#    #+#              #
#    Updated: 2025/08/27 20:41:17 by asthibau         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

CC = gcc
AR = ar rc

FLAGS = -Wall -Wextra -Werror

NAME = libftprintf.a

SRCS = ft_printf.c \
		ft_print_char.c \
		ft_print_dec.c \
		ft_print_hex.c \
		ft_print_hexup.c \
		ft_print_int.c \
		ft_print_ptr.c \
		ft_print_str.c \
		ft_print_uns.c \

OBJS = $(SRCS:.c=.o)

all: $(NAME)

$(NAME): $(OBJS)
		$(AR) $(NAME) $(OBJS)

%.o: %.c libftprintf.h
		$(CC) $(FLAGS) -c $< -o $@

clean:
		rm -f $(OBJS)

fclean: clean
		rm -f $(NAME)

re: fclean all

.PHONY: all clean fclean re