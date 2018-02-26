#!/bin/sh

set -e

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
    coreutils \
    diff-so-fancy \
    dos2unix \
    gettext \
    git \
    michaeldfallen/formula/git-radar \
    git-standup \
    gnupg\
    htop \
    httpie \
    jmeter \
    linode/cli/linode-cli \
    logstalgia \
    nettle \
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
    recime/tools/recime-cli \
    siege \
    sl \
    speedtest_cli \
    tree \
    watch \
    tig\
    tldr \
    dep \
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

cask_apps="\
    adobe-photoshop-cc \
    alfred \
    anki \
    appcleaner \
    atom \
    bartender \
    boom \
    brave \
    calibre \
    cloudup \
    diffmerge \
    docker \
    dropbox \
    evernote \
    firefox \
    flycut \
    gfxcardstatus \
    gitkraken \
    google-chrome \
    iterm2 \
    medis \
    postman \
    robomongo \
    sdformatter \
    sequel-pro \
    skype \
    slack \
    smartgit \
    spotify \
    spotify-notifications \
    sublime-text \
    vagrant \
    virtualbox \
    black-screen \
    cathode \
    charles \
    cyberduck \
    google-chrome \
    gpgtools \
    hyper \
    insomnia \
    intellij-idea \
    izip \
    keybase \
    kindle \
    kitematic \
    messenger \
    goofy \
    mongohub \
    mysqlworkbench \
    phpstorm \
    pomotodo \
    rescuetime \
    rubymine \
    skitch \
    sqlpro-for-sqlite \
    textwrangler \
    things \
    tubbler \
    unrarx \
    vagrant \
    viscosity \
    visual-studio-code \
    caskroom/versions/visual-studio-code-insiders \
    vlc \
    xmind \
    jumpcut \
    dep \
    vanilla \
"

declare -a mas_apps
declare -A mas_apps=(
    [amphetamine]=937984704
    [magnet]=441258766
    [onepassword]=443987910
    [spark]=1176895641
    [unarchiver]=425424353
    # [tweetbot]=557168941
    # [fantastical2]=975937182
)

BREW_COMMAND="brew"
CASK_COMMAND="brew cask"
MAS_COMMAND="mas"


usage_long() {
	cat << EOF
NAME
	macsetup

SYNOPSYS
	bash <(curl -s https://raw.githubusercontent.com/m4grio/macsetup/master/setup.sh)

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
            BREW_COMMAND=_brew_dryrun
            CASK_COMMAND=_cask_dryrun
            MAS_COMMAND=_mas_dryrun
            ;;
	esac
	shift
done

message() {
    tput setaf 12
    printf "~> "
    tput setaf 14
    echo "$@"
    tput sgr0
}

_brew_dryrun() {
    tput setaf 6
    echo "brew $@"
    tput sgr0
}

_cask_dryrun() {
    tput setaf 6
    echo "brew cask $@"
    tput sgr0
}

_mas_dryrun() {
    tput setaf 6
    echo "mas $@"
    tput sgr0
}

main() {
    if hash brew 2>/dev/null; then
        message Install Homebrew
        /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    fi

    message Update Brew
    $BREW_COMMAND update

    message Installing Cask
    $BREW_COMMAND tap caskroom/cask

    message Install Tooling and Packages
    $BREW_COMMAND install $brew_packages

    message Install Languages
    $BREW_COMMAND install $brew_langs

    message nstall Databases
    $BREW_COMMAND install $brew_dbs

    message Install Cask Apps
    $CASK_COMMAND install $cask_apps

    message Install Apps from Appstore
    $MAS_COMMAND install ${mas_apps[@]}

    message Cleanup Brew
    $BREW_COMMAND cleanup

    message Cleanup Cask Installs
    $BREW_COMMAND cask cleanup

    message Installing Oh My Zsh
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
}

main
