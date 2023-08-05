#! /bin/bash

# Determine sudo
if hash "sudo" &>/dev/null; then
    sudo="sudo"
else
    sudo=""
fi

os=$(uname)
if [[ ! $os == "Linux" ]] && [[ ! $os == "Darwin" ]]; then
    echo "This script does not support this OS."
    echo "Try consulting https://github.com/hyunwoongko/python-mecab-kor/issues"
    exit 0
fi

install_requirements(){
    # TODO: if not [automake --version]
    if [ "$os" == "Linux" ]; then
        if [ "$(grep -Ei 'debian|buntu|mint' /etc/*release)" ]; then
            $sudo apt-get update && $sudo apt-get install -y build-essential curl python3-devel git
        elif [ "$(grep -Ei 'fedora|redhat' /etc/*release)" ]; then
            $sudo yum groupinstall -y 'Development Tools' && $sudo yum install -y curl python3-devel git
        fi
    elif [ "$os" == "Darwin" ]; then
        if [[ $(command -v brew) == "" ]]; then
            echo "This script require Homebrew!"
            echo "Try https://brew.sh/"
            exit 0
        fi
        if [[ $(uname -m) == 'arm64' ]]; then
          arch -arm64 brew install curl
        else
          brew install curl
        if
    fi
}

install_requirements