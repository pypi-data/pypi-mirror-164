#!/bin/sh
set -e

# Get branch and hash
git_hash=$(git rev-parse --short "${GITHUB_SHA}")
git_branch=${GITHUB_REF#refs/heads/}
setuppy_version=$(python --version)

echo "Commit ${git_hash} on ${git_branch}"
echo "Built with ${setuppy_version}"
