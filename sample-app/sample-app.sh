#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
ART_DIR="$REPO_ROOT/artifacts/day4/docker"

mkdir -p "$ART_DIR"

cd "$SCRIPT_DIR"

rm -rf tempdir
mkdir -p tempdir/templates tempdir/static

cp sample_app.py tempdir/.
cp -r templates/. tempdir/templates/.
cp -r static/. tempdir/static/.

echo "FROM python:3.11-slim" > tempdir/Dockerfile
echo "RUN pip install --no-cache-dir --progress-bar off flask" >> tempdir/Dockerfile
echo "COPY ./static /home/myapp/static/" >> tempdir/Dockerfile
echo "COPY ./templates /home/myapp/templates/" >> tempdir/Dockerfile
echo "COPY sample_app.py /home/myapp/" >> tempdir/Dockerfile
echo "EXPOSE 5050" >> tempdir/Dockerfile
echo 'CMD ["python3", "/home/myapp/sample_app.py"]' >> tempdir/Dockerfile

docker rm -f samplerunning 2>/dev/null || true
docker rmi sampleapp:day4 2>/dev/null || true

cd tempdir
docker build -t sampleapp:day4 . | tee "$ART_DIR/sampleapp_build_log.txt"
docker run -t -d -p 5050:5050 -e STUDENT_TOKEN="${STUDENT_TOKEN:-}" --name samplerunning sampleapp:day4
docker ps --no-trunc | tee "$ART_DIR/sampleapp_docker_ps.txt"
