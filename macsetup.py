from __future__ import print_function

import sys
import subprocess

brew_packages = [
    'ansible',
    'cask',
    'homebrew/completions/brew-cask-completion',
    'dnsmasq',
    'mas',
    'wget',
    'ack',
    'autoconf',
    'automake',
    'awscli',
    'cmake',
    'coreutils',
    'diff-so-fancy',
    'dos2unix',
    'gettext',
    'git',
    'michaeldfallen/formula/git-radar',
    'git-standup',
    'gnup',
    'htop',
    'httpie',
    'jmeter',
    'linode/cli/linode-cli',
    'logstalgia',
    'nettle',
    'openssl openssl@1.1',
    'parallel',
    'pcre',
    'pidof',
    'putty',
    'pwgen',
    'python',
    'rancher-cli',
    'rbenv rbenv-bundler',
    'readline',
    'recime/tools/recime-cli',
    'siege',
    'sl',
    'speedtest_cli',
    'tree',
    'watch',
    'ti',
    'tldr',
    'dep',
]

brew_langs = [
    'go',
    'erlang',
    'elixir',
    'php',
    'php70',
    'php70-xdebug',
    'node',
]

brew_dbs = [
    'elasticsearch23',
    'mariadb100',
    'mongodb',
    'postgresql',
    'redis',
    'sqlite',
]

cask_apps = [
    'adobe-photoshop-cc',
    'alfred',
    'anki',
    'appcleaner',
    'atom',
    'bartender',
    'boom',
    'brave',
    'calibre',
    'cloudup',
    'diffmerge',
    'docker',
    'dropbox',
    'evernote',
    'firefox',
    'flycut',
    'gfxcardstatus',
    'gitkraken',
    'google-chrome',
    'iterm2',
    'medis',
    'postman',
    'robomongo',
    'sdformatter',
    'sequel-pro',
    'skype',
    'slack',
    'smartgit',
    'spotify',
    'spotify-notifications',
    'sublime-text',
    'vagrant',
    'virtualbox',
    'black-screen',
    'cathode',
    'charles',
    'cyberduck',
    'google-chrome',
    'gpgtools',
    'hyper',
    'insomnia',
    'intellij-idea',
    'izip',
    'keybase',
    'kindle',
    'kitematic',
    'messenger',
    'goofy',
    'mongohub',
    'mysqlworkbench',
    'phpstorm',
    'pomotodo',
    'rescuetime',
    'rubymine',
    'skitch',
    'sqlpro-for-sqlite',
    'textwrangler',
    'things',
    'tubbler',
    'unrarx',
    'vagrant',
    'viscosity',
    'visual-studio-code',
    'caskroom/versions/visual-studio-code-insiders',
    'vlc',
    'xmind',
    'jumpcut',
    'dep',
    'vanilla',
]

mas_apps = [
    '937984704',  # amphetamine
    '441258766',  # magnet
    '443987910',  # onepassword
    '1176895641', # spark
    '425424353',  # unarchiver
    # '557168941',  # tweetbot
    # '975937182',  # fantastical2
]

class Program:
    dry_run = False
    dry_run_program = 'echo'

    def __init__(self, argv=[]):
        self.dry_run = '-d' in argv

    def install(self, args):
        return "{dry_run_program} {install_program} install {args}".format(**dict(
            dry_run_program='echo' if self.dry_run else '',
            install_program=self.install_program,
            args=' '.join(x for x in args)
        ))

class Brew(Program):
    install_program = 'brew'

class Cask(Program):
    install_program = 'brew cask'

class Mas(Program):
    install_program = 'mas'

class Flags:
    dry_run=False
    brew_packages=True
    brew_langs=True
    brew_dbs=True
    cask_apps=True
    mas_apps=True

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def message(message='', color=Colors.HEADER):
    message = "{color}~> {message}".format(**dict(
        color=color,
        message=message,
    )) + Colors.ENDC
    print(message)

def set_flags(argv=[]):
    Flags.dry_run       = '-d' in argv
    Flags.brew_packages = not '--no-packages' in argv
    Flags.brew_langs    = not '--no-languages' in argv
    Flags.brew_dbs      = not '--no-dbs' in argv
    Flags.cask_apps     = not '--no-apps' in argv
    Flags.mas_apps      = not '--no-mas' in argv


def print_help_and_exit():
    print("""
NAME
	macsetup.py

SYNOPSYS
	python <(curl -s https://raw.githubusercontent.com/m4grio/macsetup/master/macsetup.py)

DESCRIPTION
	Installs good stuff in your shiny new Mac.

OPTIONS
	-d/--dry-run     Echo commands rather than running them
	--no-packages    Do not install any package from Homebrew
	--no-languages   Do not install any programming language
	--no-dbs         Do not install any databases
	--no-apps        Do not install any application from Caskroom
	--no-mas         Do not install any application from App Store
    """)
    sys.exit(0)


if __name__ == '__main__':

    if subprocess.call("hash brew 2> /dev/null", shell=True):
        message("Installing Homebrew...")
        subprocess.call('/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"')

    set_flags(sys.argv)

    if any(x in ['-h', '--h', '--help'] for x in sys.argv):
        print_help_and_exit()

    message("Updating Brew...")
    subprocess.call(Brew(sys.argv).install(brew_packages), shell=True)
