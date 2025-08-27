/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: asthibau <asthibau@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/05/15 20:56:05 by asthibau          #+#    #+#             */
/*   Updated: 2025/05/24 16:01:03 by asthibau         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int		ft_wordcount(const char *s, char c);
void	*ft_free(char **strs, int wc);
char	*ft_wordcpy(const char *s, int start, int end);

char	**ft_split(const char *s, char c)
{
	char	**result;
	int		i;
	int		j;
	int		wordstart;

	i = -1;
	j = 0;
	wordstart = -1;
	result = ft_calloc((ft_wordcount(s, c) + 1), sizeof(char *));
	if (!result)
		return (NULL);
	while (i++ < (int)ft_strlen(s))
	{
		if (s[i] != c && wordstart < 0)
			wordstart = i;
		else if ((s[i] == c || s[i] == '\0') && wordstart >= 0)
		{
			result[j] = ft_wordcpy(s, wordstart, i);
			if (!(result[j]))
				return (ft_free(result, j));
			wordstart = -1;
			j++;
		}
	}
	return (result);
}

int	ft_wordcount(const char *s, char c)
{
	int	wc;
	int	i;

	wc = 0;
	i = 0;
	while (*s)
	{
		if (*s != c && i == 0)
		{
			i = 1;
			wc++;
		}
		else if (*s == c)
			i = 0;
		s++;
	}
	return (wc);
}

void	*ft_free(char **strs, int wc)
{
	int	i;

	i = 0;
	while (i < wc)
	{
		free(strs[i]);
		i++;
	}
	free (strs);
	return (NULL);
}

char	*ft_wordcpy(const char *s, int start, int end)
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
