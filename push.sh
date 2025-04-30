#!/bin/sh

printf "Please enter commit message: "
read commit_message

if [ -z "$commit_message" ]; then
  echo "❌ Commit message cannot be empty."
  exit 1
fi

if [ ! -d ".git" ]; then
  git init
  echo "✅ Git repository initialized."
  git remote add origin https://github.com/lyhou123/Honeyport_Simulator.git
  echo "✅ Remote repository added."
fi

# Add, commit, and push
git add .
git commit -m "$commit_message"
git branch -M main
git push -u origin main

echo "🚀 Code pushed to remote repository successfully."
