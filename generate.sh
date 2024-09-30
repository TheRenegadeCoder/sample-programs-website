#!/bin/sh
set -e

echo "*** Generate Webpages and Images ***"
python scripts/automate.py

echo ""
echo "*** Build With Jekyll ***"
# Use image that is a close to what is used for GitHub actions
export GITHUB_PAGES_IMAGE=ghcr.io/actions/jekyll-build-pages
export GITHUB_PAGES_VERSION=v1.0.13
docker run --rm \
    -v "$PWD/docs:/srv/jekyll:Z" \
    -w "/srv/jekyll" \
    -e JEKYLL_ENV=development \
    --entrypoint="" \
    -it $GITHUB_PAGES_IMAGE:$GITHUB_PAGES_VERSION \
    bash -c "rm -f Gemfile.lock && \
        bundle install && \
        chown $(id -u):$(id -g) Gemfile.lock && \
        jekyll clean --config _config.yml && \
        jekyll build -V --config _config.yml && \
        chown -R  $(id -u):$(id -g) _site"

echo ""
echo "*** Change Base URL For Generated Files ***"
LOCAL_URL=http://localhost:8000
find docs/_site -type f -name '*.html' -exec sed -i "s@https://sampleprograms\.io/@${LOCAL_URL}/@g" '{}' ';'

echo ""
echo "*** Start Webserver ***"
cd docs/_site
python -m http.server >/dev/null &
pid=$!
trap "printf '\n\n*** Kill webserver (PID %s) ***\n' $pid; \
    trap - INT HUP ABRT TERM EXIT; \
    (kill $pid || true); \
    git checkout ../languages ../projects ../index.md; \
    git clean -f ../languages ../projects" INT HUP ABRT TERM EXIT
sleep 5

echo ""
echo "*** Open Index ***"
echo "Press Ctrl+C to exit"
INDEX_URL="${LOCAL_URL}/index.html"
# Linux
if command -V xdg-open >/dev/null 2>&1
then
    xdg-open "${INDEX_URL}"
# WSL2
elif command -V explorer.exe >/dev/null 2>&1
then
    # Windows Explorer exits with invalid status
    explorer.exe "${INDEX_URL}" || true
# Mac, if failed, give up!
elif !open "${INDEX_URL}" >/dev/null 2>&1
then
    echo "Cannot open web browser."
    echo "Please open ${INDEX_URL} in your web browser."
fi

sleep infinity
