;; [[file:../../org/resources/install.org::*Configure MELPA][Configure MELPA:1]]
(require 'package)

(setq package-archives
      '(("melpa" . "https://melpa.org/packages/")
        ("gnu" . "https://elpa.gnu.org/packages/")
        ("org" . "http://orgmode.org/elpa/")))

(package-initialize)
(package-refresh-contents)
;; Configure MELPA:1 ends here

;; [[file:../../org/resources/install.org::*Install Packages][Install Packages:1]]
(package-install 'org)
(package-install 'use-package)
(package-install 'yaml-mode)
(package-install 'dockerfile-mode)
(package-install 'terraform-mode)
(package-install 'graphviz-dot-mode)
(package-install 'plantuml-mode)
(package-install 'toml-mode)
;; Install Packages:1 ends here
