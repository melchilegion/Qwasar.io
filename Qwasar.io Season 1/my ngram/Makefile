CC=gcc
CFLAGS=-Wall -Wextra -Werror

all: my_ngram

my_ngram: my_ngram.o
	$(CC) $(CFLAGS) -o $@ $<

my_ngram.o: my_ngram.c
	$(CC) $(CFLAGS) -c $<

clean:
	rm -f *.o

fclean: clean
	rm -f my_ngram

re: fclean all