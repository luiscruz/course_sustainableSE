# course_sustainableSE
Website of the course Sustainable Software Engineering (CS4415) at TU Delft.

## Build & Run

The easiest way to get the website running locally is by building and running
the [Docker](https://docs.docker.com/get-started/) container specified in the
Dockerfile. In order to do so, you must have Docker installed on your
system. Official instructions can be found
[here](https://docs.docker.com/get-docker/), although most Linux distributions
provide a Docker package of some kind; for Arch-based distros, `pacman -S
docker docker-buildx` should do the trick.

Once you have Docker installed, run the following from the project folder:

```
docker build . -t sse-site
docker run -p 4000:4000 -v $(pwd):/myapp -it sse-site
```

The website should then be available at <http://localhost:4000/course_sustainableSE/2025/>.
