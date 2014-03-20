#!/bin/bash
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

if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

if [ $# -ne 1 ]; then
    echo "Usage: scripts/setup-linux.sh [user-to-grant-schroot-access]"
    exit 1
fi

# install required packages
apt-get install --assume-yes git-core xz-utils build-essential mingw-w64 nsis debootstrap schroot rinse

# create the directory which will hold the chroot environments
if [ -d /srv/chroot-wkhtmltopdf ]; then
    rm -fr /srv/chroot-wkhtmltopdf
fi
mkdir -p /srv/chroot-wkhtmltopdf

# create chroots for Debian Wheezy
debootstrap --arch=i386  --variant=buildd wheezy /srv/chroot-wkhtmltopdf/wheezy-i386  http://ftp.us.debian.org/debian/
debootstrap --arch=amd64 --variant=buildd wheezy /srv/chroot-wkhtmltopdf/wheezy-amd64 http://ftp.us.debian.org/debian/

# update packages and install build dependencies
cat > /srv/chroot-wkhtmltopdf/wheezy-amd64/etc/apt/sources.list <<EOF
deb http://ftp.debian.org/debian/ wheezy         main
deb http://ftp.debian.org/debian/ wheezy-updates main
deb http://security.debian.org/   wheezy/updates main
EOF
cat > /srv/chroot-wkhtmltopdf/wheezy-amd64/bootstrap.sh <<EOF
apt-get update
apt-get dist-upgrade --assume-yes
# tools required for building WebKit
apt-get install --assume-yes git bison flex m4 gperf flexc++ ruby python
# taken from http://qt-project.org/doc/qt-4.8/install-x11.html#note-content-228
apt-get install --assume-yes libssl-dev libfontconfig1-dev libfreetype6-dev libx11-dev libxcursor-dev libxext-dev libxfixes-dev libxft-dev libxi-dev libxrandr-dev libxrender-dev
rm /bootstrap.sh
EOF
cp /srv/chroot-wkhtmltopdf/wheezy-amd64/bootstrap.sh         /srv/chroot-wkhtmltopdf/wheezy-i386/bootstrap.sh
cp /srv/chroot-wkhtmltopdf/wheezy-amd64/etc/apt/sources.list /srv/chroot-wkhtmltopdf/wheezy-i386/etc/apt/sources.list

chroot         /srv/chroot-wkhtmltopdf/wheezy-amd64/ bash /bootstrap.sh
linux32 chroot /srv/chroot-wkhtmltopdf/wheezy-i386/  bash /bootstrap.sh

rm /srv/chroot-wkhtmltopdf/wheezy-amd64/var/cache/apt/archives/*.deb
rm /srv/chroot-wkhtmltopdf/wheezy-i386/var/cache/apt/archives/*.deb

# create chroots for Centos 5
linux32 rinse --arch i386  --distribution centos-5 --directory /srv/chroot-wkhtmltopdf/centos5-i386
rinse         --arch amd64 --distribution centos-5 --directory /srv/chroot-wkhtmltopdf/centos5-amd64

# update packages and install development tools and build dependencies
cat > /srv/chroot-wkhtmltopdf/centos5-amd64/bootstrap.sh <<EOF
yum install -y wget
wget http://dl.fedoraproject.org/pub/epel/5/i386/epel-release-5-4.noarch.rpm
rpm -i epel-release-5-4.noarch.rpm
rm -f epel-release-5-4.noarch.rpm
wget http://centos.karan.org/el5/ruby187/kbs-el5-ruby187.repo -O /etc/yum.repos.d/kbs-el5-rb187.repo
yum update -y
yum install -y gcc gcc-c++ make qt4-devel openssl-devel diffutils perl xz git
yum install -y bison flex m4 gperf ruby python26 perl-version
mkdir -p /override
ln -s /usr/bin/python2.6 /override/python
rm /bootstrap.sh
EOF
cp /srv/chroot-wkhtmltopdf/centos5-amd64/bootstrap.sh /srv/chroot-wkhtmltopdf/centos5-i386/bootstrap.sh
echo "exclude = *.i?86">>/srv/chroot-wkhtmltopdf/centos5-amd64/etc/yum.conf
chroot         /srv/chroot-wkhtmltopdf/centos5-amd64 bash /bootstrap.sh
linux32 chroot /srv/chroot-wkhtmltopdf/centos5-i386  bash /bootstrap.sh

# create schroot configuration
cat > /etc/schroot/chroot.d/wkhtmltopdf <<EOF
[wkhtmltopdf-wheezy-i386]
type=directory
directory=/srv/chroot-wkhtmltopdf/wheezy-i386/
description=Debian Wheezy i386 for wkhtmltopdf
users=$1
root-users=root
personality=linux32

[wkhtmltopdf-wheezy-amd64]
type=directory
directory=/srv/chroot-wkhtmltopdf/wheezy-amd64/
description=Debian Wheezy amd64 for wkhtmltopdf
users=$1
root-users=root

[wkhtmltopdf-centos5-i386]
type=directory
directory=/srv/chroot-wkhtmltopdf/centos5-i386/
description=CentOS 5 i386 for wkhtmltopdf
users=$1
root-users=root
personality=linux32

[wkhtmltopdf-centos5-amd64]
type=directory
directory=/srv/chroot-wkhtmltopdf/centos5-amd64/
description=CentOS 5 amd64 for wkhtmltopdf
users=$1
root-users=root
EOF

echo "Environments set up successfully."
