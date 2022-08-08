all: main

CC = g++
LD = g++
OBJ = build/*.o
SRC = src/*

main: $(OBJ)
	$(LD) $(OBJ) -o build/main


$(OBJ): $(SRC)
	$(CC) -c $(SRC)
	mv *.o build/


.PHONY: clean
clean:
	find build ! -name '.gitignore' -delete

