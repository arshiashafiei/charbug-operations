<https://docs.docker.com/build/building/multi-stage/>
multi stages  build are good. yes.

some new things I learned:

- BuildKit only builds the stages that the target stage depends on.
- COPY --from=nginx:latest /etc/nginx/nginx.conf /nginx.conf
- When you build your image, you don't necessarily need to build the entire Dockerfile including every stage. You can specify a target build stage.

---

<https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/proxy-load-balancer?view=aspnetcore-8.0>

<https://andrewlock.net/exploring-the-dotnet-8-preview-updates-to-docker-images-in-dotnet-8/>
