#!/bin/bash

clear
echo -e " \033[1;31;40m\  \ \033[1;97m    ______"
echo -e "  \033[1;31;40m\  \ \033[1;97m  |        \      /     /\      |\   |"
echo -e "   \033[1;31;40m\  \ \033[1;97m |______   \    /     /  \     | \  |"
echo -e "   \033[1;31;40m/  / \033[1;97m |          \  /     /____\    |  \ |"
echo -e "  \033[1;31;40m/  / \033[1;97m  |______     \/     /      \   |   \| \033[1;31;40mBy TheEthicalGuy\033[1;97m"
echo -e " \033[1;31;40m/  / \033[1;97m  "

tool_name="evan"
script_path="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"  # Dynamic script directory

echo -e "#!/bin/bash\ncd $script_path\npython3 $script_path/$tool_name.py \"\$@\"" > $tool_name
chmod +x $tool_name
sudo mv $tool_name /usr/local/bin/

if [ -f "$script_path/requirements.txt" ]; then
    echo ""
    echo -e "\033[1;32m Installing requirements..."
    # تخزين الإخراج في ملف
    pip3 install -r $script_path/requirements.txt > pip_install_output.txt 2>&1
    rm pip_install_output.txt
    sleep 5
    # التحقق من نجاح التثبيت
    if [ $? -eq 0 ]; then
        echo " done :)"
        echo -e "\033[1;97m type 'evan -h' to know how to use it"
    else
        echo -e "\033[1;31;40m there is an error occurred during installation"
    fi
else
    echo -e "\033[1;31;40m you need to reinstall the tool"
fi
