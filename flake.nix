{
  description = "An app to show the crime data of Los Angeles";

  inputs = { nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable"; };

  outputs = inputs@{ flake-parts, ... }: 
    flake-parts.lib.mkFlake { inherit inputs; } {
      systems = [ "x86_64-linux" "aarch64-linux" "aarch64-darwin" "x86_64-darwin" ];

      perSystem = { config, self', inputs', pkgs, system, ... }:
        let
          name = "api";
          vendorHash = null;
        in
        {
          devShells = {
            data = pkgs.mkShell {
              packages = [
                pkgs.postgresql
                (pkgs.python311.withPackages(ps:[
                  ps.psycopg
                ]))
              ];
            };
            api = pkgs.mkShell {
              inputsFrom = [ self'.packages.api ];
            };
          };
          packages = {
            api = pkgs.buildGoModule {
              inherit name vendorHash;
              src = "./api/";
            };
          };
        };
  };
}
