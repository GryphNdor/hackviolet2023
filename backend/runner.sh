#!/bin/sh

echo "process started"
python3 google-image-scraper $1 
echo "scraping completed"
python3 [] $1
echo "faces found"