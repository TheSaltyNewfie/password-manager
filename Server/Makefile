all: main

CC = g++
LD = g++
OBJ = build/*.o
SRC = src/*
INC = -I/include/

main: $(OBJ)
	$(LD) $(OBJ) -o build/main -pthread -lpqxx -lpq


$(OBJ): $(SRC)
	$(CC) $(INC) -c $(SRC) 
	mv *.o build/


.PHONY: clean
clean:
	find build ! -name '.gitignore' -delete

