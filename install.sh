#!/bin/bash

# OpenClaw Wikipedia Skill Installation Script

echo "Installing OpenClaw Wikipedia Skill..."

# Check if running in OpenClaw environment
if [ -z "$OPENCLAW_WORKSPACE" ]; then
    echo "Warning: OPENCLAW_WORKSPACE environment variable not set."
    echo "Please ensure you're running this in an OpenClaw environment."
fi

# Get the user's OpenClaw workspace directory
WORKSPACE_DIR="${OPENCLAW_WORKSPACE:-$HOME/.openclaw/workspace}"

# Create skills directory if it doesn't exist
SKILLS_DIR="$WORKSPACE_DIR/skills"
mkdir -p "$SKILLS_DIR"

# Copy the skill to the skills directory
SKILL_SRC="./skills/wikipedia"
SKILL_DST="$SKILLS_DIR/wikipedia"

if [ -d "$SKILL_DST" ]; then
    echo "Updating existing Wikipedia skill..."
    rm -rf "$SKILL_DST"
else
    echo "Installing Wikipedia skill..."
fi

cp -r "$SKILL_SRC" "$SKILL_DST"

# Install Python dependencies
echo "Installing Python dependencies..."
pip3 install requests

echo "Installation completed!"
echo ""
echo "To verify the installation:"
echo "python3 $SKILL_DST/scripts/search.py \"test\" --lang en"
echo ""
echo "For more information, check the README.md file."