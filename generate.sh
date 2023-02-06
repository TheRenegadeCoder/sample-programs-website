#!/bin/bash
echo "*** Generate Webpages ***"
python scripts/automate.py

echo ""
echo "*** Generate Images ***"
sources=sources/images/
images=docs/assets/images/
logo=icon-small.png
for file in "$sources"*
do
    echo "- Processing ${file}"
    image-titler --path "$file" --output "$images" --logo "$images$logo"
    filename=$(basename "$file")
    edit=$(cd "$images" && ls -t | head -n1)
    mv "$images$edit" "$images$filename" 
done

echo ""
./jekyll.sh
