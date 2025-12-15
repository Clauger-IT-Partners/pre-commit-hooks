# Clauger Pre-commit Hooks

Repo unique regroupant tous les hooks pre-commit utilisés par Clauger.

## Installation

Dans votre `.pre-commit-config.yaml` :

```yaml
repos:
  - repo: https://github.com/clauger/pre-commit-hooks
    rev: v1.0.0
    hooks:
      - id: detect-private-key
      - id: gitleaks
        args: ['--config', '.gitleaks.toml']
```

## Hooks disponibles

| Hook | Description |
|------|-------------|
| `detect-private-key` | Détecte les clés privées (RSA, DSA, EC, OpenSSH, PGP) |
| `gitleaks` | Détection avancée de secrets avec gitleaks |
| `check-yaml` | Vérifie la syntaxe YAML |
| `check-json` | Vérifie la syntaxe JSON |
| `end-of-file-fixer` | Assure une nouvelle ligne en fin de fichier |
| `trailing-whitespace` | Supprime les espaces en fin de ligne |
| `check-merge-conflict` | Détecte les marqueurs de conflit git |
| `check-added-large-files` | Bloque les fichiers > 500KB |

## Prérequis

### Gitleaks

Le hook `gitleaks` nécessite que gitleaks soit installé sur le système :

```bash
# macOS
brew install gitleaks

# Linux (Debian/Ubuntu)
sudo apt-get install gitleaks

# Via Go
go install github.com/gitleaks/gitleaks/v8@latest
```

## Mise à jour

```bash
pre-commit autoupdate
```

## Sources

Les hooks Python sont basés sur [pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks) (MIT License).

Le hook gitleaks utilise [gitleaks](https://github.com/gitleaks/gitleaks).
