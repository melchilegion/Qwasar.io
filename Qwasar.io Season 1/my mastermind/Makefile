CC=gcc
CFLAGS=-Wall -Wextra -Werror

all: my_mastermind

my_mastermind: my_mastermind.o
	$(CC) $(CFLAGS) -o $@ $<

my_mastermind.o: my_mastermind.c
	$(CC) $(CFLAGS) -c $<

clean:
	rm -f *.o

fclean: clean
	rm -f my_mastermind

re: fclean all