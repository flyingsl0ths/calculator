# shell.nix

{ pkgs ? import <nixpkgs> { } }:
with pkgs; mkShell {
  nativeBuildInputs = [
    git
    nixpkgs-fmt
    python310
    python310Packages.pip
    shellcheck
    shfmt
  ];
}
