with (import <nixpkgs> { });
let
  deps = python-packages: with python-packages; [
    pillow
  ];
  python-with-deps = python39.withPackages deps;
in
mkShell {
  buildInputs = [
    python-with-deps
    black
  ];
}
