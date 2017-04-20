#!/bin/sh

set -xe

BREW_COMMAND=brew


usage_long() {
	cat << EOF
NAME
	macsetup

SYNOPSYS
	bash <(curl -s https://raw.githubusercontent.com/<username>/macsetup/master/setup.sh)

DESCRIPTION
	Installs good stuff in your shiny new mac.

OPTIONS
	-d/--dry-run	Echoes commands rather than running them
EOF
exit 0
}

while test $# != 0
do
	case "$1" in
		-h|--h|--he|--hel|--help|help)
			usage_long
			;;
		-d|--dry-run*)
            BREW_COMMAND=echo
		*)
			# Pass thru anything that may be meant for fetch.
			[ -n "$1" ] && FILE=$1
			;;
	esac
	shift
done
main

echo ------------- Install Homebrew -------------
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

echo ------------- Update Brew -------------
$BREW_COMMAND update

echo ------------- Installing Cask -------------
$BREW_COMMAND tap caskroom/cask

brew_packages="\
    ansible \
    cask \
    homebrew/completions/brew-cask-completion \
    dnsmasq \
    mas \
    wget \
    ack \
    autoconf \
    automake \
    awscli \
    cmake \
    composer \
    coreutils \
    delve \
    diff-so-fancy \
    dos2unix \
    gettext \
    git \
    git-radar \
    git-standup \
    gnupg\
    htop \
    docker \
    jmeter \
    linode-cli \
    logstalgia \
    maven \
    nettle \
    nmap \
    openssl openssl@1.1 \
    parallel \
    pcre \
    pidof \
    putty \
    pwgen \
    python \
    rancher-cli \
    rbenv rbenv-bundler \
    readline \
    recime-cli \
    siege \
    sl \
    speedtest_cli \
    tree \
    watch \
    yarn \
"
brew_langs="\
    go \
    erlang \
    elixir \
    php \
    php70 \
    php70-xdebug \
    node \
"

brew_dbs="\
    elasticsearch23 \
    mariadb100 \
    mongodb \
    postgresql \
    redis \
    sqlite \
"
echo ------------- Install Tooling and Packages -------------
$BREW_COMMAND install $brew_packages

echo ------------- Install Languages -------------
$BREW_COMMAND install $brew_langs

echo ------------- Install Databases -------------
$BREW_COMMAND install $brew_dbs


echo ------------- Install Cask Apps -------------
# brew cask install alfred
# brew cask install anki
# brew cask install appcleaner
# brew cask install atom
# brew cask install bartender
# brew cask install calibre
# brew cask install cloudup
# brew cask install diffmerge
# brew cask install docker
# brew cask install dropbox
# brew cask install evernote
# brew cask install firefox
# brew cask install flycut
# brew cask install gfxcardstatus
# brew cask install gitkraken
# brew cask install google-chrome
# brew cask install iterm2
# brew cask install medis
# brew cask install postman
# brew cask install robomongo
# brew cask install sdformatter
# brew cask install sequel-pro
# brew cask install skype
# brew cask install slack
# brew cask install smartgit
# brew cask install spotify
# brew cask install spotify-notifications
# brew cask install sublime-text
# brew cask install vagrant
# brew cask install virtualbox


echo  ------------- Install Apps from Appstore -------------
# #Magnet
# mas install 441258766
# #ColorSnapper2
# mas install 969418666
# #1password
# mas install 443987910
# #Reeder
# mas install 880001334
# #Pages
# mas install 409201541
# #Spark
# mas install 1176895641
# #The Unarchiver
# mas install 425424353
# #Fantastical 2
# mas install 975937182
# #Tweetbot
# mas install 557168941

echo ------------- Cleanup Brew -------------
$BREW_COMMAND cleanup

echo ------------- Cleanup Cask Installs -------------
$BREW_COMMAND cask cleanup

echo ------------- Installing Oh My Zsh
# sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
