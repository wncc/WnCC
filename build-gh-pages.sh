#!/bin/bash

mkdir built
gem install jekyll
JEKYLL_ENV=production jekyll build --destination built --config _config.gh-pages.yml
