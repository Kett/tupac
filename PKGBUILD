# This is an example PKGBUILD file. Use this as a start to creating your own,
# and remove these comments. For more information, see 'man PKGBUILD'.
# NOTE: Please fill out the license field for your package! If it is unknown,
# then please put 'unknown'.

# Contributor: Francesc Ortiz <francescortiz@gmail.com>
pkgname=tupac
pkgver=0.5.3.2
pkgrel=1
pkgdesc="A cached pacman implementation that boosts some pacman operations: faster searches, AND searches, aur support, colored output, system sanity check, frontend friendly and more..."
arch=('i686' 'x86_64')
url="http://lapacaloca.com/arch/pajman"
license=('GPL')
groups=()
depends=('gcc' 'pacman' 'yaourt' 'php' 'libxml2')
makedepends=()
provides=()
conflicts=()
replaces=()
backup=()
options=()
install=
source=(http://github.com/Kett/tupac/tree/master/tars/tupac-$pkgver.tar.gz?raw=true)
noextract=()
md5sums=('5491282a0e6cbfe408d0f8420f1f69fa')

build() {
  cp -r $startdir/src/tupac/* $startdir/pkg/

  chmod a+rwx $startdir/pkg/var/lib/tupac
}

# vim:set ts=2 sw=2 et:
