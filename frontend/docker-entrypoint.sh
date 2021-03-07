#!/bin/bash

set -e

echo "*** Run entry-point ***"

if [[ "$1" = "entry" ]]; then
    yarn start
    echo "Start Frontend"

elif [[ "$1" = "test" ]]; then
    # run test
    yarn install
    yarn test

elif [[ "$1" = "sleep" ]]; then
    # run infinity sleep
    exec sleep infinity

else
    # run by default
    exec "$@"
fi