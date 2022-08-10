all: main

CC = g++
LD = g++
OBJ = build/*.o
SRC = src/*
INC = -I/include/

main: $(OBJ)
	$(LD) $(OBJ) -o build/main -pthread -lpqxx -lpq


$(OBJ): $(SRC)
	$(CC) -c $(INC) $(SRC) -std=c++20
	mv *.o build/


.PHONY: clean
clean:
	find build ! -name '.gitignore' -delete

