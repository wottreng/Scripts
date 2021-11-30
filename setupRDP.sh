sudo apt install xrdp xorgxrdp -y
echo env -u SESSION_MANAGER -u DBUS_SESSION_BUS_ADDRESS cinnamon-session>~/.xsession
# connect to rdp with Remmina app: sudo apt install Remmina
# allow firewall opening: sudo ufw allow 3389
