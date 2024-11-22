<https://docs.docker.com/build/building/multi-stage/>
multi stages  build are good. yes.

some new things I learned:

- BuildKit only builds the stages that the target stage depends on.
- COPY --from=nginx:latest /etc/nginx/nginx.conf /nginx.conf
- When you build your image, you don't necessarily need to build the entire Dockerfile including every stage. You can specify a target build stage.

---

<https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/proxy-load-balancer?view=aspnetcore-8.0>

<https://andrewlock.net/exploring-the-dotnet-8-preview-updates-to-docker-images-in-dotnet-8/>

docker exec -it -u root baeldung bash

/opt/mssql-tools18/bin/sqlcmd -S localhost -d uicpc -No -Q "select * from Files" -o /opt/files.csv  -s","" -C -U sa -P PAASSS

sudo docker cp mssql:/opt/files.csv .

backup db:
sqlcmd -S localhost -U sa -Q "BACKUP DATABASE [demodb] TO DISK = N'/var/opt/mssql/data/demodb.bak' WITH NOFORMAT, NOINIT, NAME = 'demodb-full', SKIP, NOREWIND, NOUNLOAD, STATS = 10"

sudo docker exec -it mssql /opt/mssql-tools18/bin/sqlcmd -S localhost -d uicpc -No -Q "delete FROM Teams WHERE Id=13;" -C -U sa
