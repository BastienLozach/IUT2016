#!/bin/bash

find $1 -name '*.java' -exec cat {} + | wc -l


