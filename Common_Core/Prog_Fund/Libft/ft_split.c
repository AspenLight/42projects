/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aspthiba <aspthiba@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/20 11:01:38 by aspthiba          #+#    #+#             */
/*   Updated: 2026/04/21 20:08:23 by aspthiba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static int	ft_wc(const char *s, char c)
{
	int	wc;
	int	word;

	wc = 0;
	word = 0;
	while (*s)
	{
		if (*s != c && word == 0)
		{
			word = 1;
			wc++;
		}
		else if (*s == c)
			word = 0;
		s++;
	}
	return (wc);
}

static void	*ft_free(char **strs, int wc)
{
	int	i;

	i = 0;
	while (i < wc)
	{
		free(strs[i]);
		i++;
	}
	free(strs);
	return (NULL);
}

static char	*ft_wordcpy(const char *s, int start, int end)
{
	char	*word;
	int		i;

	i = 0;
	word = malloc((end - start + 1) * sizeof(char));
	if (!word)
		return (NULL);
	while (start < end)
	{
		word[i] = s[start];
		i++;
		start++;
	}
	word[i] = '\0';
	return (word);
}

char	**ft_split(const char *s, char c)
{
	char	**result;
	int		i;
	int		j;
	int		wordstart;

	i = -1;
	j = 0;
	wordstart = -1;
	result = ft_calloc((ft_wc(s, c) + 1), sizeof(char *));
	if (!result)
		return (NULL);
	while (i++ < (int)ft_strlen(s))
	{
		if (s[i] != c && wordstart < 0)
			wordstart = i;
		else if ((s[i] == c || s[i] == '\0') && wordstart >= 0)
		{
			result[j] = ft_wordcpy(s, wordstart, i);
			if (!result[j])
				return (ft_free(result, j));
			wordstart = -1;
			j++;
		}
	}
	return (result);
}
/*
char **ft_split(const char *s, char c)
This function allocates and returns an array of strings
obtained by splitting given string 's' with given character 'c'
as a delimiter. Array is NULL terminated.
Returns the created array.
*/
