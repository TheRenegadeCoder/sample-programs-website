#!/bin/bash
echo "*** Build With Jekyll ***"
export JEKYLL_VERSION=3.8
docker run --rm \
    -e "JEKYLL_UID=$(id -u)" \
    -e "JEKYLL_GID=$(id -g)" \
    -v "$PWD/docs:/srv/jekyll:Z" \
    -w "/srv/jekyll" \
    -it jekyll/jekyll:$JEKYLL_VERSION \
    bash -c "bundle install && jekyll build -V --config _config.yml"

echo ""
echo "*** Change Base URL For Generated Files ***"
find docs/_site -type f -name '*.html' -exec sed -i 's!https://sampleprograms\.io/!http://localhost:8000/!g' '{}' ';'

echo ""
echo "*** Start Webserver ***"
cd docs/_site
python -m http.server >/dev/null &
pid=$!
trap "printf '\n\n*** Kill webserver (PID %s) ***' $pid; kill $pid" SIGINT SIGHUP SIGABRT

echo ""
echo "*** Open Index ***"
echo "Press Ctrl+C to exit"
xdg-open "http://localhost:8000/index.html"
sleep infinity
