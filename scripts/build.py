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
    'tag'       : 'OpenSSL_1_0_1f',
    'build'     : {
        'msvc2010-win32': {
            'configure' : 'VC-WIN32 no-asm',
            'build'     : ['ms\\do_ms.bat', 'nmake /f ms\\nt.mak install'],
            'libs'      : ['ssleay32.lib', 'libeay32.lib'],
            'os_libs'   : '-lUser32 -lAdvapi32 -lGdi32 -lCrypt32'
        },
        'msvc2010-win64': {
            'configure' : 'VC-WIN64A',
            'build'     : ['ms\\do_win64a.bat', 'nmake /f ms\\nt.mak install'],
            'libs'      : ['ssleay32.lib', 'libeay32.lib'],
            'os_libs'   : '-lUser32 -lAdvapi32 -lGdi32 -lCrypt32'
        },
        'mingw-w64-cross-win32': {
            'configure' : '--cross-compile-prefix=i686-w64-mingw32- no-shared no-asm mingw64',
            'build'     : ['make', 'make install'],
            'libs'      : ['libssl.a', 'libcrypto.a'],
            'os_libs'   : '-lws2_32 -lgdi32 -lcrypt32'
        },
        'mingw-w64-cross-win64': {
            'configure' : '--cross-compile-prefix=x86_64-w64-mingw32- no-shared no-asm mingw64',
            'build'     : ['make', 'make install'],
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

    'msvc2010': [
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
    'msvc2010-win32':        'msvc2010',
    'msvc2010-win64':        'msvc2010',
    'centos5-i386':          'linux_schroot',
    'centos5-amd64':         'linux_schroot',
    'wheezy-i386':           'linux_schroot',
    'wheezy-amd64':          'linux_schroot',
    'mingw-w64-cross-win32': 'mingw64_cross',
    'mingw-w64-cross-win64': 'mingw64_cross'
}

# --------------------------------------------------------------- HELPERS

import os, sys, subprocess, shutil, multiprocessing

from os.path import exists

CPU_COUNT = max(2, multiprocessing.cpu_count()-1)   # leave one CPU free

def error(msg):
    print msg
    sys.exit(1)

def shell(cmd):
    ret = os.system(cmd)
    if ret != 0:
        error("command failed: exit code %d" % ret)

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
    text = text[:text.index('-')]
    os.chdir(os.path.join(basedir, '..'))
    hash = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).strip()
    return ('%s-%s' % (text, hash), text)

def build_openssl(config, basedir):
    if not config in OPENSSL['build']:
        return

    srcdir = os.path.join(basedir, 'openssl')
    dstdir = os.path.join(basedir, config, 'openssl')

    def is_compiled():
        compiled = exists(os.path.join(dstdir, 'include', 'openssl', 'ssl.h'))
        for lib in OPENSSL['build'][config]['libs']:
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
        opts = OPENSSL['build'][config]
        shell('perl Configure --openssldir=%s %s' % (dstdir, opts['configure']))
        for cmd in opts['build']:
            shell(cmd)
        shell('git clean -fdx')
        if not is_compiled():
            error("Unable to compile OpenSSL for your system, aborting.")

# --------------------------------------------------------------- MSVC 2010

def check_msvc2010(config):
    for key in ['Configuration', 'TARGET_PLATFORM', 'TARGET_CPU']:
        if not key in os.environ:
            error("Please run under appropriate 'Windows SDK 7.1 Command Prompt'.")

    if os.environ['TARGET_PLATFORM'] not in ['XP', 'LH', 'SRV', 'LHS']:
        error("Please configure for 'Windows Server 2008 Release' or earlier.")

    if os.environ['Configuration'] != 'Release':
        error("Please configure for release mode.")

    if os.environ['TARGET_CPU'] not in ['x86', 'x64']:
        error("Please configure CPU for either x86 or x64.")

    if os.environ['TARGET_CPU'] == 'x86' and config == 'msvc2010-win64':
        error("Error: SDK configured for x86 but trying to build 64-bit.")

    if os.environ['TARGET_CPU'] == 'x64' and config == 'msvc2010-win32':
        error("Error: SDK configured for x64 but trying to build 32-bit.")

def build_msvc2010(config, basedir):
    build_openssl(config, basedir)

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
    args.extend(QT_CONFIG['msvc2010'])
    args.append('-I %s\\include' % ssldir)
    args.append('-L %s\\lib' % ssldir)
    args.append('OPENSSL_LIBS="-L%s -lssleay32 -llibeay32 %s"' % \
        (ssldir.replace('\\', '\\\\'), OPENSSL['build'][config]['os_libs']))

    os.chdir(qtdir)
    shell('%s\\..\\qt\\configure.exe %s' % (basedir, ' '.join(args)))
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

    shell('%s\\bin\\qmake %s\\..\\wkhtmltopdf.pro' % (qtdir, basedir))
    shell('nmake')

    found = False
    for pfile in ['ProgramFiles(x86)', 'ProgramFiles']:
        if not pfile in os.environ or not exists(os.path.join(os.environ[pfile], 'NSIS', 'makensis.exe')):
            continue
        found = True

        version, simple_version = get_version(basedir)
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
    shell('%s-gcc --version' % MINGW_W64_PREFIX[config])

def build_mingw64_cross(config, basedir):
    build_openssl(config, basedir)

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
    args.append('-device-option CROSS_COMPILE=%s-' % MINGW_W64_PREFIX[config])

    os.environ['OPENSSL_LIBS'] = '-lssl -lcrypto -L %s/lib %s' % (ssldir, OPENSSL['build'][config]['os_libs'])

    os.chdir(qtdir)
    shell('%s/../qt/configure %s' % (basedir, ' '.join(args)))
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

    # set up cross compiling prefix correctly (isn't set by make install)
    os.environ['QTDIR'] = qtdir
    shell('%s/bin/qmake -set CROSS_COMPILE %s-' % (qtdir, MINGW_W64_PREFIX[config]))
    shell('%s/bin/qmake -spec win32-g++-4.6 %s/../wkhtmltopdf.pro' % (qtdir, basedir))
    shell('make')
    shutil.copy('bin/libwkhtmltox0.a', 'bin/wkhtmltox.lib')

    version, simple_version = get_version(basedir)
    os.chdir(os.path.join(basedir, '..'))
    shell('makensis -DVERSION=%s -DSIMPLE_VERSION=%s -DTARGET=%s wkhtmltox.nsi' % \
            (version, simple_version, config))

# -------------------------------------------------- Linux schroot environment

def check_linux_schroot(config):
    shell('schroot -c wkhtmltopdf-%s -- gcc --version' % config)

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
        wk_args.append('--qmakearg="QMAKE_CFLAGS+=-march=i486"')
        wk_args.append('--qmakearg="QMAKE_CXXFLAGS+=-march=i486"')
    lines.append('../../../qt/configure %s || exit 1' % ' '.join(args))
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
    lines.append('cd ../../app')
    lines.append('GIT_DIR=../../../.git ../qt/bin/qmake ../../../wkhtmltopdf.pro')
    lines.append('make -j%d || exit 1' % CPU_COUNT)
    lines.append('strip bin/wkhtmltopdf bin/wkhtmltoimage')
    lines.append('cp bin/wkhtmlto* ../wkhtmltox-%s/bin' % version)
    lines.append('cp -P bin/libwkhtmltox*.so.* ../wkhtmltox-%s/lib' % version)
    lines.append('cp ../../../include/wkhtmltox/*.h ../wkhtmltox-%s/include/wkhtmltox' % version)
    lines.append('cp ../../../include/wkhtmltox/dll*.inc ../wkhtmltox-%s/include/wkhtmltox' % version)
    lines.append('cd ..')
    lines.append('tar -c -v --use-compress-program=xz -f ../wkhtmltox-%s_linux-%s.tar.xz wkhtmltox-%s/' % (version, config, version))
    lines.append('# end of build script')

    open(script, 'w').write('\n'.join(lines))
    os.chdir(dir)
    shell('chmod +x build.sh')
    shell('schroot -c wkhtmltopdf-%s -- ./build.sh' % config)

# --------------------------------------------------------------- command line

def usage():
    print "Usage: scripts/build.py [target] where target is one of:\n *",
    opts = list(BUILDERS.keys())
    opts.sort()
    print '\n * '.join(opts)
    sys.exit(0)

def main():
    basedir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'static-build')
    mkdir_p(basedir)

    if len(sys.argv) != 2 or sys.argv[1] not in BUILDERS:
        usage()

    config = sys.argv[1]
    globals()['check_%s' % BUILDERS[config]](config)
    globals()['build_%s' % BUILDERS[config]](config, os.path.realpath(basedir))

if __name__ == '__main__':
    main()
