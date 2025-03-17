# Deployment files for Charbug contest

In this repository, resides the necessary files, scripts, and other configs that we used for deploying domjudge and the signup website for the first Charbug programming contest held in 5th and 6th of December, 2024 at University of Isfahan.

By the good people at [UI-ACM student community](https://t.me/ui_acm).

For further information visit the contest [Telegram channel](https://t.me/CharBug).

If by any chance you find any bugs or problems in this repository, we would be happy to get your feedback, it might be useful for the next people that are going to hold this kind of contests. So feel free to create a pull request or an issue.

## Useful Commands

**backup and download users uploaded files:**

```bash
/opt/mssql-tools18/bin/sqlcmd -S localhost -d uicpc -No -Q "select * from Files" -o /opt/files.csv  -s","" -C -U sa -P YOUR_PASS
sudo docker cp mssql:/opt/files.csv .
```

**backup mssql db:**

```bash
sqlcmd -S localhost -U sa -Q "BACKUP DATABASE [uicpc] TO DISK = N'/var/opt/mssql/data/uicpcNov23.bak' WITH NOFORMAT, NOINIT, NAME = 'uicpc-full', SKIP, NOREWIND, NOUNLOAD, STATS = 10" -C
```

**Deleting specific users or teams from the database:**

```bash
sudo docker exec -it mssql /opt/mssql-tools18/bin/sqlcmd -S localhost -d uicpc -No -Q "delete FROM Teams WHERE Id=13;" -C -U sa

sudo docker exec -it mssql /opt/mssql-tools18/bin/sqlcmd -S localhost -d uicpc -No -Q "delete FROM Users WHERE TeamId=50;" -C -U sa
```

**backup mariadb(dump):**

```bash
sudo docker exec -u root -it mariadb bash
mariadb-dump -u root -p --all-databases > alldb2.sql
docker cp mariadb:/alldb2.sql .
rsync -Pa arshia@171.22.24.41:/home/arshia/alldb2.sql .
```

**restore db:**

```bash
mariadb -u root -p < alldump.sql
```

**Useful links that were useful during the deployment process:**

<https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/proxy-load-balancer?view=aspnetcore-8.0>

<https://andrewlock.net/exploring-the-dotnet-8-preview-updates-to-docker-images-in-dotnet-8/>

if you think there are a lot of things wrong with this repository that's because it is.
but from a "if it runs don't touch it" standpoint, well, it runs. And it runs just fine. I was lazy and didn't had time to abide by every best practice. :)
