/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nmak <nmak@learner.42.tech>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/30 19:46:38 by nmak              #+#    #+#             */
/*   Updated: 2026/05/05 17:20:37 by nmak             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static int	ft_wordcount(char const *s, char c)
{
	int	count;
	int	is_word;

	count = 0;
	is_word = 0;
	while (*s)
	{
		if (!is_word && *s != c)
		{
			count++;
			is_word = 1;
		}
		if (*s == c)
			is_word = 0;
		s++;
	}
	return (count);
}

static int	ft_wordlen(char const *s, char c)
{
	int	i;

	i = 0;
	while (s[i] && s[i] != c)
		i++;
	return (i);
}

static char	*ft_fillword(char const *s, char c)
{
	int		i;
	int		j;
	char	*word;

	i = 0;
	j = 0;
	word = malloc(ft_wordlen(s, c) + 1);
	if (!word)
		return (NULL);
	while (s[i] && s[i] == c)
		i++;
	while (s[i] && s[i] != c)
		word[j++] = s[i++];
	word[j] = '\0';
	return (word);
}

static void	ft_free_res(char **res, int i)
{
	while (i--)
		free (res[i]);
	free (res);
}

char	**ft_split(char const *s, char c)
{
	int		i;
	int		wordcount;
	char	**res;

	if (!s)
		return (NULL);
	wordcount = ft_wordcount(s, c);
	res = malloc(sizeof(char *) * (wordcount + 1));
	if (!res)
		return (NULL);
	i = 0;
	while (i < wordcount)
	{
		while (*s && *s == c)
			s++;
		res[i++] = ft_fillword(s, c);
		if (!res[i - 1])
			return (ft_free_res(res, i - 1), NULL);
		s += ft_wordlen(s, c);
	}
	res[i] = NULL;
	return (res);
}
