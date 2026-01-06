#!/bin/bash

RED="\033[1;31m"
GREEN="\033[1;32m"
BLUE="\033[1;34m"
YELLOW="\033[1;33m"
RESET="\033[0m"

clear
echo -e "${BLUE}==============================="
echo -e "        RAMclean Installer      "
echo -e "===============================${RESET}"
echo ""

if [ "$EUID" -ne 0 ]; then
  echo -e "${YELLOW}This script needs sudo. Run it as:"
  echo "sudo ./install.sh"
  exit 1
fi

SCRIPT_PATH="/usr/local/bin/ramclean-dropcache"

echo -e "${GREEN}Creating RAMclean script...${RESET}"
cat << 'EOF' > "$SCRIPT_PATH"
#!/bin/sh
sync
echo 3 > /proc/sys/vm/drop_caches
EOF

echo -e "${GREEN}Setting permissions...${RESET}"
chown root:root "$SCRIPT_PATH"
chmod 755 "$SCRIPT_PATH"

echo -e "${BLUE}Final file status:${RESET}"
ls -l "$SCRIPT_PATH"

echo ""
echo -e "${GREEN}Installation completed successfully!${RESET}"
echo -e "${YELLOW}You can now run RAMclean.py and press Clean RAM.${RESET}"
echo ""
