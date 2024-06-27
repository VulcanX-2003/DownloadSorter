# Maintainer: Your Name <your.email@example.com>
pkgname=sorter
pkgver=0.1.0
pkgrel=1
pkgdesc="Automatically sort downloaded files into OS-specific directories."
arch=('any')
url="https://github.com/yourusername/sorter"
license=('MIT')
depends=('python' 'python-watchdog')
source=("$pkgname-$pkgver.tar.gz")
sha256sums=('SKIP')

build() {
  cd "$srcdir"
  python setup.py build
}

package() {
  cd "$srcdir"
  python setup.py install --root="$pkgdir" --optimize=1
  install -Dm755 src/sorter.py "$pkgdir/usr/bin/sorter"
  install -Dm644 sorter.service "$pkgdir/usr/lib/systemd/system/sorter.service"
}
