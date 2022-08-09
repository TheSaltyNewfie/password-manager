all: main

CC = g++
LD = g++
OBJ = build/*.o
SRC = src/*
INC = -I/include/

main: $(OBJ)
	$(LD) $(OBJ) -o build/main -pthread



$(OBJ): $(SRC)
	$(CC) -c $(SRC)
	mv *.o build/


.PHONY: clean
clean:
	find build ! -name '.gitignore' -delete

