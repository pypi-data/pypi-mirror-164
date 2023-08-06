from __future__ import annotations

import json
from enum import Enum, auto
from io import StringIO
from urllib.request import urlopen

from lxml.html import parse
from packaging.requirements import Requirement
from packaging.version import Version


class PkgType(Enum):
    PYTHON = auto()
    JS = auto()


def update(index_url: str, npm_registry: str, spec: str, pkg_type: PkgType) -> str:
    if pkg_type is PkgType.PYTHON:
        return update_python(index_url, spec)
    else:
        return update_js(npm_registry, spec)


def update_js(npm_registry: str, spec: str) -> str:
    ver_at = spec.rfind("@")
    package = spec[: len(spec) if ver_at == -1 else ver_at]
    version = get_js_pkgs(npm_registry, package)[0]
    ver = str(version)
    while ver.endswith(".0"):
        ver = ver[:-2]
    return f"{package}@{ver}"


def get_js_pkgs(npm_registry: str, package: str) -> list[Version]:
    with urlopen(f"{npm_registry}/{package}") as handler:
        text = handler.read().decode("utf-8")
    info = json.loads(text)
    return sorted((v for v in (Version(i) for i in info["versions"].keys()) if not v.is_prerelease), reverse=True)


def update_python(index_url: str, spec: str) -> str:
    req = Requirement(spec)
    eq = any(s for s in req.specifier if s.operator == "==")
    for version in get_pkgs(index_url, req.name):
        if eq or all(s.contains(str(version)) for s in req.specifier):
            break
    else:
        return spec
    ver = str(version)
    ver = ver.split("+")[0]  # strip build numbers
    while ver.endswith(".0"):
        ver = ver[:-2]
    c_ver = next(
        (s.version for s in req.specifier if (s.operator == ">=" and not eq) or (eq and s.operator == "==")), None
    )
    if c_ver is None:
        new_ver = req.name
        if req.extras:
            new_ver = f"{new_ver}[{', '.join(req.extras)}]"
        new_ver = f"{new_ver}{',' if req.specifier else ''}>={ver}"
        if req.marker:
            new_ver = f"{new_ver};{req.marker}"
        new_req = str(Requirement(new_ver))
    else:
        op = "==" if eq else ">="
        new_req = str(req).replace(f"{op}{c_ver}", f"{op}{ver}")
    return new_req


def get_pkgs(index_url: str, package: str) -> list[Version]:
    with urlopen(f"{index_url}/{package}") as handler:
        text = handler.read().decode("utf-8")

    root = parse(StringIO(text))

    versions: set[Version] = set()
    for element in root.iter("a"):
        if element.text:
            file = element.text
            if file.endswith(".tar.bz2"):
                file = file[:-8]
            if file.endswith(".tar.gz"):
                file = file[:-7]
            if file.endswith(".whl"):
                file = file[:-4]
            if file.endswith(".zip"):
                file = file[:-4]
            parts = file.split("-")
            for part in parts[1:]:
                if part.split(".")[0].isnumeric():
                    break
            else:
                continue
            try:
                version = Version(part)
            except ValueError:
                pass
            else:
                versions.add(version)
    return sorted((v for v in versions if not v.is_prerelease), reverse=True)


__all__ = [
    "update",
    "PkgType",
]
