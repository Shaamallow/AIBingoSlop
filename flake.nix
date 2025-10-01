{
  description = "Python 3.12 Project to generate Bingo Chart on AI Slop Startup";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs =
    {
      self,
      nixpkgs,
      flake-utils,
    }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = import nixpkgs { inherit system; };
      in
      {
        devShells.default = pkgs.mkShell {
          packages = with pkgs; [
            python312
            uv
            python312Packages.pip
            python312Packages.ruff
          ];

          shellHook = ''
            echo "Python 3.12 dev shell with UV"
            echo "Run 'uv pip install -e .' to install your package in editable mode"
          '';
        };
      }
    );
}
