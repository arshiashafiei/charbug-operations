# syntax=docker/dockerfile:1
FROM --platform=$BUILDPLATFORM mcr.microsoft.com/dotnet/sdk:8.0 AS build
ARG CONFIGURATION=release
WORKDIR /source

COPY --link registration-backend/*.csproj .
RUN dotnet restore && \
    dotnet tool install --global dotnet-ef
ENV PATH="$PATH:/root/.dotnet/tools"

COPY --link registration-backend/. .
RUN dotnet publish -c $CONFIGURATION --no-restore -o /app && \
    dotnet ef migrations bundle


# Runtime stage
FROM mcr.microsoft.com/dotnet/aspnet:8.0
EXPOSE 8080
WORKDIR /app
COPY --link --from=build /app /source/efbundle ./
USER $APP_UID
ENTRYPOINT ["dotnet", "registration-backend.dll"]
