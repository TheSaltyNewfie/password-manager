# Requirements
- ## Crow (HTTP/S library)
- - run `git clone https://github.com/CrowCpp/Crow.git`
- - run `mkdir build`
- - run `cmake ..`
- ## PostgreSQL (database)
- - run `sudo apt install libpqxx libpq postgres`
- - run `sudo systemctl start postgresql`
- - run `createuser server -d -r -s`
- - run `createdb server`
- - run ```bash
# It's a bit iffy with the order in which migrations are run
./migrations.sh up && ./migrations.sh up
``` 


