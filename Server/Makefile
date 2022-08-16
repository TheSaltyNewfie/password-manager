all: main

CC = g++
LD = g++
OBJ = build/*.o
SRC = src/*
INC = -Iinclude/

main: $(OBJ)
	$(LD) $(OBJ) -o build/main -pthread -lpqxx -lpq -lssl -L/usr/lib


$(OBJ): $(SRC)
	$(CC) -c $(INC) $(SRC) -std=gnu++2a -Wall
	mv *.o build/


.PHONY: clean
clean:
	find build ! -name '.gitignore' -delete

