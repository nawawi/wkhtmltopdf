#!/usr/bin/env python
#
# Copyright 2014 wkhtmltopdf authors
#
# This file is part of wkhtmltopdf.
#
# wkhtmltopdf is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# wkhtmltopdf is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with wkhtmltopdf.  If not, see <http:#www.gnu.org/licenses/>.

# --------------------------------------------------------------- CONFIGURATION

QT5_URL = 'https://github.com/qtproject/qt5.git'
OPENSSL = {
    'repository': 'https://github.com/openssl/openssl.git',
    'branch'    : 'OpenSSL_1_0_1-stable',
    'tag'       : 'OpenSSL_1_0_1g',
    'build'     : {
        'msvc*-win32*': {
            'configure' : 'VC-WIN32 no-asm',
            'debug'     : 'debug-VC-WIN32 no-asm',
            'build'     : ['ms\\do_ms.bat', 'nmake /f ms\\nt.mak install'],
            'libs'      : ['ssleay32.lib', 'libeay32.lib'],
            'os_libs'   : '-lUser32 -lAdvapi32 -lGdi32 -lCrypt32'
        },
        'msvc*-win64*': {
            'configure' : 'VC-WIN64A',
            'debug'     : 'debug-VC-WIN64A',
            'build'     : ['ms\\do_win64a.bat', 'nmake /f ms\\nt.mak install'],
            'libs'      : ['ssleay32.lib', 'libeay32.lib'],
            'os_libs'   : '-lUser32 -lAdvapi32 -lGdi32 -lCrypt32'
        },
        'mingw-w64-cross-win32': {
            'configure' : '--cross-compile-prefix=i686-w64-mingw32- no-shared no-asm mingw64',
            'build'     : ['make', 'make install_sw'],
            'libs'      : ['libssl.a', 'libcrypto.a'],
            'os_libs'   : '-lws2_32 -lgdi32 -lcrypt32'
        },
        'mingw-w64-cross-win64': {
            'configure' : '--cross-compile-prefix=x86_64-w64-mingw32- no-shared no-asm mingw64',
            'build'     : ['make', 'make install_sw'],
            'libs'      : ['libssl.a', 'libcrypto.a'],
            'os_libs'   : '-lws2_32 -lgdi32 -lcrypt32'
        }
    }
}

QT_CONFIG = {
    'common' : [
        '-opensource',
        '-confirm-license',
        '-fast',
        '-release',
        '-static',
        '-graphicssystem raster',
        '-no-script',
        '-no-webkit',
        '-exceptions',              # required by XmlPatterns
        '-xmlpatterns',             # required for TOC support
        '-qt-zlib',                 # use bundled versions of libraries
        '-qt-libpng',
        '-qt-libjpeg',
        '-no-libmng',
        '-no-libtiff',
        '-no-accessibility',
        '-no-stl',
        '-no-qt3support',
        '-no-phonon',
        '-no-phonon-backend',
        '-no-opengl',
        '-no-declarative',
        '-no-scripttools',
        '-no-sql-ibase',
        '-no-sql-mysql',
        '-no-sql-odbc',
        '-no-sql-psql',
        '-no-sql-sqlite',
        '-no-sql-sqlite2',
        '-no-mmx',
        '-no-3dnow',
        '-no-sse',
        '-no-sse2',
        '-no-multimedia',
        '-nomake demos',
        '-nomake docs',
        '-nomake examples',
        '-nomake tools',
        '-nomake tests',
        '-nomake translations'
    ],

    'msvc': [
        '-mp',
        '-qt-style-windows',
        '-qt-style-cleanlooks',
        '-no-style-windowsxp',
        '-no-style-windowsvista',
        '-no-style-plastique',
        '-no-style-motif',
        '-no-style-cde',
        '-openssl-linked'           # static linkage for OpenSSL
    ],

    'posix': [
        '-silent',                  # perform a silent build
        '-xrender',                 # xrender support is required
        '-largefile',
        '-rpath',
        '-openssl',                 # load OpenSSL binaries at runtime
        '-no-dbus',
        '-no-nis',
        '-no-cups',
        '-no-iconv',
        '-no-pch',
        '-no-gtkstyle',
        '-no-nas-sound',
        '-no-sm',
        '-no-xshape',
        '-no-xinerama',
        '-no-xcursor',
        '-no-xfixes',
        '-no-xrandr',
        '-no-mitshm',
        '-no-xinput',
        '-no-xkb',
        '-no-glib',
        '-no-gstreamer',
        '-D ENABLE_VIDEO=0',        # required as otherwise gstreamer gets linked in
        '-no-openvg',
        '-no-xsync',
        '-no-audio-backend',
        '-no-sse3',
        '-no-ssse3',
        '-no-sse4.1',
        '-no-sse4.2',
        '-no-avx',
        '-no-neon'
    ],

    'mingw-w64-cross' : [
        '-silent',                  # perform a silent build
        '-openssl-linked',          # static linkage for OpenSSL
        '-no-reduce-exports',
        '-no-rpath',
        '-xplatform win32-g++-4.6'
    ]
}

WEBKIT_CONFIG = {
    'common' : [
        '--qt',
        '--release',
        '--qmakearg="CONFIG+=static"',
        '--qmakearg="CONFIG+=production_build"',
        '--qmakearg="CONFIG+=use_all_in_one_files"',
        '--qmakearg="DEFINES+=Q_NODLL"',
        '--qmakearg="DEFINES+=STATIC"',
        '--qmakearg="DEFINES+=QT_STATIC"',
        '--qmakearg="DEFINES+=WTF_USE_3D_GRAPHICS=0"',
        '--no-webkit2',
        '--no-3d-rendering',
        '--no-webgl',
        '--no-gamepad',
        '--no-video',
        '--no-xslt',
        '--no-force-sse2',
        '--no-inspector',
        '--no-javascript-debugger',
        '--no-sql-database',
        '--no-netscape-plugin-api'
    ],

    'msvc2010': [
        '--qmakearg="QMAKE_CXXFLAGS+=/MP"',
        '--qmakearg="QMAKE_CFLAGS+=/MP"'
    ],

    'mingw-w64-cross' : [
        '--qmakearg="CONFIG+=silent"',
        '--qmakearg="QMAKE_CXXFLAGS+=-Wno-c++0x-compat"'
    ],

    'posix' : [
        '--qmakearg="CONFIG+=silent"',
        '--qmakearg="QT_CONFIG+=no-pkg-config"',            # disables HAVE_SQLITE3=1
        '--qmakearg="DEFINES+=WTF_USE_LIBJPEG=0"',
        '--qmakearg="DEFINES+=WTF_USE_LIBPNG=0"',
        '--qmakearg="DEFINES+=WTF_USE_ZLIB=0"'
    ]
}

BUILDERS = {
    'msvc2008-win32':        'msvc',
    'msvc2008-win64':        'msvc',
    'msvc2010-win32':        'msvc',
    'msvc2010-win64':        'msvc',
    'msvc2012-win32':        'msvc',
    'msvc2012-win64':        'msvc',
    'msvc2013-win32':        'msvc',
    'msvc2013-win64':        'msvc',
    'msvc-winsdk71-win32':   'msvc_winsdk71',
    'msvc-winsdk71-win64':   'msvc_winsdk71',
    'setup-mingw-w64':       'setup_mingw64',
    'setup-schroot-centos5': 'setup_schroot',
    'setup-schroot-centos6': 'setup_schroot',
    'setup-schroot-wheezy':  'setup_schroot',
    'setup-schroot-trusty':  'setup_schroot',
    'setup-schroot-precise': 'setup_schroot',
    'update-all-schroots':   'update_schroot',
    'centos5-i386':          'linux_schroot',
    'centos5-amd64':         'linux_schroot',
    'centos6-i386':          'linux_schroot',
    'centos6-amd64':         'linux_schroot',
    'wheezy-i386':           'linux_schroot',
    'wheezy-amd64':          'linux_schroot',
    'trusty-i386':           'linux_schroot',
    'trusty-amd64':          'linux_schroot',
    'precise-i386':          'linux_schroot',
    'precise-amd64':         'linux_schroot',
    'mingw-w64-cross-win32': 'mingw64_cross',
    'mingw-w64-cross-win64': 'mingw64_cross'
}

CHROOT_SETUP  = {
    'wheezy': [
        ('debootstrap', 'wheezy', 'http://ftp.us.debian.org/debian/'),
        ('write_file', 'etc/apt/sources.list', """
deb     http://ftp.debian.org/debian/ wheezy         main contrib non-free
deb     http://ftp.debian.org/debian/ wheezy-updates main contrib non-free
deb     http://security.debian.org/   wheezy/updates main contrib non-free
deb-src http://ftp.debian.org/debian/ wheezy         main contrib non-free
deb-src http://ftp.debian.org/debian/ wheezy-updates main contrib non-free
deb-src http://security.debian.org/   wheezy/updates main contrib non-free"""),
        ('shell', 'apt-get update'),
        ('shell', 'apt-get dist-upgrade --assume-yes'),
        ('shell', 'apt-get install --assume-yes xz-utils'),
        ('shell', 'apt-get build-dep --assume-yes libqt4-core'),
        ('write_file', 'update.sh', 'apt-get update\napt-get dist-upgrade --assume-yes\n'),
        ('schroot_conf', 'Debian Wheezy')
    ],

    'trusty': [
        ('debootstrap', 'trusty', 'http://archive.ubuntu.com/ubuntu/'),
        ('write_file', 'etc/apt/sources.list', """
deb     http://archive.ubuntu.com/ubuntu/ trusty          main restricted universe multiverse
deb     http://archive.ubuntu.com/ubuntu/ trusty-updates  main restricted universe multiverse
deb     http://archive.ubuntu.com/ubuntu/ trusty-security main restricted universe multiverse
deb-src http://archive.ubuntu.com/ubuntu/ trusty          main restricted universe multiverse
deb-src http://archive.ubuntu.com/ubuntu/ trusty-updates  main restricted universe multiverse
deb-src http://archive.ubuntu.com/ubuntu/ trusty-security main restricted universe multiverse"""),
        ('shell', 'apt-get update'),
        ('shell', 'apt-get dist-upgrade --assume-yes'),
        ('shell', 'apt-get install --assume-yes xz-utils'),
        ('shell', 'apt-get build-dep --assume-yes libqt4-core'),
        ('write_file', 'update.sh', 'apt-get update\napt-get dist-upgrade --assume-yes\n'),
        ('schroot_conf', 'Ubuntu Trusty')
    ],

    'precise': [
        ('debootstrap', 'precise', 'http://archive.ubuntu.com/ubuntu/'),
        ('write_file', 'etc/apt/sources.list', """
deb     http://archive.ubuntu.com/ubuntu/ precise          main restricted universe multiverse
deb     http://archive.ubuntu.com/ubuntu/ precise-updates  main restricted universe multiverse
deb     http://archive.ubuntu.com/ubuntu/ precise-security main restricted universe multiverse
deb-src http://archive.ubuntu.com/ubuntu/ precise          main restricted universe multiverse
deb-src http://archive.ubuntu.com/ubuntu/ precise-updates  main restricted universe multiverse
deb-src http://archive.ubuntu.com/ubuntu/ precise-security main restricted universe multiverse"""),
        ('shell', 'apt-get update'),
        ('shell', 'apt-get dist-upgrade --assume-yes'),
        ('shell', 'apt-get install --assume-yes xz-utils'),
        ('shell', 'apt-get build-dep --assume-yes libqt4-core'),
        ('write_file', 'update.sh', 'apt-get update\napt-get dist-upgrade --assume-yes\n'),
        ('schroot_conf', 'Ubuntu Precise')
    ],

    'centos5': [
        ('rinse', 'centos-5'),
        ('shell', 'yum update -y'),
        ('append_file:amd64', 'etc/yum.conf', 'exclude = *.i?86\n'),
        ('shell', 'yum install -y gcc gcc-c++ make qt4-devel openssl-devel diffutils perl xz'),
        ('write_file', 'update.sh', 'yum update -y\n'),
        ('schroot_conf', 'CentOS 5')
    ],

    'centos6': [
        ('rinse', 'centos-6'),
        ('shell', 'yum update -y'),
        ('append_file:amd64', 'etc/yum.conf', 'exclude = *.i?86\n'),
        ('shell', 'yum install -y gcc gcc-c++ make qt4-devel openssl-devel diffutils perl tar xz'),
        ('write_file', 'update.sh', 'yum update -y\n'),
        ('schroot_conf', 'CentOS 6')
    ]
}

# --------------------------------------------------------------- HELPERS

import os, sys, platform, subprocess, shutil, re, fnmatch, multiprocessing

from os.path import exists

CPU_COUNT = max(2, multiprocessing.cpu_count()-1)   # leave one CPU free

def rchop(s, e):
    if s.endswith(e):
        return s[:-len(e)]
    return s

def error(msg):
    print msg
    sys.exit(1)

def shell(cmd):
    ret = os.system(cmd)
    if ret != 0:
        error("command failed: exit code %d" % ret)

def get_output(*cmd):
    try:
        return subprocess.check_output(cmd, stderr=subprocess.STDOUT).strip()
    except subprocess.CalledProcessError:
        return None

def rmdir(path):
    if exists(path):
        shutil.rmtree(path)

def mkdir_p(path):
    if not exists(path):
        os.makedirs(path)

def get_version(basedir):
    text = open(os.path.join(basedir, '..', 'VERSION'), 'r').read()
    if '-' not in text:
        return (text, text)
    version = text[:text.index('-')]
    os.chdir(os.path.join(basedir, '..'))
    hash = get_output('git', 'rev-parse', '--short', 'HEAD')
    if not hash:
        return (text, version)
    return ('%s-%s' % (version, hash), version)

def build_openssl(config, basedir):
    cfg = None
    for key in OPENSSL['build']:
        if fnmatch.fnmatch(config, key):
            cfg = key

    if not cfg:
        return

    srcdir = os.path.join(basedir, 'openssl')
    dstdir = os.path.join(basedir, config, 'openssl')

    def is_compiled():
        compiled = exists(os.path.join(dstdir, 'include', 'openssl', 'ssl.h'))
        for lib in OPENSSL['build'][cfg]['libs']:
            compiled = compiled and exists(os.path.join(dstdir, 'lib', lib))
        return compiled

    if not exists(os.path.join(srcdir, '.git')):
        rmdir(srcdir)
        rmdir(dstdir)
        os.chdir(basedir)
        shell('git clone --branch %s --single-branch %s openssl' % (OPENSSL['branch'], OPENSSL['repository']))

    os.chdir(srcdir)
    shell('git clean -fdx')
    shell('git reset --hard HEAD')
    shell('git checkout %s' % (OPENSSL['tag']))

    if not is_compiled():
        opts = OPENSSL['build'][cfg]
        shell('perl Configure --openssldir=%s %s' % (dstdir, opts['configure']))
        for cmd in opts['build']:
            shell(cmd)
        shell('git clean -fdx')
        if not is_compiled():
            error("Unable to compile OpenSSL for your system, aborting.")

    return OPENSSL['build'][cfg]['os_libs']

def check_running_on_debian():
    if not sys.platform.startswith('linux') or not exists('/etc/apt/sources.list'):
        error('This can only be run on a Debian/Ubuntu distribution, aborting.')

    if os.geteuid() != 0:
        error('This script must be run as root.')

    if platform.architecture()[0] == '64bit' and 'amd64' not in ARCH:
        ARCH.insert(0, 'amd64')

PACKAGE_NAME = re.compile(r'ii\s+(.+?)\s+.*')
def install_packages(*names):
    lines = get_output('dpkg-query', '--list', *names).split('\n')
    avail = [PACKAGE_NAME.match(line).group(1) for line in lines if PACKAGE_NAME.match(line)]

    if len(avail) != len(names):
        shell('apt-get update')
        shell('apt-get install --assume-yes %s' % (' '.join(names)))

# --------------------------------------------------------------- Linux chroot

ARCH = ['i386']

def check_setup_schroot(config):
    check_running_on_debian()
    login = get_output('logname')
    if not login:
        error('Unable to determine the login for which schroot access is to be given.')

    if login == 'root':
        error('Please run via sudo to determine login for which schroot access is to be given.')

def build_setup_schroot(config, basedir):
    install_packages('git', 'debootstrap', 'schroot', 'rinse')

    login  = get_output('logname')
    chroot = config[1+config.rindex('-'):]
    for arch in ARCH:
        print '******************* %s-%s' % (chroot, arch)
        root_dir = '/opt/wkhtmltopdf-build/%s-%s' % (chroot, arch)
        rmdir(root_dir)
        mkdir_p(root_dir)
        for command in CHROOT_SETUP[chroot]:
            # handle architecture-specific commands
            name = command[0]
            if ':' in name:
                if name[1+name.rindex(':'):] != arch:
                    continue
                else:
                    name = name[:name.rindex(':')]

            # handle commands
            if name == 'debootstrap':
                shell('debootstrap --arch=%(arch)s --variant=buildd %(distro)s %(dir)s %(url)s' % {
                    'arch': arch, 'dir': root_dir, 'distro': command[1], 'url': command[2] })
            elif name == 'rinse':
                cmd = (arch == 'i386' and 'linux32 rinse' or 'rinse')
                shell('%s --arch %s --distribution %s --directory %s' % (cmd, arch, command[1], root_dir))
            elif name == 'shell':
                cmd = (arch == 'i386' and 'linux32 chroot' or 'chroot')
                shell('%s %s %s' % (cmd, root_dir, command[1]))
            elif name == 'write_file':
                open(os.path.join(root_dir, command[1]), 'w').write(command[2].strip())
            elif name == 'append_file':
                open(os.path.join(root_dir, command[1]), 'a').write(command[2].strip())
            elif name == 'schroot_conf':
                cfg = open('/etc/schroot/chroot.d/wkhtmltopdf-%s-%s' % (chroot, arch), 'w')
                cfg.write('[wkhtmltopdf-%s-%s]\n' % (chroot, arch))
                cfg.write('type=directory\ndirectory=%s/\n' % root_dir)
                cfg.write('description=%s %s for wkhtmltopdf\n' % (command[1], arch))
                cfg.write('users=%s\nroot-users=root\n' % login)
                if arch == 'i386' and 'amd64' in ARCH:
                    cfg.write('personality=linux32\n')
                cfg.close()

def check_update_schroot(config):
    check_running_on_debian()
    if not get_output('schroot', '--list'):
        error('Unable to determine the list of available schroots.')

def build_update_schroot(config, basedir):
    for name in get_output('schroot', '--list').split('\n'):
        print '******************* %s' % name[name.index('wkhtmltopdf-'):]
        shell('schroot -c %s -- /bin/bash /update.sh' % name[name.index('wkhtmltopdf-'):])

def check_setup_mingw64(config):
    check_running_on_debian()

def build_setup_mingw64(config, basedir):
    install_packages('build-essential', 'mingw-w64', 'nsis')

# --------------------------------------------------------------- MSVC (2008-2013)

MSVC_LOCATION = {
    'msvc2008': 'VS90COMNTOOLS',
    'msvc2010': 'VS100COMNTOOLS',
    'msvc2012': 'VS110COMNTOOLS',
    'msvc2013': 'VS120COMNTOOLS'
}

def check_msvc(config):
    version, arch = rchop(config, '-dbg').split('-')
    env_var = MSVC_LOCATION[version]
    if not env_var in os.environ:
        error("%s does not seem to be installed." % version)

    vcdir = os.path.join(os.environ[env_var], '..', '..', 'VC')
    if not exists(os.path.join(vcdir, 'vcvarsall.bat')):
        error("%s: unable to find vcvarsall.bat" % version)

    if arch == 'win32' and not exists(os.path.join(vcdir, 'bin', 'cl.exe')):
        error("%s: unable to find the x86 compiler" % version)

    if arch == 'win64' and not exists(os.path.join(vcdir, 'bin', 'amd64', 'cl.exe')) \
                       and not exists(os.path.join(vcdir, 'bin', 'x86_amd64', 'cl.exe')):
        error("%s: unable to find the amd64 compiler" % version)

def build_msvc(config, basedir):
    msvc, arch = rchop(config, '-dbg').split('-')
    vcdir = os.path.join(os.environ[MSVC_LOCATION[msvc]], '..', '..', 'VC')
    vcarg = 'x86'
    if arch == 'win64':
        if exists(os.path.join(vcdir, 'bin', 'amd64', 'cl.exe')):
            vcarg = 'amd64'
        else:
            vcarg = 'x86_amd64'

    python = sys.executable
    process = subprocess.Popen('("%s" %s>nul)&&"%s" -c "import os; print repr(os.environ)"' % (
        os.path.join(vcdir, 'vcvarsall.bat'), vcarg, python), stdout=subprocess.PIPE, shell=True)
    stdout, _ = process.communicate()
    exitcode = process.wait()
    if exitcode != 0:
        error("%s: unable to initialize the environment" % msvc)

    os.environ.update(eval(stdout.strip()))

    build_msvc_common(config, basedir)

# --------------------------------------------------------------- MSVC via Windows SDK 7.1

def check_msvc_winsdk71(config):
    for pfile in ['ProgramFiles(x86)', 'ProgramFiles']:
        if pfile in os.environ and exists(os.path.join(os.environ[pfile], 'Microsoft SDKs', 'Windows', 'v7.1', 'Bin', 'SetEnv.cmd')):
            return
    error("Unable to detect the location of Windows SDK 7.1")

def build_msvc_winsdk71(config, basedir):
    arch = config[config.rindex('-'):]
    setenv = None
    for pfile in ['ProgramFiles(x86)', 'ProgramFiles']:
        if not pfile in os.environ:
            continue
        setenv = os.path.join(os.environ[pfile], 'Microsoft SDKs', 'Windows', 'v7.1', 'Bin', 'SetEnv.cmd')

    mode = debug and '/Debug' or '/Release'
    if arch == 'win64':
        args = '/2008 /x64 %s' % mode
    else:
        args = '/2008 /x86 %s' % mode

    python = sys.executable
    process = subprocess.Popen('("%s" %s>nul)&&"%s" -c "import os; print repr(os.environ)"' % (
        setenv, args, python), stdout=subprocess.PIPE, shell=True)
    stdout, _ = process.communicate()
    exitcode = process.wait()
    if exitcode != 0:
        error("unable to initialize the environment for Windows SDK 7.1")

    os.environ.update(eval(stdout.strip()))

    build_msvc_common(config, basedir)

def build_msvc_common(config, basedir):
    version, simple_version = get_version(basedir)
    ssl_libs = build_openssl(config, basedir)

    qt5dir = os.path.join(basedir, 'qt5')
    if not exists(os.path.join(qt5dir, '.git')):
        rmdir(qt5dir)
        os.chdir(basedir)
        shell('git clone %s qt5' % QT5_URL)

    ssldir = os.path.join(basedir, config, 'openssl')
    qtdir  = os.path.join(basedir, config, 'qt')
    wkdir  = os.path.join(basedir, config, 'webkit')
    mkdir_p(qtdir)
    mkdir_p(wkdir)

    args = []
    args.extend(QT_CONFIG['common'])
    args.extend(QT_CONFIG['msvc'])
    args.append('-I %s\\include' % ssldir)
    args.append('-L %s\\lib' % ssldir)
    args.append('OPENSSL_LIBS="-L%s -lssleay32 -llibeay32 %s"' % \
        (ssldir.replace('\\', '\\\\'), ssl_libs))

    os.chdir(qtdir)
    if not exists('is_configured'):
        shell('%s\\..\\qt\\configure.exe %s' % (basedir, ' '.join(args)))
        open('is_configured', 'w').write('')
    shell('nmake')

    args = []
    args.extend(WEBKIT_CONFIG['common'])
    args.extend(WEBKIT_CONFIG['msvc2010'])

    os.environ['QTDIR']           = qtdir
    os.environ['PATH']            = '%s;%s\\bin;%s\\gnuwin32\\bin' % (os.environ['PATH'], qtdir, qt5dir)
    os.environ['SQLITE3SRCDIR']   = os.path.join(basedir, '..', 'qt', 'src', '3rdparty', 'sqlite')
    os.environ['WEBKITOUTPUTDIR'] = wkdir

    os.chdir(wkdir)
    shell('perl ../../../webkit/Tools/Scripts/build-webkit %s' % ' '.join(args))
    os.chdir(os.path.join(wkdir, 'Release'))
    shell('nmake install')

    appdir = os.path.join(basedir, config, 'app')
    mkdir_p(appdir)
    os.chdir(appdir)
    rmdir('bin')
    mkdir_p('bin')

    os.environ['WKHTMLTOX_VERSION'] = version

    shell('%s\\bin\\qmake %s\\..\\wkhtmltopdf.pro' % (qtdir, basedir))
    shell('nmake')

    found = False
    for pfile in ['ProgramFiles(x86)', 'ProgramFiles']:
        if not pfile in os.environ or not exists(os.path.join(os.environ[pfile], 'NSIS', 'makensis.exe')):
            continue
        found = True

        makensis = os.path.join(os.environ[pfile], 'NSIS', 'makensis.exe')
        os.chdir(os.path.join(basedir, '..'))
        shell('"%s" /DVERSION=%s /DSIMPLE_VERSION=%s /DTARGET=%s wkhtmltox.nsi' % \
                (makensis, version, simple_version, config))

    if not found:
        print "\n\nCould not build installer as NSIS was not found."

# ------------------------------------------------ MinGW-W64 Cross Environment

MINGW_W64_PREFIX = {
    'mingw-w64-cross-win32' : 'i686-w64-mingw32',
    'mingw-w64-cross-win64' : 'x86_64-w64-mingw32',
}

def check_mingw64_cross(config):
    shell('%s-gcc --version' % MINGW_W64_PREFIX[rchop(config, '-dbg')])

def build_mingw64_cross(config, basedir):
    version, simple_version = get_version(basedir)
    ssl_libs = build_openssl(config, basedir)

    ssldir = os.path.join(basedir, config, 'openssl')
    qtdir  = os.path.join(basedir, config, 'qt')
    wkdir  = os.path.join(basedir, config, 'webkit')

    mkdir_p(qtdir)
    mkdir_p(wkdir)

    args = []
    args.extend(QT_CONFIG['common'])
    args.extend(QT_CONFIG['mingw-w64-cross'])
    args.append('--prefix=%s'   % qtdir)
    args.append('-I %s/include' % ssldir)
    args.append('-L %s/lib'     % ssldir)
    args.append('-device-option CROSS_COMPILE=%s-' % MINGW_W64_PREFIX[rchop(config, '-dbg')])

    os.environ['OPENSSL_LIBS'] = '-lssl -lcrypto -L %s/lib %s' % (ssldir, ssl_libs)

<<<<<<< HEAD
    os.chdir(qtdir)
    shell('%s/../qt/configure %s' % (basedir, ' '.join(args)))
=======
    os.chdir(build)
    if not exists('is_configured'):
        shell('%s/../qt/configure %s' % (basedir, ' '.join(args)))
        shell('touch is_configured')
>>>>>>> upstream/master
    shell('make -j%d' % CPU_COUNT)

    args = []
    args.extend(WEBKIT_CONFIG['common'])
    args.extend(WEBKIT_CONFIG['mingw-w64-cross'])

    os.environ['QTDIR']           = qtdir
    os.environ['PATH']            = '%s:%s/bin' % (os.environ['PATH'], qtdir)
    os.environ['SQLITE3SRCDIR']   = os.path.join(basedir, '..', 'qt', 'src', '3rdparty', 'sqlite')
    os.environ['WEBKITOUTPUTDIR'] = wkdir

    os.chdir(wkdir)
    shell('perl ../../../webkit/Tools/Scripts/build-webkit %s' % ' '.join(args))
    os.chdir(os.path.join(wkdir, 'Release'))
    shell('make install')

    appdir = os.path.join(basedir, config, 'app')
    mkdir_p(appdir)
    os.chdir(appdir)
    shell('rm -f bin/*')

    # set up cross compiling prefix correctly (isn't set by make install)
    os.environ['QTDIR'] = qtdir
    os.environ['WKHTMLTOX_VERSION'] = version
    shell('%s/bin/qmake -set CROSS_COMPILE %s-' % (qtdir, MINGW_W64_PREFIX[rchop(config, '-dbg')]))
    shell('%s/bin/qmake -spec win32-g++-4.6 %s/../wkhtmltopdf.pro' % (qtdir, basedir))
    shell('make')
    shutil.copy('bin/libwkhtmltox0.a', 'bin/wkhtmltox.lib')

    os.chdir(os.path.join(basedir, '..'))
    shell('makensis -DVERSION=%s -DSIMPLE_VERSION=%s -DTARGET=%s wkhtmltox.nsi' % \
            (version, simple_version, config))

# -------------------------------------------------- Linux schroot environment

def check_linux_schroot(config):
    shell('schroot -c wkhtmltopdf-%s -- gcc --version' % rchop(config, '-dbg'))

def build_linux_schroot(config, basedir):
    version, simple_version = get_version(basedir)

    dir    = os.path.join(basedir, config)
    script = os.path.join(dir, 'build.sh')
    dist   = os.path.join(dir, 'wkhtmltox-%s' % version)

    mkdir_p(os.path.join(dir, 'qt'))
    mkdir_p(os.path.join(dir, 'webkit'))
    mkdir_p(os.path.join(dir, 'app'))

    rmdir(dist)
    mkdir_p(os.path.join(dist, 'bin'))
    mkdir_p(os.path.join(dist, 'include', 'wkhtmltox'))
    mkdir_p(os.path.join(dist, 'lib'))

    args = []
    args.extend(QT_CONFIG['common'])
    args.extend(QT_CONFIG['posix'])
    args.append('--prefix=%s' % os.path.join(dir, 'qt'))

    wk_args = []
    wk_args.extend(WEBKIT_CONFIG['common'])
    wk_args.extend(WEBKIT_CONFIG['posix'])

    lines = ['#!/bin/bash']
    lines.append('# start of autogenerated build script')
    lines.append('cd qt')
    if config == 'centos5-i386':
        lines.append('export CFLAGS=-march=i486')
        lines.append('export CXXFLAGS=-march=i486')
<<<<<<< HEAD
        wk_args.append('--qmakearg="QMAKE_CFLAGS+=-march=i486"')
        wk_args.append('--qmakearg="QMAKE_CXXFLAGS+=-march=i486"')
    lines.append('../../../qt/configure %s || exit 1' % ' '.join(args))
=======

    lines.append('if [ ! -f is_configured ]; then')
    lines.append('  ../../../qt/configure %s || exit 1' % ' '.join(args))
    lines.append('  touch is_configured')
    lines.append('fi')
>>>>>>> upstream/master
    lines.append('if ! make -j%d -q; then\n  make -j%d || exit 1\nfi' % (CPU_COUNT, CPU_COUNT))
    lines.append('export QTDIR=`pwd`')
    if config.startswith('centos5'):
        lines.append('export PATH=/override:$PATH:$QTDIR/bin')  # to pick up python 2.6
    else:
        lines.append('export PATH=$PATH:$QTDIR/bin')
    lines.append('export SQLITE3SRCDIR=$QTDIR/../../../qt/src/3rdparty/sqlite')
    lines.append('export WEBKITOUTPUTDIR=$QTDIR/../webkit')
    lines.append('cd ../webkit')
    lines.append('if ! perl ../../../webkit/Tools/Scripts/build-webkit %s; then' % ' '.join(wk_args))
    lines.append('  cd Release\n  make -j%d || exit 1\n  cd ..\nfi' % CPU_COUNT)
    lines.append('cd Release')
    lines.append('make install || exit 1')
<<<<<<< HEAD
    lines.append('cd ../../app')
    lines.append('GIT_DIR=../../../.git ../qt/bin/qmake ../../../wkhtmltopdf.pro')
=======
    lines.append('cd ../app')
    lines.append('rm -f bin/*')
    lines.append('export WKHTMLTOX_VERSION=%s' % version)
    lines.append('../qt/bin/qmake ../../../wkhtmltopdf.pro')
>>>>>>> upstream/master
    lines.append('make -j%d || exit 1' % CPU_COUNT)
    lines.append('strip bin/wkhtmltopdf bin/wkhtmltoimage')
    lines.append('cp bin/wkhtmlto* ../wkhtmltox-%s/bin' % version)
    lines.append('cp -P bin/libwkhtmltox*.so.* ../wkhtmltox-%s/lib' % version)
    lines.append('cp ../../../include/wkhtmltox/*.h ../wkhtmltox-%s/include/wkhtmltox' % version)
    lines.append('cp ../../../include/wkhtmltox/dll*.inc ../wkhtmltox-%s/include/wkhtmltox' % version)
    lines.append('cd ..')
    lines.append('tar -c -v -f ../wkhtmltox-%s_linux-%s.tar wkhtmltox-%s/' % (version, config, version))
    lines.append('xz --compress -9 ../wkhtmltox-%s_linux-%s.tar' % (version, config))
    lines.append('# end of build script')

    open(script, 'w').write('\n'.join(lines))
    os.chdir(dir)
    shell('chmod +x build.sh')
    shell('schroot -c wkhtmltopdf-%s -- ./build.sh' % rchop(config, '-dbg'))

# --------------------------------------------------------------- command line

def usage(exit_code=2):
    print "Usage: scripts/build.py <target> [-clean] [-debug]\n\nThe supported targets are:\n",
    opts = list(BUILDERS.keys())
    opts.sort()
    for opt in opts:
        print '* %s' % opt
    sys.exit(exit_code)

def main():
    basedir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'static-build')
    mkdir_p(basedir)

    if len(sys.argv) == 1:
        usage(0)

    config = sys.argv[1]
    if config not in BUILDERS:
        usage()

    for arg in sys.argv[2:]:
        if not arg in ['-clean', '-debug']:
            usage()

    final_config = config
    if '-debug' in sys.argv[2:]:
        # use the debug OpenSSL configuration if possible
        ssl = OPENSSL['build']
        for key in ssl:
            if fnmatch.fnmatch(config, key) and 'debug' in ssl[key]:
                ssl[key]['configure'] = ssl[key]['debug']
        # use a debug build of QT and WebKit
        cfg = QT_CONFIG['common']
        cfg[cfg.index('-release')] = '-debug'
        cfg[cfg.index('-webkit')]  = '-webkit-debug'
        final_config += '-dbg'

    if '-clean' in sys.argv[2:]:
        rmdir(os.path.join(basedir, config))

    globals()['check_%s' % BUILDERS[config]](final_config)
    globals()['build_%s' % BUILDERS[config]](final_config, os.path.realpath(basedir))

if __name__ == '__main__':
    main()
