from __future__ import print_function

import sys
import subprocess

taps = [
    'caskroom/cask',
    'caskroom/versions',
    'linode/cli',
    'michaeldfallen/formula',
    'recime/tools',
]

brew_packages = [
    'ansible',
    'cask',
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
    'git-radar',
    'git-standup',
    'gnupg',
    'htop',
    'httpie',
    'jmeter',
    'linode-cli',
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
    'recime-cli',
    'siege',
    'sl',
    'speedtest_cli',
    'tree',
    'watch',
    'tig',
    'tldr',
    'dep',
]

brew_langs = [
    'go',
    'erlang',
    'elixir',
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
    'gpg-suite',
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
    'visual-studio-code-insiders',
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
        return "{dry_run_program} {binary} install {args}".format(**dict(
            dry_run_program='echo' if self.dry_run else '',
            binary=self.binary,
            args=' '.join(x for x in args)
        ))

class Brew(Program):
    binary = 'brew'

    def tap(self, args):
        return "{dry_run_program} {binary} tap {args}".format(**dict(
            dry_run_program='echo' if self.dry_run else '',
            binary=self.binary,
            args=' '.join(x for x in args)
        ))

    def update(self):
        return "{dry_run_program} {binary} update".format(**dict(
            dry_run_program='echo' if self.dry_run else '',
            binary=self.binary,
        ))

class Cask(Program):
    binary = 'brew cask'

class Mas(Program):
    binary = 'mas'

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
    Flags.brew_langs    = not '--no-langs' in argv
    Flags.brew_dbs      = not '--no-dbs' in argv
    Flags.cask_apps     = not '--no-apps' in argv
    Flags.mas_apps      = not '--no-mas' in argv


def print_help_and_exit():
    print("""
NAME
	setup.py

SYNOPSYS
	python <(curl -s https://raw.githubusercontent.com/m4grio/macsetup/master/setup.py)

DESCRIPTION
	Install good stuff in your shiny new Mac.

OPTIONS
	-d/--dry-run     Echo commands rather than running them
	--no-packages    Do not install any package from Homebrew
	--no-langs       Do not install any programming language
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

    brew = Brew(sys.argv)

    message("Updating Brew...")
    subprocess.call(brew.update(), shell=True)

    message("Tapping...")
    subprocess.call(brew.tap(taps), shell=True)

    if Flags.brew_packages:
        message("Installing packages...")
        subprocess.call(brew.install(brew_packages), shell=True)

    if Flags.brew_langs:
        message("Installing languages...")
        subprocess.call(brew.install(brew_langs), shell=True)

    if Flags.brew_dbs:
        message("Installing databases...")
        subprocess.call(brew.install(brew_dbs), shell=True)

    if Flags.cask_apps:
        message("Installing applications from Caskroom...")
        subprocess.call(Cask(sys.argv).install(cask_apps), shell=True)

    if Flags.mas_apps:
        message("Installing applications from App Store...")
        subprocess.call(Mas(sys.argv).install(mas_apps), shell=True)
