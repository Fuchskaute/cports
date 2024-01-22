pkgname = "thermald"
pkgver = "2.5.5"
pkgrel = 0
archs = ["x86_64"]
# don't use autogen.sh, it generates files that force reconf in do_build
build_style = "gnu_configure"
make_cmd = "gmake"
make_dir = "."
hostmakedepends = [
    "autoconf",
    "autoconf-archive",
    "automake",
    "dbus-glib",
    "gettext",
    "glib-devel",
    "gmake",
    "gtk-doc-tools",
    "libtool",
    "pkgconf",
]
makedepends = [
    "dbus-devel",
    "dbus-glib-devel",
    "glib-devel",
    "libevdev-devel",
    "libxml2-devel",
    "upower-devel",
    "xz-devel",
]
pkgdesc = "Thermal daemon for x86_64-based Intel CPUs"
maintainer = "miko <mikoxyzzz@gmail.com>"
license = "GPL-2.0-or-later"
url = "https://github.com/intel/thermal_daemon"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d5d6d8213fcfd6f3cf073b993225699154b1e22f6053332830231da5038ce8a9"
hardening = ["vis"]


# autoreconf fails otherwise
def pre_configure(self):
    self.mkdir("m4")


def post_install(self):
    self.install_file(
        "data/org.freedesktop.thermald.service.in",
        "usr/share/dbus-1/system-services",
        0o644,
        "org.freedesktop.thermald.service",
    )
    self.install_license("COPYING")
    self.install_service(self.files_path / "thermald")
