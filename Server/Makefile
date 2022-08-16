all: main
CC = g++
LD = g++
OBJ = build/*.o
SRC = src/*
INC = -Iinclude/

main: $(OBJ)
	$(LD) $(OBJ) -o build/main -pthread -L/usr/local/opt/openssl/lib -lcrypto -lpqxx -lpq -lssl -DCROW_ENABLE_SSL


$(OBJ): $(SRC)
	$(CC) -c $(INC) $(SRC) -std=gnu++2a -Wall -Dis_prod=$$PRODUCTION 
	mv *.o build/


.PHONY: clean
clean:
	find build ! -name '.gitignore' ! -name 'build' -delete

