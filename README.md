# Charbug Contest Deployment Files

This repository contains the deployment files, scripts, and configurations used to set up **DOMjudge** and the **main website** for the **first Charbug programming contest**, held on **December 5–6, 2024**, at the **University of Isfahan**.

By the good people at [UI-ACM Student Community](https://t.me/ui_acm).

For updates and announcements, check out the contest [Telegram channel](https://t.me/CharBug).

If by any chance you find bugs or issues, feel free to open a pull request or issue — your feedback helps future organizers.

## Special Thanks to

- **Saeed Abadian** [@saeed0920](https://github.com/saeed0920) (who only came to the event cause of his genuine passion.)
- **Zahra Masoumi** [@asAlwaysZahra](https://github.com/asAlwaysZahra) (who was like a one-person dev team all by herself.)
- **Soroush Nekoozadeh** [@Soroushnk](https://github.com/Soroushnk) (who really liked intense situations and was really trying to find a cheater in the event, which he did.)

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

## 📚 Resources We Found Helpful

- [ASP.NET Core Deployment Behind a Proxy](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/proxy-load-balancer?view=aspnetcore-8.0)
- [Docker Changes in .NET 8](https://andrewlock.net/exploring-the-dotnet-8-preview-updates-to-docker-images-in-dotnet-8/)

if you think there are a lot of things wrong with this repository that's because it is.
but from a "if it runs don't touch it" standpoint, well, it runs. And it runs just fine. I was lazy and didn't have time to abide by every best practice. :)
