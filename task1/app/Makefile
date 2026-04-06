Make file:

CC = gcc
CFLAGS = -Wall

app: main.o code.o
	$(CC) $(CFLAGS) -o app main.o code.o

main.o: main.c
	$(CC) $(CFLAGS) -c main.c

code.o: code.c
	$(CC) $(CFLAGS) -c code.c

clean:
	rm -f *.o app