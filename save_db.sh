#!/bin/bash
MSSQL_PASS="Pass"
sudo docker exec -u root mssql /opt/mssql-tools18/bin/sqlcmd -S localhost -d uicpc -No -Q "select * from Teams" -o /opt/teams.csv  -s"," -C -U sa -P $MSSQL_PASS
sudo docker exec -u root mssql /opt/mssql-tools18/bin/sqlcmd -S localhost -d uicpc -No -Q "select * from Users" -o /opt/users.csv  -s"," -C -U sa -P $MSSQL_PASS
sudo docker exec -u root mssql /opt/mssql-tools18/bin/sqlcmd -S localhost -d uicpc -No -Q "select * from Files" -o /opt/files.csv  -s"," -C -U sa -P $MSSQL_PASS

sudo docker cp mssql:/opt/files.csv .
sudo docker cp mssql:/opt/teams.csv .
sudo docker cp mssql:/opt/users.csv .
