# INTRODUCTION

This is a basic [Flask](http://flask.pocoo.org) (Python microframework) boilerplate starter for my dokku deployments. I use it for quickly bootstrap a small app and prototype without having to structure my app.

It is based on the [Fbone](https://github.com/imwilsonxu/fbone) for the best practices and app structure. 

Feel free to use it and start your own Flask projects!


## FEATURES
- [bootstrap3] (https://github.com/twitter/bootstrap).


## Problem Install mysql-python on new mac

Error

   clang: error: unknown argument: '-mno-fused-madd' [-Wunused-command-line-argument-hard-error-in-future]

Fix   
   
   export ARCHFLAGS="-Wno-error=unused-command-line-argument-hard-error-in-future"
   

## Start (Local setup)

    virtualenv .pyenv
    source .pyenv/bin/activate
    


## Deploy

This is deployed with gunicorn. 