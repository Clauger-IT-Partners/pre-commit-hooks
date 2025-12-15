# Clauger Pre-commit Hooks

Collection de hooks [pre-commit](https://pre-commit.com/) pour la détection de secrets et la validation de code.

## Installation

Ajoutez ce repo dans votre `.pre-commit-config.yaml` :

```yaml
repos:
  - repo: https://github.com/clauger/pre-commit-hooks
    rev: v1.0.0
    hooks:
      - id: detect-private-key
      - id: gitleaks
```

Puis installez les hooks :

```bash
pre-commit install
```

## Hooks disponibles

### detect-private-key

Détecte les clés privées dans les fichiers stagés.

**Types détectés :**
- RSA Private Key
- DSA Private Key
- EC Private Key
- OpenSSH Private Key
- PGP Private Key Block
- PKCS#8 Private Key (chiffré ou non)

**Usage :**
```yaml
- id: detect-private-key
```

### gitleaks

Détection avancée de secrets avec [gitleaks](https://github.com/gitleaks/gitleaks).

**Prérequis :** gitleaks doit être installé sur le système.

```bash
# macOS
brew install gitleaks

# Linux (via Go)
go install github.com/gitleaks/gitleaks/v8@latest

# Windows (via Chocolatey)
choco install gitleaks
```

**Usage :**
```yaml
- id: gitleaks
```

Avec une configuration personnalisée :
```yaml
- id: gitleaks
  args: ['--config', '.gitleaks.toml']
```

## Configuration recommandée

Exemple complet pour un projet :

```yaml
repos:
  - repo: https://github.com/clauger/pre-commit-hooks
    rev: v1.0.0
    hooks:
      - id: detect-private-key
      - id: gitleaks

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: check-yaml
      - id: check-json
      - id: end-of-file-fixer
      - id: trailing-whitespace
      - id: check-merge-conflict
      - id: check-added-large-files
        args: ['--maxkb=500']
```

## Mise à jour

```bash
pre-commit autoupdate
```

## Licence

MIT - Basé sur [pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks).
