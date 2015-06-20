#!/bin/bash

set -x

tmp=$(mktemp -d)

trap cleanup EXIT
cleanup() {
    set +e
    [ -z "$tmp" -o ! -d "$tmp" ] || rm -rf "$tmp"
}

unset CDPATH
pwd=$(pwd)
date=$(date +%Y%m%d)
package=vid.stab
branch=master
name=vid.stab

pushd ${tmp}
git clone https://github.com/georgmartius/${package}.git
cd ${package}
git checkout ${branch}
tag=$(git rev-list HEAD -n 1 | cut -c 1-7)
#version=`git describe --tags | sed 's/^.//' | cut -d '-' -f 1`
version=`git describe --tags | sed 's|release-||g' | cut -d '-' -f 1`
git archive --prefix="${name}-${version}/" --format=tar master > "$pwd"/${name}-${version}-${date}-${tag}.tar
