pkgname = "chrony"
pkgver = "4.5"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-user=_chrony",
    "--with-sendmail=/usr/bin/sendmail",
    "--enable-ntp-signd",
    "--enable-scfilter",
]
make_cmd = "gmake"
make_dir = "."
hostmakedepends = ["pkgconf", "gmake"]
makedepends = [
    "gnutls-devel",
    "libcap-devel",
    "libedit-devel",
    "libseccomp-devel",
    "linux-headers",
    "nettle-devel",
]
checkdepends = ["bash"]
pkgdesc = "NTP client and server"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://chrony-project.org"
source = f"https://chrony-project.org/releases/{pkgname}-{pkgver}.tar.gz"
sha256 = "19fe1d9f4664d445a69a96c71e8fdb60bcd8df24c73d1386e02287f7366ad422"
file_modes = {
    "var/log/chrony": ("_chrony", "_chrony", 0o755),
    "var/lib/chrony": ("_chrony", "_chrony", 0o755),
}

system_users = [
    {
        "name": "_chrony",
        "id": None,
        "home": "/var/lib/chrony",
    }
]


def post_install(self):
    # config
    self.install_file(
        "examples/chrony.conf.example1", "etc", name="chrony.conf"
    )
    # default dirs
    self.install_dir("var/log/chrony", empty=True)
    self.install_dir("var/lib/chrony", empty=True)
    # tmpfiles.d
    self.install_file(self.files_path / "chrony.conf", "usr/lib/tmpfiles.d")
    # dinit services
    self.install_service(self.files_path / "chronyd")
    self.install_service(self.files_path / "chrony", enable=True)


configure_gen = []
