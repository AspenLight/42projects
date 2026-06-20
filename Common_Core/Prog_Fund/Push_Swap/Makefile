
#	====[ Variables ]====

NAME =			push_swap

CC =			cc
CFLAGS =		-Wall -Wextra -Werror -MMD -MP

FILES = 		main.c						\
				stack_utils.c				\
				stack_free.c				\
				input_checker.c				\
				input_checker_utils.c		\
				op_swap.c					\
				op_push.c					\
				op_rotate.c					\
				op_reverse_rotate.c			\
				sort_insertion.c			\
				sort_bucket.c				\
				sort_bucket_utils.c			\
				sort_radix.c				\
				sort_utils.c				\
				normalizer.c				\
				normalizer_utils.c			\
				bench_mode.c				\
				ft_print_err.c

SRCDIR =		./sources
SRCS =			$(addprefix $(SRCDIR)/, $(FILES))

OBJDIR =		./objects
OBJS =			$(patsubst $(SRCDIR)/%, $(OBJDIR)/%, $(SRCS:%.c=%.o))

LIBDIR = 		./LIBFT
LIB =			$(LIBDIR)/libft.a

INCDIR =		./includes $(LIBDIR)/includes

#	====[ Rules ]====

$(NAME):		$(OBJS)
				@$(MAKE) --no-print-directory -C $(LIBDIR)
				@$(CC) $(CFLAGS) -o $@ $^ $(LIB)

$(OBJDIR)/%.o:	$(SRCDIR)/%.c | $(OBJDIR)
				@$(CC) $(CFLAGS) -o $@ -c $< $(foreach dir,$(INCDIR),-I$(dir))

$(OBJDIR):
				@mkdir -p $@

all:			$(NAME)

clean:	
				@$(MAKE) clean --no-print-directory -C $(LIBDIR)
				@rm -r $(OBJDIR)

fclean:	
				@$(MAKE) fclean --no-print-directory -C $(LIBDIR)
				@rm -r $(OBJDIR)
				@rm $(NAME)

re:				fclean all

#	====[ Phony ]====

.PHONY:			all clean fclean re

#	====[ Includes ]====

-include $(OBJS:.o=.d)


