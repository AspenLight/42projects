/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aspthiba <aspthiba@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/23 19:08:09 by aspthiba          #+#    #+#             */
/*   Updated: 2026/03/25 18:06:56 by aspthiba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

int	ft_charset(char c, char *charset)
{
	int	i;

	i = 0;
	while (charset[i])
	{
		if (c == charset[i])
			return (1);
		i++;
	}
	return (0);
}

int	ft_wc(char *str, char *charset)
{
	int	i;
	int	wc;

	i = 0;
	wc = 0;
	while (str[i])
	{
		if (i == 0 && ft_charset(str[i], charset) == 0)
			wc++;
		else if (ft_charset(str[i], charset) == 0
			&& ft_charset(str[i - 1], charset))
			wc++;
		i++;
	}
	return (wc);
}

char	*ft_alloc_word(char *str, char *charset)
{
	int		size;
	int		i;
	char	*word;

	size = 0;
	i = 0;
	while (str[size] && ft_charset(str[size], charset) == 0)
		size++;
	word = malloc((size + 1) * sizeof(char));
	if (!word)
		return (NULL);
	while (i < size)
	{
		word[i] = str[i];
		i++;
	}
	word[i] = '\0';
	return (word);
}

char	**ft_split(char *str, char *charset)
{
	char	**split;
	int		i;
	int		j;

	i = 0;
	j = 0;
	split = malloc((ft_wc(str, charset) + 1) * sizeof(char *));
	if (!split)
		return (NULL);
	while (str[i])
	{
		while (str[i] && ft_charset(str[i], charset) == 1)
			i++;
		if (str[i])
		{
			split[j] = ft_alloc_word(&str[i], charset);
			while (str[i] && ft_charset(str[i], charset) == 0)
				i++;
			j++;
		}
	}
	split[j] = 0;
	return (split);
}
/*
#include <unistd.h>
int	main(void)
{
	char	**res;
	int		i;
	int		j;
	res = ft_split("Ceci Est+Un-Test^", " +-");
	i = 0;
	write(1, "Test avec : Ceci Est+Un-Test^ : \n", 34);
	while (res[i])
	{
		j = 0;
		while (res[i][j])
		{
			write(1, &res[i][j], 1);
			j++;
		}
		write(1, "\n", 1);
		i++;
	}
	return (0);
}
*/
