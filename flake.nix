nix
{
  description = "E-commerce Project";
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/stable-24.05";
  outputs = { self, nixpkgs, }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs { inherit system; };  
   in
   {
     devShells.${system}.default = import ./.idx/dev.nix {inherit pkgs;};
   };
}