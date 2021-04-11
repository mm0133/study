
app.out: main.o math.o print_functions.o
	gcc -o app.out main.o math.o print_functions.o


main.o: main.c print_functions.h math.h
math.o: math.c 
print_functions.o: print_functions.c

clean:
	rm *.o app.out

