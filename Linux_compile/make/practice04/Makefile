CC=gcc
CFLAGS=-g -Wall
OBJS=main.o math.o print_functions.o
TARGET=app.out

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) -o $@ $^

main.o: main.c print_functions.h math.h
math.o: math.c 
print_functions.o: print_functions.c

clean:
	rm *.o
	rm -f $(TARGET)


